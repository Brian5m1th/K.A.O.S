# assistant\app\service\agent_service.py

## Símbolos

- [[assistant_app_service_agent_service]] — code: agent_service.py
- [[assistant_app_service_agent_service_get_graph]] — code: _get_graph()
- [[assistant_app_service_agent_service_make_state]] — code: _make_state()
- [[assistant_app_service_agent_service_agentservice]] — code: AgentService
- [[assistant_app_service_agent_service_agentservice_process_message]] — code: .process_message()
- [[assistant_app_service_agent_service_agentservice_stream_message]] — code: .stream_message()

## Dependências

- [[assistant_app_service_agent_service_agentservice]] → `uses` → [[assistant_app_agent_state_agentstate]]
- [[assistant_app_service_agent_service]] → `contains` → [[assistant_app_service_agent_service_agentservice]]
- [[assistant_app_service_agent_service]] → `contains` → [[assistant_app_service_agent_service_get_graph]]
- [[assistant_app_service_agent_service]] → `contains` → [[assistant_app_service_agent_service_make_state]]
- [[assistant_app_service_agent_service_agentservice_process_message]] → `calls` → [[assistant_app_service_agent_service_get_graph]]
- [[assistant_app_service_agent_service_agentservice_stream_message]] → `calls` → [[assistant_app_service_agent_service_get_graph]]
- [[assistant_app_service_agent_service_agentservice_process_message]] → `calls` → [[assistant_app_service_agent_service_make_state]]
- [[assistant_app_service_agent_service_agentservice_stream_message]] → `calls` → [[assistant_app_service_agent_service_make_state]]
- [[assistant_app_service_agent_service_make_state]] → `references` → [[assistant_app_service_agent_service_py_agentstate]]
- [[assistant_app_service_agent_service_agentservice]] → `method` → [[assistant_app_service_agent_service_agentservice_process_message]]
- [[assistant_app_service_agent_service_agentservice]] → `method` → [[assistant_app_service_agent_service_agentservice_stream_message]]