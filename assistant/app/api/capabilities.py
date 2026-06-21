from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.repositories.capability_policy_repository import (
    CapabilityPolicyRepository,
)

router = APIRouter(prefix="/api/capabilities", tags=["Capabilities"])


@router.get("")
async def list_policies(
    session: AsyncSession = Depends(get_session),
):
    repo = CapabilityPolicyRepository(session)
    records = await repo.list_all()
    return {
        "total": len(records),
        "policies": [
            {
                "id": r.id,
                "capability": r.capability,
                "priority": r.priority_order,
                "model_id": r.model_id,
                "model_name": r.model_name,
            }
            for r in records
        ],
    }


@router.get("/{capability}")
async def get_policies_by_capability(
    capability: str,
    session: AsyncSession = Depends(get_session),
):
    repo = CapabilityPolicyRepository(session)
    records = await repo.get_by_capability(capability)
    return {
        "capability": capability,
        "total": len(records),
        "policies": [
            {
                "id": r.id,
                "priority": r.priority_order,
                "model_id": r.model_id,
                "model_name": r.model_name,
            }
            for r in records
        ],
    }


@router.post("/{capability}")
async def create_policy(
    capability: str,
    priority_order: int,
    model_id: int,
    session: AsyncSession = Depends(get_session),
):
    repo = CapabilityPolicyRepository(session)
    policy_id = await repo.upsert(
        capability=capability,
        priority_order=priority_order,
        model_id=model_id,
    )
    return {"status": "created", "id": policy_id}


@router.delete("/{policy_id}")
async def delete_policy(
    policy_id: int,
    session: AsyncSession = Depends(get_session),
):
    repo = CapabilityPolicyRepository(session)
    deleted = await repo.delete(policy_id)
    return {"status": "deleted" if deleted else "not_found"}
