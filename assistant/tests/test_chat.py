from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.domain.workflow import WorkflowType


@pytest.fixture
def client() -> AsyncClient:
    app.state.api_key = "test-api-key"
    transport = ASGITransport(app=app)
    return AsyncClient(
        transport=transport,
        base_url="http://test",
        headers={"x-api-key": "test-api-key"},
    )


@pytest.mark.asyncio
async def test_send_message_streams_response(client: AsyncClient) -> None:
    mock_router = MagicMock()

    async def fake_stream(*args, **kwargs):
        yield "Hello world!"

    mock_router.stream = fake_stream

    with patch("app.api.chat._smart_router", mock_router):
        mock_classifier = AsyncMock()
        from app.domain.intent import IntentResult

        mock_classifier.classify = AsyncMock(
            return_value=IntentResult(workflow=WorkflowType.AGENT, confidence=0.5)
        )
        with patch("app.api.chat._get_classifier", return_value=mock_classifier):
            response = await client.post(
                "/api/chat/message",
                json={
                    "session_id": "test-session",
                    "message": "Olá",
                },
            )

    assert response.status_code == 200
    assert response.text == "Hello world!"


@pytest.mark.asyncio
async def test_send_message_empty_content_returns_422(client: AsyncClient) -> None:
    response = await client.post(
        "/api/chat/message",
        json={
            "session_id": "test-session",
            "message": "",
        },
    )

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_readiness_degraded_when_ollama_unavailable(client: AsyncClient) -> None:
    with patch(
        "app.service.llm_service.LLMService.check_availability",
        return_value=False,
    ):
        response = await client.get("/health/readiness")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "degraded"
    assert data["services"]["ollama"] is False


@pytest.mark.asyncio
async def test_readiness_ready_when_ollama_available(client: AsyncClient) -> None:
    with patch(
        "app.service.llm_service.LLMService.check_availability",
        return_value=True,
    ):
        response = await client.get("/health/readiness")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert data["services"]["ollama"] is True
