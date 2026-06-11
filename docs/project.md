# Projeto — K.A.O.S

> Knowledge AI Operating System — Assistente pessoal offline com IA local.

---

## Qualidade (Quality Attributes)

| Atributo | Prioridade | Estratégia |
|:---------|:-----------|:-----------|
| Privacidade | 🔴 Crítica | 100% offline, modelos locais, sem telemetria |
| Baixa Latência | 🟡 Alta | Streaming, cache de embeddings, lazy loading |
| Modularidade | 🟡 Alta | Camadas isoladas (RAG, Agente, Obsidian, API) |
| Simplicidade | 🟢 Média | Mínimo de abstrações, código direto |
| Testabilidade | 🟢 Média | Testes unitários, fixtures locais sem rede |

---

## Active Initiatives

| Iniciativa | Status | Relacionado |
|:-----------|:-------|:------------|
| P12 Logging Pattern | ✅ Feito | `docs/patterns.md` |
| ListNotesTool | ⬜ Pendente | Fase 3 |
| LangGraph + OpenAI Proxy | 🟡 Em andamento | Fase 7 |
| Streaming real | ⬜ Pendente | Fase 7 |
| Vault folder structure | ⬜ Pendente | Fase 4 |
| RAG testing | ⬜ Pendente | Fase 5 |
| Long-term memory | ⬜ Pendente | Fase 8 |

---

## Branching Strategy

```
main              → estável, releases
├── feature/*     → novas funcionalidades (um branch por passo do backlog)
├── fix/*         → correções de bugs
└── refactor/*    → refatorações sem mudança funcional
```

**Convenções:**
- `feature/logging-marker-standard` — implementar padrão de logs
- `feature/list-notes-tool` — implementar ListNotesTool
- `fix/openai-proxy-streaming` — corrigir streaming
- `refactor/agent-service` — refatorar AgentService

---

## Stack

| Camada | Tecnologia |
|:-------|:-----------|
| Runtime | Python 3.13 |
| Framework | FastAPI |
| LLM | Ollama (Qwen3 4B) |
| Vector DB | Qdrant |
| Agente | LangGraph + LangChain |
| Embeddings | sentence-transformers (BGE-M3) |
| Logs | loguru |
| Watcher | watchdog |
