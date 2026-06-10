Source: Notas no ClickUp
Tags: #arquitetura #clean-architecture #patterns-and-principles
Related: [[index]] [[00_visao_geral]] [[02_fluxo_dados]] [[03_infraestrutura_docker]]

# Estrutura de Diretórios e Camadas (Spring Boot Style)

Esta nota descreve a organização do código-fonte do projeto. Seguindo a filosofia de desenvolvimento corporativo, dividimos a aplicação em camadas bem definidas para isolar responsabilidades e facilitar testes automatizados.

```
ai-assistant/
├── app/
│   ├── api/          # 1. Camada Controller (FastAPI Routers)
│   ├── service/      # 2. Camada Service (Business Logic)
│   ├── repository/   # 3. Camada Repository (Data Access)
│   ├── domain/       # 4. Camada Domain (Entidades e DTOs)
│   ├── agent/        # 5. Camada Agent (LangGraph State Machine)
│   ├── tools/        # 6. Camada Tools (Ferramentas para a IA)
│   ├── rag/          # 7. Camada RAG (Embedding e Chunking)
│   ├── config/       # 8. Camada Config (Configurações e Variáveis)
│   └── main.py       # Ponto de Entrada da API
└── docs/             # Documentação do Vault Obsidian
```

---

## 🏢 Detalhamento das Camadas

### 1. API (Controllers)
Os arquivos em `app/api/` são os pontos de entrada HTTP/WebSocket.
- **Responsabilidade**: Expor endpoints, gerenciar CORS, lidar com status HTTP e autenticação leve.
- **Arquivos principais**:
  - `chat.py`: Streaming de respostas via SSE (Server-Sent Events) ou WebSockets.
  - `tools.py`: Endpoints para gerenciar/testar o status das ferramentas.
  - `health.py`: Liveness/Readiness probes para monitoramento local.

### 2. Service (Business Logic)
Os arquivos em `app/service/` realizam a orquestração e contêm as regras de negócio puras.
- **Responsabilidade**: Coordenar a lógica entre Repositories, RAG e a execução do LangGraph.
- **Arquivos principais**:
  - `agent_service.py`: Inicializa o grafo do agente por thread de chat e envia os inputs.
  - `rag_service.py`: Orquestra a busca vetorial e injeção de contexto.
  - `obsidian_sync.py`: Controla o pipeline de leitura e indexação das notas.

### 3. Repository (Data Access)
Os arquivos em `app/repository/` isolam o acesso a qualquer banco ou serviço de armazenamento de dados.
- **Responsabilidade**: Traduzir chamadas do Service em queries SQL ou buscas vetoriais.
- **Arquivos principais**:
  - `pg_repository.py`: Interface SQLModel para salvar histórico de conversas e estado no PostgreSQL.
  - `vector_store.py`: Interface para buscar por similaridade e payload filtering no Qdrant.

### 4. Domain (Modelos e DTOs)
Os arquivos em `app/domain/` contêm os modelos de dados reutilizáveis da aplicação.
- **Responsabilidade**: Validar dados usando Pydantic v2.
- **Arquivos principais**:
  - `chat.py`: Modelos como `ChatMessageRequest`, `ChatSession` e `AgentResponse`.
  - `document.py`: Modelos como `DocumentChunk` e `FileMetadata`.

### 5. Agent (LangGraph)
Os arquivos em `app/agent/` implementam a máquina de estado inteligente da IA.
- **Responsabilidade**: Definir o Grafo do Agente, transições de nós, loops de pensamento e execução de ferramentas.
- **Arquivos principais**:
  - `state.py`: O `TypedDict` que representa o estado persistente do fluxo.
  - `graph.py`: A estrutura ligando nós (nodes) e arestas condicionais (conditional edges).

### 6. Tools
Os arquivos em `app/tools/` disponibilizam capacidades externas para o agente.
- **Responsabilidade**: Formatar as funções como ferramentas compatíveis com Langchain/Langgraph.
- **Arquivos principais**:
  - `github_tool.py`: Operações de git local ou API.
  - `docker_tool.py`: Monitoramento local de containers.
  - `n8n_tool.py`: Disparo de webhooks de automação.

---

## 🔗 Relação com outras Notas
- Para ver como os dados passam por essas camadas, consulte [[02_fluxo_dados]].
- Para ver a infraestrutura necessária para suportar esses bancos, consulte [[03_infraestrutura_docker]].
