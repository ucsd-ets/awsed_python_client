from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.environment_enrollment_result import EnvironmentEnrollmentResult
from ...types import Response


def _get_kwargs(
    slug: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/environments/{slug}/roster".format(client.base_url, slug=slug)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[List["EnvironmentEnrollmentResult"], str]]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(str, response.json())
        return response_403
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = []
        _response_401 = response.json()
        for response_401_item_data in _response_401:
            response_401_item = EnvironmentEnrollmentResult.from_dict(response_401_item_data)

            response_401.append(response_401_item)

        return response_401
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EnvironmentEnrollmentResult.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[List["EnvironmentEnrollmentResult"], str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    slug: str,
    *,
    client: Client,
) -> Response[Union[List["EnvironmentEnrollmentResult"], str]]:
    """List enrollments for environment

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['EnvironmentEnrollmentResult'], str]]
    """

    kwargs = _get_kwargs(
        slug=slug,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    slug: str,
    *,
    client: Client,
) -> Optional[Union[List["EnvironmentEnrollmentResult"], str]]:
    """List enrollments for environment

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['EnvironmentEnrollmentResult'], str]
    """

    return sync_detailed(
        slug=slug,
        client=client,
    ).parsed


async def asyncio_detailed(
    slug: str,
    *,
    client: Client,
) -> Response[Union[List["EnvironmentEnrollmentResult"], str]]:
    """List enrollments for environment

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[List['EnvironmentEnrollmentResult'], str]]
    """

    kwargs = _get_kwargs(
        slug=slug,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    slug: str,
    *,
    client: Client,
) -> Optional[Union[List["EnvironmentEnrollmentResult"], str]]:
    """List enrollments for environment

    Args:
        slug (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[List['EnvironmentEnrollmentResult'], str]
    """

    return (
        await asyncio_detailed(
            slug=slug,
            client=client,
        )
    ).parsed
