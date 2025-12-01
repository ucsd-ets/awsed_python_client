from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

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
    homeFileSystem: Optional[str]
    enrollments: List[str]


@dataclass
class UserRequestJson:
    username: str
    firstName: Optional[str]
    lastName: Optional[str]
    roles: Optional[List[str]]
    apiKey: Optional[str]
    uid: int
    homeFileSystem: Optional[str]

    def __init__(
        self,
        username=None,
        firstName=None,
        lastName=None,
        roles=None,
        apiKey=None,
        uid=None,
        homeFileSystem=None,
    ):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.roles = roles
        self.apiKey = apiKey
        self.uid = uid
        self.homeFileSystem = homeFileSystem


@dataclass
class UserResult:
    username: str
    firstName: Optional[str]
    lastName: Optional[str]
    uid: int
    role: Optional[str]


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
    extraYaml: str
    command: str
    volumeMounts: Optional[List[KubernetesVolumeMount]] = field(default_factory=list)
    volumes: Optional[List[KubernetesVolume]] = field(default_factory=list)
    args: Optional[List[str]] = field(default_factory=list)
    environment: Optional[List[KubernetesEnvironmentVariable]] = field(default_factory=list)
    labels: Optional[Dict[str, Optional[str]]] = field(default_factory=dict)
    postStart: Optional[List[str]] = field(default_factory=list)
    preStop: Optional[List[str]] = field(default_factory=list)


@dataclass
class PlayerJson:
    name: str
    minCpu: int
    maxCpu: int
    minMemory: int
    maxMemory: int
    gpu: int

@dataclass
class Zone:
    name: str
    nodeSelector: str
    tolerations: str
    type: str
    labels: str
    weight: int

@dataclass
class UserLaunchProfileJson:
    name: str
    application: ApplicationJson
    player: PlayerJson
    course: str
    displayName: str
    description: str
    volumes: Optional[List[dict]] = field(default_factory=list)
    zones: List[Zone] = field(default_factory=list)


@dataclass
class UserLaunchProfilesResult:
    launchProfiles: List[UserLaunchProfileJson]


@dataclass
class FileSystemResult:
    identifier: str
    server: str
    path: str
    type: str = "workspace"


@dataclass
class ListFileSystemsResultJson:
    fileSystems: List[FileSystemResult]


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
    tags: Optional[List[str]]
    enrollments: Optional[List[UserResult]]
    courseId: str
    pool: Optional[ImmutablePool]
    active: Optional[bool]
    grader: Optional[UserResult]
    fileSystem: Optional[FileSystemResult]
    snowTicket: Optional[str]
    quarter: Optional[str]
    subject: Optional[str]
    courseNumber: Optional[str]
    instructor: Optional[str]
    instructorEmail: Optional[str]
    courseName: Optional[str]


@dataclass
class CourseJson:
    courseId: str


@dataclass
class TeamResult:
    teamName: str
    sanitizedTeamName: Optional[str]
    uniqueName: Optional[str]
    gid: int
    members: Optional[List[UserResult]]
    course: Optional[CourseResult]


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
class Volume:
    type: str
    name: str
    server: str
    path: str
    accessMode: str
    pvcName: str


@dataclass
class EnvironmentJson:
    volumes: List[Volume]


@dataclass
class EnrollmentResult:
    username: str
    firstName: Optional[str]
    lastName: Optional[str]
    uid: int
    token: Optional[str]


@dataclass
class EnvironmentEnrollmentResult:
    enrollments: Optional[List[EnrollmentResult]]


@dataclass
class ListEnrollmentsForm:
    courseSlugs: List[str]
    username: str
    courseSlug: List[str]


@dataclass
class ListCoursesResultJson:
    courses: List[CourseJson]

@dataclass
class Quota:
    user: str
    resources: Dict[str, Any]

@dataclass
class UserQuotaResponse:
    quota: Quota

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


@dataclass
class EnrollmentJson:
    username: str
    course: str








