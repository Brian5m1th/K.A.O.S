# assistant\app\workflows\impl\registry.py

## Símbolos

- [[assistant_app_workflows_impl_registry]] — code: registry.py
- [[assistant_app_workflows_impl_registry_register_workflows]] — code: register_workflows()

## Dependências

- [[assistant_app_workflows_impl_registry_register_workflows]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_register_workflow]]
- [[assistant_app_workflows_impl_registry_register_workflows]] → `indirect_call` → [[assistant_app_workflows_impl_agent_agentworkflow]]
- [[assistant_app_workflows_impl_registry_register_workflows]] → `indirect_call` → [[assistant_app_workflows_impl_chat_chatworkflow]]
- [[assistant_app_workflows_impl_registry_register_workflows]] → `indirect_call` → [[assistant_app_workflows_impl_coding_codingworkflow]]
- [[assistant_app_workflows_impl_registry_register_workflows]] → `indirect_call` → [[assistant_app_workflows_impl_ingest_ingestworkflow]]
- [[assistant_app_workflows_impl_registry_register_workflows]] → `indirect_call` → [[assistant_app_workflows_impl_memory_memoryworkflow]]
- [[assistant_app_workflows_impl_registry_register_workflows]] → `indirect_call` → [[assistant_app_workflows_impl_rag_ragworkflow]]
- [[assistant_app_workflows_impl_registry]] → `contains` → [[assistant_app_workflows_impl_registry_register_workflows]]
- [[assistant_app_workflows_impl_registry_register_workflows]] → `indirect_call` → [[assistant_app_workflows_impl_research_researchworkflow]]