import os
from hamcrest import assert_that, equal_to
from awsed.client import DefaultAwsedClient
from awsed.types import *


class TestAwsedClient:
    # noinspection PyMethodMayBeStatic
    def setup_method(self) -> None:
        os.environ['AWSED_ENDPOINT'] = 'https://awsed.ucsd.edu/api'
        os.environ['AWSED_API_KEY'] = "1234"

    # noinspection PyMethodMayBeStatic
    def teardown_method(self) -> None:
        os.environ.pop('AWSED_ENDPOINT')
        os.environ.pop('AWSED_API_KEY')
        
    def test_get_user(self, requests_mock):
        requests_mock.get('https://awsed.ucsd.edu/api/users/johndoe', text="""
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
            """)
            
        c = DefaultAwsedClient()
        user = c.describe_user("johndoe")
        
        assert_that(user, equal_to(UserResultJson(
            username="johndoe",
            firstName="john",
            lastName="doe",
            uid=12345,
            enrollments=["ABC100", "ABC101"]
        )))
        
    def test_list_user_launch_profiles(self, requests_mock):
        requests_mock.get('https://awsed.ucsd.edu/api/user-launch-profiles/johndoe', text="""
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
            """)

        c = DefaultAwsedClient()
        launch_profiles = c.list_user_launch_profiles("johndoe")

        assert_that(launch_profiles, equal_to(UserLaunchProfilesResult(
            launchProfiles=[
                UserLaunchProfileJson(
                    name="Profile1",
                    application=ApplicationJson(
                        name="App1",
                        image="app1-image",
                        description="Description of App1",
                        pullPolicy="Always",
                        volumeMounts=[
                            KubernetesVolumeMount(name="volume1", mountPath="/mnt/data", mountPropagation="Bidirectional", subPath="sub/path", subPathExpr="sub/path/expr", readOnly=True)
                        ],
                        volumes=[
                            KubernetesVolume(name="volume2", type="nfs", server="nfs-server", path="/nfs/share", accessMode="ReadWriteOnce", pvcName="nfs-pvc", nfs=True, hostPath=False)
                        ],
                        command="start-app",
                        args=["arg1", "arg2"],
                        environment=[
                            KubernetesEnvironmentVariable(name="ENV_VAR_1", value="value1")
                        ],
                        extraYaml="apiVersion: v1\nkind: ConfigMap"
                    ),
                    player=PlayerJson(name="Player1", minCpu=1, maxCpu=4, minMemory=4096, maxMemory=8192, gpu=1),
                    course="Course1"
                )
            ]
        )))



    def test_list_enrollments_for_environment(self, requests_mock):
        requests_mock.get('https://awsed.ucsd.edu/api/enrollments', text="""
            {
                "username": "johndoe",
                "firstName": "john",
                "lastName": "doe",
                "uid": 12345,
                "token": "abc123"
            }
            """)

        c = DefaultAwsedClient()
        form = ListEnrollmentsForm(courseSlugs=["ABC100", "ABC101"])
        enrollment_result = c.list_enrollments_for_environment(form, "johndoe")

        assert_that(enrollment_result, equal_to(EnvironmentEnrollmentResult(
            username="johndoe",
            firstName="john",
            lastName="doe",
            uid=12345,
            token="abc123"
        )))
    
    def test_import_enrollments(self, requests_mock):
        requests_mock.post('https://awsed.ucsd.edu/api/enrollments', text="Enrollments imported successfully")

        c = DefaultAwsedClient()
        csv_content = "username,firstName,lastName,uid\njohndoe,John,Doe,12345"
        result = c.import_enrollments(csv_content, dry_run=False)

        assert_that(result, equal_to("Enrollments imported successfully"))

    def test_list_pools_under_root(self, requests_mock):
        requests_mock.get('https://awsed.ucsd.edu/api/pool-roots/pool_root', text="""
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
            """)

        c = DefaultAwsedClient()
        pools_result = c.list_pools_under_root("pool_root")

        assert_that(pools_result, equal_to(PoolsResult(
            pools=[
                PoolJson(
                    name="Pool1",
                    root="pool_root",
                    predicate="predicate",
                    ou="ou",
                    courseName="ABC100",
                    mode="mode"
                )
            ]
        )))

    def test_post_course_environment(self, requests_mock):
        requests_mock.post('https://awsed.ucsd.edu/api/courses/ABC100/environments', text="""
            {
                "name": "CourseEnv",
                "environment": "env",
                "status": "APPROVED",
                "notes": "Test environment created successfully"
            }
            """)

        c = DefaultAwsedClient()
        course_environment = AssociateCourseEnvironmentRequestBody(
            environment="env",
            status="APPROVED",
            notes="Test environment created successfully"
        )
        result = c.post_course_environment("ABC100", course_environment)

        assert_that(result, equal_to("""
            {
                "name": "CourseEnv",
                "environment": "env",
                "status": "APPROVED",
                "notes": "Test environment created successfully"
            }
            """))

    def test_get_course_environment(self, requests_mock):
        requests_mock.get('https://awsed.ucsd.edu/api/courses/ABC100/environments/env', text="""
            {
                "name": "CourseEnv",
                "environment": "env",
                "status": "APPROVED",
                "notes": "Test environment"
            }
            """)

        c = DefaultAwsedClient()
        course_environment = c.get_course_environment("ABC100", "env")

        assert_that(course_environment, equal_to(CourseEnvironmentResult(
            name="CourseEnv",
            environment="env",
            status="APPROVED",
            notes="Test environment"
        )))
        
    def test_patch_course_environment(self, requests_mock):
        course = "ABC100"
        environment = "env1"
        modification = ModifyCourseEnvironmentRequestBody(status="READY", notes="Updated notes")
        
        requests_mock.patch(f'https://awsed.ucsd.edu/api/courses/{course}/environments/{environment}', text="""
            {
                "name": "ABC100",
                "environment": "env1",
                "status": "READY",
                "notes": "Updated notes"
            }
            """)
            
        c = DefaultAwsedClient()
        result = c.patch_course_environment(course, environment, modification)
        
        assert_that(result, equal_to(CourseEnvironmentResult(
            name="ABC100",
            environment="env1",
            status="READY",
            notes="Updated notes"
        )))

    def test_list_course_environments(self, requests_mock):
        request = ListCourseEnvironmentsRequestBody(status="APPROVED", subject="CS", term="Fall", authentication=Authentication(student=True))
        
        requests_mock.get('https://awsed.ucsd.edu/api/course-environments', text="""
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
            """)
            
        c = DefaultAwsedClient()
        result = c.list_course_environments(request)
        
        assert_that(result, equal_to(ListCourseEnvironmentsResultJson(
            environments=[
                ListCourseEnvironmentJson(environment="env1", status="APPROVED", notes="Environment 1"),
                ListCourseEnvironmentJson(environment="env2", status="READY", notes="Environment 2")
            ]
        )))

    def test_generate_aws_credentials(self, requests_mock):
        course = "ABC100"
        role = "instructor"
        
        requests_mock.post(f'https://awsed.ucsd.edu/api/courses/{course}/roles/{role}/credentials', text="generated_aws_credentials")
            
        c = DefaultAwsedClient()
        result = c.generate_aws_credentials(course, role)
        
        assert_that(result, equal_to("generated_aws_credentials"))

    def test_list_courses(self, requests_mock):
        username = "johndoe"
        tag = "tag1"
        
        requests_mock.get('https://awsed.ucsd.edu/api/courses', text="""
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
            """)
            
        c = DefaultAwsedClient()
        result = c.list_courses(username, tag)
        
        assert_that(result, equal_to(ListCoursesResultJson(
            courses=[
                CourseResult(courseId="ABC100"),
                CourseResult(courseId="ABC101")
            ]
        )))
        
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
            instructorEmail="john@example.com"
        )
        
        requests_mock.post('https://awsed.ucsd.edu/api/courses', text="""
            "Course created successfully."
            """)
            
        c = DefaultAwsedClient()
        result = c.create_course(course_data)
        
        assert_that(result, equal_to("Course created successfully."))

    def test_list_course_launch_profiles(self, requests_mock):
        course_slug = "CS101"
        response_data = {
            "launchProfiles": [
                {
                    "name": "Profile1",
                    "application": {
                        "name": "App1",
                        "image": "app1_image",
                        "description": "Application 1",
                        "pullPolicy": "Always"
                        # ... other application data
                    },
                    "player": {
                        "name": "Player1",
                        "minCpu": 1,
                        "maxCpu": 4,
                        "minMemory": 512,
                        "maxMemory": 2048,
                        "gpu": 1
                        # ... other player data
                    }
                }
                # ... other launch profiles
            ]
        }
        
        requests_mock.get(f'https://awsed.ucsd.edu/api/courses/{course_slug}/launch-profiles', json=response_data)
        
        c = DefaultAwsedClient()
        result = c.list_course_launch_profiles(course_slug)
        
        assert_that(result, equal_to(ListLaunchProfilesJson(**response_data)))

    def test_create_course_launch_profile(self, requests_mock):
        course_slug = "CS101"
        launch_profile_data = LaunchProfileRequestJson(
            launchProfileName="Profile1",
            courseName=course_slug,
            applicationName="App1",
            playerName="Player1"
        )
        
        requests_mock.post(f'https://awsed.ucsd.edu/api/courses/{course_slug}/launch-profiles', text="""
            "Launch profile created successfully."
            """)
            
        c = DefaultAwsedClient()
        result = c.create_course_launch_profile(course_slug, launch_profile_data)
        
        assert_that(result, equal_to("Launch profile created successfully."))

    def test_get_course(self, requests_mock):
        course_slug = "CS101"
        response_data = {
            "tags": [],
            "enrollments": [
                {
                    "username": "johndoe",
                    "firstName": "John",
                    "lastName": "Doe",
                    "uid": 12345,
                    "role": "student"
                    # ... other enrollment data
                }
                # ... other enrollments
            ],
            "courseId": course_slug,
            "pool": {
                "name": "pool1",
                "poolRootName": "pool_root",
                "rule": "rule1",
                "ou": "ou1",
                "courseName": course_slug,
                "mode": "mode1"
            },
            "active": True,
            "grader": {
                "username": "grader1",
                "firstName": "Grader",
                "lastName": "One",
                "uid": 54321,
                "role": "grader"
            },
            "fileSystem": {
                "identifier": "fs1",
                "server": "server1",
                "path": "/path/to/fs1"
            },
            "snowTicket": "ticket123",
            "quarter": "Fall",
            "subject": "Computer Science",
            "courseNumber": "101",
            "instructor": "John Doe",
            "instructorEmail": "john@example.com",
            "courseName": course_slug
        }
        
        requests_mock.get(f'https://awsed.ucsd.edu/api/courses/{course_slug}', json=response_data)
        
        c = DefaultAwsedClient()
        result = c.get_course(course_slug)
        
        assert_that(result, equal_to(CourseResult(**response_data)))

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
            instructorEmail="prof@example.com"
        )

        requests_mock.patch('https://awsed.ucsd.edu/api/courses/CS101', text="Course updated successfully")
        
        c = DefaultAwsedClient()
        response_text = c.update_course("CS101", course_data)
        
        assert_that(response_text).is_equal_to("Course updated successfully")
    
    def test_list_teams(self, requests_mock):
        requests_mock.get('https://awsed.ucsd.edu/api/courses/ABC101/teams', text="""
            {
                "teams": [
                    {
                        "teamName": "TeamA",
                        "sanitizedTeamName": "teama",
                        "uniqueName": "unique1",
                        "gid": 123,
                        "members": [
                            {
                                "username": "user1",
                                "firstName": "John",
                                "lastName": "Doe",
                                "uid": 101,
                                "role": "Student"
                            }
                        ]
                    }
                ]
            }
            """)
        
        c = DefaultAwsedClient()
        teams_result = c.list_teams("ABC101")
        
        assert_that(teams_result.teams).is_length(1)
        assert_that(teams_result.teams[0].teamName).is_equal_to("TeamA")
    
    def test_list_enrollments(self, requests_mock):
        form = ListEnrollmentsForm(courseSlug=["ABC100"], username="johndoe")
        requests_mock.get('https://awsed.ucsd.edu/api/enrollments', text="""
            {
                "username": "johndoe",
                "firstName": "John",
                "lastName": "Doe",
                "uid": 101,
                "token": "token123"
            }
            """)
        
        c = DefaultAwsedClient()
        enrollment_result = c.list_enrollments(form, username="johndoe")
        
        assert_that(enrollment_result.username).is_equal_to("johndoe")
    
    def test_describe_environment(self, requests_mock):
        requests_mock.get('https://awsed.ucsd.edu/api/environments/env123', text="""
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
            """)
        
        c = DefaultAwsedClient()
        environment = c.describe_environment("env123")
        
        assert_that(environment.volumes).is_length(1)
    
    def test_upload_enrollments(self, requests_mock):
        csv_content = "username,firstName,lastName,uid,role\njohndoe,John,Doe,101,Student"
        requests_mock.post('https://awsed.ucsd.edu/api/enrollments', text="Enrollments uploaded successfully")
        
        c = DefaultAwsedClient()
        response_text = c.upload_enrollments(csv_content, dry_run=False)
        
        assert_that(response_text).is_equal_to("Enrollments uploaded successfully")
    
    def test_list_enrollments_for_environment(self, requests_mock):
        requests_mock.get('https://awsed.ucsd.edu/api/environments/env123/roster', text="""
            {
                "username": "johndoe",
                "firstName": "John",
                "lastName": "Doe",
                "uid": 101,
                "token": "token123"
            }
            """)
        
        c = DefaultAwsedClient()
        enrollment_result = c.list_enrollments_for_environment("env123")
        
        assert_that(enrollment_result.username).is_equal_to("johndoe")
    
    def test_list_teams_for_user(self, requests_mock):
        requests_mock.get('https://awsed.ucsd.edu/api/teams', text="""
            {
                "teams": [
                    {
                        "teamName": "TeamA",
                        "sanitizedTeamName": "teama",
                        "uniqueName": "unique1",
                        "gid": 123,
                        "members": [
                            {
                                "username": "user1",
                                "firstName": "John",
                                "lastName": "Doe",
                                "uid": 101,
                                "role": "Student"
                            }
                        ]
                    }
                ]
            }
            """)
        
        c = DefaultAwsedClient()
        teams_result = c.list_teams(username="johndoe")
        
        assert_that(teams_result.teams).is_length(1)
        assert_that(teams_result.teams[0].teamName).is_equal_to("TeamA")



    # def test_list_courses_by_tag(self, requests_mock):
    #     """test list courses by tag"""
    #     requests_mock.get('https://awsed.ucsd.edu/api/courses?tag=teams-enabled', text="""
    #         {
    #             "courses": [
    #                 {
    #                     "courseId": "BENG134_FA20_A00"
    #                 },
    #                 {
    #                     "courseId": "BIPN145_FA20_A00"
    #                 }
    #             ]
    #         }
    #           """)
    #     c = DefaultAwsedClient()
    #     courses = c.list_courses_by_tag("teams-enabled")

    #     assert_that(courses, equal_to(
    #         ListCourseResponse(courses=[
    #             CourseCourseResponse(courseId="BENG134_FA20_A00"),
    #             CourseCourseResponse(courseId="BIPN145_FA20_A00")

    #         ])
    #     ))

    # def test_list_courses_by_tag2(self, requests_mock):
    #     """test list courses by tag"""
    #     requests_mock.get('https://awsed.ucsd.edu/api/courses?tag=tag2', text="""
    #         {
    #             "courses": [
    #                 {
    #                     "courseId": "COGS108_FA20_A00"
    #                 },
    #                 {
    #                     "courseId": "COGS18_FA20_A00"
    #                 }
    #             ]
    #         }
    #           """)
    #     c = DefaultAwsedClient()
    #     courses = c.list_courses_by_tag("tag2")

    #     assert_that(courses, equal_to(
    #         ListCourseResponse(courses=[
    #             CourseCourseResponse(courseId="COGS108_FA20_A00"),
    #             CourseCourseResponse(courseId="COGS18_FA20_A00")

    #         ])
    #     ))

    # def test_list_courses_by_tag4(self, requests_mock):
    #     """test list courses by tag"""
    #     requests_mock.get('https://awsed.ucsd.edu/api/courses?tag=tag3', text="""
    #         {
    #             "courses": []
    #         }
    #           """)
    #     c = DefaultAwsedClient()
    #     courses = c.list_courses_by_tag("tag3")

    #     assert_that(courses, equal_to(
    #         ListCourseResponse(courses=[])
    #     ))

    # def test_list_courses_by_tag3(self, requests_mock):
    #     """test list courses by tag"""
    #     requests_mock.get('https://awsed.ucsd.edu/api/courses', text="""
    #         {
    #             "courses": []
    #         }
    #           """)
    #     c = DefaultAwsedClient()
    #     courses = c.list_courses()

    #     assert_that(courses, equal_to(
    #         ListCourseResponse(courses=[])
    #     ))

    # def test_describe_course(self, requests_mock):
    #     """test list courses by tag"""
    #     requests_mock.get('https://awsed.ucsd.edu/api/courses/cse101', text="""
    #         {
    #             "courseId": "cse101",
    #             "grader": {
    #                 "username": "grader",
    #                 "uid": 1234
    #             },
    #             "fileSystem": {
    #                 "identifier": "test-workspaces",
    #                 "server": "nfs.example.com",
    #                 "path": "/export/workspaces"
    #             }
    #         }
    #           """)
    #     c = DefaultAwsedClient()
    #     courses = c.describe_course("cse101")

    #     assert_that(courses, equal_to(CourseJson(
    #         courseId='cse101',
    #         tags=None,
    #         enrollments=[],
    #         fileSystem=FileSystemJson(
    #             identifier='test-workspaces',
    #             server='nfs.example.com',
    #             path='/export/workspaces'),
    #         grader=UserResultJson(username='grader', uid=1234))
    #     ))

    # def test_course_teams(self, requests_mock):
    #     """test list courses by tag"""

    #     requests_mock.get('https://awsed.ucsd.edu/api/courses/cse101/teams', text="""
    #         {"teams": [
    #         {
    #             "gid": 3000,
    #             "members": [
    #                 {
    #                     "firstName": "string",
    #                     "lastName": "string",
    #                     "role": "string",
    #                     "uid": 0,
    #                     "username": "user1"
    #                 }
    #             ],
    #             "teamName": "string"
    #         },
    #         {
    #             "gid": 4000,
    #             "members": [
    #                 {
    #                     "firstName": "string",
    #                     "lastName": "string",
    #                     "role": "string",
    #                     "uid": 0,
    #                     "username": "user2"
    #                 }
    #             ],
    #             "teamName": "string"
    #         }
    #     ]}
    #           """)
    #     c = DefaultAwsedClient()
    #     teams = c.list_teams_for_course("cse101")

    #     assert teams == ListTeamsResponse(
    #         teams=[
    #             TeamJson(
    #                 gid=3000,
    #                 members=[
    #                     UserResultJson(
    #                         firstName="string",
    #                         lastName="string",
    #                         role="string",
    #                         uid=0,
    #                         username="user1")],
    #                 teamName="string"
    #             ),
    #             TeamJson(
    #                 gid=4000,
    #                 members=[
    #                     UserResultJson(
    #                         firstName="string",
    #                         lastName="string",
    #                         role="string",
    #                         uid=0,
    #                         username="user2")],
    #                 teamName="string"
    #             )])
