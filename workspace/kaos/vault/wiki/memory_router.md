# assistant\app\router\memory_router.py

## Símbolos

- [[assistant_app_router_memory_router]] — code: memory_router.py
- [[assistant_app_router_memory_router_memoryrouter]] — code: MemoryRouter
- [[assistant_app_router_memory_router_memoryrouter_init]] — code: .__init__()
- [[assistant_app_router_memory_router_memoryrouter_get_vault_path]] — code: ._get_vault_path()
- [[assistant_app_router_memory_router_memoryrouter_search_wiki_local]] — code: ._search_wiki_local()
- [[assistant_app_router_memory_router_memoryrouter_retrieve_context]] — code: .retrieve_context()
- [[assistant_app_router_memory_router_memoryrouter_process]] — code: .process()
- [[assistant_app_router_memory_router_memoryrouter_stream]] — code: .stream()
- [[assistant_app_router_memory_router_rationale_25]] — code: Retorna o caminho do vault, se configurado.
- [[assistant_app_router_memory_router_rationale_33]] — code: Busca no wiki local (wiki/index.md + wiki/synthesis/) antes de ir ao Qdrant.

## Dependências

- [[assistant_app_router_memory_router_memoryrouter]] → `uses` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_router_memory_router_memoryrouter_init]] → `calls` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_router_memory_router_memoryrouter]] → `uses` → [[assistant_app_rag_retriever_semantic_retriever_semanticretriever]]
- [[assistant_app_router_memory_router_memoryrouter_init]] → `calls` → [[assistant_app_rag_retriever_semantic_retriever_semanticretriever]]
- [[assistant_app_router_memory_router]] → `contains` → [[assistant_app_router_memory_router_memoryrouter]]
- [[assistant_app_router_memory_router_memoryrouter]] → `method` → [[assistant_app_router_memory_router_memoryrouter_get_vault_path]]
- [[assistant_app_router_memory_router_memoryrouter]] → `method` → [[assistant_app_router_memory_router_memoryrouter_init]]
- [[assistant_app_router_memory_router_memoryrouter]] → `method` → [[assistant_app_router_memory_router_memoryrouter_process]]
- [[assistant_app_router_memory_router_memoryrouter]] → `method` → [[assistant_app_router_memory_router_memoryrouter_retrieve_context]]
- [[assistant_app_router_memory_router_memoryrouter]] → `method` → [[assistant_app_router_memory_router_memoryrouter_search_wiki_local]]
- [[assistant_app_router_memory_router_memoryrouter]] → `method` → [[assistant_app_router_memory_router_memoryrouter_stream]]
- [[assistant_app_router_memory_router_memoryrouter_get_vault_path]] → `references` → [[assistant_app_router_memory_router_py_path]]
- [[assistant_app_router_memory_router_memoryrouter_search_wiki_local]] → `calls` → [[assistant_app_router_memory_router_memoryrouter_get_vault_path]]
- [[assistant_app_router_memory_router_rationale_25]] → `rationale_for` → [[assistant_app_router_memory_router_memoryrouter_get_vault_path]]
- [[assistant_app_router_memory_router_memoryrouter_retrieve_context]] → `calls` → [[assistant_app_router_memory_router_memoryrouter_search_wiki_local]]
- [[assistant_app_router_memory_router_rationale_33]] → `rationale_for` → [[assistant_app_router_memory_router_memoryrouter_search_wiki_local]]
- [[assistant_app_router_memory_router_memoryrouter_process]] → `calls` → [[assistant_app_router_memory_router_memoryrouter_retrieve_context]]
- [[assistant_app_router_memory_router_memoryrouter_stream]] → `calls` → [[assistant_app_router_memory_router_memoryrouter_retrieve_context]]