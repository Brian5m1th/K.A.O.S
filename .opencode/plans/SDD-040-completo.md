# SDD-040 — Universal Orchestration Platform

**Status:** Approved
**Version:** 1.0
**Date:** 2026-06-21

---

## 1. Objective

Refatorar o K.A.O.S de uma aplicação centrada em Ollama para uma plataforma universal de orquestração de IA baseada em capacidades, workflows e observabilidade desde o núcleo.

## 2. Architecture Pillars

| # | Pillar | Description |
|---|---|---|
| 1 | Capability Driven | User chooses by capability, not by provider |
| 2 | Workflow Driven | Execution is workflow-based, not route-based |
| 3 | Model Router | Selects best model for required capabilities |
| 4 | Provider Selector | Picks provider for selected model |
| 5 | Circuit Breaker | Protects against cascading failures |
| 6 | Service Registry | Single registry for all components |
| 7 | Structured Observability | JSON logs, correlation IDs, Event Bus |
| 8 | OpenTelemetry + CostTracker | Traces, metrics, cost tracking |
| 9 | Feature Flags + Versioning | Safe rollouts, backward compatibility |
| 10 | Dead Letter Queue | Failed execution forensics |

## 3. Core Concepts

### 3.1 CapabilityProfile

```python
@dataclass
class CapabilityProfile:
    capabilities: list[str] = field(default_factory=list)
```

Capabilities are **strings**, not booleans. New capabilities (speech_to_text, browser_use, computer_use) require zero schema changes.

Initial capabilities: `fast_chat`, `reasoning`, `coding`, `long_context`, `vision`, `tool_calling`, `rag`.

### 3.2 ExecutionPlan

```python
@dataclass
class ExecutionPlan:
    execution_id: UUID
    trace_id: UUID
    user_id: UUID
    session_id: UUID
    workflow: str
    selected_model: str
    capabilities: list[str]
    provider_configs: dict[str, Any]
```

### 3.3 BaseWorkflow

```python
class BaseWorkflow(ABC):
    name: str
    version: str
    @property
    def required_capabilities(self) -> list[str]: ...
    async def execute(self, plan, request) -> AsyncIterator[str]: ...
    async def healthcheck(self) -> bool: ...
```

### 3.4 BaseChatProvider

```python
class BaseChatProvider(ABC):
    provider_name: str
    async def chat(self, messages, **kwargs) -> str: ...
    async def stream(self, messages, **kwargs) -> AsyncIterator[str]: ...
    async def models(self) -> list[str]: ...
    async def healthcheck(self) -> bool: ...
```

### 3.5 ServiceRegistry

```python
class ServiceRegistry:
    _workflows: dict[str, type[BaseWorkflow]] = {}
    _chat_providers: dict[str, type[BaseChatProvider]] = {}
    _embedding_providers: dict[str, type[BaseEmbeddingProvider]] = {}
    _vector_stores: dict[str, type[BaseVectorStore]] = {}
    _memory_providers: dict[str, type[BaseMemoryProvider]] = {}
```

## 4. Execution Flow

```
User → IntentClassifier → workflow name
→ ServiceRegistry.get_workflow(name)
→ Workflow.required_capabilities
→ ModelRouter.select_model(capabilities, user_id)
→ ProviderSelector.select(provider, model)
→ ExecutionPlan
→ PlanExecutor.execute(plan, request)
→ Streaming Response
```

## 5. Database Schema

Tables: `models`, `capability_policies`, `provider_configs`, `user_profiles`, `user_model_profiles`, `feature_flags`, `failed_executions`.

## 6. Observability

- Structured JSON logging with trace_id, execution_id in every line
- Event Bus: Logger, Metrics, Tracing, CostTracker, Audit as subscribers
- OpenTelemetry spans (orchestrator → model_router → workflow → steps)
- Prometheus metrics (requests, duration, tokens, fallbacks, errors)
- CostTracker per request, workflow, user, provider, monthly

## 7. Implementation Phases

| Phase | Name | Deliverables |
|---|---|---|
| **1** | Core Contracts + Registry | ExecutionPlan, CapabilityProfile, BaseWorkflow, BaseProviders, ServiceRegistry, EventBus interface |
| **2** | Database Schema | 6 tables + repositories |
| **3** | Model Router + Selector + Circuit Breaker | ModelRouter, ProviderSelector, HealthCache, CircuitBreaker |
| **4** | Provider Adapters | Chat/Embedding/Vector/Memory adapters |
| **5** | Workflow Registry | 7 workflows with versioning |
| **6** | Orchestrator + API + DLQ | Orchestrator, PlanExecutor, Dead Letter Queue |
| **7** | Desktop APIs | Profile, model profiles, policies endpoints |
| **8** | Observability + Event Bus | Structured logging, Event Bus implementation |
| **8.5** | Production Observability | CostTracker, OpenTelemetry, Prometheus, Grafana |
| **9** | Launcher Design | Architecture document |
| **10** | Refactor + Tests + Docs | Ruff, coverage, docs |
