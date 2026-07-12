# assistant\app\workflows\impl\rag.py

## Símbolos

- [[assistant_app_workflows_impl_rag]] — code: rag.py
- [[assistant_app_workflows_impl_rag_ragworkflow]] — code: RagWorkflow
- [[assistant_app_workflows_impl_rag_ragworkflow_required_capabilities]] — code: .required_capabilities()
- [[assistant_app_workflows_impl_rag_ragworkflow_execute]] — code: .execute()
- [[assistant_app_workflows_impl_rag_ragworkflow_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_workflows_impl_rag_ragworkflow]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_rag_ragworkflow_execute]] → `calls` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_rag_ragworkflow]] → `uses` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_rag_ragworkflow_execute]] → `references` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_rag_ragworkflow]] → `uses` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_rag_ragworkflow_execute]] → `references` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_rag_ragworkflow]] → `uses` → [[assistant_app_registry_service_registry_serviceregistry]]
- [[assistant_app_workflows_impl_rag_ragworkflow_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_chat_provider]]
- [[assistant_app_workflows_impl_rag_ragworkflow_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_embedding_provider]]
- [[assistant_app_workflows_impl_rag_ragworkflow_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_vector_store]]
- [[assistant_app_workflows_impl_rag_ragworkflow]] → `inherits` → [[assistant_app_workflows_base_baseworkflow]]
- [[assistant_app_workflows_impl_rag]] → `contains` → [[assistant_app_workflows_impl_rag_ragworkflow]]
- [[assistant_app_workflows_impl_rag_ragworkflow]] → `method` → [[assistant_app_workflows_impl_rag_ragworkflow_execute]]
- [[assistant_app_workflows_impl_rag_ragworkflow]] → `method` → [[assistant_app_workflows_impl_rag_ragworkflow_healthcheck]]
- [[assistant_app_workflows_impl_rag_ragworkflow]] → `method` → [[assistant_app_workflows_impl_rag_ragworkflow_required_capabilities]]