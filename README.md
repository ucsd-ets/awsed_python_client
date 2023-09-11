# AWSed Python Client

`awsed_python_client` is a python client for `awsed.ucsd.edu` API.

## Installation

To install awsed `awsed_python_client` run

```
    pip install git+https://github.com/ucsd-ets/awsed_python_client@Rebuild
```

or add `git+https://github.com/ucsd-ets/awsed_python_client@Rebuild` to your `requirments.txt`

## Getting Started

Please follow the installation procedure and initialize the client as such:

```python3
    from awsed.client import DefaultClient 

    awsed_cleint = DefaultClient(endpoint='awsed_endpoint.com', awsed_api_key='42')
```

## API Endpoints

### Users

#### describe_user

Return user information.

##### Parameters

* username: str -  username of a student

##### Return type

* UserResultJson - user information

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### list_user_launch_profiles

List user's lunch profiles

##### Parameters

* username: str - username of a student

##### Return type

* UserLaunchProfilesResult - information about user launch profiles

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

---

### Enrollments

#### list_enrollments

List all or user's enrollments

##### Parameters

* form: ListEnrollmentsForm - needs courseId, username
* username: Optional[str] - if you want to list enrollments for a specific user

##### Return type

* EnvironmentEnrollmentResult - list of enrollments

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### import_enrollments

Load enrollments into `awsed.ucsd.edu`

##### Parameters

* csv_content: str - a properly formated csv string
* dry_run: bool = False - weather r not to actually intitiate the enrollment import

##### Return type

* bool - always True if posted successfuly

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

---

### Pool Roots

#### list_pools_under_root

List pools configured under a pool root

##### Parameters

* pool_root_name: str - name of pool root

##### Return type

* PoolsResult - list of pool roots information

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

---

### Course Environments

#### post_course_environment

Associate a course with an environment

##### Parameters

* course_name: str - course ID
* course_environment: AssociateCourseEnvironmentRequestBody - required environment, status and notes

##### Return type

* bool - always True if posted successfuly

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### get_course_environment

Describe a course environment

##### Parameters

* course: str - course ID
* environment: str - environment name

##### Return type

* CourseEnvironmentResult - information about course environment

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### patch_course_environment

Update a course environment

##### Parameters

* course: str - course ID
* environment: str - environment name
* modification: ModifyCourseEnvironmentRequestBody - includes status and notes

##### Return type

* bool - always True if posted successfuly

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### list_course_environments

List course environments

##### Parameters

* request: ListCourseEnvironmentsRequestBody - includes status, subject, term and authentication

##### Return type

* ListCourseEnvironmentsResultJson - list of courses

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

---

### AWS Credentials

#### generate_aws_credentials

Generate AWS credentials for a user

##### Parameters

* course: str - course ID
* role: str - role of a user

##### Return type

* bool - always True if posted successfuly

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

---

### Courses

#### list_courses

List active courses

##### Parameters

* username: str = None - optional to list all courses for a given user
* tag: str = None - optional to list all courses with a given tag

##### Return type

* ListCoursesResultJson - list of CoursesJson data

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### create_course

Create a course

##### Parameters

* course: CourseRequestJson - including name, studentRole, instructorRole, awsCredentialId, grader, fileSystem, active, snowTicket, quarter, subject, courseNumber, instructor and instructorEmail

##### Return type

* bool - always True if posted successfuly

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### list_course_launch_profiles

List launch profiles for a course

##### Parameters

* course: str - course ID

##### Return type

* ListLaunchProfilesJson - list of LaunchProfileJson containing launch profiles data

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### create_course_launch_profile

Create a lunch profile fo a course

##### Parameters

* course: str - course ID
* launch_profile: LaunchProfileRequestJson - including launchProfileName, courseName, applicationName and playerName

##### Return type

* bool - always True if posted successfuly

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### describe_course

Describe a course

##### Parameters

* course: str - course ID

##### Return type

* CourseResult - course information

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### update_course

Update course info

##### Parameters

* course: str - course ID
* course_data: CourseRequestJson - including name, studentRole, instructorRole, awsCredentialId, grader, fileSystem, active, snowTicket, quarter, subject, courseNumber, instructor and instructorEmail

##### Return type

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### list_course_teams

#### Parameters 

* course: str - course ID

##### Return type

* TeamsResult - list of TeamResult with teams data

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

---

### Environments

#### list_enrollments_slug

List enrollments for environment

#### Parameters

* slug: str - course ID

##### Return type

* EnvironmentJson - list of Environment's volumes

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

#### list_enrollments_roster

List enrollments for environment

#### Parameters

* slug: str - course ID

##### Return type

* EnvironmentEnrollmentResult - list of enrollments for the environment

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx

---

### Teams

#### list_teams

List teams for a username

#### Parameters

* username: str - user's username

##### Return type

* TeamsResult - list of TeamResult with teams data

##### Raises

* requests.exceptions.HTTPError - raises error when call result code is not 2xx
