from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.user_profile_repository import (
    UserProfileRepository,
    UserProfileRecord,
)

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.get("/{user_id}")
async def get_user(user_id: str, session: AsyncSession = Depends(get_session)):
    repo = UserProfileRepository(session)
    record = await repo.get(user_id)
    if record is None:
        return {"exists": False}
    return {"exists": True, "profile": record}


@router.put("/{user_id}")
async def upsert_user(
    user_id: str,
    theme: str = "dark",
    language: str = "pt-BR",
    vault_path: str = "",
    auto_update: bool = True,
    telemetry_enabled: bool = False,
    session: AsyncSession = Depends(get_session),
):
    repo = UserProfileRepository(session)
    record = UserProfileRecord(
        user_id=user_id,
        theme=theme,
        language=language,
        vault_path=vault_path,
        auto_update=auto_update,
        telemetry_enabled=telemetry_enabled,
    )
    await repo.upsert(record)
    return {"status": "saved", "user_id": user_id}
