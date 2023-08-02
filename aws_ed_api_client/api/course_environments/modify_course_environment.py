from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.api_error_result import ApiErrorResult
from ...models.modify_course_environment_request_body import ModifyCourseEnvironmentRequestBody
from ...types import Response


def _get_kwargs(
    course: str,
    environment: str,
    *,
    client: Client,
    json_body: ModifyCourseEnvironmentRequestBody,
) -> Dict[str, Any]:
    url = "{}/api/courses/{course}/environments/{environment}".format(
        client.base_url, course=course, environment=environment
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ApiErrorResult]]:
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ApiErrorResult.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ApiErrorResult.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ApiErrorResult.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ApiErrorResult.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ApiErrorResult]]:
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
    json_body: ModifyCourseEnvironmentRequestBody,
) -> Response[Union[Any, ApiErrorResult]]:
    """Update a course environment

    Args:
        course (str):
        environment (str):
        json_body (ModifyCourseEnvironmentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiErrorResult]]
    """

    kwargs = _get_kwargs(
        course=course,
        environment=environment,
        client=client,
        json_body=json_body,
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
    json_body: ModifyCourseEnvironmentRequestBody,
) -> Optional[Union[Any, ApiErrorResult]]:
    """Update a course environment

    Args:
        course (str):
        environment (str):
        json_body (ModifyCourseEnvironmentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiErrorResult]
    """

    return sync_detailed(
        course=course,
        environment=environment,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    course: str,
    environment: str,
    *,
    client: Client,
    json_body: ModifyCourseEnvironmentRequestBody,
) -> Response[Union[Any, ApiErrorResult]]:
    """Update a course environment

    Args:
        course (str):
        environment (str):
        json_body (ModifyCourseEnvironmentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ApiErrorResult]]
    """

    kwargs = _get_kwargs(
        course=course,
        environment=environment,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    course: str,
    environment: str,
    *,
    client: Client,
    json_body: ModifyCourseEnvironmentRequestBody,
) -> Optional[Union[Any, ApiErrorResult]]:
    """Update a course environment

    Args:
        course (str):
        environment (str):
        json_body (ModifyCourseEnvironmentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ApiErrorResult]
    """

    return (
        await asyncio_detailed(
            course=course,
            environment=environment,
            client=client,
            json_body=json_body,
        )
    ).parsed
