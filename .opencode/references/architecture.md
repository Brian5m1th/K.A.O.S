---
description: Documento de referencia da arquitetura do K.A.O.S
globs: 
---
# Arquitetura do K.A.O.S

## Stack

- **Backend:** Python 3.13, FastAPI, LangGraph, SQLAlchemy async, Qdrant
- **Frontend:** React 18, TypeScript 5.5, Tauri 2, Zustand 5, Tailwind 3
- **Infra:** Docker Compose, PostgreSQL 16, Ollama, n8n, Prometheus, Grafana, Loki
- **CI/CD:** GitHub Actions, Ruff, pytest, tsc

## Camadas

### Backend (assistant/app/)
- `main.py` - App init, middleware, router registration
- `api/*.py` - FastAPI routers (auth, chat, models, orchestrator, audit, architecture)
- `domain/` - Pydantic models (ChatRequest, ExecutionPlan, etc.)
- `observability/` - EventBus pub/sub (22 events, 6 subscribers)
- `orchestrator/` - PlanExecutor, CircuitBreaker, DeadLetterQueue
- `providers/` - Chat/Embedding/Vector/Memory adapters (Ollama, OpenAI, Anthropic, Gemini)
- `workflows/` - Workflow definitions (chat, reasoning, coding, rag, agent)
- `audit/` - KIRL (FeatureRegistry, AuditEngine, DRLSnapshot, DriftSubscriber)
- `ai/vault_analyzer/` - AI Vault Analyzer (drift detection, evidence, suggestions)

### Frontend (desktop/src/)
- FSD (Feature-Sliced Design): app > pages > widgets > features > entities > shared
- `shared/lib/stores/` - Zustand stores (system, chat, agent, auth, ui, app, drift)
- `shared/lib/event-bus.ts` - TypeScript EventBus (graph:*, docs:* events)
- `shared/lib/command-registry.ts` - CTRL+K command palette
- `shared/ui/` - 15 reusable components (Card, Badge, Tabs, Dialog, etc.)
- `features/documentation-audit/` - KIRL frontend (drift-store, graph/, heatmap/, auto-doc/)
- `pages/documentation/` - Documentation Health dashboard
- `pages/architecture/` - Architecture Graph (interactive SVG)

### KIRL (docs/runtime/)
- `registry/features-index.json` - FeatureRegistry export
- `registry/commit-map.json` - CommitMapper export
- `audit/coverage-report.json` - AuditEngine report
- `architecture/` - Analysis, graph, issues, suggestions, history
- `auto-generated/` - AUTO-SDDs gerados pelo SDDGenerator

## Fluxos Principais

### Chat
```
User -> Chat UI -> POST /api/chat/message -> IntentClassifier -> WorkflowRouter
  -> ModelRouter -> ProviderSelector -> PlanExecutor -> SSE streaming -> Chat UI
```

### Auditoria KIRL
```
Run Audit (manual/30s automatico) -> AuditEngine.run_audit()
  -> FeatureRegistry.load() + CommitMapper.generate() + SDDResolver.scan() + CodeScanner.scan()
  -> DriftReport (coverage, missing, outdated, inconsistent, orphaned)
  -> DRLSnapshot.build() -> EventBus (audit.completed) -> UI atualiza
```

### AI Vault Analyzer
```
POST /api/architecture/analyze -> VaultReader.scan() + DriftEngine.calculate()
  -> EvidenceEngine.collect() -> AnalyzerEngine.analyze() -> SuggestionEngine.generate()
  -> persist JSONs -> EventBus (vault.analysis.completed)
```

## Dependencias FSD (Frontend)
```
app/ -> widgets/ -> features/ -> entities/ -> shared/
(pages tambem podem acessar widgets, features, entities, shared)
Nenhuma camada pode importar de camadas superiores.
shared/ nao importa nada do projeto.
```
