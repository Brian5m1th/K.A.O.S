# assistant\app\dependencies\services.py

## Símbolos

- [[assistant_app_dependencies_services]] — code: services.py
- [[assistant_app_dependencies_services_init_services]] — code: init_services()
- [[assistant_app_dependencies_services_get_graph_service]] — code: get_graph_service()
- [[assistant_app_dependencies_services_get_memory_service]] — code: get_memory_service()
- [[assistant_app_dependencies_services_get_retrieval_service]] — code: get_retrieval_service()
- [[assistant_app_dependencies_services_get_inference_service]] — code: get_inference_service()
- [[assistant_app_dependencies_services_get_planner_service]] — code: get_planner_service()
- [[assistant_app_dependencies_services_get_evidence_service]] — code: get_evidence_service()
- [[assistant_app_dependencies_services_get_knowledge_service]] — code: get_knowledge_service()
- [[assistant_app_dependencies_services_rationale_1]] — code: Dependency Injection — FastAPI service wiring.  Centralizes service instantiatio
- [[assistant_app_dependencies_services_rationale_31]] — code: Initialize all services with default provider registries.
- [[assistant_app_dependencies_services_rationale_83]] — code: Dependency injection: GraphService singleton.

## Dependências

- [[assistant_app_dependencies_services_get_evidence_service]] → `references` → [[assistant_app_core_services_evidence_service_evidenceservice]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_core_services_evidence_service_evidenceservice]]
- [[assistant_app_dependencies_services_get_graph_service]] → `references` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_core_services_graph_service_graphservice]]
- [[assistant_app_dependencies_services_get_inference_service]] → `references` → [[assistant_app_core_services_inference_service_inferenceservice]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_core_services_inference_service_inferenceservice]]
- [[assistant_app_dependencies_services_get_knowledge_service]] → `references` → [[assistant_app_core_services_knowledge_service_knowledgeservice]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_core_services_knowledge_service_knowledgeservice]]
- [[assistant_app_dependencies_services_get_planner_service]] → `references` → [[assistant_app_core_services_planner_service_plannerservice]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_core_services_planner_service_plannerservice]]
- [[assistant_app_dependencies_services_get_retrieval_service]] → `references` → [[assistant_app_core_services_retrieval_service_retrievalservice]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_core_services_retrieval_service_retrievalservice]]
- [[assistant_app_dependencies_services]] → `contains` → [[assistant_app_dependencies_services_get_evidence_service]]
- [[assistant_app_dependencies_services]] → `contains` → [[assistant_app_dependencies_services_get_graph_service]]
- [[assistant_app_dependencies_services]] → `contains` → [[assistant_app_dependencies_services_get_inference_service]]
- [[assistant_app_dependencies_services]] → `contains` → [[assistant_app_dependencies_services_get_knowledge_service]]
- [[assistant_app_dependencies_services]] → `contains` → [[assistant_app_dependencies_services_get_memory_service]]
- [[assistant_app_dependencies_services]] → `contains` → [[assistant_app_dependencies_services_get_planner_service]]
- [[assistant_app_dependencies_services]] → `contains` → [[assistant_app_dependencies_services_get_retrieval_service]]
- [[assistant_app_dependencies_services]] → `contains` → [[assistant_app_dependencies_services_init_services]]
- [[assistant_app_dependencies_services_rationale_1]] → `rationale_for` → [[assistant_app_dependencies_services]]
- [[assistant_app_dependencies_services_get_evidence_service]] → `calls` → [[assistant_app_dependencies_services_init_services]]
- [[assistant_app_dependencies_services_get_graph_service]] → `calls` → [[assistant_app_dependencies_services_init_services]]
- [[assistant_app_dependencies_services_get_inference_service]] → `calls` → [[assistant_app_dependencies_services_init_services]]
- [[assistant_app_dependencies_services_get_knowledge_service]] → `calls` → [[assistant_app_dependencies_services_init_services]]
- [[assistant_app_dependencies_services_get_memory_service]] → `calls` → [[assistant_app_dependencies_services_init_services]]
- [[assistant_app_dependencies_services_get_planner_service]] → `calls` → [[assistant_app_dependencies_services_init_services]]
- [[assistant_app_dependencies_services_get_retrieval_service]] → `calls` → [[assistant_app_dependencies_services_init_services]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_dependencies_services_py_memoryservice]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_providers_graph_graphify_adapter_graphifyadapter]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_providers_graph_networkx_fallback_networkxfallback]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_providers_inference_openai_adapter_claudeadapter]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_providers_inference_openai_adapter_geminiadapter]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_providers_inference_openai_adapter_openaiadapter]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_providers_memory_postgres_memory_adapter_postgresmemoryadapter]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]]
- [[assistant_app_dependencies_services_init_services]] → `calls` → [[assistant_app_providers_retrieval_qdrant_adapter_qdrantadapter]]
- [[assistant_app_dependencies_services_rationale_31]] → `rationale_for` → [[assistant_app_dependencies_services_init_services]]
- [[assistant_app_dependencies_services_rationale_83]] → `rationale_for` → [[assistant_app_dependencies_services_get_graph_service]]
- [[assistant_app_dependencies_services_get_memory_service]] → `references` → [[assistant_app_dependencies_services_py_memoryservice]]