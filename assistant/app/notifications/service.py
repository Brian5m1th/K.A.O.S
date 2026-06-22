from loguru import logger
from app.notifications.models import Notification, NotificationLevel


class NotificationService:
    _notifications: list[Notification] = []

    @classmethod
    def notify(
        cls,
        level: NotificationLevel,
        title: str,
        message: str = "",
        source: str = "",
        data: dict | None = None,
    ) -> Notification:
        notification = Notification(
            level=level,
            title=title,
            message=message,
            source=source,
            data=data,
        )
        cls._notifications.append(notification)
        logger.info(f"[notification] {level.value}: {title}")
        return notification

    @classmethod
    def list(cls, unread_only: bool = False, limit: int = 50) -> list[Notification]:
        result = cls._notifications
        if unread_only:
            result = [n for n in result if not n.read]
        return sorted(result, key=lambda n: n.created_at, reverse=True)[:limit]

    @classmethod
    def mark_read(cls, notification_id: str) -> bool:
        for n in cls._notifications:
            if str(n.id) == notification_id:
                n.read = True
                return True
        return False

    @classmethod
    def mark_all_read(cls) -> None:
        for n in cls._notifications:
            n.read = True

    @classmethod
    def clear(cls) -> None:
        cls._notifications.clear()
