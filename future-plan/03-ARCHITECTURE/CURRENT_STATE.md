# ARCHITECTURE Epic - CURRENT STATE: Codebase Review

## 1. Existing Directory Structure Analysis

The current K.A.O.S backend (`assistant/app/`) uses a technical-layered package structure:

```text
assistant/app/
├── api/              # FastAPI HTTP + SSE endpoints (44 files)
├── core/             # Configuration, MCP, startup boot managers
├── orchestrator/     # Plan execution, circuit breakers, fallback loops
├── providers/        # Database, vector, and LLM provider drivers
├── audit/            # KIRL engine (Drift and Feature Registries)
├── rag/              # Ingestion, chunking, and embedding logic
├── agent/            # LangGraph workflows and nodes
├── domain/           # Ports and shared entities
└── capability/       # Central Capability registry mapping
```

---

## 2. Issues with Layered Architecture

- **Feature Dispersion (Spaghetti Code):** Adding a new capability requires modifying files across 5-7 different folders (defining models in `models/`, routers in `api/`, services in `services/`, and tests in `tests/`).
- **High Static Coupling:** Services import each other directly, creating cyclic dependencies. For example, `rag` imports the `embedding` provider, which imports `config`, which imports `observability`.
- **Static Mounting:** Routers must be imported and mounted manually in `main.py`. This requires editing the core engine whenever a feature is added or removed.
- **Synchronous Event Communication:** The current EventBus is in-memory and synchronous, blocking request loops when events are published.
