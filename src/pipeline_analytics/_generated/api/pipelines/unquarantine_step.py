from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.step_quarantine import StepQuarantine
from typing import cast



def _get_kwargs(
    pipeline_id: str,
    step: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/pipelines/{pipeline_id}/steps/{step}/quarantine".format(pipeline_id=quote(str(pipeline_id), safe=""),step=quote(str(step), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | StepQuarantine | None:
    if response.status_code == 200:
        response_200 = StepQuarantine.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | StepQuarantine]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    pipeline_id: str,
    step: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | StepQuarantine]:
    """ Clear a step's quarantine

     Session-only. The step raises the `flaky_step` health signal again if it is still flaky. A step with
    no quarantine is fine: the answer is the same.

    Args:
        pipeline_id (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StepQuarantine]
     """


    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
step=step,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    pipeline_id: str,
    step: str,
    *,
    client: AuthenticatedClient,

) -> Error | StepQuarantine | None:
    """ Clear a step's quarantine

     Session-only. The step raises the `flaky_step` health signal again if it is still flaky. A step with
    no quarantine is fine: the answer is the same.

    Args:
        pipeline_id (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StepQuarantine
     """


    return sync_detailed(
        pipeline_id=pipeline_id,
step=step,
client=client,

    ).parsed

async def asyncio_detailed(
    pipeline_id: str,
    step: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | StepQuarantine]:
    """ Clear a step's quarantine

     Session-only. The step raises the `flaky_step` health signal again if it is still flaky. A step with
    no quarantine is fine: the answer is the same.

    Args:
        pipeline_id (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StepQuarantine]
     """


    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
step=step,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    pipeline_id: str,
    step: str,
    *,
    client: AuthenticatedClient,

) -> Error | StepQuarantine | None:
    """ Clear a step's quarantine

     Session-only. The step raises the `flaky_step` health signal again if it is still flaky. A step with
    no quarantine is fine: the answer is the same.

    Args:
        pipeline_id (str):
        step (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StepQuarantine
     """


    return (await asyncio_detailed(
        pipeline_id=pipeline_id,
step=step,
client=client,

    )).parsed
