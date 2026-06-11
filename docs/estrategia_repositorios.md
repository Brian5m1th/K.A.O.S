Source: Notas no ClickUp
Tags: #arquitetura #github #monorepo #multi-repo #patterns-and-principles
Related: [[index]] [[00_visao_geral]] [[01_estrutura_pastas]] [[sdd_roadmap]]

# Estratégia de Repositórios da Plataforma de IA

## Objetivo

Definir a estratégia de organização dos repositórios GitHub para suportar a evolução da plataforma de IA pessoal baseada em Python, Obsidian, RAG, Spring Boot e N8N.

---

## Contexto

A plataforma será composta por múltiplos componentes com responsabilidades distintas:

* Inteligência Artificial
* Regras de negócio
* Infraestrutura
* Memória baseada em Obsidian
* Integrações externas

Para evitar acoplamento excessivo e facilitar a manutenção, a arquitetura deverá ser organizada em repositórios especializados.

---

## Estratégia Inicial

Durante o MVP será utilizado um **Monorepo**.

Estrutura:

```text
kaos-platform/

├── assistant/
├── backend/
├── infra/
└── docs/
```

### Benefícios

* Menor complexidade operacional
* CI/CD simplificado
* Desenvolvimento mais rápido
* Facilidade de refatoração

---

## Evolução para Multi-Repositório

Quando o projeto atingir maturidade suficiente, a estrutura deverá ser separada.

### Repositório 1 — kaos-assistant

Responsabilidade:

* FastAPI
* LangGraph
* Ollama
* Obsidian Integration
* RAG
* Qdrant Integration
* Agent Tools

Estrutura:

```text
kaos-assistant/

├── app/
├── agent/
├── rag/
├── obsidian/
├── api/
├── tests/
└── docker/
```

---

### Repositório 2 — kaos-backend

Responsabilidade:

* Regras de negócio
* APIs REST
* Persistência
* Segurança
* Eventos

Tecnologias:

* Java 21
* Spring Boot
* PostgreSQL

Estrutura:

```text
kaos-backend/

├── domain/
├── application/
├── infrastructure/
├── api/
└── tests/
```

---

### Repositório 3 — kaos-infra

Responsabilidade:

* Docker Compose
* N8N
* PostgreSQL
* Qdrant
* Observabilidade

Estrutura:

```text
kaos-infra/

├── docker/
├── postgres/
├── qdrant/
├── n8n/
├── monitoring/
└── docs/
```

---

## Fluxo de Comunicação

```text
Usuário
 ↓
K.A.O.S
 ↓
Spring Boot API
 ↓
Banco de Dados

K.A.O.S
 ↓
N8N
 ↓
Serviços Externos
```

---

## Diretrizes

* Nenhuma regra de negócio deve existir na IA.
* Toda persistência deve ser centralizada no Backend.
* Integrações externas devem ser delegadas ao N8N sempre que possível.
* O Obsidian será a memória principal da IA.
* O Qdrant será a memória vetorial.

---

## Resultado Esperado

Separação clara entre:

* Inteligência
* Negócio
* Infraestrutura

Permitindo evolução independente de cada componente.
