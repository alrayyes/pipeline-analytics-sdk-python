from enum import StrEnum

class FailureCategory(StrEnum):
    CODE_TESTS = "code_tests"
    CONFIG_SECRETS = "config_secrets"
    INFRASTRUCTURE = "infrastructure"
    NETWORK_TIMEOUTS = "network_timeouts"
    UNCATEGORISED = "uncategorised"

    def __str__(self) -> str:
        return str(self.value)
