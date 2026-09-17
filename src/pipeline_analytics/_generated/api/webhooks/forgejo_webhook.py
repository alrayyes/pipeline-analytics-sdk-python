from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.forgejo_webhook_body import ForgejoWebhookBody
from ...types import Response


def _get_kwargs(
    *,
    body: ForgejoWebhookBody,
    x_forgejo_signature: str,
    x_forgejo_event: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["X-Forgejo-Signature"] = x_forgejo_signature

    headers["X-Forgejo-Event"] = x_forgejo_event

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhooks/forgejo",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

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
    *,
    client: AuthenticatedClient | Client,
    body: ForgejoWebhookBody,
    x_forgejo_signature: str,
    x_forgejo_event: str,
) -> Response[Any | Error]:
    """Forgejo Actions webhook receiver

    Args:
        x_forgejo_signature (str):
        x_forgejo_event (str):
        body (ForgejoWebhookBody): Forgejo's workflow run/job event payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        x_forgejo_signature=x_forgejo_signature,
        x_forgejo_event=x_forgejo_event,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ForgejoWebhookBody,
    x_forgejo_signature: str,
    x_forgejo_event: str,
) -> Any | Error | None:
    """Forgejo Actions webhook receiver

    Args:
        x_forgejo_signature (str):
        x_forgejo_event (str):
        body (ForgejoWebhookBody): Forgejo's workflow run/job event payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return sync_detailed(
        client=client,
        body=body,
        x_forgejo_signature=x_forgejo_signature,
        x_forgejo_event=x_forgejo_event,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ForgejoWebhookBody,
    x_forgejo_signature: str,
    x_forgejo_event: str,
) -> Response[Any | Error]:
    """Forgejo Actions webhook receiver

    Args:
        x_forgejo_signature (str):
        x_forgejo_event (str):
        body (ForgejoWebhookBody): Forgejo's workflow run/job event payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
    """

    kwargs = _get_kwargs(
        body=body,
        x_forgejo_signature=x_forgejo_signature,
        x_forgejo_event=x_forgejo_event,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ForgejoWebhookBody,
    x_forgejo_signature: str,
    x_forgejo_event: str,
) -> Any | Error | None:
    """Forgejo Actions webhook receiver

    Args:
        x_forgejo_signature (str):
        x_forgejo_event (str):
        body (ForgejoWebhookBody): Forgejo's workflow run/job event payload.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_forgejo_signature=x_forgejo_signature,
            x_forgejo_event=x_forgejo_event,
        )
    ).parsed
