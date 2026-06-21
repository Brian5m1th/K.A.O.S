import pytest

from app.providers.chat.ollama import OllamaChatProvider
from app.providers.chat.openai import OpenAIChatProvider
from app.providers.chat.anthropic import AnthropicChatProvider
from app.providers.chat.gemini import GeminiChatProvider
from app.providers.embedding.bge import BgeEmbeddingProvider
from app.providers.embedding.openai import OpenAIEmbeddingProvider
from app.providers.vector.qdrant import QdrantVectorStore
from app.providers.memory.obsidian import ObsidianMemoryProvider
from app.providers.memory.postgres import PostgresMemoryProvider
from app.providers.base.chat import BaseChatProvider
from app.providers.base.embedding import BaseEmbeddingProvider
from app.providers.base.vector_store import BaseVectorStore
from app.providers.base.memory import BaseMemoryProvider
from app.providers.register_all import register_all_providers
from app.registry.service_registry import ServiceRegistry
from app.domain.chat import Message


class TestOllamaChatProvider:
    def test_provider_name(self):
        assert OllamaChatProvider.provider_name == "ollama"

    def test_is_chat_provider(self):
        provider = OllamaChatProvider()
        assert isinstance(provider, BaseChatProvider)


class TestOpenAIChatProvider:
    def test_provider_name(self):
        assert OpenAIChatProvider.provider_name == "openai"

    def test_is_chat_provider(self):
        provider = OpenAIChatProvider()
        assert isinstance(provider, BaseChatProvider)


class TestAnthropicChatProvider:
    def test_provider_name(self):
        assert AnthropicChatProvider.provider_name == "anthropic"

    def test_is_chat_provider(self):
        provider = AnthropicChatProvider()
        assert isinstance(provider, BaseChatProvider)


class TestGeminiChatProvider:
    def test_provider_name(self):
        assert GeminiChatProvider.provider_name == "gemini"

    def test_is_chat_provider(self):
        provider = GeminiChatProvider()
        assert isinstance(provider, BaseChatProvider)


class TestBgeEmbeddingProvider:
    def test_provider_name(self):
        assert BgeEmbeddingProvider.provider_name == "bge"

    def test_is_embedding_provider(self):
        provider = BgeEmbeddingProvider()
        assert isinstance(provider, BaseEmbeddingProvider)


class TestOpenAIEmbeddingProvider:
    def test_provider_name(self):
        assert OpenAIEmbeddingProvider.provider_name == "openai"

    def test_is_embedding_provider(self):
        provider = OpenAIEmbeddingProvider()
        assert isinstance(provider, BaseEmbeddingProvider)


class TestQdrantVectorStore:
    def test_store_name(self):
        assert QdrantVectorStore.store_name == "qdrant"

    def test_is_vector_store(self):
        store = QdrantVectorStore()
        assert isinstance(store, BaseVectorStore)


class TestObsidianMemoryProvider:
    def test_provider_name(self):
        assert ObsidianMemoryProvider.provider_name == "obsidian"

    def test_is_memory_provider(self):
        provider = ObsidianMemoryProvider()
        assert isinstance(provider, BaseMemoryProvider)


class TestPostgresMemoryProvider:
    def test_provider_name(self):
        assert PostgresMemoryProvider.provider_name == "postgres"

    def test_is_memory_provider(self):
        provider = PostgresMemoryProvider()
        assert isinstance(provider, BaseMemoryProvider)


class TestRegisterAllProviders:
    def test_register_all(self):
        ServiceRegistry._chat_providers.clear()
        ServiceRegistry._embedding_providers.clear()
        ServiceRegistry._vector_stores.clear()
        ServiceRegistry._memory_providers.clear()

        register_all_providers()

        assert "ollama" in ServiceRegistry.list_chat_providers()
        assert "openai" in ServiceRegistry.list_chat_providers()
        assert "anthropic" in ServiceRegistry.list_chat_providers()
        assert "gemini" in ServiceRegistry.list_chat_providers()
        assert "bge" in ServiceRegistry.list_embedding_providers()
        assert "openai" in ServiceRegistry.list_embedding_providers()
        assert "qdrant" in ServiceRegistry.list_vector_stores()
        assert "obsidian" in ServiceRegistry.list_memory_providers()
        assert "postgres" in ServiceRegistry.list_memory_providers()

    def test_get_chat_provider_instances(self):
        register_all_providers()

        ollama = ServiceRegistry.get_chat_provider("ollama", {"model": "qwen3:4b"})
        assert isinstance(ollama, OllamaChatProvider)

        openai = ServiceRegistry.get_chat_provider("openai", {"model": "gpt-4o"})
        assert isinstance(openai, OpenAIChatProvider)

    def test_get_embedding_provider_instances(self):
        register_all_providers()

        bge = ServiceRegistry.get_embedding_provider("bge")
        assert isinstance(bge, BgeEmbeddingProvider)

        openai_emb = ServiceRegistry.get_embedding_provider("openai", {"model": "text-embedding-3-small"})
        assert isinstance(openai_emb, OpenAIEmbeddingProvider)

    def test_get_vector_store_instances(self):
        register_all_providers()

        qdrant = ServiceRegistry.get_vector_store("qdrant")
        assert isinstance(qdrant, QdrantVectorStore)

    def test_get_memory_provider_instances(self):
        register_all_providers()

        obsidian = ServiceRegistry.get_memory_provider("obsidian")
        assert isinstance(obsidian, ObsidianMemoryProvider)

        postgres = ServiceRegistry.get_memory_provider("postgres")
        assert isinstance(postgres, PostgresMemoryProvider)
