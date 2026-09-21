from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.settings_forge_filter import SettingsForgeFilter
from ..models.settings_pipelines_health_filter import SettingsPipelinesHealthFilter
from ..models.settings_pipelines_sort_order import SettingsPipelinesSortOrder
from ..models.settings_theme import SettingsTheme






T = TypeVar("T", bound="Settings")



@_attrs_define
class Settings:
    """ 
        Attributes:
            theme (SettingsTheme):
            forge_filter (SettingsForgeFilter):
            pipelines_health_filter (SettingsPipelinesHealthFilter):
            pipelines_repo_selector (str): A tracked repo's id, or "all" for every repo -- not validated against an enum,
                since the set of valid values changes with what's currently tracked.
            pipelines_sort_order (SettingsPipelinesSortOrder):
     """

    theme: SettingsTheme
    forge_filter: SettingsForgeFilter
    pipelines_health_filter: SettingsPipelinesHealthFilter
    pipelines_repo_selector: str
    pipelines_sort_order: SettingsPipelinesSortOrder
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        theme = self.theme.value

        forge_filter = self.forge_filter.value

        pipelines_health_filter = self.pipelines_health_filter.value

        pipelines_repo_selector = self.pipelines_repo_selector

        pipelines_sort_order = self.pipelines_sort_order.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "theme": theme,
            "forgeFilter": forge_filter,
            "pipelinesHealthFilter": pipelines_health_filter,
            "pipelinesRepoSelector": pipelines_repo_selector,
            "pipelinesSortOrder": pipelines_sort_order,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        theme = SettingsTheme(d.pop("theme"))




        forge_filter = SettingsForgeFilter(d.pop("forgeFilter"))




        pipelines_health_filter = SettingsPipelinesHealthFilter(d.pop("pipelinesHealthFilter"))




        pipelines_repo_selector = d.pop("pipelinesRepoSelector")

        pipelines_sort_order = SettingsPipelinesSortOrder(d.pop("pipelinesSortOrder"))




        settings = cls(
            theme=theme,
            forge_filter=forge_filter,
            pipelines_health_filter=pipelines_health_filter,
            pipelines_repo_selector=pipelines_repo_selector,
            pipelines_sort_order=pipelines_sort_order,
        )


        settings.additional_properties = d
        return settings

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
