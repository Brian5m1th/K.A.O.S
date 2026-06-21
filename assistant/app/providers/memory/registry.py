from app.providers.memory.obsidian import ObsidianMemoryProvider
from app.providers.memory.postgres import PostgresMemoryProvider
from app.registry.service_registry import ServiceRegistry


def register_memory_providers() -> None:
    ServiceRegistry.register_memory_provider("obsidian", ObsidianMemoryProvider)
    ServiceRegistry.register_memory_provider("postgres", PostgresMemoryProvider)
