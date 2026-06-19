Source: Antigravity AI
Tags: #backlog #planejamento #roadmap
Related: [[index]] [[sdd_obsidian_memoria]] [[00_visao_geral]]

# Backlog — IA Pessoal Offline com Obsidian

> Rastreamento completo de todas as tarefas de desenvolvimento, organizadas por tipo e prioridade.

---

## 📊 Visão Geral de Progresso

| Fase | Nome | Itens | Status |
| :---: | :--- | :---: | :---: |
| 1 | Fundação | 7 | ✅ Completa |
| 2 | IA Local | 10 | ✅ Completa |
| 3 | Integração Obsidian | 15 | ✅ Completa |
| 4 | Organização do Vault | 12 | ✅ Completa |
| 5 | RAG | 7 | ✅ Completa |
| 6 | Atualização Automática | 5 | ✅ Completa |
| 7 | Agente Inteligente | 6 | ✅ Completa |
| 8 | Memória de Longo Prazo | 6 | ✅ Completa |
| 8B | User Context | 8 | ✅ Completa |
| 9 | Integrações Online | 6 | ✅ Completa |
| 10 | Produção | 6 | ⬜ Aguardando |
| 11 | Otimização e Roteamento | 8 | ✅ Completa |
| 12 | Knowledge Wiki Layer | 23 | ✅ Completa |
| 13 | Provedor Híbrido de LLM | 13 | ✅ Completa |
| 14 | CI/CD + Desktop | 10 | 🔄 Em Progresso |
| 15 | Otimização de Build Desktop | 8 | ⬜ Planejado |

---

---

## Legenda de Categorias

| Tag | Significado |
|:----|:------------|
| `TODO` | Tarefa pendente, priorizada |
| `DEBT` | Dívida técnica a ser paga |
| `IDEA` | Ideia não validada, sem prioridade |

---

## Mapa de Dependências entre Fases

```mermaid
graph LR
    F1[Fase 1\nFundação] --> F2[Fase 2\nIA Local]
    F1 --> F3[Fase 3\nObsidian]
    F2 --> F3
    F3 --> F4[Fase 4\nOrg. Vault]
    F3 --> F5[Fase 5\nRAG]
    F5 --> F6[Fase 6\nAuto Update]
    F5 --> F7[Fase 7\nAgente]
    F6 --> F7
    F7 --> F8[Fase 8\nMemória LP]
    F7 --> F9[Fase 9\nIntegrações]
    F8 --> F10[Fase 10\nProdução]
    F9 --> F10
    F10 --> F11[Fase 11\nOtimização]
    F7 --> F12[Fase 12\nWiki Layer]
    F5 --> F12
    F11 --> F12
    F12 --> F13[Fase 13\nLLM Provider]
    F7 --> F13
```

---

---

## Próximas Tarefas Prioritárias

- [x] **Testar pipeline wiki completo**: draft mode, ingest, approve, lint
- [x] **Testar fallback LLM**: fallback automático testado
- [x] **Auditoria RAG**: GET `/rag/diagnostics` + logs de score distribution
- [x] **Dockerfile + vault mount**: volume persistente + init automático
- [x] **User Context**: middleware headers + propagacão completa
- [x] **Setup guide**: Documentar modos de execução (Windows, WSL, Docker)
- [x] **Integrações**: N8N, webhooks, tools externas

---

## Fase 1 — Fundação ✅

> Relacionado: [[01_estrutura_pastas]]

- [x] Configurar Python 3.13
- [x] Configurar ambiente virtual (`uv`)
- [x] Estruturar projeto base (`app/`, `tests/`, `docker/`, `docs/`)
- [x] Configurar Docker Compose (serviços base)
- [x] Configurar FastAPI (ponto de entrada + health check)
- [x] Configurar sistema de logs (`loguru`)
- [x] Configurar arquivos de ambiente (`.env` + `pydantic-settings`)

---

## Fase 2 — IA Local ✅

> Relacionado: [[sdd_fase2_ia_local]] [[sdd_arquitetura_orquestracao]]

- [x] Instalar Ollama
- [x] Baixar modelo Qwen3 4B (`ollama pull qwen3:4b`)
- [x] Criar serviço de comunicação com Ollama (`app/service/llm_service.py`)
- [x] Criar endpoint de chat (`POST /api/chat/message`)
- [x] Integrar Open WebUI (configurar no Docker Compose)
- [x] Validar funcionamento 100% offline
- [x] Criar proxy OpenAI (`POST /v1/chat/completions`) em `app/api/openai.py`
- [x] Criar system prompt do K.A.O.S. em `app/config/prompts.py`
- [x] Configurar CORS no FastAPI
- [x] Aumentar timeout do LLMService (120s → 600s)

---

## Fase 3 — Integração com Obsidian ✅

> Relacionado: [[sdd_obsidian_tools]] [[sdd_obsidian_memoria]]

### ⚙️ Configuração

- [x] Identificar caminho absoluto do Vault no sistema
- [x] Configurar `OBSIDIAN_VAULT_PATH` no `.env`
- [x] Criar módulo `app/obsidian/` com `__init__.py`

### 📖 Leitura

- [x] Implementar `ObsidianService` (`app/obsidian/services/obsidian_service.py`)
- [x] Implementar `ReadNoteTool` — leitura de nota por caminho relativo
- [x] Implementar `ListNotesTool` — listagem de notas por pasta
- [x] Testar leitura de arquivos Markdown existentes no Vault

### ✏️ Escrita

- [x] Implementar `CreateNoteTool` — criação de nota com título, pasta e conteúdo
- [x] Implementar `UpdateNoteTool` — sobrescrição ou append de nota existente
- [x] Implementar `DeleteNoteTool` — remoção de nota com tratamento de erros
- [ ] Validar criação de notas geradas pelo Python no Obsidian

### 🔍 Busca

- [x] Implementar `SearchNotesTool` — busca textual por palavra-chave
- [x] Implementar busca textual com `grep` / walk do filesystem
- [x] Criar testes automatizados para todas as tools (`tests/unit/obsidian/`)

---

## Fase 4 — Organização do Vault ✅

- [x] Criar estrutura padrão de pastas no Vault (endpoint `POST /indexing/init-folders`)

Pastas criadas via `vault_init.py`:

- [x] `Projetos/` — status e escopo de projetos ativos
- [x] `Arquitetura/` — decisões e padrões arquiteturais
- [x] `SDD/` — System Design Documents
- [x] `Estudos/` — resumos de aprendizado
- [x] `IA/` — prompts, modelos e experimentos
- [x] `Python/` — padrões, libs e tutoriais Python
- [x] `Java/` — ecossistema Java e Spring Boot
- [x] `AWS/` — infraestrutura e comandos AWS
- [x] `CI-CD/` — pipelines e automações de deploy
- [x] `Diário/` — registros diários e resumos de reuniões
- [x] `Inbox/` — ponto de entrada para notas sem categorização

---

## Fase 5 — RAG ✅

> Relacionado: [[sdd_obsidian_rag]]

- [x] Subir Qdrant via Docker Compose (`qdrant/qdrant`)
- [x] Configurar embeddings (modelo `BAAI/bge-m3`)
- [x] Implementar chunking de documentos (`app/rag/chunking/`)
- [x] Indexar notas do Obsidian (`app/rag/indexer/`)
- [x] Criar retriever semântico (`app/rag/retriever/`)
- [x] Testar consultas contextuais (testes em `tests/integration/rag/`)

---

## Fase 6 — Atualização Automática ✅

> Relacionado: [[sdd_obsidian_watcher]]

- [x] Adicionar `watchdog` como dependência do projeto
- [x] Detectar evento de **criação** de arquivos `.md`
- [x] Detectar evento de **alteração** de arquivos `.md`
- [x] Detectar evento de **exclusão** de arquivos `.md`
- [x] Disparar reindexação automática no Qdrant para cada evento

---

## Fase 7 — Agente Inteligente ✅

> Relacionado: [[02_fluxo_dados]]

- [x] Instalar LangGraph (`uv add langgraph`)
- [x] Criar `Agent Orchestrator` (`app/agent/graph.py`) com nós e arestas condicionais
- [x] Criar `Tool Registry` — mapeamento de 7 ferramentas disponíveis ao agente
- [x] Integrar ferramentas do Obsidian ao Tool Registry
- [x] Implementar nó de planejamento de tarefas (`planner`)
- [x] Conectar o grafo LangGraph ao endpoint de chat (`/api/chat/message` e `/v1/chat/completions`)

---

## Fase 8 — Memória de Longo Prazo ✅

- [x] Criar memória de preferências (`Vault/IA/preferencias.md`)
- [x] Criar memória de projetos (notas em `Vault/Projetos/`)
- [x] Criar memória de arquitetura (notas em `Vault/Arquitetura/`)
- [x] Criar memória de estudos (notas em `Vault/Estudos/`)
- [x] Implementar comando **"salve esta conversa"** → `save_conversation` tool
- [x] Implementar comando **"atualize esta nota"** → busca + `UpdateNoteTool`

---

## Fase 8B — User Context & Multiusuário ✅

> Relacionado: [[sdd_user_context_propagation]] [[02_fluxo_dados]] [[sdd_obsidian_memoria]]

- [x] Criar UserContext model (`app/domain/user.py`)
- [x] Adicionar user_id ao ChatRequest e ChatCompletionRequest
- [x] Adicionar user_id, username, role ao AgentState
- [x] Escopar MemoryService por usuário (`Vault/users/{user_id}/`)
- [x] Atualizar save_conversation tool com user_id
- [x] Propagar UserContext nos endpoints e routers (middleware + headers)
- [x] Adicionar user_id aos logs (auditoria)
- [x] Criar MemoryRepository protocol para futura migração PostgreSQL

---

## Fase 9 — Integrações Online ✅

- [x] Subir N8N via Docker Compose
- [x] Criar integração via Webhook (N8N recebe e envia eventos ao FastAPI)
- [x] Integrar GitHub (consulta de repositórios e código)
- [x] Criar webhooks router (`app/api/webhooks.py`)
- [x] Criar GitHub tools (`app/tools/github_tools.py`)
- [x] Adicionar N8N service ao docker-compose.yml

---

## Fase 10 — Produção

- [ ] Configurar autenticação (JWT ou API Key no FastAPI)
- [ ] Configurar backups automáticos do Vault (script + cron)
- [ ] Configurar monitoramento (Prometheus + Grafana ou Loki)
- [x] Configurar CI/CD (GitHub Actions para lint, tests e build)
- [ ] Criar documentação técnica (`docs/README_tecnico.md`)
- [ ] Criar documentação de instalação (`docs/INSTALL.md`)

---

---

## Fase 11 — Otimização de Performance e Roteamento Inteligente ✅

- [x] Criar `IntentClassifier` com fast path (keyword match) + LLM fallback (Qwen3 4B)
- [x] Criar `FastRouter` — execução direta de tools (sem LLM, sem RAG, sem LangGraph)
- [x] Criar `MemoryRouter` — RAG + LLM sem LangGraph
- [x] Criar `SmartRouter` — LangGraph completo (wrapping AgentService)
- [x] Criar `ResponseCache` — cache de respostas frequentes com TTL
- [x] Integrar roteamento em `chat.py` e `openai.py`
- [x] Criar `ListProjectsTool` e registrar no TOOL_REGISTRY
- [x] Adicionar suporte a modelo rápido (Qwen3 4B) vs principal (`settings.py`)

---

## Fase 12 — Knowledge Wiki Layer (Schema + Tools + Ingestion)

> Relacionado: [[sdd_knowledge_wiki_layer]]

### Schema & Estrutura ✅
- [x] Criar `AGENTS.md` (EN) na raiz do wiki
- [x] Criar `AGENTS.pt-BR.md` (PT) na raiz do wiki
- [x] Criar estrutura wiki/ (entities, concepts, sources, synthesis)
- [x] Adicionar pastas raw/ e wiki/ ao vault_init.py
- [x] Criar frontmatter YAML padronizado nas tools de nota
- [x] Criar index.md e log.md iniciais (bootstrap)

### Ferramentas Wiki ✅
- [x] Implementar create_entity_tool + update_entity_tool com draft mode
- [x] Implementar create_concept_tool + update_concept_tool com draft mode
- [x] Implementar create_source_page_tool com draft mode
- [x] Implementar create_synthesis_tool com draft mode
- [x] Implementar append_log_tool + update_index_tool
- [x] Implementar approve_draft / reject_draft / list_drafts tools
- [x] Registrar todas as tools no TOOL_REGISTRY

### Ingestion Pipeline ✅
- [x] Implementar ingest_source node no LangGraph
- [x] Adicionar entry point condicional no graph.py (ingest vs query)
- [x] Adicionar intent type INGEST no IntentClassifier
- [x] Pipeline completo: source → entities → concepts → index → log

### Query Evolution ✅
- [x] Modificar retrieve para consultar index.md + wiki antes do Qdrant
- [x] Tool file_synthesis_page para respostas complexas
- [x] Atualizar SYSTEM_PROMPT_KAOS para wiki awareness

### Manutenção
- [x] Implementar lint_wiki_tool (contradictions, orphans, broken links)
- [x] Testar pipeline completo com draft mode (`tests/unit/agent/test_ingest.py`)

---

## Fase 13 — Provedor Híbrido de LLM ✅

> Relacionado: [[sdd_llm_provider_hybrid]]

### Abstração + Factory ✅
- [x] Criar interface BaseProvider (app/llm/provider.py)
- [x] Criar LLMFactory com build() e resolve() (app/llm/factory.py)
- [x] Migrar OllamaProvider de ChatOllama direto para app/llm/providers/

### Provedores Cloud ✅
- [x] Implementar OpenAIProvider
- [x] Implementar ClaudeProvider
- [x] Implementar GeminiProvider
- [x] Adicionar MODEL_MAP e FALLBACK_CHAIN ao settings.py
- [x] Adicionar API keys (OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY) ao .env

### Refatoração do Core ✅
- [x] Refatorar planner.py para usar LLMFactory
- [x] Refatorar IntentClassifier para usar LLMFactory
- [x] Refatorar MemoryRouter para usar LLMFactory
- [x] Refatorar openai.py proxy para usar LLMFactory

### Métricas + Fallback ✅
- [x] Implementar ProviderMetrics (provider, model, latency, tokens, cost)
- [x] Implementar chat_with_fallback (fallback automático)
- [x] Log estruturado de métricas por provider
- [x] Testar fallback: fallback chain testado (`tests/unit/llm/test_factory.py`)

---

---

## Fase 15 — Otimização de Build Desktop

> Relacionado: [[sdd_desktop_build_optimization]]

### Caching (Rust + Node)

- [ ] Implementar `Swatinem/rust-cache@v2` no workflow desktop (cache `target/`, cargo registry, cargo git)
- [ ] Implementar `actions/setup-node` com `cache: npm` (cache `node_modules`)

### Build Condicional

- [ ] Adicionar `paths` filter no trigger do workflow desktop (`desktop/**`, `src-tauri/**`, `Cargo.toml`, `Cargo.lock`, `package.json`)
- [ ] Ignorar paths de documentação (`README.md`, `docs/**`, `wiki/**`, `*.md`)

### Pipeline Separada

- [ ] Criar `desktop-ci.yml` — workflow independente para build Tauri (lint + test + build + artifact)
- [ ] Criar `desktop-release.yml` — workflow de release apenas por tag (download artifact + GitHub Release)
- [ ] Remover job `tauri` do `ci.yml` (migrado para `desktop-ci.yml`)

### Cache de Artefatos Frontend

- [ ] Cachear `.vite/` e `dist/` com `actions/cache@v4`

### Self Hosted Runner (Opcional)

- [ ] Configurar runner auto-hospedado (SSD NVMe, 32GB+, Ryzen 7+)
- [ ] Documentar setup para builds 3-5x mais rápidos

### Métricas

- [ ] Adicionar logging de métricas: frontend build time, rust build time, tauri build time, total pipeline time

## Divida Tecnica (DEBT)

- [x] Corrigir patch target em `tests/test_openai.py` (mira `app.api.openai_compat` ao inves de `app.api.openai`)
- [x] Substituir streaming fake do AgentService por streaming real do LangGraph
- [x] Remover bypass do LangGraph no proxy OpenAI (`/v1/chat/completions` conecta direto no Ollama)
- [x] Adicionar `ruff` como dependencia de dev para lint
- [x] Adicionar `.env.example` ao repositorio
- [x] **Auditoria RAG**: `GET /rag/diagnostics` + logs de score distribution no retrieve
- [x] **Dockerfile**: Volume persistente `/vault` + init automático via startup lifespan
- [x] **Setup guide**: Documentar modos de execução (Windows nativo, WSL, Docker) com `.env` próprio para cada ambiente

---

---

## Fase 14 — CI/CD + Desktop Launcher

> Relacionado: [[sdd-031-ci-cd-auto-update]]

### GitHub Actions

- [x] CI workflow (lint + test em PRs e pushes)
- [x] Release workflow (Docker + GitHub Release em tags)
- [x] Docker Publish workflow (nightly images no GHCR)
- [x] Auto Update Check workflow (semanal)

### KAOS.exe Desktop (Tauri + React)

- [x] Provider selection screen (Ollama, OpenAI, Claude, Gemini)
- [x] Vault configuration screen (path + init)
- [x] Chat screen (messages + offline mode)
- [x] Tauri Rust backend (check_server, check_ollama commands)
- [x] Auto-update plugin configuration (Tauri updater)

### Pendentes

- [ ] Gerar assets de ícone (32x32, 128x128, icns, ico)
- [ ] Gerar chave de assinatura para auto-update (Tauri updater pubkey)
- [ ] Testar build Tauri em Windows (npm run tauri build)
- [ ] Corrigir healthcheck Docker: retry loop (app leva 30-60s para baixar modelo)
- [ ] Testar pipeline CI no GitHub (precisa de secrets do GHCR)
- [ ] Cosign para assinatura de imagens Docker

## Ideias (IDEA)

- [ ] Auto-tagging de notas baseado em embeddings
- [ ] Sugestao de conexoes entre notas (grafos)
- [ ] Dashboard web para visualizar status do sistema
- [ ] Exportacao de conversas para markdown

---

*Atualizado em 2026-06-18.*
