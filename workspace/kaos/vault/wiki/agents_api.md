# assistant\app\api\agents_api.py

## Símbolos

- [[assistant_app_api_agents_api]] — code: agents_api.py
- [[assistant_app_api_agents_api_agentconfigpayload]] — code: AgentConfigPayload
- [[assistant_app_api_agents_api_list_agent_statuses]] — code: list_agent_statuses()
- [[assistant_app_api_agents_api_start_agent]] — code: start_agent()
- [[assistant_app_api_agents_api_stop_agent]] — code: stop_agent()
- [[assistant_app_api_agents_api_pause_agent]] — code: pause_agent()
- [[assistant_app_api_agents_api_resume_agent]] — code: resume_agent()
- [[assistant_app_api_agents_api_chatpayload]] — code: ChatPayload
- [[assistant_app_api_agents_api_chat_with_agent]] — code: chat_with_agent()

## Dependências

- [[assistant_app_api_agents_api]] → `contains` → [[assistant_app_api_agents_api_agentconfigpayload]]
- [[assistant_app_api_agents_api]] → `contains` → [[assistant_app_api_agents_api_chat_with_agent]]
- [[assistant_app_api_agents_api]] → `contains` → [[assistant_app_api_agents_api_chatpayload]]
- [[assistant_app_api_agents_api]] → `contains` → [[assistant_app_api_agents_api_list_agent_statuses]]
- [[assistant_app_api_agents_api]] → `contains` → [[assistant_app_api_agents_api_pause_agent]]
- [[assistant_app_api_agents_api]] → `contains` → [[assistant_app_api_agents_api_resume_agent]]
- [[assistant_app_api_agents_api]] → `contains` → [[assistant_app_api_agents_api_start_agent]]
- [[assistant_app_api_agents_api]] → `contains` → [[assistant_app_api_agents_api_stop_agent]]
- [[assistant_app_api_agents_api]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_agents_api_agentconfigpayload]] → `inherits` → [[assistant_app_api_agents_api_py_basemodel]]
- [[assistant_app_api_agents_api_agentconfigpayload]] → `uses` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_api_agents_api_start_agent]] → `references` → [[assistant_app_api_agents_api_agentconfigpayload]]
- [[assistant_app_api_agents_api_chatpayload]] → `inherits` → [[assistant_app_api_agents_api_py_basemodel]]
- [[assistant_app_api_agents_api_chat_with_agent]] → `references` → [[assistant_app_api_agents_api_chatpayload]]
- [[assistant_app_api_agents_api_chatpayload]] → `uses` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_api_agents_api_chat_with_agent]] → `calls` → [[assistant_app_llm_factory_llmfactory]]