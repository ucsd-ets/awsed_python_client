from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_course_environment_json import ListCourseEnvironmentJson


T = TypeVar("T", bound="ListCourseEnvironmentsResultJson")


@attr.s(auto_attribs=True)
class ListCourseEnvironmentsResultJson:
    """
    Attributes:
        environments (Union[Unset, List['ListCourseEnvironmentJson']]):
    """

    environments: Union[Unset, List["ListCourseEnvironmentJson"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        environments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.environments, Unset):
            environments = []
            for environments_item_data in self.environments:
                environments_item = environments_item_data.to_dict()

                environments.append(environments_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if environments is not UNSET:
            field_dict["environments"] = environments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.list_course_environment_json import ListCourseEnvironmentJson

        d = src_dict.copy()
        environments = []
        _environments = d.pop("environments", UNSET)
        for environments_item_data in _environments or []:
            environments_item = ListCourseEnvironmentJson.from_dict(environments_item_data)

            environments.append(environments_item)

        list_course_environments_result_json = cls(
            environments=environments,
        )

        list_course_environments_result_json.additional_properties = d
        return list_course_environments_result_json

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
