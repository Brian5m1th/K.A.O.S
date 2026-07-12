# assistant\app\domain\execution_plan.py

## Símbolos

- [[assistant_app_domain_execution_plan]] — code: execution_plan.py
- [[assistant_app_domain_execution_plan_capabilityprofile]] — code: CapabilityProfile
- [[assistant_app_domain_execution_plan_capabilityprofile_has]] — code: .has()
- [[assistant_app_domain_execution_plan_capabilityprofile_has_any]] — code: .has_any()
- [[assistant_app_domain_execution_plan_capabilityprofile_has_all]] — code: .has_all()
- [[assistant_app_domain_execution_plan_capabilityprofile_merge]] — code: .merge()
- [[assistant_app_domain_execution_plan_capabilityprofile_len]] — code: .__len__()
- [[assistant_app_domain_execution_plan_executionplan]] — code: ExecutionPlan
- [[assistant_app_domain_execution_plan_executionplan_create]] — code: .create()
- [[assistant_app_domain_execution_plan_executionplan_capability_profile]] — code: .capability_profile()

## Dependências

- [[assistant_app_domain_execution_plan]] → `contains` → [[assistant_app_domain_execution_plan_capabilityprofile]]
- [[assistant_app_domain_execution_plan]] → `contains` → [[assistant_app_domain_execution_plan_executionplan]]
- [[assistant_app_domain_execution_plan]] → `imports_from` → [[assistant_app_domain_execution_plan_py_uuid]]
- [[assistant_app_domain_execution_plan_capabilityprofile]] → `method` → [[assistant_app_domain_execution_plan_capabilityprofile_has]]
- [[assistant_app_domain_execution_plan_capabilityprofile]] → `method` → [[assistant_app_domain_execution_plan_capabilityprofile_has_all]]
- [[assistant_app_domain_execution_plan_capabilityprofile]] → `method` → [[assistant_app_domain_execution_plan_capabilityprofile_has_any]]
- [[assistant_app_domain_execution_plan_capabilityprofile]] → `method` → [[assistant_app_domain_execution_plan_capabilityprofile_len]]
- [[assistant_app_domain_execution_plan_capabilityprofile_merge]] → `calls` → [[assistant_app_domain_execution_plan_capabilityprofile]]
- [[assistant_app_domain_execution_plan_executionplan_capability_profile]] → `references` → [[assistant_app_domain_execution_plan_capabilityprofile]]
- [[assistant_app_domain_execution_plan_executionplan]] → `method` → [[assistant_app_domain_execution_plan_executionplan_capability_profile]]
- [[assistant_app_domain_execution_plan_executionplan]] → `method` → [[assistant_app_domain_execution_plan_executionplan_create]]
- [[assistant_app_domain_execution_plan_executionplan_create]] → `references` → [[assistant_app_domain_execution_plan_py_uuid]]