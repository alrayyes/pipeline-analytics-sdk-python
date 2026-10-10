from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.quarantine import Quarantine





T = TypeVar("T", bound="StepQuarantine")



@_attrs_define
class StepQuarantine:
    """ 
        Attributes:
            quarantined (bool):
            quarantine (Quarantine | Unset): A person's mark on a flaky step. Present only while it is in force.
     """

    quarantined: bool
    quarantine: Quarantine | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.quarantine import Quarantine # noqa: PLC0415
        quarantined = self.quarantined

        quarantine: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quarantine, Unset):
            quarantine = self.quarantine.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "quarantined": quarantined,
        })
        if quarantine is not UNSET:
            field_dict["quarantine"] = quarantine

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.quarantine import Quarantine # noqa: PLC0415
        d = dict(src_dict)
        quarantined = d.pop("quarantined")

        _quarantine = d.pop("quarantine", UNSET)
        quarantine: Quarantine | Unset
        if isinstance(_quarantine,  Unset):
            quarantine = UNSET
        else:
            quarantine = Quarantine.from_dict(_quarantine)




        step_quarantine = cls(
            quarantined=quarantined,
            quarantine=quarantine,
        )


        step_quarantine.additional_properties = d
        return step_quarantine

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
