from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.router.intent_classifier import IntentType


@pytest.fixture
def client() -> AsyncClient:
    app.state.api_key = "test-api-key"
    transport = ASGITransport(app=app)
    return AsyncClient(
        transport=transport,
        base_url="http://test",
        headers={"x-api-key": "test-api-key"},
    )


async def _read_sse(stream) -> str:
    full = ""
    async for line in stream.aiter_lines():
        if line.startswith("data: ") and line != "data: [DONE]":
            import json

            chunk = json.loads(line[6:])
            content = chunk["choices"][0]["delta"].get("content", "")
            full += content
    return full


@pytest.mark.asyncio
async def test_openai_chat_completions(client: AsyncClient) -> None:
    mock_agent = MagicMock()

    async def _mock_stream(session_id, user_message, **kwargs):
        for token in ["Resposta ", "do ", "RAG + Ollama"]:
            yield token

    mock_agent.stream_message = _mock_stream

    mock_classifier = MagicMock()
    mock_classifier.classify = AsyncMock(return_value=IntentType.SMART)

    with patch("app.api.openai._get_classifier", return_value=mock_classifier):
        with patch("app.api.openai.AgentService", return_value=mock_agent):
            async with client.stream(
                "POST",
                "/v1/chat/completions",
                json={
                    "model": "qwen3:14b",
                    "messages": [
                        {"role": "user", "content": "O que tem no meu vault?"}
                    ],
                },
            ) as response:
                assert response.status_code == 200
                content = await _read_sse(response)
                assert content == "Resposta do RAG + Ollama"


@pytest.mark.asyncio
async def test_openai_chat_completions_no_user_message(
    client: AsyncClient,
) -> None:
    async def _mock_stream(session_id, user_message, **kwargs):
        for token in ["Resposta padrao"]:
            yield token

    mock_agent = MagicMock()
    mock_agent.stream_message = _mock_stream

    mock_classifier = MagicMock()
    mock_classifier.classify = AsyncMock(return_value=IntentType.SMART)

    with patch("app.api.openai._get_classifier", return_value=mock_classifier):
        with patch("app.api.openai.AgentService", return_value=mock_agent):
            async with client.stream(
                "POST",
                "/v1/chat/completions",
                json={
                    "model": "qwen3:14b",
                    "messages": [{"role": "assistant", "content": "Olá"}],
                },
            ) as response:
                assert response.status_code == 200
                content = await _read_sse(response)
                assert content == "Resposta padrao"


@pytest.mark.asyncio
async def test_openai_chat_completions_empty_body_returns_422(
    client: AsyncClient,
) -> None:
    response = await client.post("/v1/chat/completions", json={})
    assert response.status_code == 422
