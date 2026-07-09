from abc import ABC, abstractmethod
from typing import AsyncIterator, Any
from langchain_core.messages import BaseMessage


class AIRuntime(ABC):
    @abstractmethod
    async def ainvoke(self, messages: list[BaseMessage], **kwargs: Any) -> BaseMessage:
        pass

    @abstractmethod
    async def astream(
        self, messages: list[BaseMessage], **kwargs: Any
    ) -> AsyncIterator[BaseMessage]:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def type(self) -> str:
        # "local", "cloud", "hybrid"
        pass

    @property
    @abstractmethod
    def capabilities(self) -> dict[str, Any]:
        # Returns a dict of capability scores (e.g., vision, cost, latency, offline, context_window)
        pass

    @property
    @abstractmethod
    def supported_models(self) -> list[str]:
        pass


class ProviderRuntimeAdapter(AIRuntime):
    def __init__(
        self,
        provider: Any,
        runtime_type: str,
        capabilities: dict[str, Any],
        supported_models: list[str],
    ):
        self._provider = provider
        self._type = runtime_type
        self._capabilities = capabilities
        self._models = supported_models

    async def ainvoke(self, messages: list[BaseMessage], **kwargs: Any) -> BaseMessage:
        return await self._provider.ainvoke(messages, **kwargs)

    async def astream(
        self, messages: list[BaseMessage], **kwargs: Any
    ) -> AsyncIterator[BaseMessage]:
        return self._provider.astream(messages, **kwargs)

    @property
    def name(self) -> str:
        return self._provider.provider_name

    @property
    def type(self) -> str:
        return self._type

    @property
    def capabilities(self) -> dict[str, Any]:
        return self._capabilities

    @property
    def supported_models(self) -> list[str]:
        return self._models
