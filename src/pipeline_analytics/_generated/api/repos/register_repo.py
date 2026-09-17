from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.repo import Repo
from ...models.repo_registration import RepoRegistration
from ...types import Response


def _get_kwargs(
    *,
    body: RepoRegistration,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/repos",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Repo | None:
    if response.status_code == 201:
        response_201 = Repo.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Repo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RepoRegistration,
) -> Response[Error | Repo]:
    """Register a repository for tracking

     Stores the supplied token encrypted at rest and creates a webhook on the repository (forge-
    ingestion/spec.md's "Repo tracking registration" and "Webhook registration on tracking").

    Args:
        body (RepoRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Repo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RepoRegistration,
) -> Error | Repo | None:
    """Register a repository for tracking

     Stores the supplied token encrypted at rest and creates a webhook on the repository (forge-
    ingestion/spec.md's "Repo tracking registration" and "Webhook registration on tracking").

    Args:
        body (RepoRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Repo
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RepoRegistration,
) -> Response[Error | Repo]:
    """Register a repository for tracking

     Stores the supplied token encrypted at rest and creates a webhook on the repository (forge-
    ingestion/spec.md's "Repo tracking registration" and "Webhook registration on tracking").

    Args:
        body (RepoRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Repo]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RepoRegistration,
) -> Error | Repo | None:
    """Register a repository for tracking

     Stores the supplied token encrypted at rest and creates a webhook on the repository (forge-
    ingestion/spec.md's "Repo tracking registration" and "Webhook registration on tracking").

    Args:
        body (RepoRegistration):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Repo
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
