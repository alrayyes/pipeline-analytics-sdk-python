from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.job_log import JobLog
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    run_id: str,
    job_id: str,
    *,
    lines: int | Unset = 200,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["lines"] = lines


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/runs/{run_id}/jobs/{job_id}/log".format(run_id=quote(str(run_id), safe=""),job_id=quote(str(job_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | JobLog | None:
    if response.status_code == 200:
        response_200 = JobLog.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | JobLog]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    run_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    lines: int | Unset = 200,

) -> Response[Error | JobLog]:
    """ The tail of one job's log, fetched from the forge on demand

     Fetches the log from the originating forge when asked and never stores it, so the SQLite file
    doesn't grow with log volume and a log can't outlive the forge's own retention. Returns the last
    `lines` lines (200 by default). ANSI escape sequences are passed through untouched: the client
    renders and escapes them, and must never insert a line as HTML. A forge with no log API (Forgejo
    before v16, which has none), an expired log, or a token without access answers `200` with
    `available: false` and a `reason`, so the client can say so and still show `forgeUrl`. An unknown
    run or job is `404`. GitHub's log URL is a redirect that expires after a minute, so it is followed
    server-side and never handed to the client.

    Args:
        run_id (str):
        job_id (str):
        lines (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | JobLog]
     """


    kwargs = _get_kwargs(
        run_id=run_id,
job_id=job_id,
lines=lines,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    run_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    lines: int | Unset = 200,

) -> Error | JobLog | None:
    """ The tail of one job's log, fetched from the forge on demand

     Fetches the log from the originating forge when asked and never stores it, so the SQLite file
    doesn't grow with log volume and a log can't outlive the forge's own retention. Returns the last
    `lines` lines (200 by default). ANSI escape sequences are passed through untouched: the client
    renders and escapes them, and must never insert a line as HTML. A forge with no log API (Forgejo
    before v16, which has none), an expired log, or a token without access answers `200` with
    `available: false` and a `reason`, so the client can say so and still show `forgeUrl`. An unknown
    run or job is `404`. GitHub's log URL is a redirect that expires after a minute, so it is followed
    server-side and never handed to the client.

    Args:
        run_id (str):
        job_id (str):
        lines (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | JobLog
     """


    return sync_detailed(
        run_id=run_id,
job_id=job_id,
client=client,
lines=lines,

    ).parsed

async def asyncio_detailed(
    run_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    lines: int | Unset = 200,

) -> Response[Error | JobLog]:
    """ The tail of one job's log, fetched from the forge on demand

     Fetches the log from the originating forge when asked and never stores it, so the SQLite file
    doesn't grow with log volume and a log can't outlive the forge's own retention. Returns the last
    `lines` lines (200 by default). ANSI escape sequences are passed through untouched: the client
    renders and escapes them, and must never insert a line as HTML. A forge with no log API (Forgejo
    before v16, which has none), an expired log, or a token without access answers `200` with
    `available: false` and a `reason`, so the client can say so and still show `forgeUrl`. An unknown
    run or job is `404`. GitHub's log URL is a redirect that expires after a minute, so it is followed
    server-side and never handed to the client.

    Args:
        run_id (str):
        job_id (str):
        lines (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | JobLog]
     """


    kwargs = _get_kwargs(
        run_id=run_id,
job_id=job_id,
lines=lines,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    run_id: str,
    job_id: str,
    *,
    client: AuthenticatedClient | Client,
    lines: int | Unset = 200,

) -> Error | JobLog | None:
    """ The tail of one job's log, fetched from the forge on demand

     Fetches the log from the originating forge when asked and never stores it, so the SQLite file
    doesn't grow with log volume and a log can't outlive the forge's own retention. Returns the last
    `lines` lines (200 by default). ANSI escape sequences are passed through untouched: the client
    renders and escapes them, and must never insert a line as HTML. A forge with no log API (Forgejo
    before v16, which has none), an expired log, or a token without access answers `200` with
    `available: false` and a `reason`, so the client can say so and still show `forgeUrl`. An unknown
    run or job is `404`. GitHub's log URL is a redirect that expires after a minute, so it is followed
    server-side and never handed to the client.

    Args:
        run_id (str):
        job_id (str):
        lines (int | Unset):  Default: 200.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | JobLog
     """


    return (await asyncio_detailed(
        run_id=run_id,
job_id=job_id,
client=client,
lines=lines,

    )).parsed
