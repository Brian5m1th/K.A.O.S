from typing import Any

from loguru import logger

from app.providers.base.chat import BaseChatProvider
from app.providers.base.embedding import BaseEmbeddingProvider
from app.providers.base.memory import BaseMemoryProvider
from app.providers.base.vector_store import BaseVectorStore
from app.workflows.base import BaseWorkflow


class ServiceRegistry:
    _workflows: dict[str, type[BaseWorkflow]] = {}
    _chat_providers: dict[str, type[BaseChatProvider]] = {}
    _embedding_providers: dict[str, type[BaseEmbeddingProvider]] = {}
    _vector_stores: dict[str, type[BaseVectorStore]] = {}
    _memory_providers: dict[str, type[BaseMemoryProvider]] = {}

    @classmethod
    def register_workflow(
        cls, name: str, workflow: type[BaseWorkflow]
    ) -> None:
        cls._workflows[name] = workflow
        logger.info(f"[registry] workflow registered: {name}")

    @classmethod
    def register_chat_provider(
        cls, name: str, provider: type[BaseChatProvider]
    ) -> None:
        cls._chat_providers[name] = provider
        logger.info(f"[registry] chat provider registered: {name}")

    @classmethod
    def register_embedding_provider(
        cls, name: str, provider: type[BaseEmbeddingProvider]
    ) -> None:
        cls._embedding_providers[name] = provider
        logger.info(f"[registry] embedding provider registered: {name}")

    @classmethod
    def register_vector_store(
        cls, name: str, store: type[BaseVectorStore]
    ) -> None:
        cls._vector_stores[name] = store
        logger.info(f"[registry] vector store registered: {name}")

    @classmethod
    def register_memory_provider(
        cls, name: str, provider: type[BaseMemoryProvider]
    ) -> None:
        cls._memory_providers[name] = provider
        logger.info(f"[registry] memory provider registered: {name}")

    @classmethod
    def get_workflow(cls, name: str) -> BaseWorkflow:
        if name not in cls._workflows:
            raise KeyError(f"Workflow not registered: {name}")
        return cls._workflows[name]()

    @classmethod
    def get_chat_provider(
        cls, name: str, config: dict[str, Any] | None = None
    ) -> BaseChatProvider:
        if name not in cls._chat_providers:
            raise KeyError(f"Chat provider not registered: {name}")
        provider_cls = cls._chat_providers[name]
        return provider_cls(**(config or {}))

    @classmethod
    def get_embedding_provider(
        cls, name: str, config: dict[str, Any] | None = None
    ) -> BaseEmbeddingProvider:
        if name not in cls._embedding_providers:
            raise KeyError(f"Embedding provider not registered: {name}")
        provider_cls = cls._embedding_providers[name]
        return provider_cls(**(config or {}))

    @classmethod
    def get_vector_store(
        cls, name: str, config: dict[str, Any] | None = None
    ) -> BaseVectorStore:
        if name not in cls._vector_stores:
            raise KeyError(f"Vector store not registered: {name}")
        store_cls = cls._vector_stores[name]
        return store_cls(**(config or {}))

    @classmethod
    def get_memory_provider(
        cls, name: str, config: dict[str, Any] | None = None
    ) -> BaseMemoryProvider:
        if name not in cls._memory_providers:
            raise KeyError(f"Memory provider not registered: {name}")
        provider_cls = cls._memory_providers[name]
        return provider_cls(**(config or {}))

    @classmethod
    def list_workflows(cls) -> list[str]:
        return list(cls._workflows.keys())

    @classmethod
    def list_chat_providers(cls) -> list[str]:
        return list(cls._chat_providers.keys())

    @classmethod
    def list_embedding_providers(cls) -> list[str]:
        return list(cls._embedding_providers.keys())

    @classmethod
    def list_vector_stores(cls) -> list[str]:
        return list(cls._vector_stores.keys())

    @classmethod
    def list_memory_providers(cls) -> list[str]:
        return list(cls._memory_providers.keys())
