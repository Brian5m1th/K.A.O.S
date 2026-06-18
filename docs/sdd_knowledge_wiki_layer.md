Source: LLM Wiki Pattern + K.A.O.S SDD-009
Tags: #sdd #wiki #knowledge #llm-wiki #rag #synthesis
Related: [[index]] [[00_visao_geral]] [[sdd_llm_provider_hybrid]] [[02_fluxo_dados]]

# SDD — Knowledge Wiki Layer (LLM Wiki + RAG Híbrido)

## Objetivo

Transformar o K.A.O.S de um sistema RAG passivo (chunk → embed → retrieve → LLM) para um **Sistema Operacional de Conhecimento** onde o LLM incrementalmente constrói e mantém uma wiki persistente, estruturada e interligada.

---

## Problema Atual

O sistema atual opera como RAG tradicional:

```
Obsidian Vault
    ↓
MarkdownSplitter (chunking)
    ↓
Embedder (BGE-M3 / nomic)
    ↓
Qdrant (vector store)
    ↓
SemanticRetriever (top-5)
    ↓
LLM (Qwen3)
```

**Problemas:**
- Conhecimento é rederivado a cada consulta — nada se acumula
- Não existem entidades persistentes (pessoas, projetos, tecnologias)
- Não existem conceitos consolidados (RAG, embeddings, LangGraph)
- Não existe síntese incremental — análises e comparações somem no chat
- Cross-references entre documentos são perdidas
- O LLM rediscover knowledge do zero em cada pergunta

---

## Arquitetura Alvo

```
RAW SOURCES (imutáveis)
  ├── Conversas
  ├── PDFs, Artigos
  ├── Web Clips
  ├── Notas avulsas
        ↓
INGESTION AGENT (LangGraph node)
  ├── Lê fonte completa
  ├── Extrai entidades e conceitos
  ├── Cria/atualiza páginas wiki
  ├── Atualiza index.md e log.md
  └── (Opcional) Reindexa no Qdrant
        ↓
KNOWLEDGE WIKI (estruturada, interligada)
  ├── index.md (catálogo navegável)
  ├── log.md (timeline append-only)
  ├── entities/ (Pessoa, Projeto, Tecnologia)
  ├── concepts/ (RAG, LangGraph, Embeddings)
  ├── sources/ (resumo de cada fonte)
  └── synthesis/ (análises, comparações, teses)
        ↓
QUERY PIPELINE (wiki-first, Qdrant-second)
  ├── 1. Consulta index.md
  ├── 2. Lê entities/concepts relevantes
  ├── 3. Qdrant como fallback semântico
  └── 4. LLM sintetiza com citações
        ↓
EMBEDDINGS → QDRANT → LLM
```

---

## Estrutura do Vault

```
{vault}/
├── raw/                          # Fontes imutáveis (somente leitura)
│   ├── artigo_mamba2.md
│   ├── podcast_transcricao.md
│   └── assets/                   # Imagens baixadas
│
└── wiki/                         # Conhecimento sintetizado
    ├── AGENTS.md                 # Schema — o LLM consulta antes de agir
    ├── AGENTS.pt-BR.md           # Versão em português
    ├── index.md                  # Catálogo vivo de todas as páginas
    ├── log.md                    # Timeline append-only
    │
    ├── entities/                 # Objetos concretos
    │   ├── brian.md
    │   ├── kaos.md
    │   └── qdrant.md
    │
    ├── concepts/                 # Abstrações
    │   ├── rag.md
    │   ├── embeddings.md
    │   └── langgraph.md
    │
    ├── sources/                  # Resumo de cada fonte ingerida
    │   └── 2026-06-18_artigo_llm_wiki.md
    │
    └── synthesis/                # Conhecimento derivado
        ├── comparacao_mamba_vs_rwkv.md
        └── arquitetura_rag_hibrido.md
```

---

## Frontmatter Obrigatório

Toda página wiki DEVE conter:

```yaml
---
title: Nome da Página
type: entity | concept | source | synthesis
tags:
  - tag1
  - tag2
sources:
  - source_file_name
created: 2026-06-18
updated: 2026-06-18
---
```

O campo `updated` é atualizado automaticamente pelas tools de escrita.

---

## AGENTS.md — Schema Vivo

Arquivo que define as convenções e workflows que o LLM deve seguir.

### Conteúdo principal:

1. **Convenções de nomenclatura**: `entities/{kebab-case}.md`, `concepts/{kebab-case}.md`
2. **Frontmatter obrigatório** (schema YAML acima)
3. **Workflow de ingest**: ler fonte → discutir com usuário → criar source page → extrair entidades/conceitos → atualizar index.md → append log.md
4. **Workflow de query**: ler index.md → encontrar páginas relevantes → ler páginas → sintetizar com citações
5. **Regras de Draft Mode**: toda alteração proposta primeiro como `.draft.md`, aguarda aprovação
6. **Regras de cross-reference**: entidades mencionadas devem ter backlinks; conceitos mencionados 3+ vezes merecem página própria

---

## Draft Mode

Mecanismo de segurança para evitar corrupção automática do conhecimento.

### Fluxo

```
Usuário: "ingira este source sobre Mamba"
    ↓
LLM cria: entities/mamba.draft.md, concepts/ssm.draft.md
    ↓
Usuário revisa os drafts
    ↓
Usuário: "aprovado"
    ↓
LLM renomeia: .draft.md → .md, atualiza index.md, append log.md
```

### Ferramentas

| Ferramenta | Função |
|------------|--------|
| `create_entity_draft` | Cria `entities/{slug}.draft.md` |
| `create_concept_draft` | Cria `concepts/{slug}.draft.md` |
| `create_source_draft` | Cria `sources/{slug}.draft.md` |
| `create_synthesis_draft` | Cria `synthesis/{slug}.draft.md` |
| `approve_draft(path)` | Renomeia `.draft.md` → `.md`, atualiza index + log |
| `reject_draft(path)` | Deleta `.draft.md` |
| `list_drafts()` | Lista todos os drafts pendentes |

Drafts de atualização seguem o mesmo padrão: `entities/mamba.draft.md` contém a nova versão proposta.

---

## Ferramentas Wiki

Todas registradas no `TOOL_REGISTRY` do LangGraph.

### Escrita

| Tool | Descrição |
|------|-----------|
| `create_entity(name, summary, tags)` | Cria `entities/{slug}.md` |
| `update_entity(path, content)` | Atualiza entity + campo `updated` |
| `create_concept(name, summary, tags)` | Cria `concepts/{slug}.md` |
| `update_concept(path, content)` | Atualiza concept |
| `create_source_page(title, content)` | Cria `sources/YYYY-MM-DD_slug.md` |
| `create_synthesis(title, content, citations)` | Cria `synthesis/{slug}.md` |
| `append_log(entry)` | Adiciona entrada em `log.md` (append-only) |
| `update_index()` | Regera `index.md` varrendo diretório wiki |

### Draft Mode

| Tool | Descrição |
|------|-----------|
| `create_entity_draft(name, summary, tags)` | Cria `.draft.md` |
| `create_concept_draft(name, summary, tags)` | Cria `.draft.md` |
| `create_source_draft(title, content)` | Cria `.draft.md` |
| `create_synthesis_draft(title, content, citations)` | Cria `.draft.md` |
| `approve_draft(path)` | Finaliza draft |
| `reject_draft(path)` | Remove draft |
| `list_drafts()` | Lista pendentes |

### Manutenção

| Tool | Descrição |
|------|-----------|
| `lint_wiki()` | Detecta contradictions, orphans, broken links, missing concepts |
| `read_wiki_page(path)` | Lê página wiki |
| `search_wiki(query)` | Busca textual no wiki |

---

## Ingestion Pipeline (LangGraph Node)

### Fluxo do nó `ingest_source`

```
1. source_path → lê arquivo de raw/
2. LLM analisa o conteúdo completo
3. LLM sugere: entidades, conceitos, resumo
4. Cria source page (draft)
5. Cria/atualiza entity pages (drafts)
6. Cria/atualiza concept pages (drafts)
7. Usuário aprova drafts
8. Atualiza index.md
9. Append log.md
10. (Opcional) Reindexa no Qdrant
```

### Integração no Grafo LangGraph

```python
def build_graph() -> StateGraph:
    graph = StateGraph(AgentState)

    graph.add_node("retrieve", retrieve_context)
    graph.add_node("planner", planner)
    graph.add_node("executor", executor)
    graph.add_node("ingest_source", ingest_source)  # NOVO

    graph.set_conditional_entry_point(
        detect_intent,  # NOVO: decide se é ingest ou query
        {
            "ingest": "ingest_source",
            "query": "retrieve",
        }
    )

    graph.add_edge("retrieve", "planner")
    graph.add_conditional_edges("planner", should_use_tool)
    graph.add_edge("executor", "planner")
    graph.add_edge("ingest_source", END)

    return graph.compile()
```

---

## Query Evolution

### Fluxo Atual

```
Pergunta → Qdrant (top-5 chunks) → LLM
```

### Novo Fluxo

```
Pergunta
    ↓
1. index.md (catálogo)
    ↓
2. Entities relevantes
    ↓
3. Concepts relevantes
    ↓
4. Synthesis pages relevantes
    ↓
5. Qdrant (fallback semântico)
    ↓
6. LLM sintetiza com citações
    ↓
7. (Opcional) Cria nova synthesis page
```

Prioridade: **wiki > Qdrant > modelo**.

---

## index.md — Catálogo Vivo

```markdown
# Wiki — Índice

## Entities
- [[entities/brian|Brian Smith]]
- [[entities/kaos|K.A.O.S]]
- [[entities/qdrant|Qdrant]]

## Concepts
- [[concepts/rag|Retrieval Augmented Generation]]
- [[concepts/embeddings|Embeddings]]
- [[concepts/langgraph|LangGraph]]

## Sources
- [[sources/2026-06-18_llm_wiki|LLM Wiki — 2026-06-18]]

## Synthesis
- [[synthesis/comparacao_mamba_rwkv|Mamba vs RWKV]]
```

---

## log.md — Timeline Append-only

```
## [2026-06-18] INGEST | LLM Wiki Pattern
- Source: raw/artigo_llm_wiki.md
- New entities: memex, vannevar_bush
- New concepts: knowledge_synthesis, compounding_knowledge
- Updated: index.md

## [2026-06-18] QUERY | "compare Mamba and RWKV"
- Created: synthesis/comparacao_mamba_rwkv.md
- Updated: index.md
```

Permite `grep "^## \[" log.md` para últimas N entradas.

---

## Wiki Linter

### Verificações

| Check | Descrição | Como detecta |
|-------|-----------|--------------|
| Contradictions | Página A diz X, página B diz Y | LLM compara pares de páginas |
| Orphans | Páginas sem inbound links | Conta `[[links]]` para cada página |
| Missing concepts | Conceito mencionado 3+ vezes sem página | Grep por menções sem `[[link]]` |
| Broken links | `[[pagina_inexistente]]` | Verifica se arquivo existe |
| Stale pages | `updated` muito antigo | Compara com última ingestão no log.md |

### Periodicidade

- Manual: comando "faça uma limpeza na wiki"
- Automática (futuro): após cada N ingests

---

## Relação com Outros Componentes

| Componente | Relação |
|------------|---------|
| **RAG Pipeline** | Qdrant vira camada de fallback semântico, não fonte principal |
| **LangGraph** | Novo nó `ingest_source` + entry point condicional |
| **Triple Router** | Novo intent type `INGEST` |
| **Tools existentes** | `create_note`/`update_note` ganham frontmatter YAML |
| **LLM Provider** | Wiki layer é independente do provider — funciona com qualquer LLM |
| **PostgreSQL** | (Futuro) Metadados de ingest_history, entities, concepts |

---

## Critérios de Aceite

### Fase 1 — Schema & Estrutura
- [ ] AGENTS.md criado (PT + EN)
- [ ] Pastas `raw/` e `wiki/` no vault
- [ ] `index.md` e `log.md` iniciais
- [ ] Frontmatter YAML padronizado

### Fase 2 — Ferramentas Wiki
- [ ] create_entity / update_entity funcionando
- [ ] create_concept / update_concept funcionando
- [ ] create_source_page funcionando
- [ ] create_synthesis funcionando
- [ ] append_log / update_index funcionando
- [ ] Draft Mode operacional (create_draft, approve, reject, list)

### Fase 3 — Ingestion Pipeline
- [ ] `ingest_source` node no LangGraph
- [ ] Source → entities → concepts → index → log
- [ ] Intent classifier reconhece INGEST

### Fase 4 — Query Evolution
- [ ] Retrieve consulta wiki antes do Qdrant
- [ ] Respostas complexas viram synthesis pages

### Fase 5 — Manutenção
- [ ] lint_wiki detecta contradictions, orphans, broken links
- [ ] Draft Mode protegendo alterações estruturais
