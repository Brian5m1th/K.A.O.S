import pytest
from app.runtime.registry import RuntimeRegistry
from app.runtime.communication.base import CommunicationProvider
from app.runtime.communication.manager import CommunicationRuntime


class MockProvider(CommunicationProvider):
    async def connect(self) -> bool:
        return True

    async def disconnect(self) -> bool:
        return True

    async def health(self) -> dict:
        return {"healthy": True}

    async def send(self, to: str, message: str) -> dict:
        return {"status": "sent", "to": to, "message": message, "provider": "mock"}

    async def receive(self) -> list:
        return []

    async def authenticate(self, credentials: dict) -> bool:
        return True

    async def refresh(self) -> bool:
        return True


@pytest.mark.anyio
async def test_communication_runtime_routing():
    # Verify registration
    runtime = RuntimeRegistry.get("communication")
    assert runtime is not None
    assert isinstance(runtime, CommunicationRuntime)

    # Register mock channel
    mock_channel = MockProvider()
    runtime.register_channel("mock", mock_channel)

    # Test send routing
    res = await runtime.send("12345", "Test Message", channel="mock")
    assert res["status"] == "sent"
    assert res["provider"] == "mock"
    assert res["message"] == "Test Message"

    # Test unregistered channel
    res_fail = await runtime.send("12345", "Fail", channel="unknown")
    assert res_fail["status"] == "error"
