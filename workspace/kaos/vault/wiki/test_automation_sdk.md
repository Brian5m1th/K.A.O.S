# assistant\tests\unit\test_automation_sdk.py

## Símbolos

- [[assistant_tests_unit_test_automation_sdk]] — code: test_automation_sdk.py
- [[assistant_tests_unit_test_automation_sdk_test_automation_service_trigger]] — code: test_automation_service_trigger()
- [[assistant_tests_unit_test_automation_sdk_test_automation_service_emit]] — code: test_automation_service_emit()
- [[assistant_tests_unit_test_automation_sdk_test_automation_service_wait_for]] — code: test_automation_service_wait_for()

## Dependências

- [[assistant_tests_unit_test_automation_sdk_test_automation_service_trigger]] → `calls` → [[assistant_app_core_automation_sdk_automationservice_trigger]]
- [[assistant_tests_unit_test_automation_sdk_test_automation_service_emit]] → `calls` → [[assistant_app_core_automation_sdk_automationservice_emit]]
- [[assistant_tests_unit_test_automation_sdk_test_automation_service_wait_for]] → `calls` → [[assistant_app_core_automation_sdk_automationservice_wait_for]]
- [[assistant_tests_unit_test_automation_sdk_test_automation_service_wait_for]] → `indirect_call` → [[assistant_app_models_automation_registry_automationexecution]]
- [[assistant_tests_unit_test_automation_sdk]] → `contains` → [[assistant_tests_unit_test_automation_sdk_test_automation_service_emit]]
- [[assistant_tests_unit_test_automation_sdk]] → `contains` → [[assistant_tests_unit_test_automation_sdk_test_automation_service_trigger]]
- [[assistant_tests_unit_test_automation_sdk]] → `contains` → [[assistant_tests_unit_test_automation_sdk_test_automation_service_wait_for]]