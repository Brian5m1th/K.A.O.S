# Capability Matrix — K.A.O.S vs Framework Candidates

> Coverage: ████████ = full, ██████ = partial, ░░░░ = none, ⚠️ = potential

## Core Memory Capabilities

| Capability | Graphify | GraphRAG | Graphiti | Mem0 | Cognee | LangGraph | Qdrant |
|---|---|---|---|---|---|---|---|
| Episodic Memory | ❌ | ❌ | ██████ | ████████ | ██████ | ❌ | ❌ |
| Semantic Memory | ❌ | ████████ | ❌ | ██████ | ██████ | ❌ | ████████ |
| Procedural Memory | ❌ | ❌ | ❌ | ❌ | ❌ | ██████ | ❌ |
| Temporal Memory | ❌ | ❌ | ████████ | ❌ | ❌ | ❌ | ❌ |
| Long-term Memory | ❌ | ❌ | ██████ | ████████ | ██████ | ██████ | ❌ |
| Conversation Memory | ❌ | ❌ | ❌ | ████ | ██████ | ██████ | ❌ |

## Core Knowledge Capabilities

| Capability | Graphify | GraphRAG | Graphiti | Mem0 | Cognee | LangGraph | Qdrant |
|---|---|---|---|---|---|---|---|
| Code Graph (AST) | ████████ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Knowledge Graph | ██ | ████████ | ██████ | ❌ | ██████ | ❌ | ❌ |
| Documentation Graph | ██████ | ████████ | ████ | ❌ | ██████ | ❌ | ❌ |
| Runtime Knowledge | ❌ | ❌ | ██████ | ████ | ❌ | ██████ | ❌ |
| Architecture Knowledge | ████████ | ████ | ❌ | ❌ | ████ | ❌ | ❌ |

## Core Intelligence Capabilities

| Capability | Graphify | GraphRAG | Graphiti | Mem0 | Cognee | LangGraph | Qdrant |
|---|---|---|---|---|---|---|---|
| Semantic Search | ❌ | ██████ | ❌ | ████ | ████ | ❌ | ████████ |
| Multi-hop Reasoning | ❌ | ████████ | ❌ | ❌ | ████ | ██████ | ❌ |
| Global Search | ❌ | ████████ | ❌ | ❌ | ████ | ❌ | ❌ |
| Local Search | ████████ | ██████ | ████ | ❌ | ██████ | ❌ | ██████ |
| Entity Extraction | ██████ | ████████ | ██████ | ❌ | ████████ | ❌ | ❌ |
| Relationship Extraction | ████████ | ██████ | ██████ | ❌ | ██████ | ❌ | ❌ |

## Core Agent Capabilities

| Capability | Graphify | GraphRAG | Graphiti | Mem0 | Cognee | LangGraph | Qdrant |
|---|---|---|---|---|---|---|---|
| Planning | ❌ | ❌ | ❌ | ❌ | ❌ | ████████ | ❌ |
| Execution | ❌ | ❌ | ❌ | ❌ | ❌ | ████████ | ❌ |
| Observation | ❌ | ❌ | ❌ | ❌ | ❌ | ██████ | ❌ |
| Learning | ❌ | ❌ | ████ | ██████ | ████ | ██████ | ❌ |
| Tool Registry | ██████ | ❌ | ❌ | ❌ | ❌ | ██████ | ❌ |

## Operational Capabilities

| Capability | Graphify | GraphRAG | Graphiti | Mem0 | Cognee | LangGraph | Qdrant |
|---|---|---|---|---|---|---|---|
| Incremental Updates | ██████ | ❌ | ████████ | ██████ | ❌ | ██████ | ██████ |
| Offline Support | ████████ | ❌ | ❌ | ██ | ❌ | ██ | ████████ |
| MCP Integration | ████████ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Docker Deploy | ❌ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ██████ | ████████ |
| GPU Optional | ████████ | ❌ | ⚠️ | ██████ | ██████ | ██████ | ██████ |

---

## Overlap Analysis

### High Overlap (same capability, multiple frameworks)
- **Entity Extraction:** GraphRAG, Cognee, Graphiti, Graphify (4 frameworks)
- **Knowledge Graph:** GraphRAG, Graphiti, Cognee (3 frameworks — complementary, not redundant)
- **Semantic Memory:** GraphRAG, Mem0, Cognee, Qdrant (4 frameworks — different approaches)

### Gaps (no framework covers)
- **Unified Observability:** No single framework covers Graphify + Git + Tests + Benchmarks
- **Automated Benchmarking:** No framework provides out-of-box comparison
- **Technology Observatory:** No existing framework — must be built custom

### Complementarity (modular, not competitive)
- **Graphify + GraphRAG:** Code graph (AST) + Knowledge graph (entities) — complementary
- **Mem0 + Graphiti:** Persistent identity (Mem0) + Temporal evolution (Graphiti) — complementary
- **Qdrant + FalkorDB:** Vector search (Qdrant) + Graph-native queries (FalkorDB) — complementary

---

## Recommendation Summary

| Framework | Verdict | Rationale |
|---|---|---|
| **Graphify** | ✅ **KEEP** — Core | Best-in-class code graph. Already integrated. Elevate to Evidence Engine source. |
| **GraphRAG** | 🔬 **TEST** (H3) | Multi-hop reasoning potential. High LLM cost risk. Need local Ollama mode test. |
| **Graphiti** | 🔬 **TEST** (H4) | Temporal knowledge unique value. Check Docker footprint and Graphify compatibility. |
| **Mem0** | 🔬 **TEST** (H2) | Persistent identity potential. Low risk, small footprint. |
| **Cognee** | 🔬 **TEST** (H6) | Entity extraction for docs. Check quality vs VaultReader. |
| **LangGraph** | ✅ **KEEP** — Core | Already integrated. Primary orchestration framework. |
| **FalkorDB** | ⏸️ **DEFER** | Qdrant already covers vector needs. Graph-native queries not yet needed. |
| **Letta/MemGPT** | ⏸️ **DEFER** (H5) | LangGraph + custom nodes sufficient. High complexity addition. |
| **Neo4j** | ⏸️ **DEFER** | Graphify covers code graph. No property graph need yet. |
