from app.providers.embedding.bge import BgeEmbeddingProvider
from app.providers.embedding.openai import OpenAIEmbeddingProvider
from app.registry.service_registry import ServiceRegistry


def register_embedding_providers() -> None:
    ServiceRegistry.register_embedding_provider("bge", BgeEmbeddingProvider)
    ServiceRegistry.register_embedding_provider("openai", OpenAIEmbeddingProvider)
