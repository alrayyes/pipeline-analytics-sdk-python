from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="Trend")



@_attrs_define
class Trend:
    """ 
        Attributes:
            timestamps (list[datetime.datetime]):
            p50 (list[float] | Unset): Seconds. Present on a duration trend.
            p90 (list[float] | Unset): Seconds. Present on a duration trend.
            rate (list[float] | Unset): 0-1. Present on a failure-rate trend.
     """

    timestamps: list[datetime.datetime]
    p50: list[float] | Unset = UNSET
    p90: list[float] | Unset = UNSET
    rate: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        timestamps = []
        for timestamps_item_data in self.timestamps:
            timestamps_item = timestamps_item_data.isoformat()
            timestamps.append(timestamps_item)



        p50: list[float] | Unset = UNSET
        if not isinstance(self.p50, Unset):
            p50 = self.p50



        p90: list[float] | Unset = UNSET
        if not isinstance(self.p90, Unset):
            p90 = self.p90



        rate: list[float] | Unset = UNSET
        if not isinstance(self.rate, Unset):
            rate = self.rate




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "timestamps": timestamps,
        })
        if p50 is not UNSET:
            field_dict["p50"] = p50
        if p90 is not UNSET:
            field_dict["p90"] = p90
        if rate is not UNSET:
            field_dict["rate"] = rate

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamps = []
        _timestamps = d.pop("timestamps")
        for timestamps_item_data in (_timestamps):
            timestamps_item = datetime.datetime.fromisoformat(timestamps_item_data)



            timestamps.append(timestamps_item)


        p50 = cast(list[float], d.pop("p50", UNSET))


        p90 = cast(list[float], d.pop("p90", UNSET))


        rate = cast(list[float], d.pop("rate", UNSET))


        trend = cls(
            timestamps=timestamps,
            p50=p50,
            p90=p90,
            rate=rate,
        )


        trend.additional_properties = d
        return trend

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
