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
    
    def generate_aws_credentials(self, course: str, role: str) -> str:
        json = {"role": role, "course": course}
        
        result = self.post_request(f"/api/courses/{course}/roles/{role}/credentials", json)
        
        return result.text
    
    def list_courses(self, username: str = None, tag: str = None) -> ListCoursesResultJson:
        return self.dataclass_request(ListCoursesResultJson, "/api/courses", params={'username': username, 'tag': tag})
    
    def create_course(self, course: CourseRequestJson) -> CourseRequestJson:
        result = self.post_request("/api/courses", data=course)
        return result.text
    
    def list_course_launch_profiles(self, course: str) -> ListLaunchProfilesJson:
        return self.dataclass_request(ListLaunchProfilesJson, f"/api/courses/{course}/launch-profiles")

    def create_course_launch_profile(self, course: str, launch_profile: LaunchProfileRequestJson) -> str:
        result = self.post_request(f"/api/courses/{course}/launch-profiles", data=launch_profile.json())
        return result.text
    
    def get_course(self, course: str) -> CourseResult:
        return self.dataclass_request(CourseResult, f"/api/courses/{course}")

    def update_course(self, course: str, course_data: CourseRequestJson) -> str:
        result = self.patch_request(f"/api/courses/{course}", data=course_data.json())
        return result.text
    
    def list_teams(self, course: str) -> TeamsResult:
        return self.dataclass_request(TeamsResult, f"/api/courses/{course}/teams")

    def list_enrollments(self, form: ListEnrollmentsForm, username: str = None) -> EnvironmentEnrollmentResult:
        params = {'form': form}
        if username:
            params['username'] = username
        return self.dataclass_request(EnvironmentEnrollmentResult, "/api/enrollments", params=params)

    def describe_environment(self, slug: str) -> EnvironmentJson:
        return self.dataclass_request(EnvironmentJson, f"/api/environments/{slug}")

    def upload_enrollments(self, csv_content: str, dry_run: bool = False) -> str:
        url = "/api/enrollments"
        params = {'dryRun': dry_run}
        headers = self.auth()
        headers['Content-Type'] = 'text/plain'  # Since the request content type is text/plain
        
        result = self.post_request(url, params=params, headers=headers, data=csv_content)
        
        return result.text

    def list_enrollments_for_environment(self, slug: str) -> EnvironmentEnrollmentResult:
        return self.dataclass_request(EnvironmentEnrollmentResult, f"/api/environments/{slug}/roster")
    
    def list_teams(self, username: str) -> TeamsResult:
        return self.dataclass_request(TeamsResult, "/api/teams", params={'username': username})

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
    
    def patch_request(self, url: str, params: dict = None, headers: dict = None, data: str = None) -> requests.Response:
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
