from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="FlakyRun")



@_attrs_define
class FlakyRun:
    """ 
        Attributes:
            run_id (str):
            forge_url (str): Deep link to the job this step failed in, on this specific run.
            started_at (datetime.datetime | Unset):
     """

    run_id: str
    forge_url: str
    started_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        run_id = self.run_id

        forge_url = self.forge_url

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "runId": run_id,
            "forgeUrl": forge_url,
        })
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        run_id = d.pop("runId")

        forge_url = d.pop("forgeUrl")

        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = datetime.datetime.fromisoformat(_started_at)




        flaky_run = cls(
            run_id=run_id,
            forge_url=forge_url,
            started_at=started_at,
        )


        flaky_run.additional_properties = d
        return flaky_run

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
