import os
from hamcrest import assert_that, equal_to
from awsed.client import DefaultAwsedClient
from awsed.types import ListCourseResponse, CourseCourseResponse, CourseJson, FileSystemJson, UserJson, \
    ListTeamsResponse, TeamJson


class TestAwsedClient:
    # noinspection PyMethodMayBeStatic
    def setup_method(self) -> None:
        os.environ['AWSED_ENDPOINT'] = 'https://awsed.ucsd.edu/api'
        os.environ['AWSED_API_KEY'] = "1234"

    # noinspection PyMethodMayBeStatic
    def teardown_method(self) -> None:
        os.environ.pop('AWSED_ENDPOINT')
        os.environ.pop('AWSED_API_KEY')

    def test_list_courses_by_tag(self, requests_mock):
        """test list courses by tag"""
        requests_mock.get('https://awsed.ucsd.edu/api/courses?tag=teams-enabled', text="""
            {
                "courses": [
                    {
                        "courseId": "BENG134_FA20_A00"
                    },
                    {
                        "courseId": "BIPN145_FA20_A00"
                    }
                ]
            }
              """)
        c = DefaultAwsedClient()
        courses = c.list_courses_by_tag("teams-enabled")

        assert_that(courses, equal_to(
            ListCourseResponse(courses=[
                CourseCourseResponse(courseId="BENG134_FA20_A00"),
                CourseCourseResponse(courseId="BIPN145_FA20_A00")

            ])
        ))

    def test_list_courses_by_tag2(self, requests_mock):
        """test list courses by tag"""
        requests_mock.get('https://awsed.ucsd.edu/api/courses?tag=tag2', text="""
            {
                "courses": [
                    {
                        "courseId": "COGS108_FA20_A00"
                    },
                    {
                        "courseId": "COGS18_FA20_A00"
                    }
                ]
            }
              """)
        c = DefaultAwsedClient()
        courses = c.list_courses_by_tag("tag2")

        assert_that(courses, equal_to(
            ListCourseResponse(courses=[
                CourseCourseResponse(courseId="COGS108_FA20_A00"),
                CourseCourseResponse(courseId="COGS18_FA20_A00")

            ])
        ))

    def test_list_courses_by_tag4(self, requests_mock):
        """test list courses by tag"""
        requests_mock.get('https://awsed.ucsd.edu/api/courses?tag=tag3', text="""
            {
                "courses": []
            }
              """)
        c = DefaultAwsedClient()
        courses = c.list_courses_by_tag("tag3")

        assert_that(courses, equal_to(
            ListCourseResponse(courses=[])
        ))

    def test_list_courses_by_tag3(self, requests_mock):
        """test list courses by tag"""
        requests_mock.get('https://awsed.ucsd.edu/api/courses', text="""
            {
                "courses": []
            }
              """)
        c = DefaultAwsedClient()
        courses = c.list_courses()

        assert_that(courses, equal_to(
            ListCourseResponse(courses=[])
        ))

    def test_describe_course(self, requests_mock):
        """test list courses by tag"""
        requests_mock.get('https://awsed.ucsd.edu/api/courses/cse101', text="""
            {
                "courseId": "cse101",
                "grader": {
                    "username": "grader",
                    "uid": 1234
                },
                "fileSystem": {
                    "identifier": "test-workspaces",
                    "server": "nfs.example.com",
                    "path": "/export/workspaces"
                }
            }
              """)
        c = DefaultAwsedClient()
        courses = c.describe_course("cse101")

        assert_that(courses, equal_to(CourseJson(
            courseId='cse101',
            tags=None,
            enrollments=[],
            fileSystem=FileSystemJson(
                identifier='test-workspaces',
                server='nfs.example.com',
                path='/export/workspaces'),
            grader=UserJson(username='grader', uid=1234))
        ))

    def test_course_teams(self, requests_mock):
        """test list courses by tag"""

        requests_mock.get('https://awsed.ucsd.edu/api/courses/cse101/teams', text="""
            {"teams": [
            {
                "gid": 3000,
                "members": [
                    {
                        "firstName": "string",
                        "lastName": "string",
                        "role": "string",
                        "uid": 0,
                        "username": "user1"
                    }
                ],
                "teamName": "string"
            },
            {
                "gid": 4000,
                "members": [
                    {
                        "firstName": "string",
                        "lastName": "string",
                        "role": "string",
                        "uid": 0,
                        "username": "user2"
                    }
                ],
                "teamName": "string"
            }
        ]}
              """)
        c = DefaultAwsedClient()
        teams = c.list_teams_for_course("cse101")

        assert teams == ListTeamsResponse(
            teams=[
                TeamJson(
                    gid=3000,
                    members=[
                        UserJson(
                            firstName="string",
                            lastName="string",
                            role="string",
                            uid=0,
                            username="user1")],
                    teamName="string"
                ),
                TeamJson(
                    gid=4000,
                    members=[
                        UserJson(
                            firstName="string",
                            lastName="string",
                            role="string",
                            uid=0,
                            username="user2")],
                    teamName="string"
                )])
