from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FileSystemJson:
    identifier: str
    server: str
    path: str


@dataclass
class UserJson:
    username: str
    uid: int
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    role: Optional[str] = None


@dataclass
class CourseJson:
    courseId: str
    tags: Optional[List[str]]
    enrollments: List[UserJson] = field(default_factory=lambda: [])
    fileSystem: Optional[FileSystemJson] = None
    grader: Optional[UserJson] = None


@dataclass
class CourseCourseResponse(object):
    courseId: str


@dataclass
class ListCourseResponse(object):
    courses: List[CourseCourseResponse]


@dataclass
class TeamJson:
    gid: int
    members: Optional[List[UserJson]]
    teamName: str
    uniqueName: Optional[str] = None


@dataclass
class ListTeamsResponse:
    teams: List[TeamJson]


class AwsedClient(metaclass=ABCMeta):
    @abstractmethod
    def list_teams_for_course(self, course_id: str) -> ListTeamsResponse:
        """Return the groups of a course"""
        pass

    @abstractmethod
    def list_enrollments(self) -> List:
        pass

    @abstractmethod
    def list_courses_by_tag(self, tag: str) -> ListCourseResponse:
        """Return the groups of a course"""
        pass

    @abstractmethod
    def list_courses(self) -> ListCourseResponse:
        """Return all courses"""
        pass

    @abstractmethod
    def describe_course(self, course_id: str) -> CourseJson:
        pass
