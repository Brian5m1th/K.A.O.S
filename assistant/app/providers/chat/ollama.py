from typing import AsyncIterator

from loguru import logger

from app.providers.base.chat import BaseChatProvider
from app.domain.chat import Message


class OllamaChatProvider(BaseChatProvider):
    provider_name = "ollama"

    def __init__(
        self, base_url: str = "http://localhost:11434", model: str = "qwen3:4b"
    ):
        self._base_url = base_url
        self._model = model

    async def chat(self, messages: list[Message], **kwargs) -> str:
        logger.info("[start] OllamaChatProvider - chat")

        import httpx

        payload = {
            "model": self._model,
            "messages": [m.model_dump() for m in messages],
            "stream": False,
            **kwargs,
        }
        async with httpx.AsyncClient(timeout=600.0) as client:
            response = await client.post(f"{self._base_url}/api/chat", json=payload)
            response.raise_for_status()
            data = response.json()

        logger.debug("[finish] OllamaChatProvider - chat")
        return data["message"]["content"]

    async def stream(self, messages: list[Message], **kwargs) -> AsyncIterator[str]:
        logger.info("[start] OllamaChatProvider - stream")

        import json as json_module
        import httpx

        payload = {
            "model": self._model,
            "messages": [m.model_dump() for m in messages],
            "stream": True,
            **kwargs,
        }
        async with httpx.AsyncClient(timeout=600.0) as client:
            async with client.stream(
                "POST", f"{self._base_url}/api/chat", json=payload
            ) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line:
                        chunk = json_module.loads(line)
                        if not chunk.get("done"):
                            yield chunk["message"]["content"]

        logger.debug("[finish] OllamaChatProvider - stream")

    async def models(self) -> list[str]:
        import httpx

        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(f"{self._base_url}/api/tags")
            response.raise_for_status()
            data = response.json()
            return [m["name"] for m in data.get("models", [])]

    async def healthcheck(self) -> bool:
        import httpx

        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self._base_url}/api/tags")
                return response.status_code == 200
        except httpx.ConnectError:
            return False
