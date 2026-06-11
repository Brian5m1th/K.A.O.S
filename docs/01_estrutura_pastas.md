Source: Notas no ClickUp
Tags: #arquitetura #clean-architecture #patterns-and-principles
Related: [[index]] [[00_visao_geral]] [[02_fluxo_dados]]

# Estrutura de Diretórios e Camadas

Esta nota descreve a organização do código-fonte do projeto K.A.O.S. Dividimos a aplicação em camadas bem definidas para isolar responsabilidades e facilitar testes automatizados.

```
K.A.O.S/
├── assistant/       # Serviço Python (FastAPI, LangGraph, RAG)
│   ├── app/
│   │   ├── api/          # 1. Camada Controller (FastAPI Routers)
│   │   ├── service/      # 2. Camada Service (Business Logic)
│   │   ├── domain/       # 3. Camada Domain (Entidades e DTOs)
│   │   ├── agent/        # 4. Camada Agent (LangGraph State Machine)
│   │   ├── obsidian/     # 5. Camada Obsidian (Tools + Services + Watcher)
│   │   ├── rag/          # 6. Camada RAG (Embedding, Chunking, Indexer, Retriever)
│   │   ├── memory/       # 7. Camada Memory (Memória de Longo Prazo)
│   │   ├── config/       # 8. Camada Config (Configurações e Variáveis)
│   │   └── main.py       # Ponto de Entrada da API
│   └── tests/            # Testes unitários e de integração
├── backend/         # Placeholder para futuro Spring Boot
├── infra/           # Docker Compose e infraestrutura
└── docs/            # Documentação do Vault Obsidian
```

---

## Detalhamento das Camadas

### 1. API (Controllers)
Os arquivos em `app/api/` são os pontos de entrada HTTP.
- **Responsabilidade**: Expor endpoints, gerenciar CORS, lidar com status HTTP.
- **Arquivos principais**:
  - `chat.py`: Streaming de respostas via SSE (AgentService).
  - `openai.py`: Proxy compatível com OpenAI (para Open WebUI).
  - `health.py`: Liveness/Readiness probes.
  - `indexing.py`: Reindexação completa e init de pastas.
  - `rag.py`: Busca de contexto RAG.

### 2. Service (Business Logic)
Os arquivos em `app/service/` realizam a orquestração.
- **Responsabilidade**: Coordenar a lógica entre RAG, LangGraph e LLM.
- **Arquivos principais**:
  - `agent_service.py`: Inicializa o grafo do agente e gerencia sessões.
  - `llm_service.py`: Comunicação direta com Ollama.

### 3. Domain (Modelos e DTOs)
Os arquivos em `app/domain/` contêm os modelos de dados reutilizáveis.
- **Arquivos principais**:
  - `chat.py`: Modelos `Message`, `ChatRequest`, `ChatResponse`.
  - `document.py`: Modelos `NoteReadResult`, `SearchResult`, `NoteResponse`.

### 4. Agent (LangGraph)
Os arquivos em `app/agent/` implementam a máquina de estado inteligente.
- **Responsabilidade**: Definir o Grafo do Agente, transições de nós, loops de pensamento e execução de ferramentas.
- **Arquivos principais**:
  - `state.py`: TypedDict que representa o estado persistente do fluxo.
  - `graph.py`: A estrutura ligando nós (retrieve, planner, executor) e arestas condicionais.
  - `nodes/retrieve.py`: Nó de recuperação RAG.
  - `nodes/planner.py`: Nó LLM que decide ação.
  - `nodes/executor.py`: Nó de execução de ferramentas.

### 5. Obsidian
Os arquivos em `app/obsidian/` integram o Vault Obsidian ao agente.
- **Responsabilidade**: CRUD de notas, watcher de alterações, inicialização de pastas.
- **Arquivos principais**:
  - `services/obsidian_service.py`: Serviço de acesso ao filesystem do vault.
  - `tools/`: 7 ferramentas LangChain (create, read, update, delete, search, list, save_conversation).
  - `watcher/vault_watcher.py`: Monitoramento do vault com watchdog.
  - `vault_init.py`: Criação da estrutura padrão de pastas.

### 6. RAG
Os arquivos em `app/rag/` implementam o pipeline de busca semântica.
- **Arquivos principais**:
  - `embeddings/embedder.py`: Sentence Transformers (BGE-M3).
  - `chunking/text_splitter.py`: Splitter Markdown com overlap.
  - `indexer/vault_indexer.py`: Indexação no Qdrant.
  - `retriever/semantic_retriever.py`: Busca semântica.

### 7. Memory
Os arquivos em `app/memory/` gerenciam memória de longo prazo.
- **Arquivos principais**:
  - `memory_service.py`: Salva conversas, preferências e recupera histórico.

### 8. Config
Os arquivos em `app/config/` centralizam configurações.
- **Arquivos principais**:
  - `settings.py`: Pydantic Settings a partir do `.env`.
  - `prompts.py`: System prompt do K.A.O.S.

---

## Relacao com outras Notas
- Para ver como os dados passam por essas camadas, consulte [[02_fluxo_dados]].
- Para detalhes sobre cada componente, veja os SDDs em [[index]].
