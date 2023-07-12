from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.modification import Modification


T = TypeVar("T", bound="ImportRosterResultJson")


@attr.s(auto_attribs=True)
class ImportRosterResultJson:
    """
    Attributes:
        errors (Union[Unset, List[str]]):
        modifications (Union[Unset, List['Modification']]):
    """

    errors: Union[Unset, List[str]] = UNSET
    modifications: Union[Unset, List["Modification"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[Unset, List[str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        modifications: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.modifications, Unset):
            modifications = []
            for modifications_item_data in self.modifications:
                modifications_item = modifications_item_data.to_dict()

                modifications.append(modifications_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors
        if modifications is not UNSET:
            field_dict["modifications"] = modifications

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.modification import Modification

        d = src_dict.copy()
        errors = cast(List[str], d.pop("errors", UNSET))

        modifications = []
        _modifications = d.pop("modifications", UNSET)
        for modifications_item_data in _modifications or []:
            modifications_item = Modification.from_dict(modifications_item_data)

            modifications.append(modifications_item)

        import_roster_result_json = cls(
            errors=errors,
            modifications=modifications,
        )

        import_roster_result_json.additional_properties = d
        return import_roster_result_json

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
