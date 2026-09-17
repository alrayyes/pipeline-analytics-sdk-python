"""Unit tests for the hand-written client wrapper: session-cookie
precedence and auth injection, against a fake transport
(rules/sdk-generation.md's "unit-test only the hand-written parts")."""

from __future__ import annotations

import asyncio

import httpx
import pytest

from pipeline_analytics import SESSION_COOKIE_ENV_VAR, APIError, PipelineAnalyticsClient
from pipeline_analytics.retry import AsyncRetryTransport, RetryConfig, RetryTransport


def _cookie_echo_transport(got: dict[str, str | None]) -> httpx.MockTransport:
    def handler(request: httpx.Request) -> httpx.Response:
        got["cookie"] = request.headers.get("cookie")
        return httpx.Response(200, json={"version": "dev"}, request=request)

    return httpx.MockTransport(handler)


@pytest.mark.parametrize(
    ("env", "arg", "want"),
    [
        (None, "from-arg", "session=from-arg"),
        ("from-env", None, "session=from-env"),
        ("from-env", "from-arg", "session=from-arg"),
    ],
)
def test_session_cookie_precedence(
    monkeypatch: pytest.MonkeyPatch, env: str | None, arg: str | None, want: str
) -> None:
    if env is not None:
        monkeypatch.setenv(SESSION_COOKIE_ENV_VAR, env)
    else:
        monkeypatch.delenv(SESSION_COOKIE_ENV_VAR, raising=False)

    got: dict[str, str | None] = {}
    httpx_client = httpx.Client(base_url="https://example.test", transport=_cookie_echo_transport(got))
    client = PipelineAnalyticsClient("https://example.test", session_cookie=arg, httpx_client=httpx_client)

    client.get_version()

    assert got["cookie"] == want


def test_no_cookie_sent_when_unset(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(SESSION_COOKIE_ENV_VAR, raising=False)
    got: dict[str, str | None] = {}
    httpx_client = httpx.Client(base_url="https://example.test", transport=_cookie_echo_transport(got))
    client = PipelineAnalyticsClient("https://example.test", httpx_client=httpx_client)

    client.get_version()

    assert got["cookie"] is None


def test_get_version_returns_parsed_body() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"version": "1.2.3"}, request=request)

    httpx_client = httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler))
    client = PipelineAnalyticsClient("https://example.test", httpx_client=httpx_client)

    assert client.get_version().version == "1.2.3"


def test_aget_version_returns_parsed_body() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"version": "1.2.3"}, request=request)

    async_client = httpx.AsyncClient(base_url="https://example.test", transport=httpx.MockTransport(handler))
    client = PipelineAnalyticsClient("https://example.test", httpx_async_client=async_client)

    assert asyncio.run(client.aget_version()).version == "1.2.3"


def test_context_manager_closes_underlying_client() -> None:
    httpx_client = httpx.Client(base_url="https://example.test")
    client = PipelineAnalyticsClient("https://example.test", httpx_client=httpx_client)

    with client:
        pass

    assert httpx_client.is_closed


def test_get_version_raises_api_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(500, json={"code": "internal", "message": "boom"}, request=request)

    httpx_client = httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler))
    client = PipelineAnalyticsClient("https://example.test", httpx_client=httpx_client)

    with pytest.raises(APIError) as exc_info:
        client.get_version()
    assert exc_info.value.status_code == 500


def test_aget_version_raises_api_error() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(500, json={"code": "internal", "message": "boom"}, request=request)

    async_client = httpx.AsyncClient(base_url="https://example.test", transport=httpx.MockTransport(handler))
    client = PipelineAnalyticsClient("https://example.test", httpx_async_client=async_client)

    with pytest.raises(APIError):
        asyncio.run(client.aget_version())


def test_close_closes_sync_client() -> None:
    httpx_client = httpx.Client(base_url="https://example.test")
    client = PipelineAnalyticsClient("https://example.test", httpx_client=httpx_client)

    client.close()

    assert httpx_client.is_closed


def test_aclose_closes_async_client() -> None:
    async_client = httpx.AsyncClient(base_url="https://example.test")
    client = PipelineAnalyticsClient("https://example.test", httpx_async_client=async_client)

    asyncio.run(client.aclose())

    assert async_client.is_closed


def test_async_context_manager_closes_underlying_client() -> None:
    async_client = httpx.AsyncClient(base_url="https://example.test")
    client = PipelineAnalyticsClient("https://example.test", httpx_async_client=async_client)

    async def run() -> None:
        async with client:
            pass

    asyncio.run(run())

    assert async_client.is_closed


def test_default_construction_wires_base_url_cookies_and_retry() -> None:
    # No httpx_client/httpx_async_client override -- proves the default
    # sync AND async clients are wired up correctly (base URL, session
    # cookie, and the given retry config on the retry transport), not just
    # that *a* retry transport of *some* config gets attached.
    retry = RetryConfig(max_retries=7, base_seconds=0.5)
    client = PipelineAnalyticsClient("https://example.test", session_cookie="tok123", retry=retry)

    sync_client = client.raw.get_httpx_client()
    assert sync_client.base_url == httpx.URL("https://example.test")
    assert sync_client.cookies.get("session") == "tok123"
    sync_transport = sync_client._transport
    assert isinstance(sync_transport, RetryTransport)
    assert sync_transport._retry == retry

    async_client = client.raw.get_async_httpx_client()
    assert async_client.base_url == httpx.URL("https://example.test")
    assert async_client.cookies.get("session") == "tok123"
    async_transport = async_client._transport
    assert isinstance(async_transport, AsyncRetryTransport)
    assert async_transport._retry == retry


def test_raise_on_unexpected_status_true_raises_instead_of_returning_none() -> None:
    from pipeline_analytics._generated import errors as generated_errors

    def handler(request: httpx.Request) -> httpx.Response:
        # 204 is undocumented for getVersion (only 200 is) -- with the
        # default raise_on_unexpected_status=False this parses to None;
        # with it explicitly True the generated client should raise
        # instead.
        return httpx.Response(204, request=request)

    httpx_client = httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler))
    client = PipelineAnalyticsClient("https://example.test", httpx_client=httpx_client, raise_on_unexpected_status=True)

    with pytest.raises(generated_errors.UnexpectedStatus):
        client.get_version()


def test_get_version_raises_typeerror_for_undocumented_status() -> None:
    # 204 is undocumented for getVersion (only 200 is), so the generated
    # client parses it to None -- get_version should raise a clear
    # TypeError rather than returning None typed as Version.
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(204, request=request)

    httpx_client = httpx.Client(base_url="https://example.test", transport=httpx.MockTransport(handler))
    client = PipelineAnalyticsClient("https://example.test", httpx_client=httpx_client)

    with pytest.raises(TypeError, match="unexpected getVersion response body"):
        client.get_version()


def test_aget_version_raises_typeerror_for_undocumented_status() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(204, request=request)

    async_client = httpx.AsyncClient(base_url="https://example.test", transport=httpx.MockTransport(handler))
    client = PipelineAnalyticsClient("https://example.test", httpx_async_client=async_client)

    with pytest.raises(TypeError, match="unexpected getVersion response body"):
        asyncio.run(client.aget_version())
