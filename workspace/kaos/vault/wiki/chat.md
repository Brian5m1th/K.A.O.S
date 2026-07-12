# assistant\app\workflows\impl\chat.py

## Símbolos

- [[assistant_app_workflows_impl_chat]] — code: chat.py
- [[assistant_app_workflows_impl_chat_chatworkflow]] — code: ChatWorkflow
- [[assistant_app_workflows_impl_chat_chatworkflow_required_capabilities]] — code: .required_capabilities()
- [[assistant_app_workflows_impl_chat_chatworkflow_execute]] — code: .execute()
- [[assistant_app_workflows_impl_chat_chatworkflow_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_workflows_impl_chat_chatworkflow]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_chat_chatworkflow_execute]] → `calls` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_chat_chatworkflow]] → `uses` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_chat_chatworkflow_execute]] → `references` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_chat_chatworkflow]] → `uses` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_chat_chatworkflow_execute]] → `references` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_chat_chatworkflow]] → `uses` → [[assistant_app_registry_service_registry_serviceregistry]]
- [[assistant_app_workflows_impl_chat_chatworkflow_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_chat_provider]]
- [[assistant_app_workflows_impl_chat_chatworkflow]] → `inherits` → [[assistant_app_workflows_base_baseworkflow]]
- [[assistant_app_workflows_impl_chat]] → `contains` → [[assistant_app_workflows_impl_chat_chatworkflow]]
- [[assistant_app_workflows_impl_chat_chatworkflow]] → `method` → [[assistant_app_workflows_impl_chat_chatworkflow_execute]]
- [[assistant_app_workflows_impl_chat_chatworkflow]] → `method` → [[assistant_app_workflows_impl_chat_chatworkflow_healthcheck]]
- [[assistant_app_workflows_impl_chat_chatworkflow]] → `method` → [[assistant_app_workflows_impl_chat_chatworkflow_required_capabilities]]