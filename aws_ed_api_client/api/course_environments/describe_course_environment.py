from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.course_environment_result import CourseEnvironmentResult
from ...types import Response


def _get_kwargs(
    course: str,
    environment: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/api/courses/{course}/environments/{environment}".format(
        client.base_url, course=course, environment=environment
    )

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[CourseEnvironmentResult, str]]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(str, response.json())
        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = CourseEnvironmentResult.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.OK:
        response_200 = CourseEnvironmentResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[CourseEnvironmentResult, str]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    course: str,
    environment: str,
    *,
    client: Client,
) -> Response[Union[CourseEnvironmentResult, str]]:
    """Describe a course environment

    Args:
        course (str):
        environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CourseEnvironmentResult, str]]
    """

    kwargs = _get_kwargs(
        course=course,
        environment=environment,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    course: str,
    environment: str,
    *,
    client: Client,
) -> Optional[Union[CourseEnvironmentResult, str]]:
    """Describe a course environment

    Args:
        course (str):
        environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CourseEnvironmentResult, str]
    """

    return sync_detailed(
        course=course,
        environment=environment,
        client=client,
    ).parsed


async def asyncio_detailed(
    course: str,
    environment: str,
    *,
    client: Client,
) -> Response[Union[CourseEnvironmentResult, str]]:
    """Describe a course environment

    Args:
        course (str):
        environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CourseEnvironmentResult, str]]
    """

    kwargs = _get_kwargs(
        course=course,
        environment=environment,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course: str,
    environment: str,
    *,
    client: Client,
) -> Optional[Union[CourseEnvironmentResult, str]]:
    """Describe a course environment

    Args:
        course (str):
        environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CourseEnvironmentResult, str]
    """

    return (
        await asyncio_detailed(
            course=course,
            environment=environment,
            client=client,
        )
    ).parsed
