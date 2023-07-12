from enum import Enum


class CourseEnvironmentResultStatus(str, Enum):
    APPROVED = "APPROVED"
    CANCELLED = "CANCELLED"
    INACTIVE = "INACTIVE"
    PENDING = "PENDING"
    READY = "READY"

    def __str__(self) -> str:
        return str(self.value)
