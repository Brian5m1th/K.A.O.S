# assistant\app\providers\planner\langgraph_adapter.py

## Símbolos

- [[assistant_app_providers_planner_langgraph_adapter]] — code: langgraph_adapter.py
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] — code: LangGraphAdapter
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_provider_name]] — code: .provider_name()
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_plan]] — code: .plan()
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_execute]] — code: .execute()
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_status]] — code: .status()
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_health]] — code: .health()
- [[assistant_app_providers_planner_langgraph_adapter_rationale_1]] — code: LangGraphAdapter — Wraps existing LangGraph workflows for PlannerPort.  Provides
- [[assistant_app_providers_planner_langgraph_adapter_rationale_14]] — code: LangGraph-based planning and execution adapter.
- [[assistant_app_providers_planner_langgraph_adapter_rationale_21]] — code: Decompose intent into executable steps using existing agent graph.
- [[assistant_app_providers_planner_langgraph_adapter_rationale_47]] — code: Execute a plan through existing workflow engine.

## Dependências

- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] → `uses` → [[assistant_app_domain_ports_planner_port_planstatus]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] → `uses` → [[assistant_app_domain_ports_planner_port_planstep]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_plan]] → `calls` → [[assistant_app_domain_ports_planner_port_planstep]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] → `uses` → [[assistant_app_domain_ports_planner_port_planrequest]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] → `uses` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_execute]] → `references` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_plan]] → `references` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_status]] → `references` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] → `uses` → [[assistant_app_domain_ports_planner_port_plannerport]]
- [[assistant_app_providers_planner_langgraph_adapter]] → `contains` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]]
- [[assistant_app_providers_planner_langgraph_adapter_rationale_1]] → `rationale_for` → [[assistant_app_providers_planner_langgraph_adapter]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] → `method` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_execute]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] → `method` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_health]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] → `method` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_plan]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] → `method` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_provider_name]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]] → `method` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_status]]
- [[assistant_app_providers_planner_langgraph_adapter_rationale_14]] → `rationale_for` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]]
- [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_plan]] → `references` → [[assistant_app_providers_planner_langgraph_adapter_py_planrequest]]
- [[assistant_app_providers_planner_langgraph_adapter_rationale_21]] → `rationale_for` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_plan]]
- [[assistant_app_providers_planner_langgraph_adapter_rationale_47]] → `rationale_for` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter_execute]]