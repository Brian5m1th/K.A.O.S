# assistant\app\api\knowledge_api.py

## Símbolos

- [[assistant_app_api_knowledge_api]] — code: knowledge_api.py
- [[assistant_app_api_knowledge_api_knowledgequeryrequest]] — code: KnowledgeQueryRequest
- [[assistant_app_api_knowledge_api_get_knowledge_service]] — code: get_knowledge_service()
- [[assistant_app_api_knowledge_api_query_knowledge]] — code: query_knowledge()
- [[assistant_app_api_knowledge_api_knowledge_health]] — code: knowledge_health()
- [[assistant_app_api_knowledge_api_rationale_1]] — code: Knowledge REST API — Unified knowledge coalescing queries.  Endpoints:   POST /a
- [[assistant_app_api_knowledge_api_rationale_47]] — code: Coalescing query across graph, retrieval, and memory sources.

## Dependências

- [[assistant_app_api_knowledge_api]] → `contains` → [[assistant_app_api_knowledge_api_get_knowledge_service]]
- [[assistant_app_api_knowledge_api]] → `contains` → [[assistant_app_api_knowledge_api_knowledge_health]]
- [[assistant_app_api_knowledge_api]] → `contains` → [[assistant_app_api_knowledge_api_knowledgequeryrequest]]
- [[assistant_app_api_knowledge_api]] → `contains` → [[assistant_app_api_knowledge_api_query_knowledge]]
- [[assistant_app_api_knowledge_api]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_knowledge_api_rationale_1]] → `rationale_for` → [[assistant_app_api_knowledge_api]]
- [[assistant_app_api_knowledge_api_knowledgequeryrequest]] → `inherits` → [[assistant_app_api_knowledge_api_py_basemodel]]
- [[assistant_app_api_knowledge_api_knowledgequeryrequest]] → `uses` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_api_knowledge_api_knowledgequeryrequest]] → `uses` → [[assistant_app_core_services_knowledge_service_knowledgeservice]]
- [[assistant_app_api_knowledge_api_knowledgequeryrequest]] → `uses` → [[assistant_app_core_services_memory_service_memoryservice]]
- [[assistant_app_api_knowledge_api_knowledgequeryrequest]] → `uses` → [[assistant_app_core_services_retrieval_service_retrievalservice]]
- [[assistant_app_api_knowledge_api_knowledgequeryrequest]] → `uses` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]]
- [[assistant_app_api_knowledge_api_knowledgequeryrequest]] → `uses` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]]
- [[assistant_app_api_knowledge_api_knowledgequeryrequest]] → `uses` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]]
- [[assistant_app_api_knowledge_api_query_knowledge]] → `references` → [[assistant_app_api_knowledge_api_knowledgequeryrequest]]
- [[assistant_app_api_knowledge_api_get_knowledge_service]] → `calls` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_api_knowledge_api_get_knowledge_service]] → `references` → [[assistant_app_core_services_knowledge_service_knowledgeservice]]
- [[assistant_app_api_knowledge_api_get_knowledge_service]] → `calls` → [[assistant_app_core_services_retrieval_service_retrievalservice]]
- [[assistant_app_api_knowledge_api_get_knowledge_service]] → `calls` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]]
- [[assistant_app_api_knowledge_api_get_knowledge_service]] → `calls` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]]
- [[assistant_app_api_knowledge_api_get_knowledge_service]] → `calls` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]]
- [[assistant_app_api_knowledge_api_query_knowledge]] → `references` → [[assistant_app_core_services_knowledge_service_knowledgeservice]]
- [[assistant_app_api_knowledge_api_rationale_47]] → `rationale_for` → [[assistant_app_api_knowledge_api_query_knowledge]]
- [[assistant_app_api_knowledge_api_knowledge_health]] → `references` → [[assistant_app_core_services_knowledge_service_knowledgeservice]]