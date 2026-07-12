# Ordem de Execução — Knowledge Graph Semântico K.A.O.S

## Status Geral
- [x] enriched/ models (Pydantic schemas, inference, 50+ relation types)
- [x] enriched/ parser (graph.json -> enriched)
- [x] enriched/ llm_enricher (Ollama/OpenAI, cache, prompts)
- [x] enriched/ quality (complexity, smells, coupling)
- [x] enriched/ doc_linker (DOCUMENTED_BY, ADR_RELATED)
- [x] enriched/ test_linker (TESTED_BY, TESTS, COVERS)
- [x] enriched/ risk (risk levels, TODOs, known issues)
- [x] enriched/ community (LLM summarization + hub fallback)
- [x] graph_sync/ neo4j (full/incremental sync, Cypher)
- [x] graph_sync/ qdrant (embeddings, semantic search)
- [x] graph_sync/ provenance (temporal tracking, invalidation)
- [x] graph_sync/ graph_port_v2 (EnrichedGraphAdapter)
- [x] CLI graphify enrich (com todas as flags)
- [x] Auto-enrich pos-export (GRAPHIFY_AUTO_ENRICH)
- [x] ADR/RFC/SDD extraction para TODAS as linguagens
- [x] Relacoes preservadas no aggregator (fim do colapso 'uses')
- [x] EnrichedGraphAdapter no Assistant (graph_api + knowledge_api)
- [x] 35 testes unitarios passando
- [x] graphify update . executado
- [x] Grafo enriquecido gerado (20.644 nos, 31.514 arestas)
- [x] pip install -e . (dev install)

## Status Final
- [x] **Otimizar performance** — progress bar (tqdm), filtro _should_enrich (100k->1.6k nodes), auth error handling, provider check
- [x] **MCP tools** — graph_search, graph_explain, graph_affected_by, graph_risk_report registradas no serve.py
- [x] **Dashboard** — HTML auto-contido com Chart.js: layers, risks, domains, smells, complexidade
- [ ] **CI/CD** integration com enrich automatico (proximo passo disponivel)
