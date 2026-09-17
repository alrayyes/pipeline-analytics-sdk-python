from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RateLimitStatus")


@_attrs_define
class RateLimitStatus:
    """
    Attributes:
        limit (int): Requests allowed per hour for this resource (usually "core").
        remaining (int):
        used (int):
        reset_at (datetime.datetime):
    """

    limit: int
    remaining: int
    used: int
    reset_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        remaining = self.remaining

        used = self.used

        reset_at = self.reset_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "limit": limit,
                "remaining": remaining,
                "used": used,
                "resetAt": reset_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit")

        remaining = d.pop("remaining")

        used = d.pop("used")

        reset_at = datetime.datetime.fromisoformat(d.pop("resetAt"))

        rate_limit_status = cls(
            limit=limit,
            remaining=remaining,
            used=used,
            reset_at=reset_at,
        )

        rate_limit_status.additional_properties = d
        return rate_limit_status

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
