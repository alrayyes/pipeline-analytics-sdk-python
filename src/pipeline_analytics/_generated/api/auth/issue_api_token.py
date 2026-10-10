from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_token import ApiToken
from ...models.error import Error
from ...models.issue_api_token_request import IssueApiTokenRequest
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: IssueApiTokenRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/auth/tokens",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ApiToken | Error | None:
    if response.status_code == 201:
        response_201 = ApiToken.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ApiToken | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueApiTokenRequest | Unset = UNSET,

) -> Response[ApiToken | Error]:
    """ Issue a new API token

     Session-only -- an API token can't be used to issue another one. The raw token value is returned
    once, here, and is never recoverable afterward. The token lasts 90 days unless the body asks for
    another lifetime with `ttlSeconds`; anything over 365 days (the ceiling) is clamped to it, and
    `expiresAt` in the response is the expiry actually applied.

    Args:
        body (IssueApiTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiToken | Error]
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
    body: IssueApiTokenRequest | Unset = UNSET,

) -> ApiToken | Error | None:
    """ Issue a new API token

     Session-only -- an API token can't be used to issue another one. The raw token value is returned
    once, here, and is never recoverable afterward. The token lasts 90 days unless the body asks for
    another lifetime with `ttlSeconds`; anything over 365 days (the ceiling) is clamped to it, and
    `expiresAt` in the response is the expiry actually applied.

    Args:
        body (IssueApiTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiToken | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueApiTokenRequest | Unset = UNSET,

) -> Response[ApiToken | Error]:
    """ Issue a new API token

     Session-only -- an API token can't be used to issue another one. The raw token value is returned
    once, here, and is never recoverable afterward. The token lasts 90 days unless the body asks for
    another lifetime with `ttlSeconds`; anything over 365 days (the ceiling) is clamped to it, and
    `expiresAt` in the response is the expiry actually applied.

    Args:
        body (IssueApiTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApiToken | Error]
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
    body: IssueApiTokenRequest | Unset = UNSET,

) -> ApiToken | Error | None:
    """ Issue a new API token

     Session-only -- an API token can't be used to issue another one. The raw token value is returned
    once, here, and is never recoverable afterward. The token lasts 90 days unless the body asks for
    another lifetime with `ttlSeconds`; anything over 365 days (the ceiling) is clamped to it, and
    `expiresAt` in the response is the expiry actually applied.

    Args:
        body (IssueApiTokenRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApiToken | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
