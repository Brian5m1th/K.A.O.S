from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Request, status
from loguru import logger
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.hash import hash_password
from app.auth.jwt import create_access_token, create_refresh_token
from app.database import get_session
from app.models.user import User

router = APIRouter(prefix="/api/admin", tags=["Admin"])


class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str
    role: str = "editor"


class UpdateUserRoleRequest(BaseModel):
    role: str


def _require_admin(request: Request):
    role = getattr(request.state, "role", "")
    if role != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")


@router.get("/users")
async def list_users(request: Request, session: AsyncSession = Depends(get_session)):
    _require_admin(request)
    result = await session.execute(select(User).order_by(User.created_at))
    users = result.scalars().all()
    return {
        "users": [
            {
                "id": str(u.id),
                "name": u.name,
                "email": u.email,
                "role": u.role,
                "created_at": u.created_at.isoformat() if u.created_at else "",
            }
            for u in users
        ]
    }


@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(
    request: Request,
    body: CreateUserRequest,
    session: AsyncSession = Depends(get_session),
):
    _require_admin(request)

    existing = await session.execute(select(User).where(User.email == body.email))
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Email already in use")

    if len(body.password) < 8:
        raise HTTPException(status_code=422, detail="Password must be at least 8 characters")

    user = User(
        id=uuid4(),
        name=body.name,
        email=body.email,
        password_hash=hash_password(body.password),
        role=body.role,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)

    logger.info("[admin] user created: {} ({}) role={}", user.name, user.email, user.role)
    return {
        "id": str(user.id),
        "name": user.name,
        "email": user.email,
        "role": user.role,
    }


@router.put("/users/{user_id}/role")
async def update_user_role(
    request: Request,
    user_id: str,
    body: UpdateUserRoleRequest,
    session: AsyncSession = Depends(get_session),
):
    _require_admin(request)
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.role = body.role
    await session.commit()
    logger.info("[admin] user {} role updated to {}", user_id, body.role)
    return {"status": "updated", "role": body.role}


@router.delete("/users/{user_id}")
async def delete_user(
    request: Request,
    user_id: str,
    session: AsyncSession = Depends(get_session),
):
    _require_admin(request)
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Can't delete yourself
    if str(user.id) == getattr(request.state, "user_id", ""):
        raise HTTPException(status_code=400, detail="Cannot delete yourself")

    await session.delete(user)
    await session.commit()
    logger.info("[admin] user {} deleted", user_id)
    return {"status": "deleted"}
