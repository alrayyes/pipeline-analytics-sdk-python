from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="ApiToken")



@_attrs_define
class ApiToken:
    """ 
        Attributes:
            id (str): Identifies the token for revocation (DELETE /api/auth/tokens/{tokenId}) -- not itself a usable
                credential.
            token (str): The raw token value. Returned only here, at creation; store it now, it can't be retrieved again.
            created_at (datetime.datetime):
            expires_at (datetime.datetime):
     """

    id: str
    token: str
    created_at: datetime.datetime
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        token = self.token

        created_at = self.created_at.isoformat()

        expires_at = self.expires_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "token": token,
            "createdAt": created_at,
            "expiresAt": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        token = d.pop("token")

        created_at = datetime.datetime.fromisoformat(d.pop("createdAt"))




        expires_at = datetime.datetime.fromisoformat(d.pop("expiresAt"))




        api_token = cls(
            id=id,
            token=token,
            created_at=created_at,
            expires_at=expires_at,
        )


        api_token.additional_properties = d
        return api_token

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
