from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_field_error import ApiFieldError


T = TypeVar("T", bound="ApiError")


@attr.s(auto_attribs=True)
class ApiError:
    """
    Attributes:
        timestamp (Union[Unset, str]):
        status_code (Union[Unset, int]):
        message (Union[Unset, str]):
        request (Union[Unset, str]):
        fields (Union[Unset, List['ApiFieldError']]):
    """

    timestamp: Union[Unset, str] = UNSET
    status_code: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    request: Union[Unset, str] = UNSET
    fields: Union[Unset, List["ApiFieldError"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp
        status_code = self.status_code
        message = self.message
        request = self.request
        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if message is not UNSET:
            field_dict["message"] = message
        if request is not UNSET:
            field_dict["request"] = request
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.api_field_error import ApiFieldError

        d = src_dict.copy()
        timestamp = d.pop("timestamp", UNSET)

        status_code = d.pop("statusCode", UNSET)

        message = d.pop("message", UNSET)

        request = d.pop("request", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = ApiFieldError.from_dict(fields_item_data)

            fields.append(fields_item)

        api_error = cls(
            timestamp=timestamp,
            status_code=status_code,
            message=message,
            request=request,
            fields=fields,
        )

        api_error.additional_properties = d
        return api_error

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
