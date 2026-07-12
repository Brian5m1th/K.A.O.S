# assistant\tests\unit\test_audit_engine.py

## Símbolos

- [[assistant_tests_unit_test_audit_engine]] — code: test_audit_engine.py
- [[assistant_tests_unit_test_audit_engine_testdriftreport]] — code: TestDriftReport
- [[assistant_tests_unit_test_audit_engine_testdriftreport_test_create_default]] — code: .test_create_default()
- [[assistant_tests_unit_test_audit_engine_testdriftreport_test_create_with_data]] — code: .test_create_with_data()
- [[assistant_tests_unit_test_audit_engine_testauditengine]] — code: TestAuditEngine
- [[assistant_tests_unit_test_audit_engine_testauditengine_setup_method]] — code: .setup_method()
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_get_drift_level_low]] — code: .test_get_drift_level_low()
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_get_drift_level_medium]] — code: .test_get_drift_level_medium()
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_get_drift_level_high]] — code: .test_get_drift_level_high()
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_run_audit_returns_report]] — code: .test_run_audit_returns_report()
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_load_latest_report]] — code: .test_load_latest_report()

## Dependências

- [[assistant_tests_unit_test_audit_engine_testauditengine]] → `uses` → [[assistant_app_audit_audit_engine_driftreport]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_run_audit_returns_report]] → `indirect_call` → [[assistant_app_audit_audit_engine_driftreport]]
- [[assistant_tests_unit_test_audit_engine_testdriftreport]] → `uses` → [[assistant_app_audit_audit_engine_driftreport]]
- [[assistant_tests_unit_test_audit_engine_testdriftreport_test_create_default]] → `calls` → [[assistant_app_audit_audit_engine_driftreport]]
- [[assistant_tests_unit_test_audit_engine_testdriftreport_test_create_with_data]] → `calls` → [[assistant_app_audit_audit_engine_driftreport]]
- [[assistant_tests_unit_test_audit_engine_testauditengine]] → `uses` → [[assistant_app_audit_audit_engine_auditengine]]
- [[assistant_tests_unit_test_audit_engine_testdriftreport]] → `uses` → [[assistant_app_audit_audit_engine_auditengine]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_load_latest_report]] → `calls` → [[assistant_app_audit_audit_engine_auditengine_run_audit]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_run_audit_returns_report]] → `calls` → [[assistant_app_audit_audit_engine_auditengine_run_audit]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_get_drift_level_high]] → `calls` → [[assistant_app_audit_audit_engine_auditengine_get_drift_level]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_get_drift_level_low]] → `calls` → [[assistant_app_audit_audit_engine_auditengine_get_drift_level]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_get_drift_level_medium]] → `calls` → [[assistant_app_audit_audit_engine_auditengine_get_drift_level]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_load_latest_report]] → `calls` → [[assistant_app_audit_audit_engine_auditengine_load_latest_report]]
- [[assistant_tests_unit_test_audit_engine_testauditengine]] → `uses` → [[assistant_app_audit_feature_registry_featureentry]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_load_latest_report]] → `calls` → [[assistant_app_audit_feature_registry_featureentry]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_run_audit_returns_report]] → `calls` → [[assistant_app_audit_feature_registry_featureentry]]
- [[assistant_tests_unit_test_audit_engine_testdriftreport]] → `uses` → [[assistant_app_audit_feature_registry_featureentry]]
- [[assistant_tests_unit_test_audit_engine_testauditengine]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_tests_unit_test_audit_engine_testdriftreport]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_load_latest_report]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_register]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_test_run_audit_returns_report]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_register]]
- [[assistant_tests_unit_test_audit_engine_testauditengine_setup_method]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_clear]]
- [[assistant_tests_unit_test_audit_engine]] → `contains` → [[assistant_tests_unit_test_audit_engine_testauditengine]]
- [[assistant_tests_unit_test_audit_engine]] → `contains` → [[assistant_tests_unit_test_audit_engine_testdriftreport]]
- [[assistant_tests_unit_test_audit_engine_testdriftreport]] → `method` → [[assistant_tests_unit_test_audit_engine_testdriftreport_test_create_default]]
- [[assistant_tests_unit_test_audit_engine_testdriftreport]] → `method` → [[assistant_tests_unit_test_audit_engine_testdriftreport_test_create_with_data]]
- [[assistant_tests_unit_test_audit_engine_testauditengine]] → `method` → [[assistant_tests_unit_test_audit_engine_testauditengine_setup_method]]
- [[assistant_tests_unit_test_audit_engine_testauditengine]] → `method` → [[assistant_tests_unit_test_audit_engine_testauditengine_test_get_drift_level_high]]
- [[assistant_tests_unit_test_audit_engine_testauditengine]] → `method` → [[assistant_tests_unit_test_audit_engine_testauditengine_test_get_drift_level_low]]
- [[assistant_tests_unit_test_audit_engine_testauditengine]] → `method` → [[assistant_tests_unit_test_audit_engine_testauditengine_test_get_drift_level_medium]]
- [[assistant_tests_unit_test_audit_engine_testauditengine]] → `method` → [[assistant_tests_unit_test_audit_engine_testauditengine_test_load_latest_report]]
- [[assistant_tests_unit_test_audit_engine_testauditengine]] → `method` → [[assistant_tests_unit_test_audit_engine_testauditengine_test_run_audit_returns_report]]