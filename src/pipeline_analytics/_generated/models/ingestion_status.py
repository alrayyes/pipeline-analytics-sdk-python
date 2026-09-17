from enum import StrEnum

class IngestionStatus(StrEnum):
    ACTIVE = "active"
    DEGRADED = "degraded"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
