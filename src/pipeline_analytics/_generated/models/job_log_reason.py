from enum import StrEnum

class JobLogReason(StrEnum):
    EXPIRED = "expired"
    FORBIDDEN = "forbidden"
    UNREACHABLE = "unreachable"
    UNSUPPORTED = "unsupported"

    def __str__(self) -> str:
        return str(self.value)
