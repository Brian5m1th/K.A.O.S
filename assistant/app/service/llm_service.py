from typing import AsyncIterator

import httpx
from loguru import logger

from app.config.settings import settings
from app.domain.chat import Message


class LLMService:
    def __init__(self) -> None:
        self._base_url = settings.OLLAMA_BASE_URL
        self._model = settings.OLLAMA_MODEL

    async def stream_chat(
        self,
        messages: list[Message],
    ) -> AsyncIterator[str]:
        payload = {
            "model": self._model,
            "messages": [m.model_dump() for m in messages],
            "stream": True,
        }
        logger.debug(f"Enviando {len(messages)} mensagens ao Ollama ({self._model})")

        async with httpx.AsyncClient(timeout=600.0) as client:
            async with client.stream("POST", f"{self._base_url}/api/chat", json=payload) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line:
                        import json
                        chunk = json.loads(line)
                        if not chunk.get("done"):
                            yield chunk["message"]["content"]

    async def check_availability(self) -> bool:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(f"{self._base_url}/api/tags")
                return response.status_code == 200
        except httpx.ConnectError:
            return False
