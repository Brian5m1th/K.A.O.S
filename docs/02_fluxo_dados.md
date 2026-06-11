Source: Notas no ClickUp
Tags: #langgraph #agente #fluxo #fastapi #proxy #openai
Related: [[index]] [[01_estrutura_pastas]] [[sdd_obsidian_memoria]]

# Fluxo de Dados e Ciclo de Vida do Agente

Esta nota documenta os dois caminhos que uma mensagem percorre: via **proxy OpenAI** (fluxo principal do Open WebUI) e via **API direta** (fluxo do LangGraph com ferramentas).

---

## Fluxo Principal — Proxy OpenAI (/v1/chat/completions)

Usado pelo Open WebUI. O FastAPI atua como um proxy compatível com a API da OpenAI, roteando via LangGraph Agent.

```mermaid
sequenceDiagram
    autonumber
    actor User as Usuário (Open WebUI)
    participant OWUI as Open WebUI
    participant PROXY as FastAPI (/v1/chat/completions)
    participant AGENT as AgentService (LangGraph)
    participant RAG as RAG Pipeline
    participant LLM as Ollama (qwen3:4b)

    User->>OWUI: Digita mensagem
    OWUI->>PROXY: POST /v1/chat/completions
    PROXY->>AGENT: stream_message(session_id, mensagem)
    AGENT->>RAG: retrieve_context (busca semântica no Qdrant)
    RAG-->>AGENT: Chunks relevantes do Vault
    AGENT->>LLM: planner + resposta (ChatOllama)
    LLM-->>AGENT: Stream de tokens
    AGENT-->>PROXY: Tokens via astream_events
    PROXY-->>OWUI: SSE stream (formato OpenAI)
    OWUI-->>User: Exibe resposta em tempo real
```

---

## Fluxo Interno — API Direta com LangGraph

Usado para requisições diretas, executando o grafo completo (RAG + tools).

```mermaid
sequenceDiagram
    autonumber
    actor User as Usuário (API)
    participant API as Controller (FastAPI)
    participant SVC as AgentService (Service)
    participant GRAPH as LangGraph Engine (Agent)
    participant LLM as Ollama Server (Local)

    User->>API: POST /api/chat/message
    API->>SVC: stream_message(session_id, prompt)
    SVC->>GRAPH: astream_events(initial_state)
    
    loop Ciclo do Grafo (LangGraph Loop)
        GRAPH->>GRAPH: retrieve_context (busca RAG no Qdrant)
        GRAPH->>LLM: planner (decide: tool ou resposta)
        LLM-->>GRAPH: Decisão
        alt Chamar Ferramenta
            GRAPH->>GRAPH: executor + tool (create, read, update, etc.)
            GRAPH->>GRAPH: Atualizar Estado
        else Responder
            GRAPH->>GRAPH: Gerar Mensagem Final
        end
    end
    
    GRAPH-->>SVC: Stream de eventos (on_chat_model_stream)
    SVC-->>API: Tokens
    API-->>User: Exibe resposta em tempo real
```

---

## Relacao com outras Notas
- [[sdd_arquitetura_orquestracao]] — SDD detalhada do proxy gateway
