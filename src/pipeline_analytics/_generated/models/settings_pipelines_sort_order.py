from enum import StrEnum

class SettingsPipelinesSortOrder(StrEnum):
    LASTRUN = "lastRun"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
