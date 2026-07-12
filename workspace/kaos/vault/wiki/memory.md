# assistant\app\workflows\impl\memory.py

## Símbolos

- [[assistant_app_workflows_impl_memory]] — code: memory.py
- [[assistant_app_workflows_impl_memory_memoryworkflow]] — code: MemoryWorkflow
- [[assistant_app_workflows_impl_memory_memoryworkflow_required_capabilities]] — code: .required_capabilities()
- [[assistant_app_workflows_impl_memory_memoryworkflow_execute]] — code: .execute()
- [[assistant_app_workflows_impl_memory_memoryworkflow_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_workflows_impl_memory_memoryworkflow]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_memory_memoryworkflow_execute]] → `calls` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_memory_memoryworkflow]] → `uses` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_memory_memoryworkflow_execute]] → `references` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_memory_memoryworkflow]] → `uses` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_memory_memoryworkflow_execute]] → `references` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_memory_memoryworkflow]] → `uses` → [[assistant_app_registry_service_registry_serviceregistry]]
- [[assistant_app_workflows_impl_memory_memoryworkflow_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_memory_provider]]
- [[assistant_app_workflows_impl_memory_memoryworkflow]] → `inherits` → [[assistant_app_workflows_base_baseworkflow]]
- [[assistant_app_workflows_impl_memory]] → `contains` → [[assistant_app_workflows_impl_memory_memoryworkflow]]
- [[assistant_app_workflows_impl_memory_memoryworkflow]] → `method` → [[assistant_app_workflows_impl_memory_memoryworkflow_execute]]
- [[assistant_app_workflows_impl_memory_memoryworkflow]] → `method` → [[assistant_app_workflows_impl_memory_memoryworkflow_healthcheck]]
- [[assistant_app_workflows_impl_memory_memoryworkflow]] → `method` → [[assistant_app_workflows_impl_memory_memoryworkflow_required_capabilities]]