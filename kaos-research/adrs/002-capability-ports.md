# ADR-002: Capability-First Architecture with Ports & Adapters

- **Status:** Accepted
- **Decision Owner:** KAOS Architect (System)
- **Review Date:** 2027-01-11 (6 months)
- **Date:** 2026-07-11

---

## Context

The K.A.O.S platform integrates multiple frameworks (Graphify, Qdrant, Ollama, LangGraph, AirLLM, and potentially GraphRAG, Mem0, Graphiti, Cognee). Direct framework coupling creates vendor lock-in, complicates testing, and makes framework swaps prohibitively expensive.

## Decision

**All framework integration will use a Capability-First architecture:**

```
Capability → Port (abstract interface) → Adapter → Framework
```

The Desktop layer never imports or depends on any framework directly. It only consumes K.A.O.S REST APIs served by capability Services, which route to ProviderRegistry-managed adapters.

## Evidence

1. CodeScanner deprecation proved value: removing it required changes in 3 files (graph_builder.py, knowledge_graph.py, imports). With ports/adapters, framework swaps affect only 1 adapter file.
2. Graphify connection data showed `GraphBuilder --uses--> CodeScanner` — a direct coupling that required 3 files to change.
3. ProviderRegistry pattern enables runtime provider switching without restart.

## Architecture

```
Desktop (React + Zustand)
  ↓ REST API
Service (GraphService, MemoryService, etc.)
  ↓ ProviderRegistry
Port (GraphPort, MemoryPort, etc.)
  ↓ implements
Adapter (GraphifyAdapter, Mem0Adapter, etc.)
  ↓ wraps
Framework (Graphify, Mem0, etc.)
```

## Implemented Ports

| Port | Adapters (current/planned) | Status |
|---|---|---|
| GraphPort | GraphifyAdapter, NetworkXAdapter (fallback) | ✅ Defined |
| MemoryPort | PostgresMemoryAdapter, Mem0Adapter (future) | ✅ Defined |
| RetrievalPort | QdrantAdapter | ✅ Defined |
| InferencePort | OllamaAdapter, AirLLMAdapter, OpenAIAdapter, GeminiAdapter, ClaudeAdapter | ✅ Defined |
| PlannerPort | LangGraphAdapter | ✅ Defined |
| EvidencePort | GraphifySource + GitSource + TestSource + BenchmarkSource | ✅ Defined |

## Consequences

- **Positive:** Framework-agnostic Desktop, swappable providers, testable in isolation, future-proof
- **Negative:** Additional abstraction layer, more files to maintain, initial setup overhead
- **Mitigation:** ProviderRegistry auto-activates first registered provider; services have sensible defaults

## Alternatives Considered

- **Direct framework coupling:** Rejected — creates vendor lock-in, hard to test, expensive to swap
- **Plugin system (dynamic loading):** Deferred — adds complexity; ProviderRegistry sufficient for now
