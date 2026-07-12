"""
Secrets Management API — Desktop → Backend secrets storage.

Desktop envia chaves (OpenAI, Anthropic, etc.) → Backend salva criptografado no .env / Vault.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Request
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from pathlib import Path
import json
import os
from cryptography.fernet import Fernet
from loguru import logger

from app.config.settings import settings
from app.database import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/api/secrets", tags=["Secrets"])


# ── Models ──────────────────────────────────────────────────────────────


class SecretRequest(BaseModel):
    provider: str = Field(..., description="Provider name: openai, anthropic, gemini, etc.")
    key: str = Field(..., description="API key value")
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)


class SecretResponse(BaseModel):
    provider: str
    status: str
    saved: bool


class SecretStatusResponse(BaseModel):
    provider: str
    configured: bool
    key_preview: Optional[str] = None

router = APIRouter(prefix="/api/secrets", tags=["Secrets"])


# ── Models ────────────────────────────────────────────────────────────────

class SecretRequest(BaseModel):
    provider: str = Field(..., description="Provider name: openai, anthropic, gemini, etc.")
    key: str = Field(..., description="API key / secret value")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Extra metadata")


class SecretResponse(BaseModel):
    provider: str
    saved: bool
    message: str


class SecretStatusResponse(BaseModel):
    configured: Dict[str, bool]
    missing: list[str]


# ── Encryption ──────────────────────────────────────────────────────────

def _get_cipher() -> Fernet:
    """Get or create Fernet cipher from settings.SECRET_KEY."""
    key = settings.SECRET_KEY.encode()
    # Fernet needs 32 url-safe base64 bytes
    if len(key) < 32:
        key = key.ljust(32, b'0')
    elif len(key) > 32:
        key = key[:32]
    return Fernet(Fernet.generate_key() if len(key) != 32 else Fernet(key))


def _secrets_path() -> Path:
    """Path to encrypted secrets file."""
    return Path(settings.SECRETS_FILE) if hasattr(settings, 'SECRETS_FILE') else Path("data/secrets.enc")


def _load_secrets() -> dict:
    """Load and decrypt secrets from file."""
    path = _secrets_path()
    if not path.exists():
        return {}
    try:
        cipher = _get_cipher()
        with open(path, "rb") as f:
            encrypted = f.read()
        decrypted = cipher.decrypt(encrypted).decode()
        return json.loads(decrypted)
    except Exception as e:
        logger.warning(f"[secrets] Failed to load secrets: {e}")
        return {}


def _save_secrets(secrets: dict) -> None:
    """Encrypt and save secrets to file."""
    path = _secrets_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        cipher = _get_cipher()
        encrypted = cipher.encrypt(json.dumps(secrets).encode())
        with open(path, "wb") as f:
            f.write(encrypted)
    except Exception as e:
        logger.error(f"[secrets] Failed to save secrets: {e}")
        raise HTTPException(status_code=500, detail="Failed to save secrets")


# ── API Endpoints ───────────────────────────────────────────────────────

@router.post("/set", response_model=SecretResponse)
async def set_secret(
    request: SecretRequest,
    current_user: dict = Depends(get_current_user),
):
    """Save a secret for a provider."""
    if not request.key or not request.key.strip():
        raise HTTPException(status_code=400, detail="Key cannot be empty")

    provider = request.provider.lower().strip()
    if not provider:
        raise HTTPException(status_code=400, detail="Provider name required")

    secrets = _load_secrets()
    secrets[provider] = {
        "key": request.key,
        "metadata": request.metadata or {},
    }
    _save_secrets(secrets)

    logger.info(f"[secrets] Saved secret for provider: {provider} (user: {current_user.get('id')})")
    return SecretResponse(provider=provider, saved=True, message=f"Secret for {provider} saved securely")


@router.get("/status", response_model=SecretStatusResponse)
async def secrets_status(current_user: dict = Depends(get_current_user)):
    """Check which providers have secrets configured."""
    secrets = _load_secrets()
    known_providers = ["openai", "anthropic", "gemini", "ollama", "airllm", "cohere", "groq"]
    configured = {p: p in secrets for p in known_providers}
    missing = [p for p in known_providers if p not in secrets]
    return SecretStatusResponse(configured=configured, missing=missing)


@router.delete("/{provider}")
async def delete_secret(
    provider: str,
    current_user: dict = Depends(get_current_user),
):
    """Delete a stored secret."""
    provider = provider.lower().strip()
    secrets = _load_secrets()
    if provider not in secrets:
        raise HTTPException(status_code=404, detail=f"Secret for {provider} not found")
    del secrets[provider]
    _save_secrets(secrets)
    logger.info(f"[secrets] Deleted secret for provider: {provider}")
    return {"deleted": True, "provider": provider}


@router.get("/providers")
async def list_providers():
    """List all known providers with their status."""
    secrets = _load_secrets()
    return {
        "providers": [
            {"name": p, "configured": p in secrets}
            for p in ["openai", "anthropic", "gemini", "ollama", "airllm", "cohere", "groq"]
        ]
    }