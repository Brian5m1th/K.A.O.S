from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.feature_flag_repository import FeatureFlagRepository

router = APIRouter(prefix="/api/feature-flags", tags=["Feature Flags"])


@router.get("")
async def list_flags(
    session: AsyncSession = Depends(get_session),
):
    repo = FeatureFlagRepository(session)
    records = await repo.list_all()
    return {
        "total": len(records),
        "flags": [{"flag": r.flag, "enabled": r.enabled, "description": r.description} for r in records],
    }


@router.get("/{flag}")
async def get_flag(
    flag: str,
    session: AsyncSession = Depends(get_session),
):
    repo = FeatureFlagRepository(session)
    enabled = await repo.is_enabled(flag)
    return {"flag": flag, "enabled": enabled}


@router.put("/{flag}")
async def set_flag(
    flag: str,
    enabled: bool = True,
    session: AsyncSession = Depends(get_session),
):
    repo = FeatureFlagRepository(session)
    await repo.set(flag, enabled)
    return {"status": "saved", "flag": flag, "enabled": enabled}
