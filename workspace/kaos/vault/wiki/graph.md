# assistant\app\agent\graph.py

## Símbolos

- [[assistant_app_agent_graph]] — code: graph.py
- [[assistant_app_agent_graph_should_use_tool]] — code: should_use_tool()
- [[assistant_app_agent_graph_route_entry]] — code: route_entry()
- [[assistant_app_agent_graph_build_graph]] — code: build_graph()

## Dependências

- [[assistant_app_agent_graph]] → `contains` → [[assistant_app_agent_graph_build_graph]]
- [[assistant_app_agent_graph]] → `contains` → [[assistant_app_agent_graph_route_entry]]
- [[assistant_app_agent_graph]] → `contains` → [[assistant_app_agent_graph_should_use_tool]]
- [[assistant_app_agent_graph_build_graph]] → `indirect_call` → [[assistant_app_agent_graph_should_use_tool]]
- [[assistant_app_agent_graph_should_use_tool]] → `references` → [[assistant_app_agent_graph_py_agentstate]]
- [[assistant_app_agent_graph_route_entry]] → `references` → [[assistant_app_agent_graph_py_agentstate]]
- [[assistant_app_agent_graph_build_graph]] → `indirect_call` → [[assistant_app_agent_graph_route_entry]]
- [[assistant_app_agent_graph_build_graph]] → `indirect_call` → [[assistant_app_agent_nodes_executor_executor]]
- [[assistant_app_agent_graph_build_graph]] → `indirect_call` → [[assistant_app_agent_nodes_ingest_ingest_source]]
- [[assistant_app_agent_graph_build_graph]] → `indirect_call` → [[assistant_app_agent_nodes_planner_planner]]
- [[assistant_app_agent_graph_build_graph]] → `indirect_call` → [[assistant_app_agent_nodes_retrieve_retrieve_context]]
- [[assistant_app_agent_graph_build_graph]] → `indirect_call` → [[assistant_app_agent_state_agentstate]]
- [[assistant_app_agent_graph_build_graph]] → `references` → [[stategraph]]