from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.run_detail import RunDetail
from typing import cast



def _get_kwargs(
    run_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/runs/{run_id}/steps".format(run_id=quote(str(run_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | RunDetail | None:
    if response.status_code == 200:
        response_200 = RunDetail.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | RunDetail]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | RunDetail]:
    """ One run's own steps and their statuses

     What a flaky run in GET .../flaky-runs drills down into -- scoped to a single run, so each step's
    forgeUrl points at the exact job that ran, never a different occurrence of the same step name.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RunDetail]
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
    client: AuthenticatedClient | Client,

) -> Error | RunDetail | None:
    """ One run's own steps and their statuses

     What a flaky run in GET .../flaky-runs drills down into -- scoped to a single run, so each step's
    forgeUrl points at the exact job that ran, never a different occurrence of the same step name.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RunDetail
     """


    return sync_detailed(
        run_id=run_id,
client=client,

    ).parsed

async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | RunDetail]:
    """ One run's own steps and their statuses

     What a flaky run in GET .../flaky-runs drills down into -- scoped to a single run, so each step's
    forgeUrl points at the exact job that ran, never a different occurrence of the same step name.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RunDetail]
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
    client: AuthenticatedClient | Client,

) -> Error | RunDetail | None:
    """ One run's own steps and their statuses

     What a flaky run in GET .../flaky-runs drills down into -- scoped to a single run, so each step's
    forgeUrl points at the exact job that ran, never a different occurrence of the same step name.

    Args:
        run_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RunDetail
     """


    return (await asyncio_detailed(
        run_id=run_id,
client=client,

    )).parsed
