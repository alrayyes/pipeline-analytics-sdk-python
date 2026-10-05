from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.save_forge_token_request import SaveForgeTokenRequest
from ...models.saved_forge_token import SavedForgeToken
from typing import cast



def _get_kwargs(
    *,
    body: SaveForgeTokenRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/forge-tokens",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SavedForgeToken | None:
    if response.status_code == 200:
        response_200 = SavedForgeToken.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())



        return response_413

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SavedForgeToken]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SaveForgeTokenRequest,

) -> Response[Error | SavedForgeToken]:
    """ Save a forge token, replacing the one for that forge and instance

     Session-only. Stores the token encrypted at rest, like a repo's token. Saving for a forge and
    instance that already has one replaces it. The token isn't checked against the forge here:
    registering with it is what finds out whether it works.

    Args:
        body (SaveForgeTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SavedForgeToken]
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
    client: AuthenticatedClient,
    body: SaveForgeTokenRequest,

) -> Error | SavedForgeToken | None:
    """ Save a forge token, replacing the one for that forge and instance

     Session-only. Stores the token encrypted at rest, like a repo's token. Saving for a forge and
    instance that already has one replaces it. The token isn't checked against the forge here:
    registering with it is what finds out whether it works.

    Args:
        body (SaveForgeTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SavedForgeToken
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SaveForgeTokenRequest,

) -> Response[Error | SavedForgeToken]:
    """ Save a forge token, replacing the one for that forge and instance

     Session-only. Stores the token encrypted at rest, like a repo's token. Saving for a forge and
    instance that already has one replaces it. The token isn't checked against the forge here:
    registering with it is what finds out whether it works.

    Args:
        body (SaveForgeTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SavedForgeToken]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SaveForgeTokenRequest,

) -> Error | SavedForgeToken | None:
    """ Save a forge token, replacing the one for that forge and instance

     Session-only. Stores the token encrypted at rest, like a repo's token. Saving for a forge and
    instance that already has one replaces it. The token isn't checked against the forge here:
    registering with it is what finds out whether it works.

    Args:
        body (SaveForgeTokenRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SavedForgeToken
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
