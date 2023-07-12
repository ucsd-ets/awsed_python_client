from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListEnrollmentsForm")


@attr.s(auto_attribs=True)
class ListEnrollmentsForm:
    """
    Attributes:
        course_slugs (Union[Unset, List[str]]):
        username (Union[Unset, str]):
        course_slug (Union[Unset, List[str]]):
    """

    course_slugs: Union[Unset, List[str]] = UNSET
    username: Union[Unset, str] = UNSET
    course_slug: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        course_slugs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.course_slugs, Unset):
            course_slugs = self.course_slugs

        username = self.username
        course_slug: Union[Unset, List[str]] = UNSET
        if not isinstance(self.course_slug, Unset):
            course_slug = self.course_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if course_slugs is not UNSET:
            field_dict["courseSlugs"] = course_slugs
        if username is not UNSET:
            field_dict["username"] = username
        if course_slug is not UNSET:
            field_dict["courseSlug"] = course_slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        course_slugs = cast(List[str], d.pop("courseSlugs", UNSET))

        username = d.pop("username", UNSET)

        course_slug = cast(List[str], d.pop("courseSlug", UNSET))

        list_enrollments_form = cls(
            course_slugs=course_slugs,
            username=username,
            course_slug=course_slug,
        )

        list_enrollments_form.additional_properties = d
        return list_enrollments_form

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
