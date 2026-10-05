from enum import StrEnum

class SettingsValuesPipelinesSortOrder(StrEnum):
    LASTRUN = "lastRun"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
