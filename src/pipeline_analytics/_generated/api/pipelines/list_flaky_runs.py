from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.flaky_run import FlakyRun
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    pipeline_id: str,
    *,
    step: str,
    window: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["step"] = step

    params["window"] = window


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/pipelines/{pipeline_id}/flaky-runs".format(pipeline_id=quote(str(pipeline_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[FlakyRun] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = FlakyRun.from_dict(response_200_item_data)



            response_200.append(response_200_item)

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[FlakyRun]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pipeline_id: str,
    *,
    client: AuthenticatedClient | Client,
    step: str,
    window: str | Unset = UNSET,

) -> Response[Error | list[FlakyRun]]:
    """ Every run in which one named step failed, most-recent-first

     The step-scoped drill-down from a flaky (or previously flaky) step in GET .../steps -- lets a click
    land on the run that actually failed instead of an aggregate link that may point at a run which has
    since passed. Available regardless of the pipeline's current health status, since a step's failures
    can age out of the live window before anyone gets a chance to look.

    Args:
        pipeline_id (str):
        step (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[FlakyRun]]
     """


    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
step=step,
window=window,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    pipeline_id: str,
    *,
    client: AuthenticatedClient | Client,
    step: str,
    window: str | Unset = UNSET,

) -> Error | list[FlakyRun] | None:
    """ Every run in which one named step failed, most-recent-first

     The step-scoped drill-down from a flaky (or previously flaky) step in GET .../steps -- lets a click
    land on the run that actually failed instead of an aggregate link that may point at a run which has
    since passed. Available regardless of the pipeline's current health status, since a step's failures
    can age out of the live window before anyone gets a chance to look.

    Args:
        pipeline_id (str):
        step (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[FlakyRun]
     """


    return sync_detailed(
        pipeline_id=pipeline_id,
client=client,
step=step,
window=window,

    ).parsed

async def asyncio_detailed(
    pipeline_id: str,
    *,
    client: AuthenticatedClient | Client,
    step: str,
    window: str | Unset = UNSET,

) -> Response[Error | list[FlakyRun]]:
    """ Every run in which one named step failed, most-recent-first

     The step-scoped drill-down from a flaky (or previously flaky) step in GET .../steps -- lets a click
    land on the run that actually failed instead of an aggregate link that may point at a run which has
    since passed. Available regardless of the pipeline's current health status, since a step's failures
    can age out of the live window before anyone gets a chance to look.

    Args:
        pipeline_id (str):
        step (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[FlakyRun]]
     """


    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
step=step,
window=window,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    pipeline_id: str,
    *,
    client: AuthenticatedClient | Client,
    step: str,
    window: str | Unset = UNSET,

) -> Error | list[FlakyRun] | None:
    """ Every run in which one named step failed, most-recent-first

     The step-scoped drill-down from a flaky (or previously flaky) step in GET .../steps -- lets a click
    land on the run that actually failed instead of an aggregate link that may point at a run which has
    since passed. Available regardless of the pipeline's current health status, since a step's failures
    can age out of the live window before anyone gets a chance to look.

    Args:
        pipeline_id (str):
        step (str):
        window (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[FlakyRun]
     """


    return (await asyncio_detailed(
        pipeline_id=pipeline_id,
client=client,
step=step,
window=window,

    )).parsed
