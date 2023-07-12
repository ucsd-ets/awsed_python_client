from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.course_json import CourseJson


T = TypeVar("T", bound="ListCoursesResultJson")


@attr.s(auto_attribs=True)
class ListCoursesResultJson:
    """
    Attributes:
        courses (Union[Unset, List['CourseJson']]):
    """

    courses: Union[Unset, List["CourseJson"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        courses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.courses, Unset):
            courses = []
            for courses_item_data in self.courses:
                courses_item = courses_item_data.to_dict()

                courses.append(courses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if courses is not UNSET:
            field_dict["courses"] = courses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.course_json import CourseJson

        d = src_dict.copy()
        courses = []
        _courses = d.pop("courses", UNSET)
        for courses_item_data in _courses or []:
            courses_item = CourseJson.from_dict(courses_item_data)

            courses.append(courses_item)

        list_courses_result_json = cls(
            courses=courses,
        )

        list_courses_result_json.additional_properties = d
        return list_courses_result_json

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
