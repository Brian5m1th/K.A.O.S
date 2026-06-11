Source: Notas no ClickUp
Tags: #langgraph #agente #fluxo #fastapi #proxy #openai
Related: [[index]] [[01_estrutura_pastas]] [[sdd_obsidian_memoria]] [[04_integracoes]]

# Fluxo de Dados e Ciclo de Vida do Agente

Esta nota documenta os dois caminhos que uma mensagem percorre: via **proxy OpenAI** (fluxo principal do Open WebUI) e via **API direta** (fluxo do LangGraph com ferramentas).

---

## 🟢 Fluxo Principal — Proxy OpenAI (/v1/chat/completions)

Usado pelo Open WebUI. O FastAPI atua como um proxy compatível com a API da OpenAI.

```mermaid
sequenceDiagram
    autonumber
    actor User as Usuário (Open WebUI)
    participant OWUI as Open WebUI
    participant PROXY as FastAPI (/v1/chat/completions)
    participant LLM as LLMService
    participant OLLAMA as Ollama (qwen3:4b)

    User->>OWUI: Digita mensagem
    OWUI->>PROXY: POST /v1/chat/completions
    Note over PROXY: Injeta system prompt do K.A.O.S.
    PROXY->>LLM: stream_chat(messages)
    LLM->>OLLAMA: POST /api/chat (stream)
    OLLAMA-->>LLM: Stream de tokens
    LLM-->>PROXY: Tokens
    PROXY-->>OWUI: SSE stream (formato OpenAI)
    OWUI-->>User: Exibe resposta em tempo real
```

---

## 🔵 Fluxo Interno — API Direta com LangGraph

Usado para requisições que exigem ferramentas (Obsidian, RAG, etc.)

```mermaid
sequenceDiagram
    autonumber
    actor User as Usuário (API)
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
            GRAPH->>GRAPH: Executar Tool Interna (Ex: Obsidian)
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

## 🔗 Relação com outras Notas
- [[sdd_arquitetura_orquestracao]] — SDD detalhada do proxy gateway
- [[04_integracoes]] — Ferramentas disponíveis na execução do grafo
- [[03_infraestrutura_docker]] — Detalhes de persistência das tabelas
