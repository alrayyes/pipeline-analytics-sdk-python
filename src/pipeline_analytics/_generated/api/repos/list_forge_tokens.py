from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_forge_tokens_response_200 import ListForgeTokensResponse200
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/forge-tokens",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListForgeTokensResponse200 | None:
    if response.status_code == 200:
        response_200 = ListForgeTokensResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListForgeTokensResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Error | ListForgeTokensResponse200]:
    """ The forge tokens saved for registering repositories

     Session-only. Returns each saved token in its masked form only (`****1234`); no endpoint returns the
    token itself. At most one token is saved per forge and, for Forgejo, per instance URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListForgeTokensResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Error | ListForgeTokensResponse200 | None:
    """ The forge tokens saved for registering repositories

     Session-only. Returns each saved token in its masked form only (`****1234`); no endpoint returns the
    token itself. At most one token is saved per forge and, for Forgejo, per instance URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListForgeTokensResponse200
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Error | ListForgeTokensResponse200]:
    """ The forge tokens saved for registering repositories

     Session-only. Returns each saved token in its masked form only (`****1234`); no endpoint returns the
    token itself. At most one token is saved per forge and, for Forgejo, per instance URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListForgeTokensResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Error | ListForgeTokensResponse200 | None:
    """ The forge tokens saved for registering repositories

     Session-only. Returns each saved token in its masked form only (`****1234`); no endpoint returns the
    token itself. At most one token is saved per forge and, for Forgejo, per instance URL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListForgeTokensResponse200
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
