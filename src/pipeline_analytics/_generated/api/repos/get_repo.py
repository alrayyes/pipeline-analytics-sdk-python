from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.repo import Repo
from typing import cast



def _get_kwargs(
    repo_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/repos/{repo_id}".format(repo_id=quote(str(repo_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Repo | None:
    if response.status_code == 200:
        response_200 = Repo.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

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
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | Repo]:
    """ One tracked repository

     The same repository the list returns for this id, with its token masked, so a caller can name one
    repository without paging the list.

    Args:
        repo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Repo]
     """


    kwargs = _get_kwargs(
        repo_id=repo_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | Repo | None:
    """ One tracked repository

     The same repository the list returns for this id, with its token masked, so a caller can name one
    repository without paging the list.

    Args:
        repo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Repo
     """


    return sync_detailed(
        repo_id=repo_id,
client=client,

    ).parsed

async def asyncio_detailed(
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | Repo]:
    """ One tracked repository

     The same repository the list returns for this id, with its token masked, so a caller can name one
    repository without paging the list.

    Args:
        repo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Repo]
     """


    kwargs = _get_kwargs(
        repo_id=repo_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    repo_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | Repo | None:
    """ One tracked repository

     The same repository the list returns for this id, with its token masked, so a caller can name one
    repository without paging the list.

    Args:
        repo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Repo
     """


    return (await asyncio_detailed(
        repo_id=repo_id,
client=client,

    )).parsed
