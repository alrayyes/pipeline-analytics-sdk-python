from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.web_authn_creation_options import WebAuthnCreationOptions
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/credentials/options",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | WebAuthnCreationOptions | None:
    if response.status_code == 200:
        response_200 = WebAuthnCreationOptions.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | WebAuthnCreationOptions]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Error | WebAuthnCreationOptions]:
    """ Begin an authenticated "add another passkey" ceremony

     Session-only -- an API token can't enroll another credential on the account any more than it can
    mint another token. Distinct from POST /api/auth/register/options: that ceremony is the anonymous
    first-run registration and only ever runs once per account; this one runs from within an existing
    session and excludes credentials already registered to it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebAuthnCreationOptions]
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

) -> Error | WebAuthnCreationOptions | None:
    """ Begin an authenticated "add another passkey" ceremony

     Session-only -- an API token can't enroll another credential on the account any more than it can
    mint another token. Distinct from POST /api/auth/register/options: that ceremony is the anonymous
    first-run registration and only ever runs once per account; this one runs from within an existing
    session and excludes credentials already registered to it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebAuthnCreationOptions
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Error | WebAuthnCreationOptions]:
    """ Begin an authenticated "add another passkey" ceremony

     Session-only -- an API token can't enroll another credential on the account any more than it can
    mint another token. Distinct from POST /api/auth/register/options: that ceremony is the anonymous
    first-run registration and only ever runs once per account; this one runs from within an existing
    session and excludes credentials already registered to it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebAuthnCreationOptions]
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

) -> Error | WebAuthnCreationOptions | None:
    """ Begin an authenticated "add another passkey" ceremony

     Session-only -- an API token can't enroll another credential on the account any more than it can
    mint another token. Distinct from POST /api/auth/register/options: that ceremony is the anonymous
    first-run registration and only ever runs once per account; this one runs from within an existing
    session and excludes credentials already registered to it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebAuthnCreationOptions
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
