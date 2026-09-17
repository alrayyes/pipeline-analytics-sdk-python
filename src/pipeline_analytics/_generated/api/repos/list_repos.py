from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.forge import Forge
from ...models.repo_list import RepoList
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    forge: Forge | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_forge: str | Unset = UNSET
    if not isinstance(forge, Unset):
        json_forge = forge.value

    params["forge"] = json_forge

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/repos",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | RepoList | None:
    if response.status_code == 200:
        response_200 = RepoList.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | RepoList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,

) -> Response[Error | RepoList]:
    """ List tracked repositories

    Args:
        forge (Forge | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RepoList]
     """


    kwargs = _get_kwargs(
        forge=forge,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,

) -> Error | RepoList | None:
    """ List tracked repositories

    Args:
        forge (Forge | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RepoList
     """


    return sync_detailed(
        client=client,
forge=forge,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,

) -> Response[Error | RepoList]:
    """ List tracked repositories

    Args:
        forge (Forge | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RepoList]
     """


    kwargs = _get_kwargs(
        forge=forge,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    forge: Forge | Unset = UNSET,
    limit: int | Unset = UNSET,
    offset: int | Unset = 0,

) -> Error | RepoList | None:
    """ List tracked repositories

    Args:
        forge (Forge | Unset):
        limit (int | Unset):
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RepoList
     """


    return (await asyncio_detailed(
        client=client,
forge=forge,
limit=limit,
offset=offset,

    )).parsed
