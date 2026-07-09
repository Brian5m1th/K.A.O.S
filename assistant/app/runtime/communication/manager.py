"""Communication Runtime Manager.

SDD-KAOS-EVOLUTION-001: Orchestrates and exposes multiple communication channels (WhatsApp, Email, etc.).
"""
from typing import Any, Dict
from loguru import logger

from app.runtime.communication.base import CommunicationProvider
from app.runtime.communication.whatsapp_evolution import EvolutionWhatsAppAdapter
from app.runtime.registry import RuntimeRegistry


class CommunicationRuntime:
    """Manages and routes messages through pluggable communication channels."""

    def __init__(self) -> None:
        self._channels: Dict[str, CommunicationProvider] = {
            "whatsapp": EvolutionWhatsAppAdapter(),
        }

    def register_channel(self, name: str, provider: CommunicationProvider) -> None:
        """Register a new channel provider (e.g. Email, Slack)."""
        self._channels[name] = provider
        logger.info(f"[CommunicationRuntime] Channel registered: '{name}'")

    def get_channel(self, name: str) -> CommunicationProvider | None:
        """Get provider for a channel."""
        return self._channels.get(name)

    async def send(self, to: str, message: str, channel: str = "whatsapp") -> dict[str, Any]:
        """Routes the message send request to the appropriate provider."""
        provider = self.get_channel(channel)
        if not provider:
            return {
                "status": "error",
                "message": f"Communication channel '{channel}' is not active or registered.",
            }
        return await provider.send(to, message)

    async def health(self, channel: str = "whatsapp") -> dict[str, Any]:
        """Returns health status of the provider."""
        provider = self.get_channel(channel)
        if not provider:
            return {"status": "inactive", "healthy": False}
        return await provider.health()


# Register the runtime inside RuntimeRegistry on load
communication_runtime = CommunicationRuntime()
RuntimeRegistry.register("communication", communication_runtime)
