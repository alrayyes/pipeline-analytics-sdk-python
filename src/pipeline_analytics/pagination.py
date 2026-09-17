"""A real iterator over ``GET /api/repos``, the only endpoint in
pipeline-analytics' spec with pagination -- ``limit``/``offset`` query
params and a ``hasMore`` flag on the response. Walks every page
transparently rather than handing back one page and a raw offset for the
caller to loop on by hand (rules/sdk-generation.md's "Client shape").
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator

from ._generated.api.repos import list_repos as _list_repos
from ._generated.client import Client as _GeneratedClient
from ._generated.models.forge import Forge
from ._generated.models.repo import Repo
from ._generated.models.repo_list import RepoList
from ._generated.types import UNSET, Unset
from .errors import decode_error

#: Used when the caller leaves ``limit`` unset -- ``GET /api/repos`` never
#: paginates on its own (``RepoList.has_more`` is always false with no
#: limit), so an iterator needs a default to actually walk pages.
DEFAULT_PAGE_SIZE = 50


def iter_repos(
    client: _GeneratedClient,
    *,
    forge: Forge | Unset = UNSET,
    limit: int = DEFAULT_PAGE_SIZE,
    offset: int = 0,
) -> Iterator[Repo]:
    """Iterate every tracked repo matching *forge*, walking ``GET
    /api/repos``'s offset pages transparently.

    *client* is the generated client -- pass ``PipelineAnalyticsClient.raw``
    or any ``pipeline_analytics._generated.client.Client``/
    ``AuthenticatedClient``. Raises
    :class:`~pipeline_analytics.errors.APIError` if any page's response is
    an error, and whatever the underlying ``httpx`` transport raises on a
    transport failure that exhausts its retries.

    Usage::

        for repo in iter_repos(client.raw):
            print(repo.identifier, repo.ingestion_status)
    """
    while True:
        response = _list_repos.sync_detailed(client=client, forge=forge, limit=limit, offset=offset)
        if error := decode_error(response):
            raise error

        page = response.parsed
        if page is None:
            return
        if not isinstance(page, RepoList):
            # decode_error already raised for status_code >= 400, so a
            # parsed body at this point should always be RepoList -- this
            # only guards against a future spec change adding another
            # documented 2xx shape to listRepos.
            raise TypeError(f"unexpected listRepos response body: {page!r}")

        yield from page.repos

        if not page.has_more:
            return
        offset += len(page.repos)


async def aiter_repos(
    client: _GeneratedClient,
    *,
    forge: Forge | Unset = UNSET,
    limit: int = DEFAULT_PAGE_SIZE,
    offset: int = 0,
) -> AsyncIterator[Repo]:
    """Async counterpart of :func:`iter_repos`, for
    ``PipelineAnalyticsClient`` used with ``async with``/``await``."""
    while True:
        response = await _list_repos.asyncio_detailed(client=client, forge=forge, limit=limit, offset=offset)
        if error := decode_error(response):
            raise error

        page = response.parsed
        if page is None:
            return
        if not isinstance(page, RepoList):
            raise TypeError(f"unexpected listRepos response body: {page!r}")

        for repo in page.repos:
            yield repo

        if not page.has_more:
            return
        offset += len(page.repos)
