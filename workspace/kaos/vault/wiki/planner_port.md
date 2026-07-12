# assistant\app\domain\ports\planner_port.py

## Símbolos

- [[assistant_app_domain_ports_planner_port]] — code: planner_port.py
- [[assistant_app_domain_ports_planner_port_planstatus]] — code: PlanStatus
- [[assistant_app_domain_ports_planner_port_planstep]] — code: PlanStep
- [[assistant_app_domain_ports_planner_port_planrequest]] — code: PlanRequest
- [[assistant_app_domain_ports_planner_port_planresult]] — code: PlanResult
- [[assistant_app_domain_ports_planner_port_plannerport]] — code: PlannerPort
- [[assistant_app_domain_ports_planner_port_plannerport_provider_name]] — code: .provider_name()
- [[assistant_app_domain_ports_planner_port_plannerport_plan]] — code: .plan()
- [[assistant_app_domain_ports_planner_port_plannerport_execute]] — code: .execute()
- [[assistant_app_domain_ports_planner_port_plannerport_status]] — code: .status()
- [[assistant_app_domain_ports_planner_port_plannerport_health]] — code: .health()
- [[assistant_app_domain_ports_planner_port_rationale_1]] — code: PlannerPort — Task planning and agent orchestration capability.  Decomposes comp
- [[assistant_app_domain_ports_planner_port_rationale_26]] — code: A single step in an execution plan.
- [[assistant_app_domain_ports_planner_port_rationale_38]] — code: Request to generate an execution plan.
- [[assistant_app_domain_ports_planner_port_rationale_47]] — code: Generated execution plan.
- [[assistant_app_domain_ports_planner_port_rationale_55]] — code: Interface for task planning and orchestration.      Concrete implementations:
- [[assistant_app_domain_ports_planner_port_rationale_71]] — code: Generate an execution plan from an intent.
- [[assistant_app_domain_ports_planner_port_rationale_76]] — code: Execute a previously generated plan.
- [[assistant_app_domain_ports_planner_port_rationale_81]] — code: Check the status of a plan.

## Dependências

- [[assistant_app_domain_ports_planner_port]] → `contains` → [[assistant_app_domain_ports_planner_port_plannerport]]
- [[assistant_app_domain_ports_planner_port]] → `contains` → [[assistant_app_domain_ports_planner_port_planrequest]]
- [[assistant_app_domain_ports_planner_port]] → `contains` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_domain_ports_planner_port]] → `contains` → [[assistant_app_domain_ports_planner_port_planstatus]]
- [[assistant_app_domain_ports_planner_port]] → `contains` → [[assistant_app_domain_ports_planner_port_planstep]]
- [[assistant_app_domain_ports_planner_port]] → `imports_from` → [[assistant_app_domain_ports_planner_port_py_abc]]
- [[assistant_app_domain_ports_planner_port]] → `imports_from` → [[assistant_app_domain_ports_planner_port_py_enum]]
- [[assistant_app_domain_ports_planner_port_rationale_1]] → `rationale_for` → [[assistant_app_domain_ports_planner_port]]
- [[assistant_app_domain_ports_planner_port_planstatus]] → `inherits` → [[assistant_app_domain_ports_planner_port_py_enum]]
- [[assistant_app_domain_ports_planner_port_planstatus]] → `inherits` → [[assistant_app_domain_ports_planner_port_py_str]]
- [[assistant_app_domain_ports_planner_port_rationale_26]] → `rationale_for` → [[assistant_app_domain_ports_planner_port_planstep]]
- [[assistant_app_domain_ports_planner_port_plannerport_plan]] → `references` → [[assistant_app_domain_ports_planner_port_planrequest]]
- [[assistant_app_domain_ports_planner_port_rationale_38]] → `rationale_for` → [[assistant_app_domain_ports_planner_port_planrequest]]
- [[assistant_app_domain_ports_planner_port_plannerport_execute]] → `references` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_domain_ports_planner_port_plannerport_plan]] → `references` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_domain_ports_planner_port_plannerport_status]] → `references` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_domain_ports_planner_port_rationale_47]] → `rationale_for` → [[assistant_app_domain_ports_planner_port_planresult]]
- [[assistant_app_domain_ports_planner_port_plannerport]] → `method` → [[assistant_app_domain_ports_planner_port_plannerport_execute]]
- [[assistant_app_domain_ports_planner_port_plannerport]] → `method` → [[assistant_app_domain_ports_planner_port_plannerport_health]]
- [[assistant_app_domain_ports_planner_port_plannerport]] → `method` → [[assistant_app_domain_ports_planner_port_plannerport_plan]]
- [[assistant_app_domain_ports_planner_port_plannerport]] → `method` → [[assistant_app_domain_ports_planner_port_plannerport_provider_name]]
- [[assistant_app_domain_ports_planner_port_plannerport]] → `method` → [[assistant_app_domain_ports_planner_port_plannerport_status]]
- [[assistant_app_domain_ports_planner_port_plannerport]] → `inherits` → [[assistant_app_domain_ports_planner_port_py_abc]]
- [[assistant_app_domain_ports_planner_port_rationale_55]] → `rationale_for` → [[assistant_app_domain_ports_planner_port_plannerport]]
- [[assistant_app_domain_ports_planner_port_rationale_71]] → `rationale_for` → [[assistant_app_domain_ports_planner_port_plannerport_plan]]
- [[assistant_app_domain_ports_planner_port_rationale_76]] → `rationale_for` → [[assistant_app_domain_ports_planner_port_plannerport_execute]]
- [[assistant_app_domain_ports_planner_port_rationale_81]] → `rationale_for` → [[assistant_app_domain_ports_planner_port_plannerport_status]]