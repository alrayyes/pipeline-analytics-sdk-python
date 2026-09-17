from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.repo import Repo


T = TypeVar("T", bound="RepoList")


@_attrs_define
class RepoList:
    """
    Attributes:
        repos (list[Repo]):
        has_more (bool): True when repos beyond this page match the filter. Always false when limit was omitted.
    """

    repos: list[Repo]
    has_more: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        repos = []
        for repos_item_data in self.repos:
            repos_item = repos_item_data.to_dict()
            repos.append(repos_item)

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repos": repos,
                "hasMore": has_more,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo import Repo

        d = dict(src_dict)
        repos = []
        _repos = d.pop("repos")
        for repos_item_data in _repos:
            repos_item = Repo.from_dict(repos_item_data)

            repos.append(repos_item)

        has_more = d.pop("hasMore")

        repo_list = cls(
            repos=repos,
            has_more=has_more,
        )

        repo_list.additional_properties = d
        return repo_list

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
