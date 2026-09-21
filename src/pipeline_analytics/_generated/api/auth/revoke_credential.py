from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from typing import cast



def _get_kwargs(
    credential_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/auth/credentials/{credential_id}".format(credential_id=quote(str(credential_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    credential_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Error]:
    """ Revoke a credential

     Session-only, same reasoning as addCredentialOptions. Rejected with 409 if credentialId is the
    account's last remaining credential -- revoking it would leave the account with no way to log in.

    Args:
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        credential_id=credential_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    credential_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | Error | None:
    """ Revoke a credential

     Session-only, same reasoning as addCredentialOptions. Rejected with 409 if credentialId is the
    account's last remaining credential -- revoking it would leave the account with no way to log in.

    Args:
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        credential_id=credential_id,
client=client,

    ).parsed

async def asyncio_detailed(
    credential_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Error]:
    """ Revoke a credential

     Session-only, same reasoning as addCredentialOptions. Rejected with 409 if credentialId is the
    account's last remaining credential -- revoking it would leave the account with no way to log in.

    Args:
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        credential_id=credential_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    credential_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | Error | None:
    """ Revoke a credential

     Session-only, same reasoning as addCredentialOptions. Rejected with 409 if credentialId is the
    account's last remaining credential -- revoking it would leave the account with no way to log in.

    Args:
        credential_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        credential_id=credential_id,
client=client,

    )).parsed
