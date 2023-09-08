import json
import os

import requests
from requests.exceptions import HTTPError

from dacite import from_dict
from awsed.types import *
from awsed.abstract_client import AbstractAwsedClient


class DefaultAwsedClient(AbstractAwsedClient):
    def describe_user(self, username: str) -> UserResultJson:
        return self.dataclass_request(UserResultJson, f"/users/{username}")

    def list_user_launch_profiles(self, username: str) -> UserLaunchProfilesResult:
        return self.dataclass_request(
            UserLaunchProfilesResult, f"/user-launch-profiles/{username}"
        )

    def list_enrollments(
        self, form: ListEnrollmentsForm, username: Optional[str] = None
    ) -> EnvironmentEnrollmentResult:
        params = {"form": form}
        if username:
            params["username"] = username
        return EnvironmentEnrollmentResult(
            self.list_of_dataclass_request(
                EnrollmentResult, "/enrollments", params=params
            )
        )

    def import_enrollments(self, csv_content: str, dry_run: bool = False) -> str:
        url = "/enrollments"
        params = {"dryRun": dry_run}
        headers = self.auth()
        headers[
            "Content-Type"
        ] = "text/plain"  # Since the request content type is text/plain

        result = self.post_request(
            url, params=params, headers=headers, data=csv_content
        )

        return True

    # uncomf under
    def list_pools_under_root(self, pool_root_name: str) -> PoolsResult:
        return self.dataclass_request(PoolsResult, f"/pool-roots/{pool_root_name}")

    def post_course_environment(
        self,
        course_name: str,
        course_environment: AssociateCourseEnvironmentRequestBody,
    ) -> AssociateCourseEnvironmentRequestBody:
        result = self.post_request(
            f"/courses/{course_name}/environments", data=course_environment
        )

        return True

    def get_course_environment(
        self, course: str, environment: str
    ) -> CourseEnvironmentResult:
        return self.dataclass_request(
            CourseEnvironmentResult, f"/courses/{course}/environments/{environment}"
        )

    def patch_course_environment(
        self,
        course: str,
        environment: str,
        modification: ModifyCourseEnvironmentRequestBody,
    ) -> CourseEnvironmentResult:
        result = self.patch_request(
            f"/courses/{course}/environments/{environment}", data=modification
        )

        # Return true since we didn't error out ig and idk the expected response
        return True
        # return result

    def list_course_environments(
        self, request: ListCourseEnvironmentsRequestBody
    ) -> ListCourseEnvironmentsResultJson:
        return self.dataclass_request(
            ListCourseEnvironmentsResultJson,
            "/course-environments",
            params={"request": request},
        )

    def generate_aws_credentials(self, course: str, role: str) -> str:
        json = {"role": role, "course": course}

        result = self.post_request(f"/courses/{course}/roles/{role}/credentials", json)

        return True

    def list_courses(
        self, username: str = None, tag: str = None
    ) -> ListCoursesResultJson:
        return self.dataclass_request(
            ListCoursesResultJson, "/courses", params={"username": username, "tag": tag}
        )

    def create_course(self, course: CourseRequestJson) -> CourseRequestJson:
        result = self.post_request("/courses", data=course)
        return True

    def list_course_launch_profiles(self, course: str) -> ListLaunchProfilesJson:
        return self.dataclass_request(
            ListLaunchProfilesJson, f"/courses/{course}/launch-profiles"
        )

    def create_course_launch_profile(
        self, course: str, launch_profile: LaunchProfileRequestJson
    ) -> str:
        result = self.post_request(
            f"/courses/{course}/launch-profiles", data=launch_profile
        )
        return True

    def describe_course(self, course: str) -> CourseResult:
        return self.dataclass_request(CourseResult, f"/courses/{course}")

    def update_course(self, course: str, course_data: CourseRequestJson) -> str:
        result = self.patch_request(f"/courses/{course}", data=course_data)
        return True

    def list_course_teams(self, course: str) -> TeamsResult:
        return self.dataclass_request(TeamsResult, f"/courses/{course}/teams")

    def list_enrollments_slug(self, slug: str) -> EnvironmentJson:
        return self.dataclass_request(EnvironmentJson, f"/environments/{slug}")

    def list_enrollments_roster(self, slug: str) -> EnvironmentEnrollmentResult:
        return EnvironmentEnrollmentResult(
            self.list_of_dataclass_request(
                EnrollmentResult, f"/environments/{slug}/roster"
            )
        )

    def upload_enrollments(self, csv_content: str, dry_run: bool = False) -> str:
        url = "/enrollments"
        params = {"dryRun": dry_run}
        headers = self.auth()
        headers[
            "Content-Type"
        ] = "text/plain"  # Since the request content type is text/plain

        result = self.post_request(
            url, params=params, headers=headers, data=csv_content
        )

        return True

    def list_teams(self, username: str) -> TeamsResult:
        return self.dataclass_request(
            TeamsResult, "/teams", params={"username": username}
        )

    def json_request(self, url):
        result = requests.get(self.endpoint + url, headers=self.auth())

        return result.json()

    def dataclass_request(
        self, data_class, url, params=None, noneIfNotFound=True, assertNotNone=False
    ):
        result = self.get_request(url, params)

        self.check_error(result)
        missing = self.is_result_missing(result)

        if missing and assertNotNone:
            raise AssertionError(f"Expected {url} to not be null")

        if missing and noneIfNotFound:
            return None

        # May throw a DaciteError
        return from_dict(data_class=data_class, data=result.json())

    def list_of_dataclass_request(
        self, data_class, url, params=None, noneIfNotFound=True, assertNotNone=False
    ):
        result = self.get_request(url, params)

        self.check_error(result)
        missing = self.is_result_missing(result)

        if missing and assertNotNone:
            raise AssertionError(f"Expected {url} to not be null")

        if missing and noneIfNotFound:
            return None

        output = []
        result = result.json()
        for entry in result:
            output.append(from_dict(data_class=data_class, data=entry))
        return output

    def is_result_missing(self, result):
        missing = (
            result.text == "null"
            or result.text == ""
            or result.json() is None
            or result.json() == {}
        )

        return missing

    def get_request(self, url, params):
        return requests.get(
            self.endpoint + url,
            headers=self.auth(),
            params=params,
            timeout=self.global_timeout,
        )

    def post_request(
        self, url: str, params: dict = None, headers: dict = None, data: str = None
    ) -> requests.Response:
        full_url = self.endpoint + url
        headers = headers or self.auth()

        result = requests.post(
            full_url,
            headers=headers,
            params=params,
            data=data,
            timeout=self.global_timeout,
        )
        self.check_error(result)

        return result

    def patch_request(
        self, url: str, params: dict = None, headers: dict = None, data: str = None
    ) -> requests.Response:
        full_url = self.endpoint + url
        headers = headers or self.auth()

        result = requests.patch(
            full_url,
            headers=headers,
            params=params,
            data=data,
            timeout=self.global_timeout,
        )

        print(result.text)
        self.check_error(result)

        return result

    def check_error(self, result):
        print(result.text)
        result_json = result.json()
        if result.status_code >= 400 and result.status_code < 500:
            if result_json["error"]:
                raise HTTPError(result_json["error"]["message"])
        if result.status_code >= 500:
            raise HTTPError("Internal server error", result.status_code)

    def auth(self):
        headers = {"Authorization": "AWSEd api_key=" + self.awsed_api_key}
        return headers
