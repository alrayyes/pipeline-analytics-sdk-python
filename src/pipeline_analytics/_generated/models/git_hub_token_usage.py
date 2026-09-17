from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rate_limit_status import RateLimitStatus


T = TypeVar("T", bound="GitHubTokenUsage")


@_attrs_define
class GitHubTokenUsage:
    """
    Attributes:
        token_masked (str): Last four characters only, e.g. "****1234".
        repos (list[str]): owner/name identifiers of every repo tracked under this token.
        status (RateLimitStatus | Unset):
    """

    token_masked: str
    repos: list[str]
    status: RateLimitStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token_masked = self.token_masked

        repos = self.repos

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tokenMasked": token_masked,
                "repos": repos,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.rate_limit_status import RateLimitStatus

        d = dict(src_dict)
        token_masked = d.pop("tokenMasked")

        repos = cast(list[str], d.pop("repos"))

        _status = d.pop("status", UNSET)
        status: RateLimitStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RateLimitStatus.from_dict(_status)

        git_hub_token_usage = cls(
            token_masked=token_masked,
            repos=repos,
            status=status,
        )

        git_hub_token_usage.additional_properties = d
        return git_hub_token_usage

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
