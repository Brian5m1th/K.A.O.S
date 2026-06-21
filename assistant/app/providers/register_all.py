from app.providers.chat.registry import register_chat_providers
from app.providers.embedding.registry import register_embedding_providers
from app.providers.vector.registry import register_vector_stores
from app.providers.memory.registry import register_memory_providers


def register_all_providers() -> None:
    register_chat_providers()
    register_embedding_providers()
    register_vector_stores()
    register_memory_providers()
