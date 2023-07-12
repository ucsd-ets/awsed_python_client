from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.course_environment_result_status import CourseEnvironmentResultStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CourseEnvironmentResult")


@attr.s(auto_attribs=True)
class CourseEnvironmentResult:
    """
    Attributes:
        name (Union[Unset, str]):
        environment (Union[Unset, str]):
        status (Union[Unset, CourseEnvironmentResultStatus]):
        notes (Union[Unset, str]):
        course_name (Union[Unset, str]):
        environment_slug (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    environment: Union[Unset, str] = UNSET
    status: Union[Unset, CourseEnvironmentResultStatus] = UNSET
    notes: Union[Unset, str] = UNSET
    course_name: Union[Unset, str] = UNSET
    environment_slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        environment = self.environment
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        notes = self.notes
        course_name = self.course_name
        environment_slug = self.environment_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if environment is not UNSET:
            field_dict["environment"] = environment
        if status is not UNSET:
            field_dict["status"] = status
        if notes is not UNSET:
            field_dict["notes"] = notes
        if course_name is not UNSET:
            field_dict["courseName"] = course_name
        if environment_slug is not UNSET:
            field_dict["environmentSlug"] = environment_slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        environment = d.pop("environment", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CourseEnvironmentResultStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CourseEnvironmentResultStatus(_status)

        notes = d.pop("notes", UNSET)

        course_name = d.pop("courseName", UNSET)

        environment_slug = d.pop("environmentSlug", UNSET)

        course_environment_result = cls(
            name=name,
            environment=environment,
            status=status,
            notes=notes,
            course_name=course_name,
            environment_slug=environment_slug,
        )

        course_environment_result.additional_properties = d
        return course_environment_result

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
