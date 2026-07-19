# K.A.O.S — Knowledge & Agentic Orchestration System

**Universal AI Orchestration Platform** — Conecte LLMs locais e remotos, indexes e consulte vaults de conhecimento privados, gerencie agentes, automatize fluxos de trabalho e monitore tudo com observabilidade integrada.

<p align="center">
  <img alt="GitHub Release" src="https://img.shields.io/github/v/release/Brian5m1th/K.A.O.S?include_prereleases&style=flat-square">
  <img alt="CI Status" src="https://img.shields.io/github/actions/workflow/status/Brian5m1th/K.A.O.S/ci.yml?branch=main&label=CI&style=flat-square">
  <img alt="Python" src="https://img.shields.io/badge/python-3.13-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="TypeScript" src="https://img.shields.io/badge/typescript-5.5-3178C6?style=flat-square&logo=typescript&logoColor=white">
  <img alt="Rust" src="https://img.shields.io/badge/rust-1.85-000000?style=flat-square&logo=rust&logoColor=white">
  <img alt="Tauri" src="https://img.shields.io/badge/tauri-2-FFC131?style=flat-square&logo=tauri&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/fastapi-0.115-009688?style=flat-square&logo=fastapi&logoColor=white">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-green?style=flat-square">
</p>

---

## Visao Geral

K.A.O.S e um monorepo de orquestracao de IA focado em:

- **Conhecimento privado** — Indexacao de vaults Obsidian em Qdrant com busca semantica
- **Multi-provedor** — Roteamento inteligente entre LLMs locais (Ollama, AirLLM) e cloud (OpenAI, Anthropic, Gemini)
- **Agentes autonomos** — Execucao de workflows multi-etapa com LangGraph e fallback chain
- **Observabilidade** — Metrica, log e tracing com Prometheus, Loki e Grafana
- **Automacao** — Integracao com n8n, email (IMAP/SMTP), WhatsApp (Evolution API)
- **Auditoria documental** — KIRL (Documentation Runtime Layer) valida consistencia entre codigo e docs
- **Desktop nativo** — Aplicacao Tauri com chat, dashboard, e painel de ferramentas

### Problemas que resolve

- Centralizar acesso a multiplos provedores de LLM com fallback automatico
- Indexar conhecimento privado sem depender de servicos cloud
- Auditar documentacao contra codigo automaticamente
- Fornecer painel unificado de metricas e telemetria
- Automatizar workflows com gatilhos de eventos

### Publico alvo

- Desenvolvedores que usam IA local + cloud
- Equipes que mantem vaults Obsidian e querem RAG privado
- Engenheiros de ML/LLM que precisam de orquestracao flexivel
- Projetos que exigem auditoria documental continua

---

## Funcionalidades

### Desktop (Tauri 2 + React)

| Funcionalidade | Status |
|---|---|
| Chat com streaming SSE | ✅ |
| Dashboard com metricas em tempo real | ✅ |
| Visualizador de conhecimento (RAG) | ✅ |
| Painel de ferramentas MCP | ✅ |
| Catalogo OpenCode (rules, skills, tools, agents) | ✅ |
| Command Palette (CTRL+K) | ✅ |
| Monitor de pipeline ativo | ✅ |
| Telemetria de hardware (CPU, VRAM, latencia) | ✅ |
| Auto-update com assinatura | ✅ |
| 21 paginas (chat, dashboard, agentes, arquitetura, automacao, custos, eventos, graphify, grafo de conhecimento, observabilidade, pipelines, prompts, vault e mais) | ✅ |

### Backend (FastAPI + Python 3.13)

| Funcionalidade | Status |
|---|---|
| Chat multi-provedor (Ollama, OpenAI, Anthropic, Gemini) | ✅ |
| RAG com chunking semântico e embeddings BGE/nomic | ✅ |
| Indexacao de vault Obsidian com watchdog | ✅ |
| Orquestracao de workflows com LangGraph | ✅ |
| Roteamento inteligente de modelo por capacidade | ✅ |
| Circuit breaker e Dead Letter Queue | ✅ |
| API OpenAI-compativel (`/v1/chat/completions`) | ✅ |
| Autenticacao via API Key + JWT | ✅ |
| Feature registry com sincronia via git | ✅ |
| Automacao com n8n (webhooks de eventos) | ✅ |
| Integracao Email (IMAP/SMTP) | ✅ |
| Integracao WhatsApp (Evolution API) | ✅ |
| Integracao AWS | ✅ |
| AirLLM para LLMs locais pesados | ✅ |
| Plugin system com sandbox Wasm | ✅ |
| Gestao de segredos (Secret Manager) | ✅ |
| Notificacoes | ✅ |

### Observabilidade

| Funcionalidade | Status |
|---|---|
| Prometheus metrics (instrumentor automático) | ✅ |
| Loki + Promtail para logs centralizados | ✅ |
| Grafana com dashboards provisionados | ✅ |
| OpenTelemetry tracing | ✅ |
| Cost tracking por requisicao | ✅ |
| Event Bus pub/sub com 22 eventos | ✅ |
| Node Exporter + cAdvisor (producao) | ✅ |
| Alertmanager + Blackbox Exporter (producao) | ✅ |

### KIRL — Documentation Runtime Layer

| Funcionalidade | Status |
|---|---|
| Feature Registry (autodiscover via git history) | ✅ |
| Audit Engine (comparacao codigo vs docs) | ✅ |
| Drift detection e relatorios | ✅ |
| SDD Generator automatico | ✅ |
| SDD Watcher | ✅ |
| Commit mapper | ✅ |
| Code Scanner | ✅ |
| DRL Snapshot | ✅ |
| Evidence Engine | 🚧 |
| Graphify integration | ✅ |

### Arquitetura e Capacidades

| Funcionalidade | Status |
|---|---|
| Capability Registry (autodiscover) | ✅ |
| Domain Ports (inference, memory, retrieval, planner, graph, evidence) | ✅ |
| Provider adapters (chat, embedding, vector, memory) | ✅ |
| Runtime Selector | ✅ |
| Environment Service | ✅ |
| Credential Service | ✅ |
| Bootstrap Manager (8-stage startup) | ✅ |

### MCP — Model Context Protocol

| Funcionalidade | Status |
|---|---|
| MCP Server registry | ✅ |
| MCP Health monitoring | ✅ |
| MCP tools bridge para LangGraph | ✅ |
| OpenCode Executor com sandbox Docker | ✅ |
| OpenCode Watcher | ✅ |

### Vault e Conhecimento

| Funcionalidade | Status |
|---|---|
| Obsidian vault watcher (watchdog) | ✅ |
| Vault indexer com chunking | ✅ |
| Analyzer de vault com deteccao de contradicoes | ✅ |
| Knowledge Graph file watcher | ✅ |
| Graphify integration para visualizacao arquitetural | ✅ |

### Docker e Infra

| Funcionalidade | Status |
|---|---|
| Docker Compose (dev, local, prod) | ✅ |
| PostgreSQL 16 | ✅ |
| Qdrant vector DB | ✅ |
| Ollama | ✅ |
| n8n automation | ✅ |
| Open WebUI | ✅ |
| Evolution API (WhatsApp) | ✅ |
| Cloudflare Tunnel (producao) | ✅ |
| Prometheus + Loki + Grafana | ✅ |
| Node Exporter + cAdvisor | ✅ |
| Alertmanager + Blackbox Exporter | ✅ |

---

## Arquitetura

```mermaid
graph TB
    subgraph Desktop["Desktop (Tauri 2 + React)"]
        CHAT["Chat UI (SSE)"]
        DASH["Dashboard"]
        TOOLS["Tools & Registry"]
        CP["Command Palette"]
    end

    subgraph Backend["Backend (FastAPI + Python 3.13)"]
        API["API Layer (42 routers)"]
        ORCH["Orchestrator / LangGraph"]
        PROV["Provider Layer"]
        KIRL["KIRL - Documentation Runtime"]
        CAP["Capability Registry"]
        OBS["Observability / Event Bus"]
    end

    subgraph Storage["Storage"]
        PG[(PostgreSQL)]
        QD[(Qdrant Vector DB)]
    end

    subgraph LLM["LLM Providers"]
        OLLAMA[Ollama]
        OPENAI[OpenAI]
        ANTHROPIC[Anthropic]
        GEMINI[Gemini]
        AIRLLM[AirLLM]
    end

    subgraph Infrastructure["Infrastructure (Docker)"]
        N8N[n8n]
        OW[Open WebUI]
        EVO[Evolution API]
        PROM[Prometheus]
        LOKI[Loki]
        GRAF[Grafana]
        CF[Cloudflare Tunnel]
    end

    Desktop -->|HTTP / SSE / WS| Backend
    Backend --> PG
    Backend --> QD
    Backend --> LLM
    Backend --> Infrastructure
```

### Camadas do Backend

| Camada | Descricao |
|---|---|
| **API Layer** | 42 routers (auth, chat, models, orchestrator, rag, indexing, audit, MCP, automacao, plugins, grafo, memoria, conhecimento, inferencia, planner, evidencias, segredos, etc.) |
| **Service Layer** | Logica de negocios (LLM Service, Agent Service) |
| **Workflow Layer** | Intent Classifier > Model Router > Provider Selector > Plan Executor > Circuit Breaker > DLQ |
| **Provider Layer** | Adaptadores para chat (Ollama, OpenAI, Anthropic, Gemini), embedding (BGE, OpenAI), vector (Qdrant), memoria (Postgres, Obsidian), inference, planner, graph, evidence, retrieval |
| **Capability Layer** | Registry com autodiscover, 6 domain ports definidos |
| **KIRL Layer** | Feature Registry, Audit Engine, SDD Generator, Drift Detection, Graphify |
| **Observability Layer** | Event Bus (22 eventos), Prometheus, Loki, OpenTelemetry, Cost Tracker |

### Camadas do Frontend (Feature-Sliced Design)

```
src/
  app/           # Inicializacao, providers, rotas
  pages/         # 21 paginas (uma por rota)
  widgets/       # Componentes complexos (sidebar, command-palette, topbar)
  features/      # Hooks de negocio por feature (7 features)
  entities/      # Tipos de dominio + componentes puros
  shared/        # Design system, stores (15 Zustand stores), API client
  infrastructure/ # Commands, event-bus, http, ipc, storage
  application/   # Hooks, services, stores (15 Zustand)
  domain/        # Entities, events
  presentation/  # Componentes genericos, layouts
```

---

## Estrutura do Projeto

```
K.A.O.S/
├── .github/                     # GitHub Actions (8 workflows)
│   └── workflows/
│       ├── ci.yml               # Validacao backend + desktop + docker
│       ├── release.yml           # Build multi-plataforma (Win/Linux/Mac)
│       ├── auto-release.yml      # Semantic release
│       ├── deploy.yml            # CD com rollback automatico
│       ├── registry-sync.yml     # Feature registry sync + drift check
│       ├── graphify-update.yml   # Atualizacao diaria do grafo
│       ├── auto-update.yml       # Check semanal de updates
│       └── setup-signing-key.yml # Gerenciamento de chave de assinatura
│
├── .opencode/                   # Configuracao OpenCode
│   ├── agents/                  # 8 agentes especializados
│   ├── rules/                   # 10 regras de codigo
│   ├── skills/                  # 10 habilidades
│   ├── tools/                   # 4 ferramentas
│   └── references/              # 6 documentos de referencia
│
├── assistant/                   # Backend Python (FastAPI)
│   ├── app/
│   │   ├── api/                 # 44 routers de API
│   │   ├── ai/                  # Vault Analyzer, Knowledge Graph
│   │   ├── agent/               # LangGraph agent (graph, nodes, state)
│   │   ├── audit/               # KIRL: audit engine, feature registry, SDD
│   │   ├── auth/                # Autenticacao (JWT, handshake, hash)
│   │   ├── capability/          # Capability registry
│   │   ├── capabilities/        # Implementacoes (communication, workspace)
│   │   ├── config/              # Settings + prompts
│   │   ├── core/                # Bootstrap, MCP, plugins, automacao, segredos
│   │   ├── domain/              # Entidades de dominio + ports
│   │   ├── llm/                 # Abstracoes LLM
│   │   ├── memory/              # Memoria conversacional
│   │   ├── middleware/          # API Key, User Context
│   │   ├── models/              # SQLAlchemy models
│   │   ├── notifications/       # Sistema de notificacoes
│   │   ├── observability/       # Event Bus, tracing, cost tracker
│   │   ├── obsidian/            # Vault watcher
│   │   ├── orchestrator/        # Universal orchestrator
│   │   ├── providers/           # Adaptadores (chat, embedding, vector, memory, inference, planner, retrieval, graph, evidence, email, whatsapp, aws, automacao)
│   │   ├── rag/                 # Chunking, embeddings, indexer, retriever
│   │   ├── registry/            # Service registry
│   │   ├── router/              # Roteadores (intent, workflow, memory, smart)
│   │   ├── runtime/             # Runtime selector, communication runtime
│   │   ├── service/             # LLM Service, Agent Service
│   │   ├── setup/               # Setup boot
│   │   ├── tools/               # GitHub MCP tool, n8n webhook
│   │   └── workflows/           # Workflow base + implementacoes
│   ├── migrations/              # Alembic migrations
│   ├── tests/                   # 55+ testes (unit + integration)
│   └── scripts/                 # Scripts auxiliares (17)
│
├── desktop/                     # Desktop Tauri 2 + React
│   ├── src/
│   │   ├── app/                 # Providers, layouts, routes
│   │   ├── pages/               # 21 paginas
│   │   ├── widgets/             # Command palette, sidebar, topbar
│   │   ├── features/            # 7 features (ask-ai, auto-update, dashboard, docs-audit, generate-docs, index-vault, settings)
│   │   ├── entities/            # Message, Provider
│   │   ├── shared/              # Design system (16 componentes UI), stores, API client
│   │   ├── infrastructure/      # Commands, event-bus, http, ipc, storage
│   │   ├── application/         # Hooks, services, stores (15 Zustand)
│   │   ├── domain/              # Entities, events
│   │   ├── presentation/        # Componentes genericos, layouts
│   │   └── __tests__/           # Testes (e2e, features, integration, shared)
│   └── src-tauri/               # Rust backend (Tauri)
│
├── infra/
│   ├── docker/                  # Docker Compose (dev, local, prod)
│   │   ├── docker-compose.yml        # Stack completa (dev)
│   │   ├── docker-compose.local.yml  # Stack completa (local)
│   │   ├── docker-compose.prod.yml   # Stack producao com alertas, tunnel, exporters
│   │   ├── Dockerfile                # Backend Dockerfile
│   │   ├── prometheus.yml
│   │   ├── loki.yml
│   │   ├── promtail.yml
│   │   ├── grafana-datasources.yml
│   │   ├── alertmanager.yml
│   │   ├── alerts.yml
│   │   └── blackbox.yml
│   ├── grafana/                 # Dashboards + provisioning
│   └── migrations/             # SQL schema migrations
│
├── config/                      # Configuracoes do K.A.O.S
│   ├── kaos.config.json         # Configuracao principal
│   ├── kaos.secrets.json        # Secrets criptografados
│   └── mcp.json                  # Registro de servidores MCP
│
├── docs/                        # Documentacao (Obsidian vault)
│   ├── architecture/            # Arquitetura do sistema
│   ├── api/                     # API reference
│   ├── guides/                  # Guias de uso
│   ├── sdd/                     # Software Design Documents
│   ├── governance/              # ADRs, quality gates
│   ├── wiki/                    # Base de conhecimento
│   └── ...
│
├── scripts/                     # Scripts utilitarios (12)
│   ├── check-version-consistency.js
│   ├── update-versions.js
│   ├── generate_icons.py
│   ├── gen_update_proxy.py
│   └── ...
│
├── .releaserc.json              # Configuracao semantic-release
├── .commitlintrc.json           # Commitlint config
├── package.json                 # Root (commitlint)
└── setup.ps1                    # Script de bootstrap
```

### Novas Capacidades (Sprint 7 + Q4 2026)

#### Intelligence & Memory
* **AI Architecture Reviewer**: LLM-powered analysis reading Graph + SDD + Code → suggests refactors
* **Self-Healing DRL**: Auto-detects documentation drift and applies corrective actions
* **Predictive Architecture**: Estimates change impact before merges using knowledge graph
* **Mem0 Adapter**: Persistent conversational memory with semantic search
* **GraphRAG Experiment**: Hybrid graph + vector retrieval for code-aware RAG
* **Auto-Tag Engine**: ML-based tag suggestions for vault notes using embedding similarity

#### Adapters & Integrations
* **Neo4j Adapter**: Cypher-based property graph queries for code intelligence
* **FalkorDB Adapter**: Graph-native vector search for hybrid retrieval
* **WhatsApp Integration**: Send/receive messages via Evolution API with webhook support
* **Email Integration**: SMTP send + IMAP receive with LangChain tooling
* **AWS Integration**: Read-only CLI tools (EC2, ECS) with command whitelist
* **N8N Automation**: Webhook tool, workflow import/export, GitOps sync
* **WireGuard VPN**: Production access configuration and setup scripts

#### Planning & Execution
* **LangGraphAdapter**: Real plan execution with step dependency resolution
* **Evidence Engine**: 6-source evidence collection (graphify, git, tests, benchmarks, adrs, runtime)
* **Session History**: Full conversation persistence with PostgreSQL + Obsidian export
* **Knowledge Graph**: Graphify + React Flow visualization with search and navigation

#### Documentation System
* **KIRL Audit Engine**: Automated documentation drift detection and reporting
* **Auto-Documentação Contínua**: CI/CD job syncing docs/wiki/ → Obsidian vault
* **SDD Management**: Deduplicated, single-source-of-truth architecture documents
* **Migration Maps**: Cross-reference between PT-BR and EN architecture docs

---

## Stack Tecnologica

| Tecnologia | Versao | Finalidade |
|---|---|---|
| **Python** | 3.13 | Backend / API / ML |
| **FastAPI** | 0.115+ | Framework web |
| **LangGraph** | 0.2+ | Orquestracao de workflows |
| **LangChain** | 0.3+ | Integracoes LLM |
| **SQLAlchemy** | 2.0+ | ORM async |
| **Alembic** | 1.18+ | Migrations |
| **PostgreSQL** | 16 | Banco relacional |
| **Qdrant** | latest | Vector database |
| **Ollama** | latest | LLM local |
| **AirLLM** | — | LLM local (pesado) |
| **sentence-transformers** | 3.0+ | Embeddings (BGE, nomic) |
| **Prometheus** | 2.54 | Metricas |
| **Loki** | 3.0 | Logs |
| **Grafana** | 11.1 | Dashboards |
| **n8n** | latest | Automacao low-code |
| **Open WebUI** | latest | Interface web alternativa |
| **Evolution API** | 2.1.1 | WhatsApp Business |
| **TypeScript** | 5.5 | Frontend |
| **React** | 18.3 | UI framework |
| **Tauri** | 2 | Desktop nativo (Rust) |
| **Rust** | 1.85 | Desktop backend |
| **Vite** | 5.4 | Bundler |
| **Tailwind CSS** | 3.4 | Estilizacao |
| **Zustand** | 5.0 | Gerenciamento de estado |
| **React Router** | 7.18 | Roteamento |
| **Vitest** | 2.1 | Testes frontend |
| **Playwright** | 1.48 | Testes E2E |
| **uv** | latest | Gerenciamento de pacotes Python |
| **Docker** | — | Containerizacao |
| **GitHub Actions** | — | CI/CD |
| **Cloudflare Tunnel** | — | Exposicao segura producao |
| **PyNaCl** | 1.6 | Criptografia |
| **Wasmtime** | 46.0 | Sandbox plugins |

---

## Requisitos

### Desenvolvimento

| Requisito | Versao Minima |
|---|---|
| [Docker](https://www.docker.com/) | 24+ |
| [Docker Compose](https://docs.docker.com/compose/) | 2.20+ |
| [Python](https://www.python.org/) | 3.13 |
| [uv](https://github.com/astral-sh/uv) | latest |
| [Node.js](https://nodejs.org/) | 22 |
| [npm](https://www.npmjs.com/) | 10+ |
| [Rust](https://www.rust-lang.org/) | 1.85+ (stable) |
| [Git](https://git-scm.com/) | 2.40+ |

### Producao

- Docker + Docker Compose
- 8 GB RAM minimo (16 GB recomendado)
- 20 GB de armazenamento
- GPU opcional para inferencia local

---

## Instalacao

### 1. Clone o repositorio

```bash
git clone https://github.com/Brian5m1th/K.A.O.S.git
cd K.A.O.S
```

### 2. Configure o ambiente

```bash
cp assistant/.env.example assistant/.env
# Edite assistant/.env com suas configuracoes
```

Variaveis essenciais:

```
OLLAMA_BASE_URL=http://localhost:11434
QDRANT_HOST=localhost
QDRANT_PORT=6333
DATABASE_URL=postgresql+psycopg://ai-p:ai-admin@localhost:5433/kaos
```

### 3. Inicie a infraestrutura (Docker)

```bash
cd infra/docker
docker compose up -d
```

Isso inicia: PostgreSQL, Qdrant, Ollama, n8n, Open WebUI, Prometheus, Loki, Promtail, Grafana e Evolution API.

### 4. Inicie o backend (desenvolvimento)

```bash
cd assistant
uv sync
uv run uvicorn app.main:app --reload --port 8000
```

### 5. Inicie o desktop

```bash
cd desktop
npm install
npm run tauri dev
```

### Alternativa: Tudo com Docker (recomendado para Dev)

O `docker-compose.yml` ja inclui o `kaos-api` com hot-reload:

```bash
cd infra/docker
docker compose up -d
# Backend em http://localhost:8000
# Open WebUI em http://localhost:3000
# Grafana em http://localhost:3001 (admin/admin)
# n8n em http://localhost:5678
```

### Alternativa: Producao

```bash
cd infra/docker
cp .env.example .env.prod
# Edite .env.prod
docker compose -f docker-compose.prod.yml --env-file .env.prod up -d
```

---

## Configuracao

### `.env` (backend)

| Variavel | Default | Descricao |
|---|---|---|
| `APP_NAME` | `K.A.O.S` | Nome da aplicacao |
| `APP_ENV` | `development` | Ambiente (development/production) |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | URL do Ollama |
| `OLLAMA_MODEL` | `qwen3:14b` | Modelo Ollama principal |
| `OLLAMA_FAST_MODEL` | `qwen3:4b` | Modelo Ollama rapido |
| `OPENAI_API_KEY` | — | Chave OpenAI |
| `ANTHROPIC_API_KEY` | — | Chave Anthropic |
| `GEMINI_API_KEY` | — | Chave Gemini |
| `QDRANT_HOST` | `localhost` | Host Qdrant |
| `QDRANT_PORT` | `6333` | Porta Qdrant |
| `QDRANT_COLLECTION` | `obsidian_memory` | Colecao Qdrant |
| `DATABASE_URL` | — | URL PostgreSQL |
| `CORS_ORIGINS` | `http://localhost:1420,http://localhost:3000` | Origens CORS |
| `N8N_WEBHOOK_URL` | — | Webhook n8n |
| `HF_TOKEN` | — | Token HuggingFace |
| `EMAIL_HOST` | — | Servidor IMAP |
| `WHATSAPP_API_URL` | — | URL Evolution API |
| `API_KEY` | — | Chave de API (gerada automaticamente se vazia) |

### `config/kaos.config.json`

```json
{
  "theme": "dark",
  "providers": {
    "ollama": { "url": "http://localhost:11434", "model": "qwen3:14b" },
    "openai": { "url": "https://api.openai.com/v1", "model": "gpt-4o" },
    "anthropic": { "url": "https://api.anthropic.com", "model": "claude-sonnet-4-20250514" },
    "gemini": { "url": "https://generativelanguage.googleapis.com", "model": "gemini-2.0-flash" }
  }
}
```

### `config/mcp.json`

```json
{
  "servers": [
    {
      "name": "github",
      "command": "python",
      "args": ["-m", "app.tools.github_tool"],
      "enabled": true
    }
  ]
}
```

---

## Como Executar

### Backend (desenvolvimento)

```bash
cd assistant
uv sync
uv run uvicorn app.main:app --reload --port 8000
```

### Frontend Desktop (desenvolvimento)

```bash
cd desktop
npm install
npm run tauri dev
```

### Frontend Web (Vite apenas)

```bash
cd desktop
npm install
npm run dev
# Abre em http://localhost:1420
```

### Docker (stack completa)

```bash
cd infra/docker
docker compose up -d                    # Dev
docker compose -f docker-compose.prod.yml --env-file .env.prod up -d  # Prod
```

### Scripts de setup

```powershell
.\setup.ps1              # Windows
bash assistant/scripts/setup.sh  # Linux
```

---

## Como Executar Testes

### Backend (Python)

```bash
cd assistant
uv sync --only-dev
uv run ruff check .                          # Lint
uv run ruff format --check .                  # Formatacao
uv run pytest tests/ -v --asyncio-mode=auto   # Testes (55+)
uv run pytest tests/ --cov=app --cov-report=html  # Cobertura
```

### Desktop (TypeScript/React)

```bash
cd desktop
npx tsc --noEmit                             # Type check
npx vitest run                               # Testes unitarios
npx vitest run --coverage                    # Cobertura
npx playwright test                          # Testes E2E
npx vitest --ui                              # UI mode
```

### Verificacao de versoes

```bash
node scripts/check-version-consistency.js
```

---

## Scripts

| Script | Descricao |
|---|---|
| `scripts/check-version-consistency.js` | Verifica consistencia de versao entre package.json, tauri.conf.json e Cargo.toml |
| `scripts/update-versions.js` | Atualiza versao em todos os arquivos de configuracao |
| `scripts/generate_icons.py` | Gera icones para o Tauri |
| `scripts/gen_update_proxy.py` | Gera manifest de update-proxy.json para auto-update |
| `scripts/export-graphify-obsidian.py` | Exporta grafo Graphify para Obsidian |
| `scripts/scan_docs_gaps.py` | Escaneia lacunas na documentacao |
| `scripts/fix_docs_metadata.py` | Corrige metadados de documentos |
| `assistant/scripts/setup.sh` | Setup automatizado do backend (Linux) |
| `assistant/scripts/setup.ps1` | Setup automatizado do backend (Windows) |
| `assistant/scripts/run.ps1` | Executa o backend (Windows) |
| `assistant/scripts/run-local.ps1` | Executa o backend localmente (Windows) |
| `assistant/scripts/run-local.bat` | Executa o backend localmente (Windows - CMD) |

---

## APIs

### Endpoints principais

| Metodo | Rota | Descricao |
|---|---|---|
| GET | `/health` | Health check |
| POST | `/api/chat/message` | Chat com streaming SSE |
| POST | `/v1/chat/completions` | API OpenAI-compativel |
| GET | `/v1/models` | Catalogo de modelos |
| POST | `/api/orchestrator/execute` | Execucao de workflow |
| POST | `/indexing/full` | Indexacao completa do vault |
| POST | `/rag/context` | Busca contexto RAG |
| GET | `/api/audit/status` | Status da auditoria KIRL |
| GET | `/api/graph/explain/{concept}` | Explicacao via grafo |
| POST | `/api/memory/search` | Busca na memoria |
| POST | `/api/knowledge/query` | Consulta conhecimento |
| POST | `/api/inference/invoke` | Infeccao via provedores |
| POST | `/api/planner/plan` | Planejamento |
| GET | `/api/evidence/report` | Relatorio de evidencias |
| GET | `/api/secrets/status` | Status de segredos |
| POST | `/api/auth/login` | Login / geracao de API key |
| GET | `/api/setup/providers` | Configuracao de providers |
| POST | `/api/webhooks/n8n` | Webhook n8n |
| GET | `/api/observability/metrics` | Metricas Prometheus |
| POST | `/api/mcp/servers` | Registro de servidor MCP |
| GET | `/api/automation/workflows` | Workflows de automacao |
| POST | `/api/automation/workflows/import` | Importar workflow |
| POST | `/api/plugins/execute` | Execucao de plugin em sandbox |
| GET | `/api/opencode/status` | Status do OpenCode |

42 routers disponiveis no total. Consulte `docs/api/API_REFERENCE.md` para documentacao completa.

---

## Integracoes

| Integracao | Tipo | Status |
|---|---|---|
| **OpenAI** | Chat + Embedding | ✅ |
| **Anthropic** | Chat | ✅ |
| **Gemini** | Chat | ✅ |
| **Ollama** | Chat local | ✅ |
| **AirLLM** | LLM local pesado | ✅ |
| **Qdrant** | Vector store | ✅ |
| **PostgreSQL** | Banco relacional | ✅ |
| **n8n** | Automacao low-code | ✅ |
| **Open WebUI** | Interface web alternativa | ✅ |
| **Evolution API** | WhatsApp Business | ✅ |
| **Email (IMAP/SMTP)** | Comunicacao | ✅ |
| **AWS** | Computacao cloud | ✅ |
| **GitHub** | MCP tool + Actions | ✅ |
| **Prometheus** | Metricas | ✅ |
| **Loki** | Logs | ✅ |
| **Grafana** | Dashboards | ✅ |
| **Cloudflare Tunnel** | Exposicao segura | ✅ |
| **Node Exporter** | Metricas de sistema | ✅ |
| **cAdvisor** | Metricas de container | ✅ |
| **Alertmanager** | Alertas | ✅ |
| **Blackbox Exporter** | Monitoramento externo | ✅ |
| **WireGuard** | VPN (planejado) | 📅 |

---

## MCP (Model Context Protocol)

O K.A.O.S possui um sistema de gerenciamento MCP integrado:

### Componentes

- **`config/mcp.json`** — Registro estatico de servidores MCP
- **`assistant/app/core/mcp_manager.py`** — Gerenciamento em runtime
- **`assistant/app/core/mcp_registry.py`** — Registry de servidores
- **`assistant/app/core/mcp_health.py`** — Health check dos servidores
- **`assistant/app/tools/mcp_adapter.py`** — Ponte MCP -> LangGraph TOOL_REGISTRY

### Servidores registrados

| Servidor | Comando | Ativo |
|---|---|---|
| GitHub | `python -m app.tools.github_tool` | ✅ |

### Como adicionar um servidor MCP

```json
// config/mcp.json
{
  "servers": [
    {
      "name": "meu-servidor",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem"],
      "enabled": true,
      "env": {}
    }
  ]
}
```

O servidor e automaticamente descoberto no startup e registrado no LangGraph TOOL_REGISTRY.

---

## Observabilidade

### Logs

- Formato estruturado (JSON em producao)
- Niveis configurados via `LOG_LEVEL`
- Rota para Loki + Promtail
- Logger padrao: Loguru

### Metricas (Prometheus)

- Instrumentacao automatica via `prometheus-fastapi-instrumentator`
- Rotas expostas em `/metrics`
- Metricas customizadas: tokens, custos, falhas
- Dashboards Grafana provisionados

### Tracing (OpenTelemetry)

- Spans para: orquestrador, LLM requests, workflows, providers
- Rota configurada via `setup_tracing()`

### Health Checks

| Endpoint | Descricao |
|---|---|
| `/health` | Saude basica do servico |
| `/health/readiness` | Readiness probe |
| `/health/observability` | Status dos servicos de observabilidade |

---

## Seguranca

| Mecanismo | Descricao |
|---|---|
| **API Key** | Autenticacao via header `x-api-key` ou `Authorization: Bearer` |
| **JWT** | Tokens JWT para sessoes |
| **CORS** | Origens configuradas via `CORS_ORIGINS` |
| **Handshake** | Criptografia efemera PyNaCl na inicializacao |
| **Secrets** | Gerenciamento centralizado via Secret Manager |
| **Plugin Sandbox** | Execucao isolada via Wasmtime |
| **OpenCode Executor** | Sandbox Docker com whitelist/blacklist |
| **Assinatura** | Pacotes assinados com minisign/cosign |
| **Cloudflare Tunnel** | Exposicao sem abertura de porta |

---

## CI/CD

| Workflow | Gatilho | Acao |
|---|---|---|
| **CI** | PR/ push para dev/main | Lint, testes, build docker, push GHCR, sign |
| **Release** | Tag v* | Build multi-plataforma (Windows, Linux, macOS), upload artifacts, update-proxy |
| **Auto Release** | Push para main | Semantic-release, changelog, version bump |
| **Deploy** | Push para main (assistant/) | Deploy em self-hosted, healthcheck, rollback |
| **Registry Sync** | Push para dev/main | Feature registry bootstrap + drift check |
| **Graphify Update** | Diario (03:00 UTC) | Atualizacao automatica do grafo arquitetural |
| **Auto Update** | Semanal | Verificacao de novas versoes |
| **Setup Signing Key** | Manual | Gerenciamento de chave de assinatura Tauri |

---

## Roadmap

### Concluido (v2.x)

- ✅ Orquestracao universal com LangGraph
- ✅ Multi-provedor LLM com fallback chain
- ✅ RAG com Qdrant + embeddings
- ✅ Indexacao de vault Obsidian
- ✅ KIRL (Documentation Runtime Layer)
- ✅ Observabilidade (Prometheus, Loki, Grafana)
- ✅ Desktop Tauri 2 com chat e dashboard
- ✅ Feature Registry com sync via git
- ✅ Drift detection e auditoria documental
- ✅ Automacao n8n
- ✅ Integracoes Email e WhatsApp
- ✅ Plugin system com sandbox Wasm
- ✅ OpenCode integration
- ✅ CI/CD completo com deploy e rollback
- ✅ Graphify para grafo arquitetural
- ✅ Domain ports (inference, memory, retrieval, planner, graph, evidence)
- ✅ Bootstrap Manager
- ✅ Cloudflare Tunnel
- ✅ Alertmanager + Blackbox Exporter

### Em andamento

- 🚧 Vault Analyzer (contradicao logica/cronologica)
- 🚧 Evidence Engine completo (Git + Tests)
- 🚧 Knowledge Graph (unificacao)

### Planejado

- 📅 Mem0 para memoria conversacional avancada
- 📅 GraphRAG
- 📅 AI Architecture Reviewer
- 📅 Self-Healing DRL
- 📅 Predictive Architecture
- 📅 WireGuard VPN
- 📅 Auto-documentacao continua

---

## Contribuicao

### Convencao de Commits

Seguimos [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: nova funcionalidade
fix: correcao de bug
refactor: refatoracao
test: adicao ou correcao de testes
docs: documentacao
ci: CI/CD
chore: manutencao
style: formatacao
perf: performance
```

Formatacao: descricao em lowercase, maximo 100 caracteres.

Exemplo: `feat: add MCP server registry with health checks`

### Fluxo

1. Fork do repositorio
2. Crie uma branch a partir de `dev`: `git checkout -b feat/minha-feature`
3. Commit com mensagem padrao conventional commit
4. Push e abra Pull Request para `dev`
5. Aguarde CI passar e review

### Branches

- `main` — Producao
- `dev` — Desenvolvimento (PRs vao para ca)

---

## Licenca

MIT License.

---

## Creditos

### Autores

- **Brian** — Arquiteto principal e desenvolvedor

### Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [Tauri](https://v2.tauri.app/)
- [React](https://react.dev/)
- [Qdrant](https://qdrant.tech/)
- [PostgreSQL](https://www.postgresql.org/)
- [Ollama](https://ollama.ai/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Loki](https://grafana.com/oss/loki/)
- [n8n](https://n8n.io/)
- [Open WebUI](https://openwebui.com/)
- [Cloudflare Tunnel](https://www.cloudflare.com/products/tunnel/)
- [OpenCode](https://opencode.ai)
