# Hypotheses — K.A.O.S Architecture Evolution

> Each hypothesis must be validated or rejected with evidence (benchmarks, Graphify queries, experiments).
> No framework is installed in the main K.A.O.S codebase until an ADR is approved.

---

## H1 — Graphify as Evidence Engine

**Statement:** Graphify can serve as the primary code intelligence source for the Evidence Engine, supplemented by Git history, test results, and benchmarks.

**Prediction:** Graphify's `explain`, `path`, and `query` commands provide sufficient structural evidence to detect god objects, import cycles, dependency drift, and architectural violations.

**Validation criteria:**
- [ ] Graphify detects all current import cycles (proven in state audit)
- [ ] Graphify path queries resolve symbols to files correctly (proven)
- [ ] Evidence Engine integrates Graphify + Git + Tests into unified report
- [ ] Weekly automated scan catches regressions before deployment

**Status:** 🟡 Partially validated. Graphify queries already proven. Git/Test integration pending.

---

## H2 — Mem0 for Persistent Agent Memory

**Statement:** Mem0 can provide persistent user/agent memory (preferences, identity, long-term context) that supplements PostgreSQL conversation storage.

**Prediction:** Mem0's user profile store reduces context window bloat by maintaining persistent identity separate from chat history.

**Validation criteria (kaos-research/experiments/mem0/):**
- [ ] Memory retrieval latency < 50ms
- [ ] Profile consistency across 100+ sessions
- [ ] No degradation when switching between Ollama and OpenAI providers
- [ ] Docker deployment footprint < 500MB RAM

**Status:** 🔴 Not yet tested. Requires kaos-research/experiments/mem0/ setup.

---

## H3 — GraphRAG for Multi-hop Knowledge Queries

**Statement:** Microsoft GraphRAG can answer complex multi-hop questions (e.g., "How does OllamaProvider connect to the LLM cost tracker?") that single-hop vector search cannot.

**Prediction:** GraphRAG's community summarization produces better global understanding than raw Graphify path traversal for open-ended questions.

**Validation criteria (kaos-research/experiments/graphrag/):**
- [ ] Index time for K.A.O.S docs + code < 5 minutes
- [ ] Query latency < 2 seconds for multi-hop questions
- [ ] Precision@5 > 0.8 on 10 benchmark questions
- [ ] No OpenAI dependency for index creation (use Ollama as local LLM)
- [ ] Incremental update support (new docs only, not full re-index)

**Status:** 🔴 Not yet tested. Requires kaos-research/experiments/graphrag/ setup.

---

## H4 — Graphiti for Temporal Knowledge Evolution

**Statement:** Graphiti can track how knowledge evolves over time (e.g., "What changed in the architecture between commits X and Y?").

**Prediction:** Graphiti's temporal graph captures entity relationships + timestamps better than Graphify's snapshot-based approach.

**Validation criteria (kaos-research/experiments/graphiti/):**
- [ ] Ingestion rate > 10 documents/second
- [ ] Temporal query precision > 0.7
- [ ] Docker footprint < 1GB RAM
- [ ] Compatible with Graphify's graph.json export format

**Status:** 🔴 Not yet tested. Requires kaos-research/experiments/graphiti/ setup.

---

## H5 — LangGraph for Advanced Agent Orchestration

**Statement:** LangGraph (already integrated) should remain the primary agent orchestration framework. Letta/MemGPT adds autonomous research loops but duplicates LangGraph's state machine.

**Prediction:** LangGraph + custom K.A.O.S nodes suffice for current agent workflows. Letta adds unnecessary complexity for current use cases.

**Validation criteria (kaos-research/experiments/langgraph/):**
- [ ] LangGraph handles 10 concurrent agent workflows without degradation
- [ ] Letta benchmark shows < 20% improvement over LangGraph for K.A.O.S tasks
- [ ] If improvement > 20%, Letta gains an adapter. Otherwise, rejected.

**Status:** 🟡 LangGraph already integrated. Letta evaluation pending.

---

## H6 — Cognee for Entity Extraction

**Statement:** Cognee can extract entities and relationships from K.A.O.S documentation automatically, supplementing Graphify's AST-based code graph.

**Prediction:** Cognee's LLM-based extraction produces richer documentation-to-code links than current regex-based VaultReader.

**Validation criteria (kaos-research/experiments/cognee/):**
- [ ] Entity extraction precision > 0.7 on K.A.O.S documentation
- [ ] Relationship extraction recall > 0.6
- [ ] Graph export compatible with Graphify's graph.json format
- [ ] Incremental update support

**Status:** 🔴 Not yet tested. Requires kaos-research/experiments/cognee/ setup.

---

## H7 — AirLLM for Local Large Model Inference

**Statement:** AirLLM enables running 70B+ parameter models on consumer GPUs (4-8GB VRAM) through layer-wise inference, reducing cloud API costs.

**Prediction:** AirLLM processes 70B models at > 1 token/second on 8GB GPU, making it viable for batch/documentation tasks but not real-time chat.

**Validation criteria (kaos-research/experiments/airllm/):**
- [ ] Successfully loads Llama 3.1 70B on 8GB GPU
- [ ] Token generation rate > 1 token/second
- [ ] Answer quality comparable to Ollama qwen3:14b on K.A.O.S knowledge questions
- [ ] Memory usage stays within 8GB VRAM

**Status:** 🟡 Provider created (Phase 1). Performance benchmarking pending.

---

## Summary

| Hypothesis | Framework | Risk | Validation Status |
|---|---|---|---|
| H1 | Graphify (Evidence Engine) | Low | 🟡 Partially validated |
| H2 | Mem0 (Persistent Memory) | Medium | 🔴 Not tested |
| H3 | GraphRAG (Multi-hop) | High | 🔴 Not tested |
| H4 | Graphiti (Temporal) | High | 🔴 Not tested |
| H5 | LangGraph (Orchestration) | Low | 🟡 Partially validated |
| H6 | Cognee (Entities) | Medium | 🔴 Not tested |
| H7 | AirLLM (Large Models) | Medium | 🟡 Provider exists, benchmark pending |
