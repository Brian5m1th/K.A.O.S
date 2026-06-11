# SDD — Identidade K.A.O.S & Estratégia Monorepo

**Atenção (Open Code Context)**: Este documento serve como declaração oficial da identidade do projeto e da estratégia estrutural do repositório. Ele deve ser utilizado como base de contexto para qualquer geração de código ou planejamento futuro.

---

## 1. Identidade do Projeto

*   **Nome Oficial**: K.A.O.S (anteriormente referido como "Assistente de IA Pessoal" ou "Assistente de IA Local").
*   **Identidade do Agente**: Sempre que houver um System Prompt, interação textual ou configuração, o agente deve assumir a identidade do **K.A.O.S**.
*   **Nomenclatura de Componentes Base**:
    *   `kaos-platform` (Nome global da plataforma/monorepo)
    *   `kaos-assistant` (Serviço Python/FastAPI/LangGraph)
    *   `kaos-backend` (Serviço Java/Spring Boot para regras de negócio)
    *   `kaos-infra` (Serviço de infraestrutura, Docker Compose, N8N, bancos de dados)

---

## 2. Estratégia de Repositório (Fase Atual: MVP)

Durante a fase de MVP e construção inicial, a estratégia adotada será estritamente de **Monorepo**.

A estrutura oficial no root do projeto deverá ser gerenciada dentro do monorepo `kaos-platform/`, contendo a seguinte árvore de diretórios raiz:

```text
kaos-platform/
├── assistant/     # Código do K.A.O.S (Python 3.13, FastAPI, LangGraph, RAG)
├── backend/       # Código de negócio estrito (Java, Spring Boot)
├── infra/         # Orquestração e dependências (Docker Compose, configurações do N8N)
└── docs/          # Documentação centralizada (SDDs e Notas exportáveis para o Vault Obsidian)
```

**Diretrizes de Desenvolvimento no Monorepo:**
1.  **Isolamento**: Os componentes (`assistant`, `backend`, `infra`) não devem compartilhar código diretamente na raiz. Cada pasta opera como um subprojeto isolado.
2.  **Facilidade Operacional**: Scripts globais e orquestração do `docker-compose.yml` base podem residir na raiz ou na pasta `infra/` para subir a plataforma inteira via `docker compose up -d`.
3.  **Portabilidade**: A infraestrutura respeita o SDD de Arquitetura Portável (WSL2 + Docker), sem dependências nativas ao host Windows.

---

## 3. Diretrizes Arquiteturais do K.A.O.S

1.  **Memória Principal**: Obsidian Vault via acesso filesystem e RAG (Qdrant).
2.  **Inteligência e Orquestração**: LangGraph + Ollama (`qwen3:4b`).
3.  **Execução Externa**: Toda automação e integrações com o mundo online (ex: GitHub, Email) serão passadas para o **N8N** via webhooks.
4.  **Regras de Negócio**: Qualquer regra estrita e controle transacional persistente no PostgreSQL deverá ser alocado no módulo **Spring Boot**, evitando poluição no Python do K.A.O.S.
