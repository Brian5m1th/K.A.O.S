# assistant\app\workflows\impl\agent.py

## Símbolos

- [[assistant_app_workflows_impl_agent]] — code: agent.py
- [[assistant_app_workflows_impl_agent_agentworkflow]] — code: AgentWorkflow
- [[assistant_app_workflows_impl_agent_agentworkflow_required_capabilities]] — code: .required_capabilities()
- [[assistant_app_workflows_impl_agent_agentworkflow_execute]] — code: .execute()
- [[assistant_app_workflows_impl_agent_agentworkflow_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_workflows_impl_agent_agentworkflow]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_agent_agentworkflow_execute]] → `calls` → [[assistant_app_domain_chat_message]]
- [[assistant_app_workflows_impl_agent_agentworkflow]] → `uses` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_agent_agentworkflow_execute]] → `references` → [[assistant_app_domain_chat_chatrequest]]
- [[assistant_app_workflows_impl_agent_agentworkflow]] → `uses` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_agent_agentworkflow_execute]] → `references` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_workflows_impl_agent_agentworkflow]] → `uses` → [[assistant_app_registry_service_registry_serviceregistry]]
- [[assistant_app_workflows_impl_agent_agentworkflow_execute]] → `calls` → [[assistant_app_registry_service_registry_serviceregistry_get_chat_provider]]
- [[assistant_app_workflows_impl_agent_agentworkflow]] → `inherits` → [[assistant_app_workflows_base_baseworkflow]]
- [[assistant_app_workflows_impl_agent]] → `contains` → [[assistant_app_workflows_impl_agent_agentworkflow]]
- [[assistant_app_workflows_impl_agent_agentworkflow]] → `method` → [[assistant_app_workflows_impl_agent_agentworkflow_execute]]
- [[assistant_app_workflows_impl_agent_agentworkflow]] → `method` → [[assistant_app_workflows_impl_agent_agentworkflow_healthcheck]]
- [[assistant_app_workflows_impl_agent_agentworkflow]] → `method` → [[assistant_app_workflows_impl_agent_agentworkflow_required_capabilities]]