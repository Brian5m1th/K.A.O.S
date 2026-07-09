"""Base interfaces for the Communication Runtime.

SDD-KAOS-EVOLUTION-001: Abstract provider contract for multiple communication channels.
"""
from abc import ABC, abstractmethod
from typing import Any, List


class CommunicationProvider(ABC):
    """Abstract interface defining the requirements of any Communication Provider."""

    @abstractmethod
    async def connect(self) -> bool:
        """Establish connection to the provider."""
        pass

    @abstractmethod
    async def disconnect(self) -> bool:
        """Gracefully disconnect from the provider."""
        pass

    @abstractmethod
    async def health(self) -> dict[str, Any]:
        """Check provider connection status and latency."""
        pass

    @abstractmethod
    async def send(self, to: str, message: str) -> dict[str, Any]:
        """Send message over the provider channel."""
        pass

    @abstractmethod
    async def receive(self) -> List[dict[str, Any]]:
        """Receive list of messages/notifications."""
        pass

    @abstractmethod
    async def authenticate(self, credentials: dict[str, Any]) -> bool:
        """Authenticate with the provider."""
        pass

    @abstractmethod
    async def refresh(self) -> bool:
        """Refresh auth tokens/sessions."""
        pass
