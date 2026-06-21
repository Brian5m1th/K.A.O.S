from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.provider_config_repository import (
    ProviderConfigRepository,
    ProviderConfigRecord,
)

router = APIRouter(prefix="/api/provider-configs", tags=["Provider Configs"])


@router.get("")
async def list_provider_configs(
    session: AsyncSession = Depends(get_session),
):
    repo = ProviderConfigRepository(session)
    records = await repo.list_all()
    return {
        "total": len(records),
        "configs": [
            {
                "id": r.id,
                "type": r.provider_type,
                "name": r.provider_name,
                "base_url": r.base_url,
                "is_active": r.is_active,
            }
            for r in records
        ],
    }


@router.get("/{provider_name}")
async def get_provider_config(
    provider_name: str,
    session: AsyncSession = Depends(get_session),
):
    repo = ProviderConfigRepository(session)
    record = await repo.get_by_name(provider_name)
    if record is None:
        return {"exists": False}
    return {"exists": True, "config": record}


@router.post("")
async def upsert_provider_config(
    provider_type: str,
    provider_name: str,
    api_key: str = "",
    base_url: str = "",
    is_active: bool = True,
    extra_config: dict[str, Any] = {},
    session: AsyncSession = Depends(get_session),
):
    repo = ProviderConfigRepository(session)
    record = ProviderConfigRecord(
        id=0,
        provider_type=provider_type,
        provider_name=provider_name,
        api_key=api_key or None,
        base_url=base_url or None,
        is_active=is_active,
        extra_config=extra_config,
    )
    config_id = await repo.upsert(record)
    return {"status": "saved", "id": config_id}


@router.delete("/{config_id}")
async def delete_provider_config(
    config_id: int,
    session: AsyncSession = Depends(get_session),
):
    repo = ProviderConfigRepository(session)
    deleted = await repo.delete(config_id)
    return {"status": "deleted" if deleted else "not_found"}
