# assistant\app\core\services\planner_service.py

## Símbolos

- [[assistant_app_core_services_planner_service]] — code: planner_service.py
- [[assistant_app_core_services_planner_service_plannerservice]] — code: PlannerService
- [[assistant_app_core_services_planner_service_plannerservice_init]] — code: .__init__()
- [[assistant_app_core_services_planner_service_plannerservice_plan]] — code: .plan()
- [[assistant_app_core_services_planner_service_plannerservice_execute]] — code: .execute()
- [[assistant_app_core_services_planner_service_plannerservice_status]] — code: .status()
- [[assistant_app_core_services_planner_service_plannerservice_health]] — code: .health()
- [[assistant_app_core_services_planner_service_rationale_1]] — code: PlannerService — Task planning orchestrator.
- [[assistant_app_core_services_planner_service_rationale_10]] — code: Service for task decomposition and agent orchestration.

## Dependências

- [[assistant_app_core_services_planner_service_plannerservice]] → `uses` → [[assistant_app_core_provider_registry_providerregistry]]
- [[assistant_app_core_services_planner_service]] → `contains` → [[assistant_app_core_services_planner_service_plannerservice]]
- [[assistant_app_core_services_planner_service_rationale_1]] → `rationale_for` → [[assistant_app_core_services_planner_service]]
- [[assistant_app_core_services_planner_service_plannerservice]] → `method` → [[assistant_app_core_services_planner_service_plannerservice_execute]]
- [[assistant_app_core_services_planner_service_plannerservice]] → `method` → [[assistant_app_core_services_planner_service_plannerservice_health]]
- [[assistant_app_core_services_planner_service_plannerservice]] → `method` → [[assistant_app_core_services_planner_service_plannerservice_init]]
- [[assistant_app_core_services_planner_service_plannerservice]] → `method` → [[assistant_app_core_services_planner_service_plannerservice_plan]]
- [[assistant_app_core_services_planner_service_plannerservice]] → `method` → [[assistant_app_core_services_planner_service_plannerservice_status]]
- [[assistant_app_core_services_planner_service_plannerservice]] → `uses` → [[assistant_app_domain_ports_planner_port_plannerport]]
- [[assistant_app_core_services_planner_service_plannerservice]] → `uses` → [[assistant_app_domain_ports_planner_port_planrequest]]
- [[assistant_app_core_services_planner_service_plannerservice]] → `uses` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_core_services_planner_service_rationale_10]] → `rationale_for` → [[assistant_app_core_services_planner_service_plannerservice]]
- [[assistant_app_core_services_planner_service_plannerservice_plan]] → `references` → [[assistant_app_core_services_planner_service_py_planrequest]]
- [[assistant_app_core_services_planner_service_plannerservice_plan]] → `references` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_core_services_planner_service_plannerservice_execute]] → `references` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_core_services_planner_service_plannerservice_status]] → `references` → [[assistant_app_domain_ports_planner_port_planresult]]