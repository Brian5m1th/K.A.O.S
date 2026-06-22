---
description: Estrutura de diretorios do K.A.O.S
globs: 
---
# Directory Structure

```
K.A.O.S/
├── assistant/                    # Backend Python (FastAPI)
│   ├── app/
│   │   ├── main.py               # App init, middleware, 20+ routers
│   │   ├── api/                   # FastAPI routers (auth, chat, audit, architecture...)
│   │   ├── agent/                 # LangGraph agent (StateGraph, nodes)
│   │   ├── ai/vault_analyzer/     # AI Vault Analyzer (6 engines)
│   │   ├── audit/                 # KIRL (12 modulos)
│   │   ├── config/                # Settings + prompts
│   │   ├── domain/                # Pydantic models
│   │   ├── middleware/            # API Key + User Context
│   │   ├── observability/         # EventBus + subscribers (logger, metrics, tracing, cost, audit, n8n)
│   │   ├── obsidian/              # Vault integration + watcher
│   │   ├── orchestrator/          # PlanExecutor, CircuitBreaker, DLQ
│   │   ├── providers/             # Chat/Embedding/Vector/Memory adapters
│   │   ├── rag/                   # Indexing, embeddings, retrieval
│   │   ├── service/               # LLM + Memory + Notification services
│   │   ├── tools/                 # LangGraph tools (github, obsidian)
│   │   └── workflows/             # Workflow definitions (chat, reasoning, coding, rag, agent)
│   ├── tests/                     # Unit + Integration tests
│   └── scripts/                   # validate_documentation, audit_pr_docs, generate_feature_catalog
│
├── desktop/                       # Frontend Tauri + React
│   ├── src/
│   │   ├── app/                   # Init, providers, routes, layouts
│   │   ├── pages/                 # 8+ pages (dashboard, chat, agents, documentation, architecture...)
│   │   ├── widgets/               # Sidebar, CommandPalette, TopBar
│   │   ├── features/              # Business logic hooks (ask-ai, configure-providers, documentation-audit)
│   │   ├── entities/              # Domain types (message, note, provider)
│   │   └── shared/                # UI kit, stores, utils, API client, styles
│   └── src-tauri/                 # Rust (Tauri backend)
│
├── infra/docker/                  # Docker Compose (9 services)
├── docs/                          # Documentation (submodule)
├── .github/                       # GitHub Actions
└── .opencode/                     # OpenCode config (references, rules, skills, tools, agents)
```
