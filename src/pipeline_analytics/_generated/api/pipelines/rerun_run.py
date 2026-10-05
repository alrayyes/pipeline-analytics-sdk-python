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
    run_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/runs/{run_id}/rerun".format(run_id=quote(str(run_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 501:
        response_501 = Error.from_dict(response.json())



        return response_501

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

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
    run_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Error]:
    """ Ask the forge to re-run a concluded run

     Session-only: an API token can't, and there is no MCP tool, because this writes to the forge. Re-
    runs only the failed jobs when the run failed and the whole run otherwise. The forge does the work,
    so `202` means it accepted the request, not that the run has finished. Needs a stored token with
    write access to Actions: GitHub answers a read-only token with `403 forbidden`, and the message says
    which permission is missing. A Forgejo run is `501 unsupported`, since Forgejo has no REST endpoint
    for it (found by search, not checked against a live instance). The token is never logged.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        run_id=run_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | Error | None:
    """ Ask the forge to re-run a concluded run

     Session-only: an API token can't, and there is no MCP tool, because this writes to the forge. Re-
    runs only the failed jobs when the run failed and the whole run otherwise. The forge does the work,
    so `202` means it accepted the request, not that the run has finished. Needs a stored token with
    write access to Actions: GitHub answers a read-only token with `403 forbidden`, and the message says
    which permission is missing. A Forgejo run is `501 unsupported`, since Forgejo has no REST endpoint
    for it (found by search, not checked against a live instance). The token is never logged.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        run_id=run_id,
client=client,

    ).parsed

async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Error]:
    """ Ask the forge to re-run a concluded run

     Session-only: an API token can't, and there is no MCP tool, because this writes to the forge. Re-
    runs only the failed jobs when the run failed and the whole run otherwise. The forge does the work,
    so `202` means it accepted the request, not that the run has finished. Needs a stored token with
    write access to Actions: GitHub answers a read-only token with `403 forbidden`, and the message says
    which permission is missing. A Forgejo run is `501 unsupported`, since Forgejo has no REST endpoint
    for it (found by search, not checked against a live instance). The token is never logged.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        run_id=run_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | Error | None:
    """ Ask the forge to re-run a concluded run

     Session-only: an API token can't, and there is no MCP tool, because this writes to the forge. Re-
    runs only the failed jobs when the run failed and the whole run otherwise. The forge does the work,
    so `202` means it accepted the request, not that the run has finished. Needs a stored token with
    write access to Actions: GitHub answers a read-only token with `403 forbidden`, and the message says
    which permission is missing. A Forgejo run is `501 unsupported`, since Forgejo has no REST endpoint
    for it (found by search, not checked against a live instance). The token is never logged.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        run_id=run_id,
client=client,

    )).parsed
