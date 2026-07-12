# docs\sdd\sdd_fase4_rag_pipeline.md

## Símbolos

- [[docs_sdd_sdd_fase4_rag_pipeline]] — code: sdd_fase4_rag_pipeline.md
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] — code: SDD — Fases 4 e 5: RAG Pipeline + Atualização Automática
- [[docs_sdd_sdd_fase4_rag_pipeline_objetivo]] — code: Objetivo
- [[docs_sdd_sdd_fase4_rag_pipeline_critério_de_sucesso]] — code: Critério de Sucesso
- [[docs_sdd_sdd_fase4_rag_pipeline_status_atual_concluído_fases_4_5_otimizações]] — code: Status Atual: ✅ CONCLUÍDO (Fases 4-5 + Otimizações)
- [[docs_sdd_sdd_fase4_rag_pipeline_1_estrutura_de_módulos]] — code: 1. Estrutura de Módulos
- [[docs_sdd_sdd_fase4_rag_pipeline_2_embedder_rag_embeddings_embedder_py]] — code: 2. Embedder (`rag/embeddings/embedder.py`)
- [[docs_sdd_sdd_fase4_rag_pipeline_3_text_splitter_rag_chunking_text_splitter_py]] — code: 3. Text Splitter (`rag/chunking/text_splitter.py`)
- [[docs_sdd_sdd_fase4_rag_pipeline_4_semantic_retriever_rag_retriever_semantic_retriever_py]] — code: 4. Semantic Retriever (`rag/retriever/semantic_retriever.py`)
- [[docs_sdd_sdd_fase4_rag_pipeline_dependências]] — code: Dependências
- [[docs_sdd_sdd_fase4_rag_pipeline_desbloqueia]] — code: Desbloqueia
- [[docs_sdd_sdd_fase4_rag_pipeline_resumo]] — code: Resumo
- [[docs_sdd_sdd_fase4_rag_pipeline_responsabilidades]] — code: Responsabilidades
- [[docs_sdd_sdd_fase4_rag_pipeline_dependencias]] — code: Dependencias
- [[docs_sdd_sdd_fase4_rag_pipeline_fluxos]] — code: Fluxos
- [[docs_sdd_sdd_fase4_rag_pipeline_integracoes]] — code: Integracoes
- [[docs_sdd_sdd_fase4_rag_pipeline_arquivos_relacionados]] — code: Arquivos Relacionados
- [[docs_sdd_sdd_fase4_rag_pipeline_referencias_kirl]] — code: Referencias KIRL
- [[docs_sdd_sdd_fase4_rag_pipeline_ultima_atualizacao]] — code: Ultima Atualizacao

## Dependências

- [[docs_sdd_sdd_fase4_rag_pipeline]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]]
- [[docs_sdd_sdd_fase4_rag_pipeline]] → `references` → [[docs_sdd_sdd_fase5_watcher_langgraph]]
- [[docs_sdd_sdd_fase4_rag_pipeline]] → `references` → [[docs_sdd_sdd_obsidian_rag]]
- [[docs_sdd_sdd_fase4_rag_pipeline]] → `references` → [[docs_sdd_sdd_obsidian_watcher]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_1_estrutura_de_módulos]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_2_embedder_rag_embeddings_embedder_py]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_3_text_splitter_rag_chunking_text_splitter_py]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_4_semantic_retriever_rag_retriever_semantic_retriever_py]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_arquivos_relacionados]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_critério_de_sucesso]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_dependencias]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_dependências]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_desbloqueia]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_fluxos]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_integracoes]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_objetivo]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_referencias_kirl]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_responsabilidades]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_resumo]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_status_atual_concluído_fases_4_5_otimizações]]
- [[docs_sdd_sdd_fase4_rag_pipeline_sdd_fases_4_e_5_rag_pipeline_atualização_automática]] → `contains` → [[docs_sdd_sdd_fase4_rag_pipeline_ultima_atualizacao]]