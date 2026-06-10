Source: Notas no ClickUp
Tags: #sdd #roadmap #ia-pessoal #obsidian #langgraph #fases
Related: [[index]] [[00_visao_geral]] [[sdd_obsidian_memoria]] [[sdd_obsidian_rag]] [[sdd_obsidian_tools]] [[sdd_obsidian_watcher]] [[estrategia_repositorios]]

# SDD — Roadmap Inicial da IA Offline com Obsidian

## Objetivo

Construir uma assistente de IA pessoal capaz de operar offline utilizando conhecimento armazenado em um Vault Obsidian e executar integrações externas através do N8N.

---

## Arquitetura Alvo

```text
Usuário
 ↓
Open WebUI
 ↓
FastAPI
 ↓
LangGraph
 ↓
Obsidian
 ↓
Qdrant
 ↓
N8N
```

---

## Fase 1 — Fundação

### Entregáveis

* Python 3.13
* FastAPI
* Docker
* Open WebUI
* Ollama
* Qwen3

### Critério de Sucesso

Usuário consegue conversar com a IA localmente.

---

## Fase 2 — Integração com Obsidian

### Entregáveis

* ObsidianService
* ReadNoteTool
* SearchNotesTool
* CreateNoteTool

### Critério de Sucesso

A IA consegue:

* Ler notas
* Criar notas
* Atualizar notas

---

## Fase 3 — Organização do Conhecimento

### Estrutura

```text
Vault/

├── Projetos
├── Arquitetura
├── SDD
├── Estudos
├── IA
├── Java
├── Python
├── AWS
├── CI-CD
└── Diário
```

### Critério de Sucesso

A IA categoriza conteúdos automaticamente.

---

## Fase 4 — Busca Semântica

### Tecnologias

* Qdrant
* Sentence Transformers

### Critério de Sucesso

A IA encontra informações por significado e não apenas por palavras-chave.

---

## Fase 5 — Atualização Automática

### Tecnologias

* Watchdog

### Critério de Sucesso

Alterações realizadas no Obsidian são automaticamente reindexadas.

---

## Fase 6 — Agentes

### Tecnologias

* LangGraph

### Critério de Sucesso

A IA escolhe ferramentas autonomamente.

---

## Fase 7 — Memória de Longo Prazo

### Funcionalidades

* Preferências
* Projetos
* Arquiteturas
* Estudos
* Conversas importantes

### Critério de Sucesso

A IA adapta respostas com base no histórico armazenado.

---

## Fase 8 — Integrações

### Tecnologias

* N8N
* GitHub
* Email
* AWS

### Critério de Sucesso

A IA executa ações reais em sistemas externos.

---

## Próximas Tarefas

- [ ] Configurar caminho do Vault
- [ ] Implementar ObsidianService
- [ ] Ler primeira nota
- [ ] Criar primeira nota
- [ ] Implementar busca textual
- [ ] Preparar integração com Qdrant

---

## Visão Final

A plataforma deverá funcionar como um sistema de memória pessoal inteligente onde:

* Obsidian armazena conhecimento.
* Qdrant armazena contexto semântico.
* LangGraph coordena agentes.
* Ollama executa modelos locais.
* N8N executa ações externas.
* Spring Boot concentra regras de negócio.
