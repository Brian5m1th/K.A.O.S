# assistant\app\api\planner_api.py

## Símbolos

- [[assistant_app_api_planner_api]] — code: planner_api.py
- [[assistant_app_api_planner_api_planrequest]] — code: PlanRequest
- [[assistant_app_api_planner_api_executerequest]] — code: ExecuteRequest
- [[assistant_app_api_planner_api_get_planner_service]] — code: get_planner_service()
- [[assistant_app_api_planner_api_create_plan]] — code: create_plan()
- [[assistant_app_api_planner_api_execute_plan]] — code: execute_plan()
- [[assistant_app_api_planner_api_plan_status]] — code: plan_status()
- [[assistant_app_api_planner_api_planner_health]] — code: planner_health()
- [[assistant_app_api_planner_api_rationale_1]] — code: Planner REST API — Task planning and agent orchestration.  Endpoints:   POST /ap
- [[assistant_app_api_planner_api_rationale_44]] — code: Generate an execution plan from an intent.
- [[assistant_app_api_planner_api_rationale_67]] — code: Execute a previously generated plan.
- [[assistant_app_api_planner_api_rationale_77]] — code: Check the status of a plan.

## Dependências

- [[assistant_app_api_planner_api]] → `contains` → [[assistant_app_api_planner_api_create_plan]]
- [[assistant_app_api_planner_api]] → `contains` → [[assistant_app_api_planner_api_execute_plan]]
- [[assistant_app_api_planner_api]] → `contains` → [[assistant_app_api_planner_api_executerequest]]
- [[assistant_app_api_planner_api]] → `contains` → [[assistant_app_api_planner_api_get_planner_service]]
- [[assistant_app_api_planner_api]] → `contains` → [[assistant_app_api_planner_api_plan_status]]
- [[assistant_app_api_planner_api]] → `contains` → [[assistant_app_api_planner_api_planner_health]]
- [[assistant_app_api_planner_api]] → `contains` → [[assistant_app_api_planner_api_planrequest]]
- [[assistant_app_api_planner_api]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_planner_api_rationale_1]] → `rationale_for` → [[assistant_app_api_planner_api]]
- [[assistant_app_api_planner_api_create_plan]] → `references` → [[assistant_app_api_planner_api_planrequest]]
- [[assistant_app_api_planner_api_planrequest]] → `inherits` → [[assistant_app_api_planner_api_py_basemodel]]
- [[assistant_app_api_planner_api_planrequest]] → `uses` → [[assistant_app_core_services_planner_service_plannerservice]]
- [[assistant_app_api_planner_api_planrequest]] → `uses` → [[assistant_app_domain_ports_planner_port_planrequest]]
- [[assistant_app_api_planner_api_planrequest]] → `uses` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]]
- [[assistant_app_api_planner_api_executerequest]] → `inherits` → [[assistant_app_api_planner_api_py_basemodel]]
- [[assistant_app_api_planner_api_execute_plan]] → `references` → [[assistant_app_api_planner_api_executerequest]]
- [[assistant_app_api_planner_api_executerequest]] → `uses` → [[assistant_app_core_services_planner_service_plannerservice]]
- [[assistant_app_api_planner_api_executerequest]] → `uses` → [[assistant_app_domain_ports_planner_port_planrequest]]
- [[assistant_app_api_planner_api_executerequest]] → `uses` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]]
- [[assistant_app_api_planner_api_get_planner_service]] → `references` → [[assistant_app_core_services_planner_service_plannerservice]]
- [[assistant_app_api_planner_api_get_planner_service]] → `calls` → [[assistant_app_providers_planner_langgraph_adapter_langgraphadapter]]
- [[assistant_app_api_planner_api_create_plan]] → `references` → [[assistant_app_core_services_planner_service_plannerservice]]
- [[assistant_app_api_planner_api_rationale_44]] → `rationale_for` → [[assistant_app_api_planner_api_create_plan]]
- [[assistant_app_api_planner_api_execute_plan]] → `references` → [[assistant_app_core_services_planner_service_plannerservice]]
- [[assistant_app_api_planner_api_rationale_67]] → `rationale_for` → [[assistant_app_api_planner_api_execute_plan]]
- [[assistant_app_api_planner_api_plan_status]] → `references` → [[assistant_app_core_services_planner_service_plannerservice]]
- [[assistant_app_api_planner_api_rationale_77]] → `rationale_for` → [[assistant_app_api_planner_api_plan_status]]
- [[assistant_app_api_planner_api_planner_health]] → `references` → [[assistant_app_core_services_planner_service_plannerservice]]