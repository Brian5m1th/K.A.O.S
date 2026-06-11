Source: K.A.O.S Project
Tags: #sdd #roadmap #fases
Related: [[index]] [[00_visao_geral]] [[backlog]]

# SDD — Roadmap do K.A.O.S

## Objetivo

Construir uma assistente de IA pessoal capaz de operar offline utilizando conhecimento armazenado em um Vault Obsidian e executar integracoes externas atraves do N8N.

---

## Arquitetura Alvo

```text
Open WebUI
  ↓
FastAPI (proxy OpenAI + LangGraph)
  ↓
LangGraph (orquestrador)
  ↓
Obsidian (memoria) ←→ Qdrant (RAG)
  ↓
N8N (automacao externa)
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

## Fase 8 — User Context & Multiusuário 🟡 Em Andamento

### Entregaveis
- UserContext model (user_id, username, role)
- MemoryService com escopo por usuário (`Vault/users/{user_id}/`)
- AgentState com user context
- save_conversation tool com user_id
- Logs com identificação de usuário
- MemoryRepository protocol (preparação PostgreSQL)

### Proximos Passos
- Integrar com Open WebUI Groups
- Compartilhamento de conhecimento entre usuários
- RBAC avancado

---

## Fase 9 — Integracoes ⬜

### Tecnologias
- N8N
- GitHub
- Email
- AWS

### Proximos Passos
- Subir N8N via Docker Compose
- Criar webhooks de automacao
- Integrar ferramentas externas ao Tool Registry
