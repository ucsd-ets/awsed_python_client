import os
import unittest.mock
from hamcrest import assert_that, equal_to, raises
from awsed.client import DefaultAwsedClient
from awsed.types import *

from requests.exceptions import HTTPError


class TestAwsedClient:
    client: DefaultAwsedClient

    # noinspection PyMethodMayBeStatic
    def setup_method(self) -> None:
        os.environ["AWSED_ENDPOINT"] = "https://awsed.ucsd.edu/api"
        os.environ["AWSED_API_KEY"] = "1234"
        self.client = DefaultAwsedClient(
            endpoint=os.getenv("AWSED_ENDPOINT"),
            awsed_api_key=os.getenv("AWSED_API_KEY"),
        )

    # noinspection PyMethodMayBeStatic
    def teardown_method(self) -> None:
        os.environ.pop("AWSED_ENDPOINT")
        os.environ.pop("AWSED_API_KEY")

    def test_get_user(self, requests_mock):
        requests_mock.get(
            "https://awsed.ucsd.edu/api/users/johndoe",
            text="""
            {
                "username": "johndoe",
                "firstName": "john",
                "lastName": "doe",
                "uid": 12345,
                "enrollments": [
                    "ABC100",
                    "ABC101"
                ]
            }
            """,
        )
        user = self.client.describe_user("johndoe")

        userResultJson1 = UserResultJson(
            username="johndoe",
            firstName="john",
            lastName="doe",
            uid=12345,
            enrollments=["ABC100", "ABC101"],
        )

        assert_that(user, equal_to(userResultJson1))

    def test_get_user_none(self, requests_mock):
        requests_mock.get("https://awsed.ucsd.edu/api/users/johndoe", text="""""")
        assert_that(self.client.describe_user("johndoe"), equal_to(None))

        requests_mock.get("https://awsed.ucsd.edu/api/users/johndoe", json={})
        assert_that(self.client.describe_user("johndoe"), equal_to(None))

    def test_list_user_launch_profiles(self, requests_mock):
        requests_mock.get(
            "https://awsed.ucsd.edu/api/user-launch-profiles/johndoe",
            text="""
            {
                "launchProfiles": [
                    {
                        "name": "Profile1",
                        "application": {
                            "name": "App1",
                            "image": "app1-image",
                            "description": "Description of App1",
                            "pullPolicy": "Always",
                            "volumeMounts": [
                                {
                                    "name": "volume1",
                                    "mountPath": "/mnt/data",
                                    "mountPropagation": "Bidirectional",
                                    "subPath": "sub/path",
                                    "subPathExpr": "sub/path/expr",
                                    "readOnly": true
                                }
                            ],
                            "volumes": [
                                {
                                    "name": "volume2",
                                    "type": "nfs",
                                    "server": "nfs-server",
                                    "path": "/nfs/share",
                                    "accessMode": "ReadWriteOnce",
                                    "pvcName": "nfs-pvc",
                                    "nfs": true,
                                    "hostPath": false
                                }
                            ],
                            "command": "start-app",
                            "args": [
                                "arg1",
                                "arg2"
                            ],
                            "environment": [
                                {
                                    "name": "ENV_VAR_1",
                                    "value": "value1"
                                }
                            ],
                            "extraYaml": "apiVersion: v1\\nkind: ConfigMap"
                        },
                        "player": {
                            "name": "Player1",
                            "minCpu": 1,
                            "maxCpu": 4,
                            "minMemory": 4096,
                            "maxMemory": 8192,
                            "gpu": 1
                        },
                        "course": "Course1"
                    }
                ]
            }
            """,
        )

        launch_profiles = self.client.list_user_launch_profiles("johndoe")

        assert_that(
            launch_profiles,
            equal_to(
                UserLaunchProfilesResult(
                    launchProfiles=[
                        UserLaunchProfileJson(
                            name="Profile1",
                            application=ApplicationJson(
                                name="App1",
                                image="app1-image",
                                description="Description of App1",
                                pullPolicy="Always",
                                volumeMounts=[
                                    KubernetesVolumeMount(
                                        name="volume1",
                                        mountPath="/mnt/data",
                                        mountPropagation="Bidirectional",
                                        subPath="sub/path",
                                        subPathExpr="sub/path/expr",
                                        readOnly=True,
                                    )
                                ],
                                volumes=[
                                    KubernetesVolume(
                                        name="volume2",
                                        type="nfs",
                                        server="nfs-server",
                                        path="/nfs/share",
                                        accessMode="ReadWriteOnce",
                                        pvcName="nfs-pvc",
                                        nfs=True,
                                        hostPath=False,
                                    )
                                ],
                                command="start-app",
                                args=["arg1", "arg2"],
                                environment=[
                                    KubernetesEnvironmentVariable(
                                        name="ENV_VAR_1", value="value1"
                                    )
                                ],
                                extraYaml="apiVersion: v1\nkind: ConfigMap",
                            ),
                            player=PlayerJson(
                                name="Player1",
                                minCpu=1,
                                maxCpu=4,
                                minMemory=4096,
                                maxMemory=8192,
                                gpu=1,
                            ),
                            course="Course1",
                        )
                    ]
                )
            ),
        )

    def test_list_enrollments(self, requests_mock):
        # TODO: Learn about Rest object parameters
        requests_mock.get(
            "https://awsed.ucsd.edu/api/enrollments",
            text="""
                [
                    {
                        "username": "johndoe",
                        "firstName": "john",
                        "lastName": "doe",
                        "uid": 12345,
                        "token": "abc123"
                    }
                ]
            """,
        )

        form = ListEnrollmentsForm(
            courseSlugs=["ABC100", "ABC101"], username="johndoe", courseSlug=["ABC100"]
        )
        enrollment_result = self.client.list_enrollments(form=form)

        assert_that(
            enrollment_result,
            equal_to(
                EnvironmentEnrollmentResult(
                    enrollments=[
                        EnrollmentResult(
                            username="johndoe",
                            firstName="john",
                            lastName="doe",
                            uid=12345,
                            token="abc123",
                        )
                    ]
                )
            ),
        )

    def test_list_enrollments_for_user(self, requests_mock):
        # TODO: Learn about Rest object parameters
        requests_mock.get(
            "https://awsed.ucsd.edu/api/enrollments?username=johndoe",
            text="""
                [
                    {
                        "username": "johndoe",
                        "course": "ABC100"
                    },
                    {
                        "username": "johndoe",
                        "course": "ABC101"
                    }
                ]
            """,
        )

        form = ListEnrollmentsForm(
            courseSlugs=["ABC100", "ABC101"], username="johndoe", courseSlug=["ABC100"]
        )
        enrollment_result = self.client.list_enrollments(username="johndoe")

        assert_that(
            enrollment_result,
            equal_to(
                [
                    EnrollmentJson(username="johndoe", course="ABC100"),
                    EnrollmentJson(username="johndoe", course="ABC101"),
                ]
            ),
        )

    def test_import_enrollments(self, requests_mock):
        requests_mock.post("https://awsed.ucsd.edu/api/enrollments")

        csv_content = "username,firstName,lastName,uid\njohndoe,John,Doe,12345"
        result = self.client.import_enrollments(csv_content, dry_run=False)

        assert_that(result, True)

    def test_list_pools_under_root(self, requests_mock):
        requests_mock.get(
            "https://awsed.ucsd.edu/api/pool-roots/pool_root",
            text="""
            {
                "pools": [
                    {
                        "name": "Pool1",
                        "root": "pool_root",
                        "predicate": "predicate",
                        "ou": "ou",
                        "courseName": "ABC100",
                        "mode": "mode"
                    }
                ]
            }
            """,
        )

        pools_result = self.client.list_pools_under_root("pool_root")

        assert_that(
            pools_result,
            equal_to(
                PoolsResult(
                    pools=[
                        PoolJson(
                            name="Pool1",
                            root="pool_root",
                            predicate="predicate",
                            ou="ou",
                            courseName="ABC100",
                            mode="mode",
                        )
                    ]
                )
            ),
        )

    def test_post_course_environment(self, requests_mock):
        requests_mock.post(
            "https://awsed.ucsd.edu/api/courses/ABC100/environments",
            text="""
            {
                "name": "CourseEnv",
                "environment": "env",
                "status": "APPROVED",
                "notes": "Test environment created successfully"
            }
            """,
        )

        course_environment = AssociateCourseEnvironmentRequestBody(
            environment="env",
            status="APPROVED",
            notes="Test environment created successfully",
        )
        result = self.client.post_course_environment("ABC100", course_environment)

        assert_that(result, True)

    def test_get_course_environment(self, requests_mock):
        requests_mock.get(
            "https://awsed.ucsd.edu/api/courses/ABC100/environments/env",
            text="""
            {
                "name": "CourseEnv",
                "environment": "env",
                "status": "APPROVED",
                "notes": "Test environment"
            }
            """,
        )

        course_environment = self.client.get_course_environment("ABC100", "env")

        assert_that(
            course_environment,
            equal_to(
                CourseEnvironmentResult(
                    name="CourseEnv",
                    environment="env",
                    status="APPROVED",
                    notes="Test environment",
                )
            ),
        )

    def test_patch_course_environment(self, requests_mock):
        course = "ABC100"
        environment = "env1"
        modification = ModifyCourseEnvironmentRequestBody(
            status="READY", notes="Updated notes"
        )

        requests_mock.patch(
            f"https://awsed.ucsd.edu/api/courses/{course}/environments/{environment}"
        )

        result = self.client.patch_course_environment(course, environment, modification)

        assert_that(result, True)

    def test_list_course_environments(self, requests_mock):
        requests_mock.get(
            "https://awsed.ucsd.edu/api/course-environments",
            text="""
            {
                "environments": [
                    {
                        "environment": "env1",
                        "status": "APPROVED",
                        "notes": "Environment 1"
                    },
                    {
                        "environment": "env2",
                        "status": "READY",
                        "notes": "Environment 2"
                    }
                ]
            }
            """,
        )

        request = ListCourseEnvironmentsRequestBody(
            status="APPROVED",
            subject="CS",
            term="Fall",
            authentication=Authentication(
                username="jdoe", admin=False, ta=False, student=True
            ),
        )
        result = self.client.list_course_environments(request)

        assert_that(
            result,
            equal_to(
                ListCourseEnvironmentsResultJson(
                    environments=[
                        ListCourseEnvironmentJson(
                            environment="env1", status="APPROVED", notes="Environment 1"
                        ),
                        ListCourseEnvironmentJson(
                            environment="env2", status="READY", notes="Environment 2"
                        ),
                    ]
                )
            ),
        )

    def test_generate_aws_credentials(self, requests_mock):
        course = "ABC100"
        role = "instructor"

        requests_mock.post(
            f"https://awsed.ucsd.edu/api/courses/{course}/roles/{role}/credentials",
            text="generated_aws_credentials",
        )

        result = self.client.generate_aws_credentials(course, role)

        assert_that(result, equal_to(True))

    def test_list_courses(self, requests_mock):
        username = "johndoe"
        tag = "tag1"

        requests_mock.get(
            "https://awsed.ucsd.edu/api/courses",
            text="""
            {
                "courses": [
                    {
                        "courseId": "ABC100"
                    },
                    {
                        "courseId": "ABC101"
                    }
                ]
            }
            """,
        )

        result = self.client.list_courses(username, tag)

        assert_that(
            result,
            equal_to(
                ListCoursesResultJson(
                    courses=[
                        CourseJson(courseId="ABC100"),
                        CourseJson(courseId="ABC101"),
                    ]
                )
            ),
        )

    def test_create_course(self, requests_mock):
        course_data = CourseRequestJson(
            name="CS101",
            studentRole="student",
            instructorRole="instructor",
            awsCredentialId="cred123",
            grader="grader1",
            fileSystem="fs1",
            active=True,
            snowTicket="ticket123",
            quarter="Fall",
            subject="Computer Science",
            courseNumber="101",
            instructor="John Doe",
            instructorEmail="john@example.com",
        )

        requests_mock.post(
            "https://awsed.ucsd.edu/api/courses",
            text="""
            "Course created successfully."
            """,
        )

        result = self.client.create_course(course_data)

        assert_that(result, True)

    def test_list_course_launch_profiles(self, requests_mock):
        course_slug = "CS101"
        response_data = {
            "launchProfiles": [
                {
                    "name": "ExampleLaunchProfile",
                    "application": {
                        "name": "ExampleApp",
                        "image": "app_image",
                        "description": "App description",
                        "pullPolicy": "Always",
                        "volumeMounts": [
                            {
                                "name": "volume_mount_1",
                                "mountPath": "/app/mount",
                                "mountPropagation": "None",
                                "subPath": "",
                                "subPathExpr": "",
                                "readOnly": True,
                            }
                        ],
                        "volumes": [
                            {
                                "name": "volume_1",
                                "type": "nfs",
                                "server": "nfs_server",
                                "path": "/nfs_share",
                                "accessMode": "ReadWriteOnce",
                                "pvcName": "nfs-pvc",
                                "nfs": True,
                                "hostPath": False,
                            }
                        ],
                        "command": "app_command",
                        "args": ["arg1", "arg2"],
                        "environment": [{"name": "env_var_1", "value": "env_value_1"}],
                        "extraYaml": "extra_yaml_content",
                    },
                    "player": {
                        "name": "Player1",
                        "minCpu": 1,
                        "maxCpu": 4,
                        "minMemory": 2048,
                        "maxMemory": 8192,
                        "gpu": 1,
                    },
                }
            ]
        }

        requests_mock.get(
            f"https://awsed.ucsd.edu/api/courses/{course_slug}/launch-profiles",
            json=response_data,
        )

        result = self.client.list_course_launch_profiles(course_slug)

        expected_result = ListLaunchProfilesJson(
            launchProfiles=[
                LaunchProfileJson(
                    name="ExampleLaunchProfile",
                    application=ApplicationJson(
                        name="ExampleApp",
                        image="app_image",
                        description="App description",
                        pullPolicy="Always",
                        volumeMounts=[
                            KubernetesVolumeMount(
                                name="volume_mount_1",
                                mountPath="/app/mount",
                                mountPropagation="None",
                                subPath="",
                                subPathExpr="",
                                readOnly=True,
                            )
                        ],
                        volumes=[
                            KubernetesVolume(
                                name="volume_1",
                                type="nfs",
                                server="nfs_server",
                                path="/nfs_share",
                                accessMode="ReadWriteOnce",
                                pvcName="nfs-pvc",
                                nfs=True,
                                hostPath=False,
                            )
                        ],
                        command="app_command",
                        args=["arg1", "arg2"],
                        environment=[
                            KubernetesEnvironmentVariable(
                                name="env_var_1", value="env_value_1"
                            )
                        ],
                        extraYaml="extra_yaml_content",
                    ),
                    player=PlayerJson(
                        name="Player1",
                        minCpu=1,
                        maxCpu=4,
                        minMemory=2048,
                        maxMemory=8192,
                        gpu=1,
                    ),
                )
            ]
        )

        assert_that(result, equal_to(expected_result))

    def test_create_course_launch_profile(self, requests_mock):
        course_slug = "CS101"
        launch_profile_data = LaunchProfileRequestJson(
            launchProfileName="Profile1",
            courseName=course_slug,
            applicationName="App1",
            playerName="Player1",
        )

        requests_mock.post(
            f"https://awsed.ucsd.edu/api/courses/{course_slug}/launch-profiles"
        )

        result = self.client.create_course_launch_profile(
            course_slug, launch_profile_data
        )

        assert_that(result, equal_to(True))

    def test_describe_course(self, requests_mock):
        course_slug = "CS101"
        response_data = {
            "tags": ["tag1", "tag2"],
            "enrollments": [
                {
                    "username": "user1",
                    "firstName": "John",
                    "lastName": "Doe",
                    "uid": 123,
                    "role": "student",
                }
            ],
            "courseId": "CS101",
            "pool": {
                "name": "pool1",
                "poolRootName": "pool_root",
                "rule": "rule1",
                "ou": "ou1",
                "courseName": "course1",
                "mode": "mode1",
            },
            "active": True,
            "grader": {
                "username": "grader1",
                "firstName": "Grader",
                "lastName": "Smith",
                "uid": 456,
                "role": "grader",
            },
            "fileSystem": {
                "identifier": "fs1",
                "server": "fs_server",
                "path": "/fs_path",
            },
            "snowTicket": "ST123",
            "quarter": "Q1",
            "subject": "Math",
            "courseNumber": "101",
            "instructor": "Instructor",
            "instructorEmail": "instructor@example.com",
            "courseName": "course1",
        }

        requests_mock.get(
            f"https://awsed.ucsd.edu/api/courses/{course_slug}", json=response_data
        )

        result = self.client.describe_course(course_slug)

        expected_result = CourseResult(
            tags=["tag1", "tag2"],
            enrollments=[
                UserResult(
                    username="user1",
                    firstName="John",
                    lastName="Doe",
                    uid=123,
                    role="student",
                )
            ],
            courseId="CS101",
            pool=ImmutablePool(
                name="pool1",
                poolRootName="pool_root",
                rule="rule1",
                ou="ou1",
                courseName="course1",
                mode="mode1",
            ),
            active=True,
            grader=UserResult(
                username="grader1",
                firstName="Grader",
                lastName="Smith",
                uid=456,
                role="grader",
            ),
            fileSystem=FileSystemResult(
                identifier="fs1", server="fs_server", path="/fs_path"
            ),
            snowTicket="ST123",
            quarter="Q1",
            subject="Math",
            courseNumber="101",
            instructor="Instructor",
            instructorEmail="instructor@example.com",
            courseName="course1",
        )

        assert_that(result, equal_to(expected_result))

    def test_describe_course_error(self, requests_mock):
        requests_mock.get(
            "https://awsed.ucsd.edu/api/courses/mycourse",
            json={"error": {"message": "Course not found"}},
            status_code=404,
        )

        assert_that(lambda: self.client.describe_course("mycourse"), raises(HTTPError))

    def test_update_course(self, requests_mock):
        course_data = CourseRequestJson(
            name="Updated Course",
            studentRole="Student",
            instructorRole="Instructor",
            awsCredentialId="cred123",
            grader="grader123",
            fileSystem="fs123",
            active=True,
            snowTicket="ticket123",
            quarter="Q3",
            subject="CS",
            courseNumber="101",
            instructor="prof123",
            instructorEmail="prof@example.com",
        )

        requests_mock.patch("https://awsed.ucsd.edu/api/courses/CS101")

        response_text = self.client.update_course("CS101", course_data)

        assert_that(response_text, equal_to(True))

    def test_describe_environment(self, requests_mock):
        requests_mock.get(
            "https://awsed.ucsd.edu/api/environments/env123",
            text="""
            {
                "volumes": [
                    {
                        "type": "nfs",
                        "name": "volume1",
                        "server": "nfs-server",
                        "path": "/data",
                        "accessMode": "ReadWriteMany",
                        "pvcName": "pvc123"
                    }
                ]
            }
            """,
        )

        environment = self.client.list_enrollments_slug("env123")

        assert_that(
            environment,
            equal_to(
                EnvironmentJson(
                    volumes=[
                        Volume(
                            type="nfs",
                            name="volume1",
                            server="nfs-server",
                            path="/data",
                            accessMode="ReadWriteMany",
                            pvcName="pvc123",
                        )
                    ]
                )
            ),
        )

    def test_upload_enrollments(self, requests_mock):
        csv_content = (
            "username,firstName,lastName,uid,role\njohndoe,John,Doe,101,Student"
        )
        requests_mock.post(
            "https://awsed.ucsd.edu/api/enrollments",
            text="Enrollments uploaded successfully",
        )

        response_text = self.client.upload_enrollments(csv_content, dry_run=False)

        assert_that(response_text, equal_to(True))

    def test_list_enrollments_for_environment_roster(self, requests_mock):
        requests_mock.get(
            "https://awsed.ucsd.edu/api/environments/env123/roster",
            text="""
            {
                "username": "johndoe",
                "firstName": "John",
                "lastName": "Doe",
                "uid": 101,
                "token": "token123"
            }
            """,
        )

        enrollment_result = self.client.list_enrollments_roster("env123")

        assert_that(
            enrollment_result,
            equal_to(
                EnvironmentEnrollmentResult(
                    username="johndoe",
                    firstName="John",
                    lastName="Doe",
                    uid=101,
                    token="token123",
                )
            ),
        )

    def test_list_teams(self, requests_mock):
        requests_mock.get(
            "https://awsed.ucsd.edu/api/courses/ABC101/teams",
            text="""
            {
                "teams": [
                    {
                        "teamName": "TeamA",
                        "sanitizedTeamName": "team_a",
                        "uniqueName": "team_a_123",
                        "gid": 123,
                        "members": [
                            {
                                "username": "user1",
                                "firstName": "John",
                                "lastName": "Doe",
                                "uid": 456,
                                "role": "student"
                            }
                        ],
                        "course": {
                            "tags": ["tag1", "tag2"],
                            "enrollments": [
                                {
                                    "username": "user1",
                                    "firstName": "John",
                                    "lastName": "Doe",
                                    "uid": 456,
                                    "role": "student"
                                }
                            ],
                            "courseId": "CS101",
                            "pool": {
                                "name": "pool1",
                                "poolRootName": "root_pool1",
                                "rule": "rule1",
                                "ou": "ou1",
                                "courseName": "Computer Science",
                                "mode": "mode1"
                            },
                            "active": true,
                            "grader": {
                                "username": "grader1",
                                "firstName": "Alice",
                                "lastName": "Smith",
                                "uid": 789,
                                "role": "instructor"
                            },
                            "fileSystem": {
                                "identifier": "fs1",
                                "server": "server1",
                                "path": "/path/to/files"
                            },
                            "snowTicket": "ticket123",
                            "quarter": "Fall",
                            "subject": "Computer Science",
                            "courseNumber": "101",
                            "instructor": "instructor1",
                            "instructorEmail": "instructor1@example.com",
                            "courseName": "Intro to CS"
                        }
                    }
                ]
            }
        """,
        )

        teams_result = self.client.list_course_teams("ABC101")

        # Creating expected TeamResult object with specific values
        expected_teams_result = TeamsResult(
            teams=[
                TeamResult(
                    teamName="TeamA",
                    sanitizedTeamName="team_a",
                    uniqueName="team_a_123",
                    gid=123,
                    members=[
                        UserResult(
                            username="user1",
                            firstName="John",
                            lastName="Doe",
                            uid=456,
                            role="student",
                        )
                    ],
                    course=CourseResult(
                        tags=["tag1", "tag2"],
                        enrollments=[
                            UserResult(
                                username="user1",
                                firstName="John",
                                lastName="Doe",
                                uid=456,
                                role="student",
                            )
                        ],
                        courseId="CS101",
                        pool=ImmutablePool(
                            name="pool1",
                            poolRootName="root_pool1",
                            rule="rule1",
                            ou="ou1",
                            courseName="Computer Science",
                            mode="mode1",
                        ),
                        active=True,
                        grader=UserResult(
                            username="grader1",
                            firstName="Alice",
                            lastName="Smith",
                            uid=789,
                            role="instructor",
                        ),
                        fileSystem=FileSystemResult(
                            identifier="fs1", server="server1", path="/path/to/files"
                        ),
                        snowTicket="ticket123",
                        quarter="Fall",
                        subject="Computer Science",
                        courseNumber="101",
                        instructor="instructor1",
                        instructorEmail="instructor1@example.com",
                        courseName="Intro to CS",
                    ),
                )
            ]
        )

        assert_that(teams_result, equal_to(expected_teams_result))

    def test_timeout_handling(self, mocker):
        import requests

        mock = mocker.patch.object(requests, "get")
        mock.side_effect = requests.exceptions.Timeout

        assert_that(
            lambda: self.client.describe_user("johndoe"),
            raises(requests.exceptions.Timeout),
        )

    # def test_patch_user(self):
