import secrets
from pathlib import Path

from fastapi import APIRouter, Request
from loguru import logger
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["Auth"])


class ApiKeyResponse(BaseModel):
    api_key: str
    masked: str


@router.get("/key", response_model=ApiKeyResponse)
async def get_api_key(request: Request) -> ApiKeyResponse:
    key = request.app.state.api_key
    masked = key[:6] + "*" * (len(key) - 8) + key[-2:]
    return ApiKeyResponse(api_key=key, masked=masked)


@router.post("/regenerate", response_model=ApiKeyResponse)
async def regenerate_api_key(request: Request) -> ApiKeyResponse:
    new_key = secrets.token_hex(32)
    request.app.state.api_key = new_key
    key_path = Path("data/api_key.txt")
    key_path.parent.mkdir(parents=True, exist_ok=True)
    key_path.write_text(new_key)
    logger.info("[auth] API key regenerated")
    masked = new_key[:6] + "*" * (len(new_key) - 8) + new_key[-2:]
    return ApiKeyResponse(api_key=new_key, masked=masked)
