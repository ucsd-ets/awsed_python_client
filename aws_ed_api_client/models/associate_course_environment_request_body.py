from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssociateCourseEnvironmentRequestBody")


@attr.s(auto_attribs=True)
class AssociateCourseEnvironmentRequestBody:
    """
    Attributes:
        environment (Union[Unset, str]):
        status (Union[Unset, str]):
        notes (Union[Unset, str]):
    """

    environment: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        environment = self.environment
        status = self.status
        notes = self.notes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if environment is not UNSET:
            field_dict["environment"] = environment
        if status is not UNSET:
            field_dict["status"] = status
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        environment = d.pop("environment", UNSET)

        status = d.pop("status", UNSET)

        notes = d.pop("notes", UNSET)

        associate_course_environment_request_body = cls(
            environment=environment,
            status=status,
            notes=notes,
        )

        associate_course_environment_request_body.additional_properties = d
        return associate_course_environment_request_body

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
