Source: Notas no ClickUp
Tags: #ia-pessoal #arquitetura #stack #monorepo
Related: [[index]] [[01_estrutura_pastas]] [[02_fluxo_dados]]

# Visão Geral do Assistente de IA Local

Esta é a documentação arquitetural do K.A.O.S. (Knowledge Assistant & Offline System), um ecossistema de agentes inteligentes rodando localmente.

## 🛠️ Stack Tecnológica

| Componente | Tecnologia | Papel |
| :--- | :--- | :--- |
| **Linguagem** | Python 3.13 | Base do desenvolvimento com tipagem forte. |
| **Gerenciador** | `uv` | Gerenciamento ultrarrápido de dependências. |
| **Framework Web** | FastAPI | APIs REST e proxy OpenAI-compatível. |
| **Agentes** | LangGraph | Orquestrador de fluxos agentivos com estado. |
| **Vector DB** | Qdrant | Embeddings e busca RAG. |
| **Metadata DB** | PostgreSQL | Histórico de chat, threads e metadados. |
| **LLM Local** | Ollama + Qwen3:4b | Inferência local CPU-only. |
| **Frontend Web** | Open WebUI | Interface conectada ao FastAPI via proxy OpenAI. |
| **Desktop App** | Tauri v2 + React | Launcher nativo (Win/Mac/Linux) com provider selection e auto-update. |
| **Automação** | N8N | Webhooks e integrações com serviços externos. |

---

## 🗺️ Monorepo — Estrutura de Pacotes

```
K.A.O.S/
├── assistant/           # Aplicação principal (Python)
│   ├── app/             # FastAPI + LangGraph + RAG
│   ├── tests/           # Testes unitários e de integração
│   ├── Dockerfile       # Multi-stage, Python 3.13-slim, torch CPU-only
│   └── .env.example     # Template de configuração
├── desktop/             # Desktop launcher (Tauri v2 + React)
│   ├── src/             # Frontend React (ProviderScreen, Chat, VaultConfig)
│   └── src-tauri/       # Rust backend (check_server, check_ollama, updater)
├── docs/                # Documentação (Obsidian vault)
├── infra/               # Infraestrutura (Docker Compose)
└── .github/workflows/   # CI/CD: ci.yml, desktop-ci.yml, release.yml
```

---

## 🔗 Fluxo de Requisição (Open WebUI → FastAPI → Ollama)

O Open WebUI **não** fala diretamente com o Ollama. Todas as requisições passam pelo FastAPI:

```
Open WebUI → FastAPI /v1/chat/completions → LLMService → Ollama
```

O FastAPI injeta o **system prompt do K.A.O.S.** em toda requisição e faz streaming da resposta.

---

## 🎯 Diretrizes de Projeto

1. **Design Orientado a Domínio**: Camadas inspiradas em Spring Boot para facilitar manutenção.
2. **Execução Local**: Tudo roda localmente, sem dependências externas obrigatórias.
3. **Tipagem e Pydantic**: Pydantic v2 para validação e Type Hints obrigatórios.
