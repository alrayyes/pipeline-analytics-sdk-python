"""The hand-written client wrapper. Everything under
``pipeline_analytics._generated`` is produced by openapi-python-client from
``openapi/openapi.yaml`` -- never edit it by hand, regenerate it instead
(see ``hack/fetch-spec.sh`` and ``CONTRIBUTING.md``). This module,
``errors.py``, ``retry.py`` and ``pagination.py`` are the hand-written layer
on top of it: auth injection, retry, typed errors and pagination
(rules/sdk-generation.md's "Generated vs hand-written").
"""

from __future__ import annotations

import os

import httpx

from ._generated.api.meta import get_version as _get_version
from ._generated.client import Client as _GeneratedClient
from ._generated.models.version import Version
from .errors import decode_error
from .retry import DEFAULT_RETRY_CONFIG, AsyncRetryTransport, RetryConfig, RetryTransport

#: The environment variable :class:`PipelineAnalyticsClient` falls back to
#: when no session cookie is passed explicitly via ``session_cookie``.
SESSION_COOKIE_ENV_VAR = "PIPELINE_ANALYTICS_SESSION"

_SESSION_COOKIE_NAME = "session"


class PipelineAnalyticsClient:
    """A pipeline-analytics API client.

    Every operation except :meth:`get_version` and the two webhook
    receivers requires an authenticated session. pipeline-analytics
    authenticates browsers with `WebAuthn <https://webauthn.guide/>`_, not
    an API token -- there is no headless credential-grant flow in the spec
    (a real token flow is requested in
    `alrayyes/pipeline-analytics#178 <https://github.com/alrayyes/pipeline-analytics/issues/178>`_),
    so this client can't log in for you. Get a session cookie by logging
    into the dashboard in a browser, opening dev tools, and copying the
    ``session`` cookie's value. Pass it as *session_cookie* or set
    ``PIPELINE_ANALYTICS_SESSION`` in the environment -- the constructor
    argument wins when both are given.

    The underlying generated client is available as :attr:`raw` for any
    operation this wrapper doesn't have a dedicated method for; every
    generated ``pipeline_analytics._generated.api.<tag>.<operation>``
    module's ``sync_detailed``/``asyncio_detailed`` functions take it as
    their ``client`` argument.
    """

    def __init__(
        self,
        base_url: str,
        *,
        session_cookie: str | None = None,
        retry: RetryConfig = DEFAULT_RETRY_CONFIG,
        httpx_client: httpx.Client | None = None,
        httpx_async_client: httpx.AsyncClient | None = None,
        raise_on_unexpected_status: bool = False,
    ) -> None:
        cookie = session_cookie if session_cookie is not None else os.environ.get(SESSION_COOKIE_ENV_VAR)
        cookies = {_SESSION_COOKIE_NAME: cookie} if cookie else {}

        # cookies isn't passed here, and base_url is never read back off
        # self._raw afterward either: this Client's own lazy httpx-client
        # construction is never reached -- set_httpx_client/
        # set_async_httpx_client below always override it -- so the base
        # URL and cookie both have to be applied to whichever client
        # actually sends requests instead (see below). base_url is on its
        # own statement, pragma'd, so mutating that dead value doesn't
        # mask a real mutation of raise_on_unexpected_status on the same
        # line -- that one *is* read, by every generated operation's
        # _parse_response.
        self._raw = _GeneratedClient(base_url=base_url)  # pragma: no mutate - never read back, see comment above
        self._raw.raise_on_unexpected_status = raise_on_unexpected_status

        sync_client = httpx_client
        if sync_client is None:
            sync_client = httpx.Client(base_url=base_url, transport=RetryTransport(retry=retry))
        # Apply the session cookie directly to whichever client will
        # actually send requests -- a caller-supplied httpx_client bypasses
        # the generated Client's own lazy cookie-jar construction, so the
        # cookie has to be set here rather than relying on that path.
        sync_client.cookies.update(cookies)
        self._raw.set_httpx_client(sync_client)

        async_client = httpx_async_client
        if async_client is None:
            async_client = httpx.AsyncClient(base_url=base_url, transport=AsyncRetryTransport(retry=retry))
        async_client.cookies.update(cookies)
        self._raw.set_async_httpx_client(async_client)

    @property
    def raw(self) -> _GeneratedClient:
        """The underlying generated ``Client``."""
        return self._raw

    def get_version(self) -> Version:
        """The running server's build version. Needs no session -- a good
        first call to prove the client reaches the server at all."""
        response = _get_version.sync_detailed(client=self._raw)
        if error := decode_error(response):
            raise error
        if response.parsed is None:
            # Not an assert -- holds under -O and doesn't trip bandit's
            # B101. getVersion's only documented response is 200 Version,
            # so this only fires if the spec and server ever disagree.
            raise TypeError(f"unexpected getVersion response body: {response.parsed!r}")
        return response.parsed

    async def aget_version(self) -> Version:
        """Async counterpart of :meth:`get_version`."""
        response = await _get_version.asyncio_detailed(client=self._raw)
        if error := decode_error(response):
            raise error
        if response.parsed is None:
            raise TypeError(f"unexpected getVersion response body: {response.parsed!r}")
        return response.parsed

    def close(self) -> None:
        self._raw.get_httpx_client().close()

    async def aclose(self) -> None:
        await self._raw.get_async_httpx_client().aclose()

    def __enter__(self) -> PipelineAnalyticsClient:
        return self

    def __exit__(self, *exc_info: object) -> None:
        # httpx.BaseTransport's own __exit__ ignores exc_info and just
        # closes -- our RetryTransport doesn't override that -- so there's
        # nothing this needs from *exc_info beyond letting `with` call it.
        self.close()

    async def __aenter__(self) -> PipelineAnalyticsClient:
        return self

    async def __aexit__(self, *exc_info: object) -> None:
        await self.aclose()
