"""Evolution API Adapter for WhatsApp Communication Channel.

SDD-KAOS-EVOLUTION-001: Agnostic implementation wrapping Evolution API logic.
"""
from __future__ import annotations

import hmac
import hashlib
import json
import time
from typing import Any, List
import httpx
from loguru import logger

from app.runtime.communication.base import CommunicationProvider
from app.core.credential_service import CredentialManager
from app.config.settings import settings


class EvolutionWhatsAppAdapter(CommunicationProvider):
    """Adapter for WhatsApp channel powered by Evolution API."""

    def __init__(self, api_url: str | None = None) -> None:
        self._api_url = (api_url or settings.WHATSAPP_API_URL or "").rstrip("/")
        self._license_url = "https://license.evolutionfoundation.com.br"
        self._instance_id = "550e8400-e29b-41d4-a716-446655440000"

    def _get_api_key(self) -> str | None:
        return CredentialManager.get_credential("whatsapp", "api_key")

    async def connect(self) -> bool:
        api_key = self._get_api_key()
        if not self._api_url or not api_key:
            logger.warning("[whatsapp-evolution] Missing api_url or api_key in CredentialManager.")
            return False
        return True

    async def disconnect(self) -> bool:
        # evolution-api deactivates on shutdown if requested, but we can do a local close
        return True

    async def health(self) -> dict[str, Any]:
        api_key = self._get_api_key()
        if not self._api_url or not api_key:
            return {"status": "unconfigured", "healthy": False}
        
        try:
            start = time.perf_counter()
            async with httpx.AsyncClient(timeout=5) as client:
                # Check health of local evolution api container
                resp = await client.get(
                    f"{self._api_url}/instance/fetch",
                    headers={"Authorization": f"Bearer {api_key}"}
                )
                latency = round((time.perf_counter() - start) * 1000, 2)
                if resp.is_success:
                    return {"status": "connected", "healthy": True, "latency_ms": latency}
                return {"status": f"HTTP {resp.status_code}", "healthy": False}
        except Exception as e:
            return {"status": "error", "healthy": False, "error": str(e)}

    async def send(self, to: str, message: str) -> dict[str, Any]:
        api_key = self._get_api_key()
        if not self._api_url or not api_key:
            return {"status": "error", "message": "WhatsApp not configured"}

        try:
            async with httpx.AsyncClient(timeout=15) as client:
                resp = await client.post(
                    f"{self._api_url}/message/send",
                    json={"number": to, "text": message},
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json"
                    }
                )
                if resp.is_success:
                    logger.info(f"[whatsapp-evolution] Message sent to {to}")
                    return {"status": "sent", "to": to}
                return {"status": "error", "message": f"HTTP {resp.status_code}: {resp.text}"}
        except Exception as e:
            logger.error(f"[whatsapp-evolution] Send failed: {e}")
            return {"status": "error", "message": str(e)}

    async def receive(self) -> List[dict[str, Any]]:
        # Usually handled asynchronously via webhooks, return empty list
        return []

    async def authenticate(self, credentials: dict[str, Any]) -> bool:
        """Runs the registration/polling/activation flow.
        
        Credentials can include: {"step": "init"}, {"step": "status", "token": "..."}
        """
        step = credentials.get("step")
        if step == "init":
            return await self._init_registration()
        elif step == "activate":
            token = credentials.get("token")
            api_key = credentials.get("api_key")
            if not token or not api_key:
                return False
            return await self._activate_license(token, api_key)
        return False

    async def refresh(self) -> bool:
        # license heartbeat periodic update
        api_key = self._get_api_key()
        if not api_key:
            return False
        return await self.send_heartbeat(api_key)

    # ── Wizard Helper Methods ──────────────────────────────────────────

    async def _init_registration(self) -> dict[str, Any] | None:
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.post(
                    f"{self._license_url}/v1/register/init",
                    json={
                        "tier": "community",
                        "version": "2.4.0",
                        "instance_id": self._instance_id
                    }
                )
                if resp.is_success:
                    data = resp.json()
                    return {
                        "register_url": data.get("register_url"),
                        "token": data.get("token"),
                        "instance_id": self._instance_id
                    }
                logger.error(f"[whatsapp-evolution] Init failed: {resp.text}")
        except Exception as e:
            logger.exception(f"[whatsapp-evolution] Exception during registration init: {e}")
        return None

    async def _activate_license(self, token: str, api_key: str) -> bool:
        try:
            # 1. Persist the API key in the Credential Manager
            CredentialManager.set_credential("whatsapp", "api_key", api_key)

            # 2. Call the activate endpoint on the licensing server using HMAC signature
            payload = {
                "instance_id": self._instance_id,
                "version": "2.4.0"
            }
            body = json.dumps(payload, separators=(",", ":"))
            signature = hmac.new(
                api_key.encode(),
                body.encode(),
                hashlib.sha256
            ).hexdigest()

            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.post(
                    f"{self._license_url}/v1/activate",
                    content=body,
                    headers={
                        "Content-Type": "application/json",
                        "X-API-Key": api_key,
                        "X-Signature": signature
                    }
                )
                if resp.is_success:
                    logger.info("[whatsapp-evolution] License activated successfully!")
                    return True
                logger.error(f"[whatsapp-evolution] Activation failed: {resp.text}")
        except Exception as e:
            logger.exception(f"[whatsapp-evolution] Exception during license activation: {e}")
        return False

    async def send_heartbeat(self, api_key: str) -> bool:
        try:
            payload = {
                "instance_id": self._instance_id,
                "telemetry_bundle": {
                    "features": ["whatsapp", "automation", "assistant"],
                    "uptime": 1234
                }
            }
            body = json.dumps(payload, separators=(",", ":"))
            signature = hmac.new(
                api_key.encode(),
                body.encode(),
                hashlib.sha256
            ).hexdigest()

            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.post(
                    f"{self._license_url}/v1/heartbeat",
                    content=body,
                    headers={
                        "Content-Type": "application/json",
                        "X-API-Key": api_key,
                        "X-Signature": signature
                    }
                )
                if resp.is_success:
                    logger.debug("[whatsapp-evolution] Heartbeat sent successfully.")
                    return True
                logger.warning(f"[whatsapp-evolution] Heartbeat HTTP {resp.status_code}: {resp.text}")
        except Exception as e:
            logger.error(f"[whatsapp-evolution] Heartbeat request failed: {e}")
        return False
