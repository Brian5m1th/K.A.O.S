# assistant\tests\unit\test_dashboard_contract.py

## Símbolos

- [[assistant_tests_unit_test_dashboard_contract]] — code: test_dashboard_contract.py
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract]] — code: TestDashboardContract
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_returns_required_fields]] — code: .test_dashboard_returns_required_fields()
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_returns_null_on_failure_not_fabricated]] — code: .test_dashboard_returns_null_on_failure_not_fabricated()
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_services_structure]] — code: .test_dashboard_services_structure()
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_runtime_vram_null_on_cpu_mode]] — code: .test_dashboard_runtime_vram_null_on_cpu_mode()
- [[assistant_tests_unit_test_dashboard_contract_testreadinesscontract]] — code: TestReadinessContract
- [[assistant_tests_unit_test_dashboard_contract_testreadinesscontract_test_readiness_returns_required_fields]] — code: .test_readiness_returns_required_fields()
- [[assistant_tests_unit_test_dashboard_contract_rationale_1]] — code: Contract validation tests for K.A.O.S system dashboard endpoint.  Ensures /api/s
- [[assistant_tests_unit_test_dashboard_contract_rationale_13]] — code: Validate /api/system/dashboard response schema.
- [[assistant_tests_unit_test_dashboard_contract_rationale_17]] — code: Dashboard must include services, runtime, metrics, costs, dlq, alerts.
- [[assistant_tests_unit_test_dashboard_contract_rationale_50]] — code: When sub-resolver fails, dashboard must return None, not fabricated zeros.
- [[assistant_tests_unit_test_dashboard_contract_rationale_78]] — code: Services object must have all expected keys.
- [[assistant_tests_unit_test_dashboard_contract_rationale_107]] — code: VRAM must be null when no GPU detected (Constitution Article I).
- [[assistant_tests_unit_test_dashboard_contract_rationale_138]] — code: Validate /api/system/readiness response schema.
- [[assistant_tests_unit_test_dashboard_contract_rationale_142]] — code: Readiness must include ready, degraded, message, services, vectors.

## Dependências

- [[assistant_tests_unit_test_dashboard_contract_testreadinesscontract_test_readiness_returns_required_fields]] → `calls` → [[assistant_app_api_system_system_readiness]]
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_returns_null_on_failure_not_fabricated]] → `calls` → [[assistant_app_api_system_system_dashboard]]
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_returns_required_fields]] → `calls` → [[assistant_app_api_system_system_dashboard]]
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_runtime_vram_null_on_cpu_mode]] → `calls` → [[assistant_app_api_system_system_dashboard]]
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_services_structure]] → `calls` → [[assistant_app_api_system_system_dashboard]]
- [[assistant_tests_unit_test_dashboard_contract]] → `contains` → [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract]]
- [[assistant_tests_unit_test_dashboard_contract]] → `contains` → [[assistant_tests_unit_test_dashboard_contract_testreadinesscontract]]
- [[assistant_tests_unit_test_dashboard_contract_rationale_1]] → `rationale_for` → [[assistant_tests_unit_test_dashboard_contract]]
- [[assistant_tests_unit_test_dashboard_contract_rationale_13]] → `rationale_for` → [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract]]
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract]] → `method` → [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_returns_null_on_failure_not_fabricated]]
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract]] → `method` → [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_returns_required_fields]]
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract]] → `method` → [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_runtime_vram_null_on_cpu_mode]]
- [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract]] → `method` → [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_services_structure]]
- [[assistant_tests_unit_test_dashboard_contract_rationale_17]] → `rationale_for` → [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_returns_required_fields]]
- [[assistant_tests_unit_test_dashboard_contract_rationale_50]] → `rationale_for` → [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_returns_null_on_failure_not_fabricated]]
- [[assistant_tests_unit_test_dashboard_contract_rationale_78]] → `rationale_for` → [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_services_structure]]
- [[assistant_tests_unit_test_dashboard_contract_rationale_107]] → `rationale_for` → [[assistant_tests_unit_test_dashboard_contract_testdashboardcontract_test_dashboard_runtime_vram_null_on_cpu_mode]]
- [[assistant_tests_unit_test_dashboard_contract_rationale_138]] → `rationale_for` → [[assistant_tests_unit_test_dashboard_contract_testreadinesscontract]]
- [[assistant_tests_unit_test_dashboard_contract_testreadinesscontract]] → `method` → [[assistant_tests_unit_test_dashboard_contract_testreadinesscontract_test_readiness_returns_required_fields]]
- [[assistant_tests_unit_test_dashboard_contract_rationale_142]] → `rationale_for` → [[assistant_tests_unit_test_dashboard_contract_testreadinesscontract_test_readiness_returns_required_fields]]