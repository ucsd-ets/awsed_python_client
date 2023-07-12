from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.course_result import CourseResult
    from ..models.user_result import UserResult


T = TypeVar("T", bound="TeamResult")


@attr.s(auto_attribs=True)
class TeamResult:
    """
    Attributes:
        team_name (Union[Unset, str]):
        unique_name (Union[Unset, str]):
        gid (Union[Unset, int]):
        members (Union[Unset, List['UserResult']]):
        course (Union[Unset, CourseResult]):
    """

    team_name: Union[Unset, str] = UNSET
    unique_name: Union[Unset, str] = UNSET
    gid: Union[Unset, int] = UNSET
    members: Union[Unset, List["UserResult"]] = UNSET
    course: Union[Unset, "CourseResult"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_name = self.team_name
        unique_name = self.unique_name
        gid = self.gid
        members: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members, Unset):
            members = []
            for members_item_data in self.members:
                members_item = members_item_data.to_dict()

                members.append(members_item)

        course: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.course, Unset):
            course = self.course.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_name is not UNSET:
            field_dict["teamName"] = team_name
        if unique_name is not UNSET:
            field_dict["uniqueName"] = unique_name
        if gid is not UNSET:
            field_dict["gid"] = gid
        if members is not UNSET:
            field_dict["members"] = members
        if course is not UNSET:
            field_dict["course"] = course

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.course_result import CourseResult
        from ..models.user_result import UserResult

        d = src_dict.copy()
        team_name = d.pop("teamName", UNSET)

        unique_name = d.pop("uniqueName", UNSET)

        gid = d.pop("gid", UNSET)

        members = []
        _members = d.pop("members", UNSET)
        for members_item_data in _members or []:
            members_item = UserResult.from_dict(members_item_data)

            members.append(members_item)

        _course = d.pop("course", UNSET)
        course: Union[Unset, CourseResult]
        if isinstance(_course, Unset):
            course = UNSET
        else:
            course = CourseResult.from_dict(_course)

        team_result = cls(
            team_name=team_name,
            unique_name=unique_name,
            gid=gid,
            members=members,
            course=course,
        )

        team_result.additional_properties = d
        return team_result

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
