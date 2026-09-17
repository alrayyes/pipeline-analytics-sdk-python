"""Unit tests for the hand-written pagination iterator, against a fake
transport rather than the real generated request/response mapping
(rules/sdk-generation.md's "Testing against the spec, not a hand-written
stub" -- "unit-test only the hand-written parts")."""

from __future__ import annotations

import asyncio
import itertools
from http import HTTPStatus

import httpx
import pytest

from pipeline_analytics._generated.client import Client as GeneratedClient
from pipeline_analytics._generated.models.forge import Forge
from pipeline_analytics._generated.types import Response as GeneratedResponse
from pipeline_analytics.errors import APIError
from pipeline_analytics.pagination import aiter_repos, iter_repos


def _repo(n: int) -> dict[str, str]:
    return {
        "id": f"id-{n}",
        "forge": "github",
        "identifier": f"org/repo-{n}",
        "tokenMasked": "****1234",
        "ingestionStatus": "active",
    }


def _paged_handler(recorded_requests: list[httpx.Request] | None = None) -> httpx.MockTransport:
    # Three pages (2, 1, 1 repos) so an offset bug that overwrites instead
    # of accumulates only shows up after the second page, and a captured
    # request list lets tests assert exactly which limit/offset/forge each
    # page was fetched with, not just the final identifiers.
    pages = {0: ([_repo(1), _repo(2)], True), 2: ([_repo(3)], True), 3: ([_repo(4)], False)}

    def handler(request: httpx.Request) -> httpx.Response:
        if recorded_requests is not None:
            recorded_requests.append(request)
        offset = int(request.url.params.get("offset", "0"))
        if offset not in pages:  # pragma: no cover - guards a test bug, not SDK behavior
            raise AssertionError(f"unexpected offset {offset}")
        repos, has_more = pages[offset]
        return httpx.Response(200, json={"repos": repos, "hasMore": has_more}, request=request)

    return httpx.MockTransport(handler)


def _client_with(transport: httpx.MockTransport) -> GeneratedClient:
    client = GeneratedClient(base_url="https://example.test")
    client.set_httpx_client(httpx.Client(base_url="https://example.test", transport=transport))
    client.set_async_httpx_client(httpx.AsyncClient(base_url="https://example.test", transport=transport))
    return client


def test_iter_repos_walks_every_page() -> None:
    requests: list[httpx.Request] = []
    client = _client_with(_paged_handler(requests))

    # Bounded to well beyond the real 4 items: a dropped offset/limit
    # keyword would silently re-request page 1 forever (hasMore stays
    # True), and a generator only pulled lazily via islice stops there
    # instead of hanging the test.
    identifiers = [repo.identifier for repo in itertools.islice(iter_repos(client, limit=2), 12)]

    assert identifiers == ["org/repo-1", "org/repo-2", "org/repo-3", "org/repo-4"]
    # Exact offsets requested, in order -- catches an accumulator that
    # overwrites instead of adds (only visible from the 2nd page on) and a
    # dropped `offset=`/`limit=` keyword that would fall back to the
    # generated function's own defaults (0 and unset).
    seen = [(int(r.url.params["offset"]), r.url.params["limit"]) for r in requests]
    assert seen == [(0, "2"), (2, "2"), (3, "2")]


def test_iter_repos_forwards_forge_filter() -> None:
    requests: list[httpx.Request] = []
    client = _client_with(_paged_handler(requests))

    # Only the first page matters here -- pull exactly one item rather
    # than fully draining the generator, for the same "don't hang on a
    # broken pagination loop" reason as the walk test above.
    next(iter_repos(client, forge=Forge.GITHUB, limit=2), None)

    assert requests[0].url.params["forge"] == "github"


def test_iter_repos_raises_api_error() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"code": "unauthorized", "message": "no session"}, request=request)

    client = _client_with(httpx.MockTransport(handler))

    with pytest.raises(APIError) as exc_info:
        list(iter_repos(client))

    assert exc_info.value.status_code == 401
    assert exc_info.value.code == "unauthorized"


def test_iter_repos_stops_on_undocumented_status() -> None:
    # 204 is neither an error (decode_error only fires >= 400) nor one of
    # listRepos' documented 200/401 responses, so the generated client
    # parses it to None -- iter_repos should stop cleanly rather than
    # raising or looping forever.
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(204, request=request)

    client = _client_with(httpx.MockTransport(handler))

    assert list(iter_repos(client)) == []


def test_aiter_repos_walks_every_page() -> None:
    requests: list[httpx.Request] = []
    client = _client_with(_paged_handler(requests))

    async def collect() -> list[str]:
        # Bounded the same way and for the same reason as the sync
        # version's islice above -- an async generator has no islice in
        # the stdlib, so a manual counter does the same job.
        out = []
        async for repo in aiter_repos(client, limit=2):
            out.append(repo.identifier)
            if len(out) >= 12:
                break
        return out

    identifiers = asyncio.run(collect())

    assert identifiers == ["org/repo-1", "org/repo-2", "org/repo-3", "org/repo-4"]
    seen = [(int(r.url.params["offset"]), r.url.params["limit"]) for r in requests]
    assert seen == [(0, "2"), (2, "2"), (3, "2")]


def test_aiter_repos_forwards_forge_filter() -> None:
    requests: list[httpx.Request] = []
    client = _client_with(_paged_handler(requests))

    async def collect() -> None:
        async for _ in aiter_repos(client, forge=Forge.GITHUB, limit=2):
            break  # only the first page matters -- see the sync version's comment

    asyncio.run(collect())

    assert requests[0].url.params["forge"] == "github"


def test_aiter_repos_raises_api_error() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, json={"code": "unauthorized", "message": "no session"}, request=request)

    client = _client_with(httpx.MockTransport(handler))

    async def collect() -> list[object]:
        return [repo async for repo in aiter_repos(client)]

    with pytest.raises(APIError) as exc_info:
        asyncio.run(collect())
    assert exc_info.value.status_code == 401


def test_aiter_repos_stops_on_undocumented_status() -> None:
    async def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(204, request=request)

    client = _client_with(httpx.MockTransport(handler))

    async def collect() -> list[object]:
        return [repo async for repo in aiter_repos(client)]

    assert asyncio.run(collect()) == []


def test_iter_repos_raises_typeerror_for_unexpected_parsed_type(monkeypatch: pytest.MonkeyPatch) -> None:
    # listRepos' spec only ever parses a 200 to RepoList (everything else
    # is None or an Error, both handled elsewhere) -- there's no real
    # server response that reaches the isinstance(page, RepoList) guard,
    # so exercising it means forcing the generated call's return value
    # directly rather than going through an actual transport.
    fake_response: GeneratedResponse[object] = GeneratedResponse(
        status_code=HTTPStatus.OK, content=b"{}", headers={}, parsed=object()
    )
    monkeypatch.setattr("pipeline_analytics.pagination._list_repos.sync_detailed", lambda **_kwargs: fake_response)
    client = GeneratedClient(base_url="https://example.test")

    with pytest.raises(TypeError, match="unexpected listRepos response body"):
        list(iter_repos(client))


def test_aiter_repos_raises_typeerror_for_unexpected_parsed_type(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_response: GeneratedResponse[object] = GeneratedResponse(
        status_code=HTTPStatus.OK, content=b"{}", headers={}, parsed=object()
    )

    async def fake_asyncio_detailed(**_kwargs: object) -> GeneratedResponse[object]:
        return fake_response

    monkeypatch.setattr("pipeline_analytics.pagination._list_repos.asyncio_detailed", fake_asyncio_detailed)
    client = GeneratedClient(base_url="https://example.test")

    async def collect() -> list[object]:
        return [repo async for repo in aiter_repos(client)]

    with pytest.raises(TypeError, match="unexpected listRepos response body"):
        asyncio.run(collect())
