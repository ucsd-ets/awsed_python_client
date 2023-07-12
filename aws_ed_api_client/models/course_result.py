from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_system_result import FileSystemResult
    from ..models.immutable_pool import ImmutablePool
    from ..models.user_result import UserResult


T = TypeVar("T", bound="CourseResult")


@attr.s(auto_attribs=True)
class CourseResult:
    """
    Attributes:
        tags (Union[Unset, List[str]]):
        enrollments (Union[Unset, List['UserResult']]):
        course_id (Union[Unset, str]):
        pool (Union[Unset, ImmutablePool]):
        active (Union[Unset, bool]):
        grader (Union[Unset, UserResult]):
        file_system (Union[Unset, FileSystemResult]):
        snow_ticket (Union[Unset, str]):
        quarter (Union[Unset, str]):
        subject (Union[Unset, str]):
        course_number (Union[Unset, str]):
        instructor (Union[Unset, str]):
        instructor_email (Union[Unset, str]):
    """

    tags: Union[Unset, List[str]] = UNSET
    enrollments: Union[Unset, List["UserResult"]] = UNSET
    course_id: Union[Unset, str] = UNSET
    pool: Union[Unset, "ImmutablePool"] = UNSET
    active: Union[Unset, bool] = UNSET
    grader: Union[Unset, "UserResult"] = UNSET
    file_system: Union[Unset, "FileSystemResult"] = UNSET
    snow_ticket: Union[Unset, str] = UNSET
    quarter: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    course_number: Union[Unset, str] = UNSET
    instructor: Union[Unset, str] = UNSET
    instructor_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        enrollments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.enrollments, Unset):
            enrollments = []
            for enrollments_item_data in self.enrollments:
                enrollments_item = enrollments_item_data.to_dict()

                enrollments.append(enrollments_item)

        course_id = self.course_id
        pool: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool.to_dict()

        active = self.active
        grader: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.grader, Unset):
            grader = self.grader.to_dict()

        file_system: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file_system, Unset):
            file_system = self.file_system.to_dict()

        snow_ticket = self.snow_ticket
        quarter = self.quarter
        subject = self.subject
        course_number = self.course_number
        instructor = self.instructor
        instructor_email = self.instructor_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tags is not UNSET:
            field_dict["tags"] = tags
        if enrollments is not UNSET:
            field_dict["enrollments"] = enrollments
        if course_id is not UNSET:
            field_dict["courseId"] = course_id
        if pool is not UNSET:
            field_dict["pool"] = pool
        if active is not UNSET:
            field_dict["active"] = active
        if grader is not UNSET:
            field_dict["grader"] = grader
        if file_system is not UNSET:
            field_dict["fileSystem"] = file_system
        if snow_ticket is not UNSET:
            field_dict["snowTicket"] = snow_ticket
        if quarter is not UNSET:
            field_dict["quarter"] = quarter
        if subject is not UNSET:
            field_dict["subject"] = subject
        if course_number is not UNSET:
            field_dict["courseNumber"] = course_number
        if instructor is not UNSET:
            field_dict["instructor"] = instructor
        if instructor_email is not UNSET:
            field_dict["instructorEmail"] = instructor_email

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.file_system_result import FileSystemResult
        from ..models.immutable_pool import ImmutablePool
        from ..models.user_result import UserResult

        d = src_dict.copy()
        tags = cast(List[str], d.pop("tags", UNSET))

        enrollments = []
        _enrollments = d.pop("enrollments", UNSET)
        for enrollments_item_data in _enrollments or []:
            enrollments_item = UserResult.from_dict(enrollments_item_data)

            enrollments.append(enrollments_item)

        course_id = d.pop("courseId", UNSET)

        _pool = d.pop("pool", UNSET)
        pool: Union[Unset, ImmutablePool]
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = ImmutablePool.from_dict(_pool)

        active = d.pop("active", UNSET)

        _grader = d.pop("grader", UNSET)
        grader: Union[Unset, UserResult]
        if isinstance(_grader, Unset):
            grader = UNSET
        else:
            grader = UserResult.from_dict(_grader)

        _file_system = d.pop("fileSystem", UNSET)
        file_system: Union[Unset, FileSystemResult]
        if isinstance(_file_system, Unset):
            file_system = UNSET
        else:
            file_system = FileSystemResult.from_dict(_file_system)

        snow_ticket = d.pop("snowTicket", UNSET)

        quarter = d.pop("quarter", UNSET)

        subject = d.pop("subject", UNSET)

        course_number = d.pop("courseNumber", UNSET)

        instructor = d.pop("instructor", UNSET)

        instructor_email = d.pop("instructorEmail", UNSET)

        course_result = cls(
            tags=tags,
            enrollments=enrollments,
            course_id=course_id,
            pool=pool,
            active=active,
            grader=grader,
            file_system=file_system,
            snow_ticket=snow_ticket,
            quarter=quarter,
            subject=subject,
            course_number=course_number,
            instructor=instructor,
            instructor_email=instructor_email,
        )

        course_result.additional_properties = d
        return course_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
