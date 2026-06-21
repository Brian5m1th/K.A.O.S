from app.providers.vector.qdrant import QdrantVectorStore
from app.registry.service_registry import ServiceRegistry


def register_vector_stores() -> None:
    ServiceRegistry.register_vector_store("qdrant", QdrantVectorStore)
