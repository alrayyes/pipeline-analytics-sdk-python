from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.job_log_reason import JobLogReason
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="JobLog")



@_attrs_define
class JobLog:
    """ 
        Attributes:
            available (bool): False when the forge gave no log; see `reason`. `lines` is then empty.
            lines (list[str]): The last lines of the log, oldest first, each cut at 4096 characters. Raw text, ANSI
                sequences included.
            truncated (bool): True when the log had more lines than were returned.
            forge_url (str): Deep link to the job on the forge, always present.
            reason (JobLogReason | Unset): Present when `available` is false. `unsupported`: the forge has no log API.
                `expired`: the forge no longer has this log. `forbidden`: the stored token can't read it. `unreachable`: the
                forge didn't answer.
     """

    available: bool
    lines: list[str]
    truncated: bool
    forge_url: str
    reason: JobLogReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        available = self.available

        lines = self.lines



        truncated = self.truncated

        forge_url = self.forge_url

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "available": available,
            "lines": lines,
            "truncated": truncated,
            "forgeUrl": forge_url,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        available = d.pop("available")

        lines = cast(list[str], d.pop("lines"))


        truncated = d.pop("truncated")

        forge_url = d.pop("forgeUrl")

        _reason = d.pop("reason", UNSET)
        reason: JobLogReason | Unset
        if isinstance(_reason,  Unset):
            reason = UNSET
        else:
            reason = JobLogReason(_reason)




        job_log = cls(
            available=available,
            lines=lines,
            truncated=truncated,
            forge_url=forge_url,
            reason=reason,
        )


        job_log.additional_properties = d
        return job_log

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
