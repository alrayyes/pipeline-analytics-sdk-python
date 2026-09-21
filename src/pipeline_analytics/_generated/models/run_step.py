from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RunStep")



@_attrs_define
class RunStep:
    """ 
        Attributes:
            name (str):
            status (str):
            conclusion (str | Unset):
            forge_url (str | Unset): Deep link to this exact occurrence's job on the originating forge.
     """

    name: str
    status: str
    conclusion: str | Unset = UNSET
    forge_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        conclusion = self.conclusion

        forge_url = self.forge_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "status": status,
        })
        if conclusion is not UNSET:
            field_dict["conclusion"] = conclusion
        if forge_url is not UNSET:
            field_dict["forgeUrl"] = forge_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        conclusion = d.pop("conclusion", UNSET)

        forge_url = d.pop("forgeUrl", UNSET)

        run_step = cls(
            name=name,
            status=status,
            conclusion=conclusion,
            forge_url=forge_url,
        )


        run_step.additional_properties = d
        return run_step

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
