from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
import datetime






T = TypeVar("T", bound="Quarantine")



@_attrs_define
class Quarantine:
    """ A person's mark on a flaky step. Present only while it is in force.

        Attributes:
            note (str): Why the step is quarantined; empty when none was given.
            quarantined_at (datetime.datetime): When it was marked, or last renewed.
            expires_at (datetime.datetime): Thirty days after `quarantinedAt`. After this the mark is as if never set.
     """

    note: str
    quarantined_at: datetime.datetime
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        note = self.note

        quarantined_at = self.quarantined_at.isoformat()

        expires_at = self.expires_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "note": note,
            "quarantinedAt": quarantined_at,
            "expiresAt": expires_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        note = d.pop("note")

        quarantined_at = datetime.datetime.fromisoformat(d.pop("quarantinedAt"))




        expires_at = datetime.datetime.fromisoformat(d.pop("expiresAt"))




        quarantine = cls(
            note=note,
            quarantined_at=quarantined_at,
            expires_at=expires_at,
        )


        quarantine.additional_properties = d
        return quarantine

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
