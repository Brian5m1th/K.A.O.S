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
| 9 | Integrações Online | 6 | ⬜ Aguardando |
| 10 | Produção | 6 | ⬜ Aguardando |
| 11 | Otimização e Roteamento | 8 | 🔵 Pendente |

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
    F10 --> F11
```

---

---

## Próximas Tarefas Prioritárias

- [ ] **Auditoria RAG**: Executar `/indexing/full`, validar Qdrant, logs do retriever, teste "O que existe na nota Backlog?"
- [ ] Implementar Intent Classifier (FAST/MEMORY/SMART)
- [ ] Implementar FastRouter (execução direta de tools sem LLM)
- [ ] Criar Dockerfile para o K.A.O.S (`assistant/`)

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

## Fase 3 — Integração com Obsidian

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

Pastas a criar:

- [ ] `Projetos/` — status e escopo de projetos ativos
- [ ] `Arquitetura/` — decisões e padrões arquiteturais
- [ ] `SDD/` — System Design Documents
- [ ] `Estudos/` — resumos de aprendizado
- [ ] `IA/` — prompts, modelos e experimentos
- [ ] `Python/` — padrões, libs e tutoriais Python
- [ ] `Java/` — ecossistema Java e Spring Boot
- [ ] `AWS/` — infraestrutura e comandos AWS
- [ ] `CI-CD/` — pipelines e automações de deploy
- [ ] `Diário/` — registros diários e resumos de reuniões
- [ ] `Inbox/` — ponto de entrada para notas sem categorização

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

## Fase 9 — Integrações Online

- [ ] Subir N8N via Docker Compose
- [ ] Criar integração via Webhook (N8N recebe e envia eventos ao FastAPI)
- [ ] Integrar GitHub (consulta de repositórios e código)
- [ ] Integrar Email (leitura e triagem de mensagens)
- [ ] Integrar WhatsApp (via N8N + Evolution API)
- [ ] Integrar AWS (comandos CLI e monitoramento)

---

## Fase 10 — Produção

- [ ] Configurar autenticação (JWT ou API Key no FastAPI)
- [ ] Configurar backups automáticos do Vault (script + cron)
- [ ] Configurar monitoramento (Prometheus + Grafana ou Loki)
- [ ] Configurar CI/CD (GitHub Actions para lint, tests e build)
- [ ] Criar documentação técnica (`docs/README_tecnico.md`)
- [ ] Criar documentação de instalação (`docs/INSTALL.md`)

---

---

## Fase 11 — Otimização de Performance e Roteamento Inteligente

- [ ] Criar `IntentClassifier` com fast path (keyword match) + LLM fallback (Qwen3 4B)
- [ ] Criar `FastRouter` — execução direta de tools (sem LLM, sem RAG, sem LangGraph)
- [ ] Criar `MemoryRouter` — RAG + LLM sem LangGraph
- [ ] Criar `SmartRouter` — LangGraph completo (wrapping AgentService)
- [ ] Criar `ResponseCache` — cache de respostas frequentes com TTL
- [ ] Integrar roteamento em `chat.py` e `openai.py`
- [ ] Criar `ListProjectsTool` e registrar no TOOL_REGISTRY
- [ ] Adicionar suporte a modelo rápido (Qwen3 4B) vs principal (`settings.py`)

---

## Divida Tecnica (DEBT)

- [x] Corrigir patch target em `tests/test_openai.py` (mira `app.api.openai_compat` ao inves de `app.api.openai`)
- [x] Substituir streaming fake do AgentService por streaming real do LangGraph
- [x] Remover bypass do LangGraph no proxy OpenAI (`/v1/chat/completions` conecta direto no Ollama)
- [ ] Adicionar `ruff` como dependencia de dev para lint
- [ ] Adicionar `.env.example` ao repositorio
- [ ] **Auditoria RAG**: Executar indexação inicial (`POST /indexing/full`), validar `points_count > 0`, adicionar logs de `retrieve_context` com query + contagem, teste manual "O que existe na nota Backlog?"
- [ ] **Dockerfile**: Criar `Dockerfile` para `assistant/` com volume mount do Vault (`/vault`) e `.env` configurável
- [ ] **Setup guide**: Documentar modos de execução (Windows nativo, WSL, Docker) com `.env` próprio para cada ambiente

---

## Ideias (IDEA)

- [ ] Auto-tagging de notas baseado em embeddings
- [ ] Sugestao de conexoes entre notas (grafos)
- [ ] Dashboard web para visualizar status do sistema
- [ ] Exportacao de conversas para markdown

---

*Atualizado em 2026-06-11.*
