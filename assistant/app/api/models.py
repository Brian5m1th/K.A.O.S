from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.model_repository import ModelRepository

router = APIRouter(prefix="/api/models", tags=["Models"])


@router.get("")
async def list_models(
    capability: str = "",
    session: AsyncSession = Depends(get_session),
):
    repo = ModelRepository(session)
    if capability:
        records = await repo.list_by_capability(capability)
    else:
        records = await repo.list_all()
    return {
        "total": len(records),
        "models": [
            {
                "id": r.id,
                "name": r.name,
                "provider": r.provider_name,
                "context_window": r.context_window,
                "capabilities": r.capabilities,
            }
            for r in records
        ],
    }


@router.get("/{model_name}")
async def get_model(
    model_name: str,
    session: AsyncSession = Depends(get_session),
):
    repo = ModelRepository(session)
    record = await repo.get_by_name(model_name)
    if record is None:
        return {"exists": False}
    return {"exists": True, "model": record}
