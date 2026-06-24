import secrets
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException, Request, status
from loguru import logger
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.hash import hash_password, verify_password
from app.auth.jwt import (
    create_access_token,
    create_refresh_token,
    decode_token,
)
from app.database import get_session
from app.models.user import User

router = APIRouter(prefix="/auth", tags=["Auth"])

# In-memory fallback when PostgreSQL is unavailable
_memory_users: dict[str, dict] = {}


class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class ResetPasswordRequest(BaseModel):
    email: str
    api_key: str
    new_password: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    user: dict


class UserResponse(BaseModel):
    id: str
    name: str
    email: str
    role: str
    created_at: str


class SetupStatusResponse(BaseModel):
    configured: bool


class ApiKeyStatusResponse(BaseModel):
    configured: bool
    masked: str


async def _get_db_session():
    session = None
    try:
        session_iterator = get_session()
        session = await anext(session_iterator)
    except Exception as e:
        logger.warning("[auth] database unavailable, using in-memory store: {}", e)
        yield None
        return

    try:
        yield session
    finally:
        await session.close()


@router.get("/setup-status", response_model=SetupStatusResponse)
async def get_setup_status(session: AsyncSession | None = Depends(_get_db_session)):
    logger.info("[auth-api] GET /setup-status initiated")
    if session is not None:
        try:
            result = await session.execute(select(User).limit(1))
            user = result.scalar_one_or_none()
            configured = user is not None
            logger.info("[auth-api] GET /setup-status: configured={} (db)", configured)
            return SetupStatusResponse(configured=configured)
        except Exception as e:
            logger.warning("[auth-api] GET /setup-status: db query failed: {}", e)
            pass
    configured = len(_memory_users) > 0
    logger.info("[auth-api] GET /setup-status: configured={} (memory)", configured)
    return SetupStatusResponse(configured=configured)


@router.post(
    "/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED
)
async def register(
    body: RegisterRequest, session: AsyncSession | None = Depends(_get_db_session)
):
    logger.info("[auth-api] POST /register called for email: {}", body.email)
    if len(body.password) < 8:
        raise HTTPException(
            status_code=422, detail="Password must be at least 8 characters"
        )

    # Check if admin exists
    admin_exists = False
    if session is not None:
        try:
            result = await session.execute(select(User).limit(1))
            admin_exists = result.scalar_one_or_none() is not None
        except Exception:
            pass
    admin_exists = admin_exists or len(_memory_users) > 0

    if admin_exists:
        raise HTTPException(
            status_code=400,
            detail="Admin user already exists. Use /auth/login instead.",
        )

    user_id = str(uuid4())
    password_hash = hash_password(body.password)

    if session is not None:
        try:
            user = User(
                id=uuid4(),
                name=body.name,
                email=body.email,
                password_hash=password_hash,
                role="admin",
            )
            session.add(user)
            await session.commit()
            await session.refresh(user)
            user_id = str(user.id)
            logger.info(
                "[auth] admin user created (db): {} ({})", body.name, body.email
            )
        except Exception as e:
            logger.warning("[auth] db write failed, falling back to memory: {}", e)
            _memory_users[body.email] = {
                "id": user_id,
                "name": body.name,
                "email": body.email,
                "password_hash": password_hash,
                "role": "admin",
            }
    else:
        _memory_users[body.email] = {
            "id": user_id,
            "name": body.name,
            "email": body.email,
            "password_hash": password_hash,
            "role": "admin",
        }
        logger.info(
            "[auth] admin user created (memory): {} ({})", body.name, body.email
        )

    tokens = _generate_tokens(user_id, body.email, "admin")
    return TokenResponse(
        **tokens,
        user={"id": user_id, "name": body.name, "email": body.email, "role": "admin"},
    )


@router.post("/login", response_model=TokenResponse)
async def login(
    body: LoginRequest, session: AsyncSession | None = Depends(_get_db_session)
):
    user_data = None

    # Try DB first
    if session is not None:
        try:
            result = await session.execute(select(User).where(User.email == body.email))
            db_user = result.scalar_one_or_none()
            if db_user and verify_password(body.password, db_user.password_hash):
                user_data = {
                    "id": str(db_user.id),
                    "name": db_user.name,
                    "email": db_user.email,
                    "role": db_user.role,
                }
        except Exception:
            pass

    # Fallback to memory
    if user_data is None:
        mem_user = _memory_users.get(body.email)
        if mem_user and verify_password(body.password, mem_user["password_hash"]):
            user_data = {
                "id": mem_user["id"],
                "name": mem_user["name"],
                "email": mem_user["email"],
                "role": mem_user["role"],
            }

    if not user_data:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    logger.info("[auth] user logged in: {} ({})", user_data["name"], user_data["email"])
    tokens = _generate_tokens(user_data["id"], user_data["email"], user_data["role"])
    return TokenResponse(**tokens, user=user_data)


@router.post("/reset-password")
async def reset_password(
    body: ResetPasswordRequest,
    request: Request,
    session: AsyncSession | None = Depends(_get_db_session),
):
    logger.info("[auth-api] POST /reset-password called for email: {}", body.email)

    # Verify Master API key
    app_key = getattr(request.app.state, "api_key", None)
    if not app_key or body.api_key != app_key:
        logger.warning(
            "[auth-api] reset password rejected: invalid Master API Key for: {}",
            body.email,
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Master API Key"
        )

    if len(body.new_password) < 8:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Password must be at least 8 characters",
        )

    password_hash = hash_password(body.new_password)

    updated = False
    if session is not None:
        try:
            result = await session.execute(select(User).where(User.email == body.email))
            user = result.scalar_one_or_none()
            if user:
                user.password_hash = password_hash
                await session.commit()
                updated = True
                logger.info(
                    "[auth-api] password reset successfully (db) for: {}", body.email
                )
        except Exception as e:
            logger.warning("[auth-api] failed to reset password in db: {}", e)

    if not updated:
        mem_user = _memory_users.get(body.email)
        if mem_user:
            mem_user["password_hash"] = password_hash
            updated = True
            logger.info(
                "[auth-api] password reset successfully (memory) for: {}", body.email
            )

    if not updated:
        logger.warning("[auth-api] reset password user not found: {}", body.email)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return {"message": "Password reset successfully"}


@router.get("/me", response_model=UserResponse)
async def get_me(request: Request):
    user_id = getattr(request.state, "user_id", None)
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return UserResponse(id=user_id, name="", email="", role="", created_at="")


@router.post("/refresh", response_model=TokenResponse)
async def refresh_token(body: dict):
    refresh_token_str = body.get("refresh_token", "")
    payload = decode_token(refresh_token_str)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user_id = payload.get("sub")
    email = payload.get("email", "")
    role = payload.get("role", "user")

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    tokens = _generate_tokens(user_id, email, role)
    return TokenResponse(
        **tokens, user={"id": user_id, "name": "", "email": email, "role": role}
    )


# Legacy endpoints (Fase 1 compat)


@router.get("/key", response_model=ApiKeyStatusResponse)
async def get_api_key(request: Request) -> ApiKeyStatusResponse:
    key = request.app.state.api_key
    masked = key[:6] + "*" * (len(key) - 8) + key[-2:]
    return ApiKeyStatusResponse(configured=True, masked=masked)


@router.post("/regenerate", response_model=ApiKeyStatusResponse)
async def regenerate_api_key(request: Request) -> ApiKeyStatusResponse:
    new_key = secrets.token_hex(32)
    request.app.state.api_key = new_key
    key_path = Path("data/api_key.txt")
    key_path.parent.mkdir(parents=True, exist_ok=True)
    key_path.write_text(new_key)
    logger.info("[auth] API key regenerated")
    masked = new_key[:6] + "*" * (len(new_key) - 8) + new_key[-2:]
    return ApiKeyStatusResponse(configured=True, masked=masked)


# Helpers


def _generate_tokens(user_id: str, email: str, role: str) -> dict:
    access = create_access_token({"sub": user_id, "email": email, "role": role})
    refresh = create_refresh_token({"sub": user_id, "email": email, "role": role})
    return {"access_token": access, "refresh_token": refresh}
