from enum import StrEnum

class SettingsUpdateForgeFilterType3Type1(StrEnum):
    ALL = "all"
    FORGEJO = "forgejo"
    GITHUB = "github"

    def __str__(self) -> str:
        return str(self.value)
