from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional

# Use error classes provided by requests
# @dataclass
# class ApiFieldError:
#     name: str
#     message: str

# @dataclass
# class ApiError:
#     timestamp: str
#     statusCode: int
#     message: str
#     request: str
#     fields: List[ApiFieldError]

# @dataclass
# class ApiErrorResult:
#     error: ApiError

@dataclass
class CourseRequestJson:
    name: str
    studentRole: str
    instructorRole: str
    awsCredentialId: str
    grader: str
    fileSystem: str
    active: bool
    snowTicket: str
    quarter: str
    subject: str
    courseNumber: str
    instructor: str
    instructorEmail: str

@dataclass
class LaunchProfileRequestJson:
    launchProfileName: str
    courseName: str
    applicationName: str
    playerName: str

@dataclass
class AssociateCourseEnvironmentRequestBody:
    environment: str
    status: str
    notes: str

@dataclass
class Args:
    course: str
    role: str

@dataclass
class ModifyCourseEnvironmentRequestBody:
    status: str
    notes: str

@dataclass
class UserResultJson:
    username: str
    firstName: str
    lastName: str
    uid: int
    enrollments: List[str]

@dataclass
class KubernetesEnvironmentVariable:
    name: str
    value: str

@dataclass
class KubernetesVolume:
    name: str
    type: str
    server: str
    path: str
    accessMode: str
    pvcName: str
    nfs: bool
    hostPath: bool

@dataclass
class KubernetesVolumeMount:
    name: str
    mountPath: str
    mountPropagation: str
    subPath: str
    subPathExpr: str
    readOnly: bool

@dataclass
class ApplicationJson:
    name: str
    image: str
    description: str
    pullPolicy: str
    volumeMounts: List[KubernetesVolumeMount]
    volumes: List[KubernetesVolume]
    command: str
    args: List[str]
    environment: List[KubernetesEnvironmentVariable]
    extraYaml: str

@dataclass
class PlayerJson:
    name: str
    minCpu: int
    maxCpu: int
    minMemory: int
    maxMemory: int
    gpu: int

@dataclass
class UserLaunchProfileJson:
    name: str
    application: ApplicationJson
    player: PlayerJson
    course: str

@dataclass
class UserLaunchProfilesResult:
    launchProfiles: List[UserLaunchProfileJson]

@dataclass
class FileSystemResult:
    identifier: str
    server: str
    path: str

@dataclass
class ImmutablePool:
    name: str
    poolRootName: str
    rule: str
    ou: str
    courseName: str
    mode: str

@dataclass
class CourseResult:
    tags: List[str]
    enrollments: List[UserResultJson]
    courseId: str
    pool: ImmutablePool
    active: bool
    grader: UserResultJson
    fileSystem: FileSystemResult
    snowTicket: str
    quarter: str
    subject: str
    courseNumber: str
    instructor: str
    instructorEmail: str
    courseName: str

@dataclass
class CourseJson:
    courseId: str

@dataclass
class TeamResult:
    teamName: str
    sanitizedTeamName: str
    uniqueName: str
    gid: int
    members: List[UserResultJson]
    course: CourseResult

@dataclass
class TeamsResult:
    teams: List[TeamResult]

@dataclass
class PoolAccountJson:
    accountId: str
    accountName: str
    username: str
    teamName: str

@dataclass
class PoolAccountResult:
    accounts: List[PoolAccountJson]

@dataclass
class PoolJson:
    name: str
    root: str
    predicate: str
    ou: str
    courseName: str
    mode: str

@dataclass
class PoolsResult:
    pools: List[PoolJson]

@dataclass
class EnvironmentJson:
    volumes: List[KubernetesVolume]

@dataclass
class Volume:
    type: str
    name: str
    server: str
    path: str
    accessMode: str
    pvcName: str

@dataclass
class EnvironmentEnrollmentResult:
    username: str
    firstName: str
    lastName: str
    uid: int
    token: str

@dataclass
class ListEnrollmentsForm:
    courseSlugs: List[str]
    username: str
    courseSlug: List[str]

@dataclass
class ListCoursesResultJson:
    courses: List[CourseJson]

@dataclass
class LaunchProfileJson:
    name: str
    application: ApplicationJson
    player: PlayerJson

@dataclass
class ListLaunchProfilesJson:
    launchProfiles: List[LaunchProfileJson]

@dataclass
class CourseEnvironmentResult:
    name: str
    environment: str
    status: str
    notes: str

@dataclass
class Authentication:
    username: str
    admin: bool
    ta: bool
    student: bool

@dataclass
class ListCourseEnvironmentsRequestBody:
    status: str
    subject: str
    term: str
    authentication: Authentication

@dataclass
class ListCourseEnvironmentJson:
    environment: str
    status: str
    notes: str

@dataclass
class ListCourseEnvironmentsResultJson:
    environments: List[ListCourseEnvironmentJson]