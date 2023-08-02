from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_error import ApiError


T = TypeVar("T", bound="ApiErrorResult")


@attr.s(auto_attribs=True)
class ApiErrorResult:
    """
    Attributes:
        error (Union[Unset, ApiError]):
    """

    error: Union[Unset, "ApiError"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_error import ApiError

        d = src_dict.copy()
        _error = d.pop("error", UNSET)
        error: Union[Unset, ApiError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ApiError.from_dict(_error)

        api_error_result = cls(
            error=error,
        )

        api_error_result.additional_properties = d
        return api_error_result

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
