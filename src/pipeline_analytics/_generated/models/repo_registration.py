from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.forge import Forge
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepoRegistration")


@_attrs_define
class RepoRegistration:
    """
    Attributes:
        forge (Forge):
        identifier (str):
        token (str): Repo-scoped personal access token. Never echoed back.
        forgejo_instance_url (str | Unset):
    """

    forge: Forge
    identifier: str
    token: str
    forgejo_instance_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        forge = self.forge.value

        identifier = self.identifier

        token = self.token

        forgejo_instance_url = self.forgejo_instance_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "forge": forge,
                "identifier": identifier,
                "token": token,
            }
        )
        if forgejo_instance_url is not UNSET:
            field_dict["forgejoInstanceUrl"] = forgejo_instance_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forge = Forge(d.pop("forge"))

        identifier = d.pop("identifier")

        token = d.pop("token")

        forgejo_instance_url = d.pop("forgejoInstanceUrl", UNSET)

        repo_registration = cls(
            forge=forge,
            identifier=identifier,
            token=token,
            forgejo_instance_url=forgejo_instance_url,
        )

        repo_registration.additional_properties = d
        return repo_registration

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
