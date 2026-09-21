from enum import StrEnum

class SettingsUpdatePipelinesHealthFilterType1(StrEnum):
    ALL = "all"
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"

    def __str__(self) -> str:
        return str(self.value)
