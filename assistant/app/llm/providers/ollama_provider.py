from typing import AsyncIterator, Iterator

from langchain_core.messages import BaseMessage
from langchain_ollama import ChatOllama
from loguru import logger

from app.llm.provider import BaseProvider

_MAX_RETRIES = 2


class OllamaProvider(BaseProvider):
    def __init__(self, model: str, base_url: str, **kwargs):
        self._model = model
        self._base_url = base_url
        self._kwargs = kwargs
        self._llm = ChatOllama(model=model, base_url=base_url, **kwargs)

    def _rebuild(self) -> None:
        self._llm = ChatOllama(model=self._model, base_url=self._base_url, **self._kwargs)

    def invoke(self, messages: list[BaseMessage]) -> BaseMessage:
        return self._llm.invoke(messages)

    async def ainvoke(self, messages: list[BaseMessage]) -> BaseMessage:
        return await self._llm.ainvoke(messages)

    def stream(self, messages: list[BaseMessage]) -> Iterator[BaseMessage]:
        return self._llm.stream(messages)

    async def astream(self, messages: list[BaseMessage]) -> AsyncIterator[BaseMessage]:
        for attempt in range(_MAX_RETRIES + 1):
            try:
                async for chunk in self._llm.astream(messages):
                    yield chunk
                return
            except Exception as e:
                logger.warning(
                    f"[warn] OllamaProvider - astream attempt {attempt + 1}/{_MAX_RETRIES + 1} failed: {e}"
                )
                if attempt < _MAX_RETRIES:
                    self._rebuild()
                else:
                    raise

    @property
    def model_name(self) -> str:
        return self._model

    @property
    def provider_name(self) -> str:
        return "ollama"
