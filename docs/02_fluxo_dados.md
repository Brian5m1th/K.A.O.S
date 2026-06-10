Source: Notas no ClickUp
Tags: #langgraph #agente #fluxo #fastapi
Related: [[index]] [[01_estrutura_pastas]] [[sdd_obsidian_memoria]] [[04_integracoes]]

# Fluxo de Dados e Ciclo de Vida do Agente

Esta nota documenta o caminho que uma mensagem percorre desde o envio pelo usuário (no Open WebUI) até a geração da resposta enriquecida, passando pelo LangGraph, RAG e execução de ferramentas.

---

## 🔄 Fluxo de Requisição de Chat

```mermaid
sequenceDiagram
    autonumber
    actor User as Usuário (Open WebUI)
    participant API as Controller (FastAPI)
    participant SVC as AgentService (Service)
    participant RAG as RagService (Service)
    participant DB as PostgresRepo (Repository)
    participant GRAPH as LangGraph Engine (Agent)
    participant LLM as Ollama Server (Local)

    User->>API: POST /api/chat/message (DTO)
    API->>SVC: process_message(session_id, prompt)
    SVC->>DB: Recuperar histórico de chat & estado anterior
    SVC->>RAG: search_relevant_context(prompt)
    RAG-->>SVC: Retorna Chunks Relevantes (Obsidian)
    SVC->>GRAPH: Inicializar Grafo com (Estado + Contexto + Histórico)
    
    loop Ciclo do Grafo (LangGraph Loop)
        GRAPH->>LLM: Analisar Estado + Decidir Ação (Tool Call ou Responder)
        LLM-->>GRAPH: Decisão (Chamar ferramenta X ou gerar resposta final)
        alt Chamar Ferramenta
            GRAPH->>GRAPH: Executar Tool Interna (Ex: Docker/N8N)
            GRAPH->>GRAPH: Atualizar Estado com Resultado da Tool
        else Responder
            GRAPH->>GRAPH: Gerar Mensagem Final
        end
    end
    
    GRAPH-->>SVC: Retorna Resposta Final e Novo Estado
    SVC->>DB: Salvar nova mensagem & estado atualizado
    SVC-->>API: Envia stream da resposta
    API-->>User: Exibe resposta em tempo real
```

---

## 🧠 Ciclo de Vida do Grafo do Agente (LangGraph)

O Grafo do Agente é estruturado para tomar decisões dinâmicas baseadas em loops de feedback.

```mermaid
stateDiagram-v2
    [*] --> START
    START --> RETRIEVE_CONTEXT : Injetar contexto RAG do Obsidian
    RETRIEVE_CONTEXT --> CALL_PLANNER : Invocar Planner (LLM)
    
    state CALL_PLANNER {
        [*] --> AnalisarObjetivo
        AnalisarObjetivo --> DecidirAcao
    }
    
    CALL_PLANNER --> EXECUTE_TOOLS : Decidiu usar Ferramentas
    CALL_PLANNER --> GENERATE_RESPONSE : Contexto suficiente para responder
    
    state EXECUTE_TOOLS {
        [*] --> ExecutarTool
        ExecutarTool --> GravarResultadoNoEstado
    }
    
    EXECUTE_TOOLS --> CALL_PLANNER : Retornar resultado e planejar próximo passo
    
    GENERATE_RESPONSE --> WRITE_TO_HISTORY : Persistir interação
    WRITE_TO_HISTORY --> [*]
```

### Nós do Grafo (Nodes)

1. **`retrieve_context`**: Consulta o `VectorStoreRepository` no Qdrant para puxar notas recentes do Obsidian vinculadas ao tema da conversa.
2. **`planner`**: O LLM local processa o input do usuário juntamente com o contexto recuperado. Avalia se precisa rodar alguma ferramenta (como pesquisar arquivos locais, disparar automação no N8N, ou executar comandos docker).
3. **`execute_tools`**: Roda a ferramenta selecionada de forma isolada, coletando os retornos e armazenando de forma estruturada no `State`.
4. **`generate`**: Finaliza o raciocínio montando a resposta final em formato amigável (markdown).

---

## 🔗 Relação com outras Notas
- Para entender as ferramentas disponíveis na execução do grafo, veja [[04_integracoes]].
- Para ver os detalhes de persistência das tabelas do Postgres e Qdrant, acesse [[03_infraestrutura_docker]].
