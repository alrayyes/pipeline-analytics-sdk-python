from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.settings import Settings
from ...models.settings_update import SettingsUpdate
from typing import cast



def _get_kwargs(
    *,
    body: SettingsUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/settings",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Settings | None:
    if response.status_code == 200:
        response_200 = Settings.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Settings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SettingsUpdate,

) -> Response[Error | Settings]:
    """ Update one or more settings

     A key present with a value sets it. A key present with JSON null clears it, reverting to its
    documented default on the next read -- this is also how the Pipelines page's "Reset filters" works:
    a single PATCH setting pipelinesHealthFilter/pipelinesRepoSelector/pipelinesSortOrder to null. A key
    absent from the body is left untouched. An invalid key or an enum value outside its documented set
    rejects the whole request; nothing already stored changes.

    Args:
        body (SettingsUpdate): Every property is optional; an absent one is left untouched. A
            property set to null clears it back to its documented default instead of setting it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Settings]
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
    client: AuthenticatedClient | Client,
    body: SettingsUpdate,

) -> Error | Settings | None:
    """ Update one or more settings

     A key present with a value sets it. A key present with JSON null clears it, reverting to its
    documented default on the next read -- this is also how the Pipelines page's "Reset filters" works:
    a single PATCH setting pipelinesHealthFilter/pipelinesRepoSelector/pipelinesSortOrder to null. A key
    absent from the body is left untouched. An invalid key or an enum value outside its documented set
    rejects the whole request; nothing already stored changes.

    Args:
        body (SettingsUpdate): Every property is optional; an absent one is left untouched. A
            property set to null clears it back to its documented default instead of setting it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Settings
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SettingsUpdate,

) -> Response[Error | Settings]:
    """ Update one or more settings

     A key present with a value sets it. A key present with JSON null clears it, reverting to its
    documented default on the next read -- this is also how the Pipelines page's "Reset filters" works:
    a single PATCH setting pipelinesHealthFilter/pipelinesRepoSelector/pipelinesSortOrder to null. A key
    absent from the body is left untouched. An invalid key or an enum value outside its documented set
    rejects the whole request; nothing already stored changes.

    Args:
        body (SettingsUpdate): Every property is optional; an absent one is left untouched. A
            property set to null clears it back to its documented default instead of setting it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Settings]
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
    client: AuthenticatedClient | Client,
    body: SettingsUpdate,

) -> Error | Settings | None:
    """ Update one or more settings

     A key present with a value sets it. A key present with JSON null clears it, reverting to its
    documented default on the next read -- this is also how the Pipelines page's "Reset filters" works:
    a single PATCH setting pipelinesHealthFilter/pipelinesRepoSelector/pipelinesSortOrder to null. A key
    absent from the body is left untouched. An invalid key or an enum value outside its documented set
    rejects the whole request; nothing already stored changes.

    Args:
        body (SettingsUpdate): Every property is optional; an absent one is left untouched. A
            property set to null clears it back to its documented default instead of setting it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Settings
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
