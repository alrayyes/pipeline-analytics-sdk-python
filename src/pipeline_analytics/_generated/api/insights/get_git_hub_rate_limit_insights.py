from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.git_hub_token_usage import GitHubTokenUsage
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/insights/github-rate-limit",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | list[GitHubTokenUsage] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GitHubTokenUsage.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | list[GitHubTokenUsage]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | list[GitHubTokenUsage]]:
    """GitHub REST API rate-limit usage, grouped by token

     One entry per distinct GitHub token this app holds (not per repo -- the same token often tracks more
    than one repo), with the repos it covers and the token's most recently observed rate-limit status.
    That status is read from a real API response's X-RateLimit-* headers rather than a dedicated poll,
    per GitHub's own guidance (docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)
    -- `status` is absent until a request has actually been made with that token (reconciliation
    polling, or webhook/discovery calls).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[GitHubTokenUsage]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> Error | list[GitHubTokenUsage] | None:
    """GitHub REST API rate-limit usage, grouped by token

     One entry per distinct GitHub token this app holds (not per repo -- the same token often tracks more
    than one repo), with the repos it covers and the token's most recently observed rate-limit status.
    That status is read from a real API response's X-RateLimit-* headers rather than a dedicated poll,
    per GitHub's own guidance (docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)
    -- `status` is absent until a request has actually been made with that token (reconciliation
    polling, or webhook/discovery calls).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[GitHubTokenUsage]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Error | list[GitHubTokenUsage]]:
    """GitHub REST API rate-limit usage, grouped by token

     One entry per distinct GitHub token this app holds (not per repo -- the same token often tracks more
    than one repo), with the repos it covers and the token's most recently observed rate-limit status.
    That status is read from a real API response's X-RateLimit-* headers rather than a dedicated poll,
    per GitHub's own guidance (docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)
    -- `status` is absent until a request has actually been made with that token (reconciliation
    polling, or webhook/discovery calls).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[GitHubTokenUsage]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Error | list[GitHubTokenUsage] | None:
    """GitHub REST API rate-limit usage, grouped by token

     One entry per distinct GitHub token this app holds (not per repo -- the same token often tracks more
    than one repo), with the repos it covers and the token's most recently observed rate-limit status.
    That status is read from a real API response's X-RateLimit-* headers rather than a dedicated poll,
    per GitHub's own guidance (docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)
    -- `status` is absent until a request has actually been made with that token (reconciliation
    polling, or webhook/discovery calls).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[GitHubTokenUsage]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
