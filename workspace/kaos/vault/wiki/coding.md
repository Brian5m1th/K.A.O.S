# assistant\app\workflows\impl\coding.py

## Símbolos

- [[assistant_app_workflows_impl_coding]] — code: coding.py
- [[assistant_app_workflows_impl_coding_codingworkflow]] — code: CodingWorkflow
- [[assistant_app_workflows_impl_coding_codingworkflow_required_capabilities]] — code: .required_capabilities()
- [[assistant_app_workflows_impl_coding_codingworkflow_execute]] — code: .execute()
- [[assistant_app_workflows_impl_coding_codingworkflow_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_workflows_impl_coding_codingworkflow]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_coding_codingworkflow_execute]] → `calls` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_coding_codingworkflow]] → `uses` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_coding_codingworkflow_execute]] → `references` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_coding_codingworkflow]] → `uses` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_coding_codingworkflow_execute]] → `references` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_coding_codingworkflow]] → `uses` → [[assistant_app_registry_service_registry_serviceregistry]]
- [[assistant_app_workflows_impl_coding_codingworkflow_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_chat_provider]]
- [[assistant_app_workflows_impl_coding_codingworkflow]] → `inherits` → [[assistant_app_workflows_base_baseworkflow]]
- [[assistant_app_workflows_impl_coding]] → `contains` → [[assistant_app_workflows_impl_coding_codingworkflow]]
- [[assistant_app_workflows_impl_coding_codingworkflow]] → `method` → [[assistant_app_workflows_impl_coding_codingworkflow_execute]]
- [[assistant_app_workflows_impl_coding_codingworkflow]] → `method` → [[assistant_app_workflows_impl_coding_codingworkflow_healthcheck]]
- [[assistant_app_workflows_impl_coding_codingworkflow]] → `method` → [[assistant_app_workflows_impl_coding_codingworkflow_required_capabilities]]