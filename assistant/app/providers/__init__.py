"""K.A.O.S Providers — Framework adapters for domain ports.
Re-exports from sub-packages for convenience.
Uses lazy imports to avoid circular dependencies at module load time.
"""


def get_graph_adapters():
    from app.providers.graph import GraphifyAdapter, NetworkXFallback

    return GraphifyAdapter, NetworkXFallback


def get_memory_adapters():
    from app.providers.memory import PostgresMemoryAdapter

    return (PostgresMemoryAdapter,)


def get_retrieval_adapters():
    from app.providers.retrieval import QdrantAdapter

    return (QdrantAdapter,)


def get_inference_adapters():
    from app.providers.inference import (
        OllamaAdapter,
        AirLLMAdapter,
        OpenAIAdapter,
        GeminiAdapter,
        ClaudeAdapter,
    )

    return OllamaAdapter, AirLLMAdapter, OpenAIAdapter, GeminiAdapter, ClaudeAdapter


def get_planner_adapters():
    from app.providers.planner import LangGraphAdapter

    return (LangGraphAdapter,)


def get_evidence_adapters():
    from app.providers.evidence import EvidenceEngine

    return (EvidenceEngine,)
