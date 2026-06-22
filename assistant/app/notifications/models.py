from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4


class NotificationLevel(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    SUCCESS = "success"


@dataclass
class Notification:
    id: UUID = field(default_factory=uuid4)
    level: NotificationLevel = NotificationLevel.INFO
    title: str = ""
    message: str = ""
    source: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    read: bool = False
    data: dict | None = None
