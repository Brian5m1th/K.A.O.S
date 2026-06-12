Source: K.A.O.S Project
Tags: #sdd #roadmap #fases
Related: [[index]] [[00_visao_geral]] [[backlog]]

# SDD — Roadmap do K.A.O.S

## Objetivo

Construir uma assistente de IA pessoal capaz de operar offline utilizando conhecimento armazenado em um Vault Obsidian e executar integrações externas através do N8N.

---

## Arquitetura Alvo

```text
Open WebUI
  ↓
FastAPI (Triple-Router: FAST / MEMORY / SMART)
  ↓
LangGraph (SMART) ←→ RAG (MEMORY) ←→ Tools (FAST)
  ↓
Obsidian (memória) ←→ Qdrant (RAG)
  ↓
N8N (automação externa)
```

---

## Fase 1 — Fundacao ✅

### Entregaveis
- Python 3.13 + uv
- FastAPI com health check
- Docker Compose (Postgres, Qdrant, Open WebUI)
- Logs com loguru

### Status
Aplicacao sobe e responde `GET /health` com 200 OK.

---

## Fase 2 — IA Local ✅

### Entregaveis
- LLMService (comunicacao com Ollama)
- Proxy OpenAI `/v1/chat/completions`
- System prompt do K.A.O.S
- CORS configurado

### Status
Open WebUI conversa com a IA local via proxy OpenAI.

---

## Fase 3 — Integracao com Obsidian ✅

### Entregaveis
- ObsidianService (CRUD de notas)
- 7 ferramentas LangChain (create, read, update, delete, search, list, save_conversation)
- Testes unitarios

### Status
IA consegue ler, criar, atualizar, deletar e buscar notas no Vault.

---

## Fase 4 — Busca Semantica (RAG) ✅

### Entregaveis
- Qdrant para armazenamento vetorial
- Embeddings BGE-M3 (1024 dim)
- Chunking Markdown com overlap
- Indexador automatico
- Retriever semantico

### Status
IA recupera contexto relevante do Vault por similaridade semantica.

---

## Fase 5 — Atualizacao Automatica ✅

### Entregaveis
- Watchdog monitorando o vault
- Reindexacao automatica em create/modify/delete/move
- Testes do watcher

### Status
Alteracoes no Obsidian sao automaticamente refletidas no Qdrant.

---

## Fase 6 — Agentes (LangGraph) ✅

### Entregaveis
- Grafo LangGraph (retrieve -> planner -> executor)
- Tool Registry com 7 ferramentas
- Streaming real via astream_events
- Integracao com endpoint de chat e proxy OpenAI

### Status
IA escolhe ferramentas autonomamente e responde com contexto RAG.

---

## Fase 7 — Memoria de Longo Prazo ✅

### Entregaveis
- MemoryService (preferencias, conversas)
- save_conversation tool
- Preferencias injetadas no contexto do planner
- Comandos semanticos ("salve esta conversa", "atualize esta nota")

### Status
IA adapta respostas com base no historico e preferencias armazenadas.

---

## Fase 8 — Performance, RAG & Roteamento Inteligente 🟡 Em Andamento

### Entregaveis Concluídos
- ✅ **Singleton Embedder** — `get_embedder()` evita reloads; `warmup_embedder()` no startup
- ✅ **Fast Intent Classifier** — Keywords PT-BR/EN (FAST/MEMORY); LLM fallback com `OLLAMA_FAST_MODEL`
- ✅ **Roteamento Triple-Router** — FAST (tools), MEMORY (RAG+LLM), SMART (LangGraph)
- ✅ **MemoryRouter** — RAG + Ollama streaming sem LangGraph (target 2-5s)
- ✅ **RAG Diagnostics** — Logs detalhados: query, vector_size, scores, paths, payload keys
- ✅ **Score Threshold** — `settings.RAG_SCORE_THRESHOLD=0.3` configurável
- ✅ **Observabilidade** — Métricas de tempo (ms) em MemoryRouter, SemanticRetriever, IntentClassifier
- ✅ **Warmup** — Embedder + Ollama no lifespan do FastAPI
- ✅ **OpenAI API Compat** — Legacy routes `POST /chat/completions`, `GET /models` para Open WebUI
- ✅ **Python 3.13** — `requires-python >=3.13,<3.14`, UV managed Python

### Próximos Entregáveis (Fase 8 cont.)
- [ ] **Cache de Embeddings (SQLite)** — `hash(texto)` → vector, evitar reprocessamento
- [ ] **Config Dev/Prod** — `bge-small-en-v1.5` (dev) vs `bge-m3` (prod)
- [ ] **Qdrant HNSW Tuning** — `m=32`, `ef_construct=200` para 10k+ pontos
- [ ] **Auditoria Planner** — Validar uso de `retrieved_context` no prompt final

---

## Fase 9 — Integrações Externas ⬜

### Tecnologias
- N8N
- GitHub
- Email
- AWS

### Próximos Passos
- [ ] Subir N8N via Docker Compose
- [ ] Criar webhooks de automação
- [ ] Integrar ferramentas externas ao Tool Registry
- [ ] Webhook tool para N8N
- [ ] GitHub tool (issues, PRs)
- [ ] Email tool (send/receive)
