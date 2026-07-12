# assistant\app\workflows\impl\research.py

## Símbolos

- [[assistant_app_workflows_impl_research]] — code: research.py
- [[assistant_app_workflows_impl_research_researchworkflow]] — code: ResearchWorkflow
- [[assistant_app_workflows_impl_research_researchworkflow_required_capabilities]] — code: .required_capabilities()
- [[assistant_app_workflows_impl_research_researchworkflow_execute]] — code: .execute()
- [[assistant_app_workflows_impl_research_researchworkflow_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_workflows_impl_research_researchworkflow]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_research_researchworkflow_execute]] → `calls` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_research_researchworkflow]] → `uses` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_research_researchworkflow_execute]] → `references` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_research_researchworkflow]] → `uses` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_research_researchworkflow_execute]] → `references` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_research_researchworkflow]] → `uses` → [[assistant_app_registry_service_registry_serviceregistry]]
- [[assistant_app_workflows_impl_research_researchworkflow_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_chat_provider]]
- [[assistant_app_workflows_impl_research_researchworkflow_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_embedding_provider]]
- [[assistant_app_workflows_impl_research_researchworkflow_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_vector_store]]
- [[assistant_app_workflows_impl_research_researchworkflow]] → `inherits` → [[assistant_app_workflows_base_baseworkflow]]
- [[assistant_app_workflows_impl_research]] → `contains` → [[assistant_app_workflows_impl_research_researchworkflow]]
- [[assistant_app_workflows_impl_research_researchworkflow]] → `method` → [[assistant_app_workflows_impl_research_researchworkflow_execute]]
- [[assistant_app_workflows_impl_research_researchworkflow]] → `method` → [[assistant_app_workflows_impl_research_researchworkflow_healthcheck]]
- [[assistant_app_workflows_impl_research_researchworkflow]] → `method` → [[assistant_app_workflows_impl_research_researchworkflow_required_capabilities]]