from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.user_model_profile_repository import (
    UserModelProfileRepository,
)

router = APIRouter(prefix="/api/user-model-profiles", tags=["User Model Profiles"])


@router.get("/{user_id}")
async def list_user_profiles(
    user_id: str,
    session: AsyncSession = Depends(get_session),
):
    repo = UserModelProfileRepository(session)
    records = await repo.list_by_user(user_id)
    return {
        "total": len(records),
        "profiles": [
            {"id": str(r.id), "workflow": r.workflow_type, "model": r.model_name}
            for r in records
        ],
    }


@router.get("/{user_id}/{workflow_type}")
async def get_user_profile(
    user_id: str,
    workflow_type: str,
    session: AsyncSession = Depends(get_session),
):
    repo = UserModelProfileRepository(session)
    record = await repo.get(user_id, workflow_type)
    if record is None:
        return {"exists": False}
    return {"exists": True, "model": record.model_name}


@router.put("/{user_id}/{workflow_type}")
async def upsert_user_profile(
    user_id: str,
    workflow_type: str,
    model_name: str,
    session: AsyncSession = Depends(get_session),
):
    repo = UserModelProfileRepository(session)
    profile_id = await repo.upsert(
        user_id=user_id,
        workflow_type=workflow_type,
        model_name=model_name,
    )
    return {"status": "saved", "id": str(profile_id)}


@router.delete("/{profile_id}")
async def delete_user_profile(
    profile_id: str,
    session: AsyncSession = Depends(get_session),
):
    repo = UserModelProfileRepository(session)
    deleted = await repo.delete(UUID(profile_id))
    return {"status": "deleted" if deleted else "not_found"}
