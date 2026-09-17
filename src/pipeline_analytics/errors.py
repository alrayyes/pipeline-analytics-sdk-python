"""Typed errors for the pipeline-analytics API.

Every 4xx/5xx response pipeline-analytics returns shares the same
``{code, message}`` body (see ``openapi/openapi.yaml``'s ``Error`` schema).
:func:`decode_error` turns that, plus the status code and any
``X-Request-Id`` header, into a single :class:`APIError` -- never a bare
string or a raw ``httpx.Response`` (rules/sdk-generation.md's "Client
shape").
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Protocol

_REQUEST_ID_HEADER = "X-Request-Id"


class _ErrorResponse(Protocol):
    """What :func:`decode_error` needs from a response.

    Both ``httpx.Response`` and the generated per-operation
    ``pipeline_analytics._generated.types.Response`` satisfy this
    structurally -- decoding works the same whether you call a wrapper
    method or drop down to a generated ``sync_detailed``/``asyncio_detailed``
    call directly. Declared as read-only properties (rather than plain
    attributes) so a subtype's more specific attribute types --
    ``http.HTTPStatus`` for ``status_code``, a ``MutableMapping`` for
    ``headers`` -- still satisfy the protocol; Protocol attribute matching
    is otherwise invariant.
    """

    @property
    def status_code(self) -> int: ...

    @property
    def content(self) -> bytes: ...

    @property
    def headers(self) -> Mapping[str, str]: ...


class APIError(Exception):
    """Raised for any pipeline-analytics response carrying an error body.

    Attributes:
        status_code: The HTTP status code.
        code: The API's own machine-readable error code (empty string if
            the body wasn't the documented ``{code, message}`` shape).
        message: The API's human-readable error message.
        request_id: The ``X-Request-Id`` response header, or ``None`` if
            absent.
    """

    def __init__(
        self,
        status_code: int,
        code: str,
        message: str,
        request_id: str | None = None,
    ) -> None:
        self.status_code = status_code
        self.code = code
        self.message = message
        self.request_id = request_id
        super().__init__(str(self))

    def __str__(self) -> str:
        base = f"pipeline-analytics: {self.status_code} {self.code}: {self.message}"
        if self.request_id:
            return f"{base} (request {self.request_id})"
        return base


def decode_error(response: _ErrorResponse) -> APIError | None:
    """Build an :class:`APIError` from *response*, or return ``None`` if
    its status code isn't an error.

    Decodes ``response.content`` directly rather than trusting the
    generated per-operation ``.parsed`` field, which is only populated for
    status codes the spec documents on that specific operation -- a 500 or
    429 that survived every retry attempt still needs an ``APIError``, and
    the API returns the same ``{code, message}`` shape for those too.

    Usage::

        response = sync_detailed(client=client.raw, ...)
        if error := decode_error(response):
            raise error
    """
    if response.status_code < 400:
        return None

    code = ""
    message = ""
    try:
        body = json.loads(response.content)
        if isinstance(body, dict):
            code = str(body.get("code", ""))
            message = str(body.get("message", ""))
    except ValueError:
        pass

    request_id = response.headers.get(_REQUEST_ID_HEADER) or None

    return APIError(int(response.status_code), code, message, request_id)
