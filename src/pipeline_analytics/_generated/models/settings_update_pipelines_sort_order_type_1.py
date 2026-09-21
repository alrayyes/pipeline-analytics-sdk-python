from enum import StrEnum

class SettingsUpdatePipelinesSortOrderType1(StrEnum):
    LASTRUN = "lastRun"
    NAME = "name"

    def __str__(self) -> str:
        return str(self.value)
