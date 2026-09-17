from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.forge import Forge
from ..models.ingestion_status import IngestionStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="Repo")



@_attrs_define
class Repo:
    """ 
        Attributes:
            id (str):
            forge (Forge):
            identifier (str): owner/name on the forge.
            token_masked (str): The stored token's display form, e.g. "****1234" (forge-ingestion/spec.md's "Credential
                storage" -- never the full value).
            ingestion_status (IngestionStatus):
            forgejo_instance_url (str | Unset): Set only when forge is forgejo.
            ingestion_status_reason (str | Unset): Set when ingestionStatus is degraded.
     """

    id: str
    forge: Forge
    identifier: str
    token_masked: str
    ingestion_status: IngestionStatus
    forgejo_instance_url: str | Unset = UNSET
    ingestion_status_reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        forge = self.forge.value

        identifier = self.identifier

        token_masked = self.token_masked

        ingestion_status = self.ingestion_status.value

        forgejo_instance_url = self.forgejo_instance_url

        ingestion_status_reason = self.ingestion_status_reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "forge": forge,
            "identifier": identifier,
            "tokenMasked": token_masked,
            "ingestionStatus": ingestion_status,
        })
        if forgejo_instance_url is not UNSET:
            field_dict["forgejoInstanceUrl"] = forgejo_instance_url
        if ingestion_status_reason is not UNSET:
            field_dict["ingestionStatusReason"] = ingestion_status_reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        forge = Forge(d.pop("forge"))




        identifier = d.pop("identifier")

        token_masked = d.pop("tokenMasked")

        ingestion_status = IngestionStatus(d.pop("ingestionStatus"))




        forgejo_instance_url = d.pop("forgejoInstanceUrl", UNSET)

        ingestion_status_reason = d.pop("ingestionStatusReason", UNSET)

        repo = cls(
            id=id,
            forge=forge,
            identifier=identifier,
            token_masked=token_masked,
            ingestion_status=ingestion_status,
            forgejo_instance_url=forgejo_instance_url,
            ingestion_status_reason=ingestion_status_reason,
        )


        repo.additional_properties = d
        return repo

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
