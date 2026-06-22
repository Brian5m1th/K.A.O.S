from fastapi import APIRouter
from loguru import logger
from app.notifications.service import NotificationService
from app.notifications.models import NotificationLevel

router = APIRouter(prefix="/api/notifications", tags=["Notifications"])


@router.get("/")
async def list_notifications(unread_only: bool = False, limit: int = 50) -> dict:
    notifications = NotificationService.list(unread_only=unread_only, limit=limit)
    return {
        "notifications": [
            {
                "id": str(n.id),
                "level": n.level.value,
                "title": n.title,
                "message": n.message,
                "source": n.source,
                "created_at": n.created_at.isoformat(),
                "read": n.read,
                "data": n.data,
            }
            for n in notifications
        ]
    }


@router.post("/{notification_id}/read")
async def mark_read(notification_id: str) -> dict:
    ok = NotificationService.mark_read(notification_id)
    return {"status": "read" if ok else "not_found"}


@router.post("/read-all")
async def mark_all_read() -> dict:
    NotificationService.mark_all_read()
    return {"status": "all_read"}
