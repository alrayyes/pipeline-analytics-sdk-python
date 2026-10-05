from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.forge import Forge
from ..types import UNSET, Unset






T = TypeVar("T", bound="SavedForgeToken")



@_attrs_define
class SavedForgeToken:
    """ 
        Attributes:
            id (str):
            forge (Forge):
            token_masked (str): Last four characters only, e.g. "****1234". The token is never returned.
            forgejo_instance_url (str | Unset): Set for Forgejo, absent for GitHub.
     """

    id: str
    forge: Forge
    token_masked: str
    forgejo_instance_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        forge = self.forge.value

        token_masked = self.token_masked

        forgejo_instance_url = self.forgejo_instance_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "forge": forge,
            "tokenMasked": token_masked,
        })
        if forgejo_instance_url is not UNSET:
            field_dict["forgejoInstanceUrl"] = forgejo_instance_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        forge = Forge(d.pop("forge"))




        token_masked = d.pop("tokenMasked")

        forgejo_instance_url = d.pop("forgejoInstanceUrl", UNSET)

        saved_forge_token = cls(
            id=id,
            forge=forge,
            token_masked=token_masked,
            forgejo_instance_url=forgejo_instance_url,
        )


        saved_forge_token.additional_properties = d
        return saved_forge_token

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
