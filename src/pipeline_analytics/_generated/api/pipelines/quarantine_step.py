from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.quarantine_request import QuarantineRequest
from ...models.step_quarantine import StepQuarantine
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    pipeline_id: str,
    step: str,
    *,
    body: QuarantineRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/pipelines/{pipeline_id}/steps/{step}/quarantine".format(pipeline_id=quote(str(pipeline_id), safe=""),step=quote(str(step), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

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
    body: QuarantineRequest | Unset = UNSET,

) -> Response[Error | StepQuarantine]:
    """ Mark a flaky step as known, so it stops making its pipeline unhealthy

     Session-only: an API token or an MCP client can read a quarantine but not set one. A quarantined
    step stays in the flaky list with its figures unchanged, but no longer raises the pipeline's
    `flaky_step` health signal or counts in the flaky-step ratio. The mark lasts 30 days from now;
    marking a step that is already quarantined renews it and replaces its note. It is recorded in this
    service only: no forge is contacted. The step isn't checked to be flaky, so a mark on a step that
    isn't does nothing until it is.

    Args:
        pipeline_id (str):
        step (str):
        body (QuarantineRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StepQuarantine]
     """


    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
step=step,
body=body,

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
    body: QuarantineRequest | Unset = UNSET,

) -> Error | StepQuarantine | None:
    """ Mark a flaky step as known, so it stops making its pipeline unhealthy

     Session-only: an API token or an MCP client can read a quarantine but not set one. A quarantined
    step stays in the flaky list with its figures unchanged, but no longer raises the pipeline's
    `flaky_step` health signal or counts in the flaky-step ratio. The mark lasts 30 days from now;
    marking a step that is already quarantined renews it and replaces its note. It is recorded in this
    service only: no forge is contacted. The step isn't checked to be flaky, so a mark on a step that
    isn't does nothing until it is.

    Args:
        pipeline_id (str):
        step (str):
        body (QuarantineRequest | Unset):

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
body=body,

    ).parsed

async def asyncio_detailed(
    pipeline_id: str,
    step: str,
    *,
    client: AuthenticatedClient,
    body: QuarantineRequest | Unset = UNSET,

) -> Response[Error | StepQuarantine]:
    """ Mark a flaky step as known, so it stops making its pipeline unhealthy

     Session-only: an API token or an MCP client can read a quarantine but not set one. A quarantined
    step stays in the flaky list with its figures unchanged, but no longer raises the pipeline's
    `flaky_step` health signal or counts in the flaky-step ratio. The mark lasts 30 days from now;
    marking a step that is already quarantined renews it and replaces its note. It is recorded in this
    service only: no forge is contacted. The step isn't checked to be flaky, so a mark on a step that
    isn't does nothing until it is.

    Args:
        pipeline_id (str):
        step (str):
        body (QuarantineRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StepQuarantine]
     """


    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
step=step,
body=body,

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
    body: QuarantineRequest | Unset = UNSET,

) -> Error | StepQuarantine | None:
    """ Mark a flaky step as known, so it stops making its pipeline unhealthy

     Session-only: an API token or an MCP client can read a quarantine but not set one. A quarantined
    step stays in the flaky list with its figures unchanged, but no longer raises the pipeline's
    `flaky_step` health signal or counts in the flaky-step ratio. The mark lasts 30 days from now;
    marking a step that is already quarantined renews it and replaces its note. It is recorded in this
    service only: no forge is contacted. The step isn't checked to be flaky, so a mark on a step that
    isn't does nothing until it is.

    Args:
        pipeline_id (str):
        step (str):
        body (QuarantineRequest | Unset):

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
body=body,

    )).parsed
