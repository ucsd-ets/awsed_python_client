import os

import requests
from requests.exceptions import HTTPError

from dacite import from_dict

from awsed.types import *;


class DefaultAwsedClient:
    def __init__(self):
        self.endpoint = os.environ.get('AWSED_ENDPOINT')
        self.awsed_api_key = os.environ.get('AWSED_API_KEY')

    def describe_user(self, username: str) -> UserResultJson:
        return self.dataclass_request(UserResultJson, f"/users/{username}")
    
    def list_user_launch_profiles(self, username: str) -> UserLaunchProfilesResult:
        return self.dataclass_request(UserLaunchProfilesResult, f"/user-launch-profiles/{username}")
    
    def list_enrollments_for_environment(self, form: ListEnrollmentsForm, username: Optional[str] = None) -> EnvironmentEnrollmentResult:
        params = {'form': form}
        if username:
            params['username'] = username
        return self.dataclass_request(EnvironmentEnrollmentResult, "/enrollments", params=params)

    def import_enrollments(self, csv_content: str, dry_run: bool = False) -> str:
        url = "/enrollments"
        params = {'dryRun': dry_run}
        headers = self.auth()
        headers['Content-Type'] = 'text/plain'  # Since the request content type is text/plain
        
        result = self.post_request(url, params=params, headers=headers, data=csv_content)
        
        return result.text
    
    # uncomf under
    def list_pools_under_root(self, pool_root_name: str) -> PoolsResult:
        return self.dataclass_request(PoolsResult, f"/api/pool-roots/{pool_root_name}")
    
    def post_course_environment(self, course_name: str, course_environment: AssociateCourseEnvironmentRequestBody) -> AssociateCourseEnvironmentRequestBody:
        result = self.post_request(f"/api/courses/{course_name}/environments", data=course_environment.json())
        
        return result.text
    
    def get_course_environment(self, course: str, environment: str) -> CourseEnvironmentResult:
        return self.dataclass_request(CourseEnvironmentResult, f"/api/courses/{course}/environments/{environment}")
    
    def patch_course_environment(self, course: str, environment: str, modification: ModifyCourseEnvironmentRequestBody) -> CourseEnvironmentResult:
        result = self.patch_request(f"/api/courses/{course}/environments/{environment}", data=modification.json())
        
        return result.text
    
    def list_course_environments(self, request: ListCourseEnvironmentsRequestBody) -> ListCourseEnvironmentsResultJson:
        return self.dataclass_request(ListCourseEnvironmentsResultJson, "/api/course-environments", params={'request': request})

    def json_request(self, url):
        result = requests.get(self.endpoint + url, headers=self.auth())

        return result.json()

    def dataclass_request(self, data_class, url, params=None):
        result = requests.get(self.endpoint + url, headers=self.auth(), params=params)
        
        self.check_error(result)

        return from_dict(data_class=data_class, data=result.json())
    
    def post_request(self, url: str, params: dict = None, headers: dict = None, data: str = None) -> requests.Response:
        full_url = self.endpoint + url
        headers = headers or self.auth()
        
        result = requests.post(full_url, headers=headers, params=params, data=data)
        self.check_error(result)
        
        return result
    
    def post_request(self, url: str, params: dict = None, headers: dict = None, data: str = None) -> requests.Response:
        full_url = self.endpoint + url
        headers = headers or self.auth()
        
        result = requests.patch(full_url, headers=headers, params=params, data=data)
        self.check_error(result)
        
        return result

    def check_error(self, result):
        if result.status_code >= 400 and result.status_code < 500:            
            raise HTTPError(result.json()['error']['message'])
        if result.status_code >= 500:
            raise HTTPError("Internal server error", result.status_code)

    def auth(self):
        headers = {'Authorization': 'AWSEd api_key=' + self.awsed_api_key}
        return headers
