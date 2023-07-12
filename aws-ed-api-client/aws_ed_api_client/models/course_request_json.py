from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CourseRequestJson")


@attr.s(auto_attribs=True)
class CourseRequestJson:
    """
    Attributes:
        name (Union[Unset, str]):
        student_role (Union[Unset, str]):
        instructor_role (Union[Unset, str]):
        aws_credential_id (Union[Unset, str]):
        grader (Union[Unset, str]):
        file_system (Union[Unset, str]):
        active (Union[Unset, bool]):
        snow_ticket (Union[Unset, str]):
        quarter (Union[Unset, str]):
        subject (Union[Unset, str]):
        course_number (Union[Unset, str]):
        instructor (Union[Unset, str]):
        instructor_email (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    student_role: Union[Unset, str] = UNSET
    instructor_role: Union[Unset, str] = UNSET
    aws_credential_id: Union[Unset, str] = UNSET
    grader: Union[Unset, str] = UNSET
    file_system: Union[Unset, str] = UNSET
    active: Union[Unset, bool] = UNSET
    snow_ticket: Union[Unset, str] = UNSET
    quarter: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    course_number: Union[Unset, str] = UNSET
    instructor: Union[Unset, str] = UNSET
    instructor_email: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        student_role = self.student_role
        instructor_role = self.instructor_role
        aws_credential_id = self.aws_credential_id
        grader = self.grader
        file_system = self.file_system
        active = self.active
        snow_ticket = self.snow_ticket
        quarter = self.quarter
        subject = self.subject
        course_number = self.course_number
        instructor = self.instructor
        instructor_email = self.instructor_email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if student_role is not UNSET:
            field_dict["studentRole"] = student_role
        if instructor_role is not UNSET:
            field_dict["instructorRole"] = instructor_role
        if aws_credential_id is not UNSET:
            field_dict["awsCredentialId"] = aws_credential_id
        if grader is not UNSET:
            field_dict["grader"] = grader
        if file_system is not UNSET:
            field_dict["fileSystem"] = file_system
        if active is not UNSET:
            field_dict["active"] = active
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
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        student_role = d.pop("studentRole", UNSET)

        instructor_role = d.pop("instructorRole", UNSET)

        aws_credential_id = d.pop("awsCredentialId", UNSET)

        grader = d.pop("grader", UNSET)

        file_system = d.pop("fileSystem", UNSET)

        active = d.pop("active", UNSET)

        snow_ticket = d.pop("snowTicket", UNSET)

        quarter = d.pop("quarter", UNSET)

        subject = d.pop("subject", UNSET)

        course_number = d.pop("courseNumber", UNSET)

        instructor = d.pop("instructor", UNSET)

        instructor_email = d.pop("instructorEmail", UNSET)

        course_request_json = cls(
            name=name,
            student_role=student_role,
            instructor_role=instructor_role,
            aws_credential_id=aws_credential_id,
            grader=grader,
            file_system=file_system,
            active=active,
            snow_ticket=snow_ticket,
            quarter=quarter,
            subject=subject,
            course_number=course_number,
            instructor=instructor,
            instructor_email=instructor_email,
        )

        course_request_json.additional_properties = d
        return course_request_json

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
