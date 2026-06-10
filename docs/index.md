Source: Antigravity AI
Tags: #ia-pessoal #arquitetura #index
Related: [[00_visao_geral]] [[Arquitetura da IA Pessoal Offline]]

# 🤖 Assistente de IA Pessoal Offline — Índice Central

> Hub de navegação do vault. Todos os nós do Graph View passam por aqui.

---

## 🎯 Ponto de Partida

- [[Objetivo  da IA Pessoal Offline|Objetivo do Projeto]]
- [[Arquitetura da IA Pessoal Offline|Visão da Arquitetura (alto nível)]]
- [[00_visao_geral|Visão Geral Técnica (Stack e Mapa)]]

---

## 📐 Documentação Arquitetural

| Nota | Conteúdo |
| :--- | :--- |
| [[00_visao_geral\|00 — Visão Geral]] | Stack tecnológica e mapa da documentação |
| [[01_estrutura_pastas\|01 — Estrutura de Pastas]] | Camadas do projeto (Spring Boot Style) |
| [[02_fluxo_dados\|02 — Fluxo de Dados]] | Ciclo de vida da requisição e grafo LangGraph |
| [[03_infraestrutura_docker\|03 — Infraestrutura Docker]] | Docker Compose, serviços e variáveis de ambiente |
| [[04_integracoes\|04 — Integrações Obsidian & N8N]] | Webhooks, automações e sincronização |

---

## 🧠 SDDs — System Design Documents

| Nota | Componente |
| :--- | :--- |
| [[sdd_obsidian_memoria\|SDD — Sistema de Memória]] | Arquitetura geral da memória com Obsidian |
| [[sdd_obsidian_watcher\|SDD — File Watcher & Indexer]] | Monitoramento do vault e pipeline de indexação |
| [[sdd_obsidian_rag\|SDD — Vector Search & RAG]] | Embeddings, Qdrant e recuperação semântica |
| [[sdd_obsidian_tools\|SDD — Schemas das Ferramentas]] | Tools do LangGraph para manipular notas |

---

## 🔗 Mapa de Dependências entre Componentes

```mermaid
graph TD
    IDX([🗂️ index])

    IDX --> OBJ[[Objetivo  da IA Pessoal Offline]]
    IDX --> ARQ[[Arquitetura da IA Pessoal Offline]]
    IDX --> VG[[00_visao_geral]]
    IDX --> EP[[01_estrutura_pastas]]
    IDX --> FD[[02_fluxo_dados]]
    IDX --> INF[[03_infraestrutura_docker]]
    IDX --> INT[[04_integracoes]]
    IDX --> MEM[[sdd_obsidian_memoria]]

    MEM --> WAT[[sdd_obsidian_watcher]]
    MEM --> RAG[[sdd_obsidian_rag]]
    MEM --> TOOLS[[sdd_obsidian_tools]]

    WAT --> RAG
    RAG --> TOOLS
    TOOLS --> WAT

    VG --> EP
    VG --> FD
    VG --> INF
    VG --> INT

    EP --> FD
    EP --> INF
    FD --> INT
    FD --> INF
```

---

## ✅ TODOs e Próximos Passos

- [ ] **[[03_infraestrutura_docker]]** — Detalhar Docker Compose (PostgreSQL, Qdrant, FastAPI, Open WebUI)
- [ ] **[[04_integracoes]]** — Documentar integração N8N webhooks e watcher do Obsidian
- [ ] Implementar `app/agent/graph.py` — Grafo LangGraph com nós definidos em [[02_fluxo_dados]]
- [ ] Implementar `app/tools/` — Ferramentas definidas em [[sdd_obsidian_tools]]
- [ ] Implementar `app/rag/` — Pipeline RAG definido em [[sdd_obsidian_rag]]
- [ ] Implementar `app/repository/vector_store.py` — Interface Qdrant
- [ ] Configurar File Watcher conforme [[sdd_obsidian_watcher]]
- [ ] Configurar modelos de embedding no Ollama (`bge-m3`)

---

*Gerado automaticamente — navegue pelo Graph View (`Ctrl+G`) para visualizar as conexões.*
