import os

import requests
from dacite import from_dict

from awsed.types import AwsedClient, ListCourseResponse, CourseJson, ListTeamsResponse


class DefaultAwsedClient(AwsedClient):
    def __init__(self):
        self.endpoint = os.environ.get('AWSED_ENDPOINT')
        self.awsed_api_key = os.environ.get('AWSED_API_KEY')

    def describe_course(self, course_id: str) -> CourseJson:
        return self.dataclass_request(CourseJson, f"/courses/{course_id}")

    def list_teams_for_course(self, course_id: str) -> ListTeamsResponse:
        return self.dataclass_request(ListTeamsResponse, f"/courses/{course_id}/teams")

    def list_enrollments(self) -> {}:
        return self.json_request(f"/environments/dsmlp/roster")

    def list_courses_by_tag(self, tag: str) -> ListCourseResponse:
        return self.dataclass_request(ListCourseResponse, f"/courses?tag={tag}")

    def list_courses(self) -> ListCourseResponse:
        return self.dataclass_request(ListCourseResponse, f"/courses")

    def json_request(self, url):
        result = requests.get(self.endpoint + url, headers=self.auth())

        return result.json()

    def dataclass_request(self, data_class, url):
        result = requests.get(self.endpoint + url, headers=self.auth())

        return from_dict(data_class=data_class, data=result.json())

    def auth(self):
        headers = {'Authorization': 'AWSEd api_key=' + self.awsed_api_key}
        return headers
