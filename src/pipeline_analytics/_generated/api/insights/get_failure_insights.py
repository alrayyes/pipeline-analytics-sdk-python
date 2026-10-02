from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.failure_insights import FailureInsights
from ...models.forge import Forge
from ...models.get_failure_insights_window import GetFailureInsightsWindow
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    window: GetFailureInsightsWindow | Unset = GetFailureInsightsWindow.VALUE_1,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["repoId"] = repo_id

    json_forge: str | Unset = UNSET
    if not isinstance(forge, Unset):
        json_forge = forge.value

    params["forge"] = json_forge

    json_window: str | Unset = UNSET
    if not isinstance(window, Unset):
        json_window = window.value

    params["window"] = json_window


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/insights/failures",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | FailureInsights | None:
    if response.status_code == 200:
        response_200 = FailureInsights.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | FailureInsights]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    window: GetFailureInsightsWindow | Unset = GetFailureInsightsWindow.VALUE_1,

) -> Response[Error | FailureInsights]:
    """ Failure aggregates over a window -- pass rate, MTTR, failure distribution, root-cause groups

     Backs the failure overview and root-cause views. "Stage" means step: forges expose workflows, jobs
    and steps but no stage taxonomy, so the distribution and the groups are by failing step name.
    `passRateDelta` compares against the preceding window of equal length. Failure categories are
    heuristic (step conclusion and name), never log-derived; a failure no rule matches is
    `uncategorised`.

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        window (GetFailureInsightsWindow | Unset):  Default: GetFailureInsightsWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FailureInsights]
     """


    kwargs = _get_kwargs(
        repo_id=repo_id,
forge=forge,
window=window,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    window: GetFailureInsightsWindow | Unset = GetFailureInsightsWindow.VALUE_1,

) -> Error | FailureInsights | None:
    """ Failure aggregates over a window -- pass rate, MTTR, failure distribution, root-cause groups

     Backs the failure overview and root-cause views. "Stage" means step: forges expose workflows, jobs
    and steps but no stage taxonomy, so the distribution and the groups are by failing step name.
    `passRateDelta` compares against the preceding window of equal length. Failure categories are
    heuristic (step conclusion and name), never log-derived; a failure no rule matches is
    `uncategorised`.

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        window (GetFailureInsightsWindow | Unset):  Default: GetFailureInsightsWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FailureInsights
     """


    return sync_detailed(
        client=client,
repo_id=repo_id,
forge=forge,
window=window,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    window: GetFailureInsightsWindow | Unset = GetFailureInsightsWindow.VALUE_1,

) -> Response[Error | FailureInsights]:
    """ Failure aggregates over a window -- pass rate, MTTR, failure distribution, root-cause groups

     Backs the failure overview and root-cause views. "Stage" means step: forges expose workflows, jobs
    and steps but no stage taxonomy, so the distribution and the groups are by failing step name.
    `passRateDelta` compares against the preceding window of equal length. Failure categories are
    heuristic (step conclusion and name), never log-derived; a failure no rule matches is
    `uncategorised`.

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        window (GetFailureInsightsWindow | Unset):  Default: GetFailureInsightsWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FailureInsights]
     """


    kwargs = _get_kwargs(
        repo_id=repo_id,
forge=forge,
window=window,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    repo_id: str | Unset = UNSET,
    forge: Forge | Unset = UNSET,
    window: GetFailureInsightsWindow | Unset = GetFailureInsightsWindow.VALUE_1,

) -> Error | FailureInsights | None:
    """ Failure aggregates over a window -- pass rate, MTTR, failure distribution, root-cause groups

     Backs the failure overview and root-cause views. "Stage" means step: forges expose workflows, jobs
    and steps but no stage taxonomy, so the distribution and the groups are by failing step name.
    `passRateDelta` compares against the preceding window of equal length. Failure categories are
    heuristic (step conclusion and name), never log-derived; a failure no rule matches is
    `uncategorised`.

    Args:
        repo_id (str | Unset):
        forge (Forge | Unset):
        window (GetFailureInsightsWindow | Unset):  Default: GetFailureInsightsWindow.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FailureInsights
     """


    return (await asyncio_detailed(
        client=client,
repo_id=repo_id,
forge=forge,
window=window,

    )).parsed
