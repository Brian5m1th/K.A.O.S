# assistant\app\agent\nodes\planner.py

## Símbolos

- [[assistant_app_agent_nodes_planner]] — code: planner.py
- [[assistant_app_agent_nodes_planner_get_factory]] — code: _get_factory()
- [[assistant_app_agent_nodes_planner_planner]] — code: planner()

## Dependências

- [[assistant_app_agent_nodes_planner]] → `contains` → [[assistant_app_agent_nodes_planner_get_factory]]
- [[assistant_app_agent_nodes_planner]] → `contains` → [[assistant_app_agent_nodes_planner_planner]]
- [[assistant_app_agent_nodes_planner_get_factory]] → `references` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_agent_nodes_planner_get_factory]] → `calls` → [[assistant_app_setup_provider_config_get_config_version]]
- [[assistant_app_agent_nodes_planner_planner]] → `calls` → [[assistant_app_agent_nodes_planner_get_factory]]
- [[assistant_app_agent_nodes_planner_planner]] → `references` → [[assistant_app_agent_nodes_planner_py_agentstate]]