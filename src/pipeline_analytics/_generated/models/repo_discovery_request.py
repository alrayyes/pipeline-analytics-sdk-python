from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.forge import Forge
from ..types import UNSET, Unset






T = TypeVar("T", bound="RepoDiscoveryRequest")



@_attrs_define
class RepoDiscoveryRequest:
    """ 
        Attributes:
            forge (Forge):
            token (str): Never stored -- used for this one lookup only.
            forgejo_instance_url (str | Unset):
     """

    forge: Forge
    token: str
    forgejo_instance_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        forge = self.forge.value

        token = self.token

        forgejo_instance_url = self.forgejo_instance_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "forge": forge,
            "token": token,
        })
        if forgejo_instance_url is not UNSET:
            field_dict["forgejoInstanceUrl"] = forgejo_instance_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forge = Forge(d.pop("forge"))




        token = d.pop("token")

        forgejo_instance_url = d.pop("forgejoInstanceUrl", UNSET)

        repo_discovery_request = cls(
            forge=forge,
            token=token,
            forgejo_instance_url=forgejo_instance_url,
        )


        repo_discovery_request.additional_properties = d
        return repo_discovery_request

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
