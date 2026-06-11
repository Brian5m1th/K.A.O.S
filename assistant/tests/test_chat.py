import json
from unittest.mock import AsyncMock, patch

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app


@pytest.fixture
def client() -> AsyncClient:
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_send_message_streams_response(client: AsyncClient) -> None:
    async def fake_stream(*args, **kwargs):
        tokens = ["Hello", " ", "world", "!"]
        for token in tokens:
            yield token

    with patch("app.service.llm_service.LLMService.stream_chat", new=fake_stream):
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
async def test_send_message_with_history(client: AsyncClient) -> None:
    async def fake_stream(*args, **kwargs):
        yield "Resposta com contexto"

    with patch("app.service.llm_service.LLMService.stream_chat", new=fake_stream):
        response = await client.post(
            "/api/chat/message",
            json={
                "session_id": "test-session",
                "message": "Qual era minha pergunta anterior?",
                "history": [
                    {"role": "user", "content": "Qual a capital do Brasil?"},
                    {"role": "assistant", "content": "Brasília"},
                ],
            },
        )

    assert response.status_code == 200
    assert response.text == "Resposta com contexto"


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
        new=AsyncMock(return_value=False),
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
        new=AsyncMock(return_value=True),
    ):
        response = await client.get("/health/readiness")

    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert data["services"]["ollama"] is True
