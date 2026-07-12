"""
Secrets Management API — Desktop → Backend secrets storage.

Desktop envia chaves (OpenAI, Anthropic, etc.) → Backend salva criptografado.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from pathlib import Path
import json
from cryptography.fernet import Fernet
from loguru import logger

from app.config.settings import settings

router = APIRouter(prefix="/api/secrets", tags=["Secrets"])


# ── Models ──────────────────────────────────────────────────────────────


class SecretRequest(BaseModel):
    provider: str = Field(..., description="Provider name")
    key: str = Field(..., description="API key value")
    metadata: Optional[Dict[str, Any]] = None


class SecretResponse(BaseModel):
    provider: str
    saved: bool
    message: str


# ── Encryption ──────────────────────────────────────────────────────────


def _get_cipher() -> Fernet:
    key = settings.SECRET_KEY.encode()
    if len(key) < 32:
        key = key.ljust(32, b'0')
    elif len(key) > 32:
        key = key[:32]
    return Fernet(key) if len(key) == 32 else Fernet(Fernet.generate_key())


def _secrets_path() -> Path:
    return Path(getattr(settings, 'SECRETS_FILE', "data/secrets.enc"))


def _load_secrets() -> dict:
    path = _secrets_path()
    if not path.exists():
        return {}
    try:
        cipher = _get_cipher()
        with open(path, "rb") as f:
            return json.loads(cipher.decrypt(f.read()).decode())
    except Exception as e:
        logger.warning(f"[secrets] Failed to load: {e}")
        return {}


def _save_secrets(secrets: dict) -> None:
    path = _secrets_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        cipher = _get_cipher()
        with open(path, "wb") as f:
            f.write(cipher.encrypt(json.dumps(secrets).encode()))
    except Exception as e:
        logger.error(f"[secrets] Failed to save: {e}")
        raise HTTPException(status_code=500, detail="Failed to save secrets")


# ── API Endpoints ───────────────────────────────────────────────────────


@router.post("/set")
async def set_secret(request: SecretRequest):
    if not request.key.strip():
        raise HTTPException(400, "Key cannot be empty")
    provider = request.provider.lower().strip()
    if not provider:
        raise HTTPException(400, "Provider name required")

    secrets = _load_secrets()
    secrets[provider] = {"key": request.key, "metadata": request.metadata or {}}
    _save_secrets(secrets)
    logger.info(f"[secrets] Saved secret for: {provider}")
    return SecretResponse(provider=provider, saved=True, message=f"Secret for {provider} saved")


@router.get("/status")
async def secrets_status():
    secrets = _load_secrets()
    known = ["openai", "anthropic", "gemini", "ollama", "airllm", "cohere", "groq"]
    configured = {p: p in secrets for p in known}
    return {"configured": configured, "missing": [p for p in known if p not in secrets], "total": len(secrets)}


@router.get("/providers")
async def list_providers():
    secrets = _load_secrets()
    return {"providers": [{"name": p, "configured": p in secrets} for p in ["openai", "anthropic", "gemini", "ollama", "airllm", "cohere", "groq"]]}


@router.delete("/{provider}")
async def delete_secret(provider: str):
    provider = provider.lower().strip()
    secrets = _load_secrets()
    if provider not in secrets:
        raise HTTPException(404, f"Secret for {provider} not found")
    del secrets[provider]
    _save_secrets(secrets)
    logger.info(f"[secrets] Deleted secret for: {provider}")
    return {"deleted": True, "provider": provider}
