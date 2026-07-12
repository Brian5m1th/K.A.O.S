# assistant\tests\unit\test_communication_runtime.py

## Símbolos

- [[assistant_tests_unit_test_communication_runtime]] — code: test_communication_runtime.py
- [[assistant_tests_unit_test_communication_runtime_mockprovider]] — code: MockProvider
- [[assistant_tests_unit_test_communication_runtime_mockprovider_connect]] — code: .connect()
- [[assistant_tests_unit_test_communication_runtime_mockprovider_disconnect]] — code: .disconnect()
- [[assistant_tests_unit_test_communication_runtime_mockprovider_health]] — code: .health()
- [[assistant_tests_unit_test_communication_runtime_mockprovider_send]] — code: .send()
- [[assistant_tests_unit_test_communication_runtime_mockprovider_receive]] — code: .receive()
- [[assistant_tests_unit_test_communication_runtime_mockprovider_authenticate]] — code: .authenticate()
- [[assistant_tests_unit_test_communication_runtime_mockprovider_refresh]] — code: .refresh()
- [[assistant_tests_unit_test_communication_runtime_test_communication_runtime_routing]] — code: test_communication_runtime_routing()

## Dependências

- [[assistant_tests_unit_test_communication_runtime_mockprovider]] → `inherits` → [[assistant_app_runtime_communication_base_communicationprovider]]
- [[assistant_tests_unit_test_communication_runtime_test_communication_runtime_routing]] → `indirect_call` → [[assistant_app_runtime_communication_manager_communicationruntime]]
- [[assistant_tests_unit_test_communication_runtime_test_communication_runtime_routing]] → `calls` → [[assistant_app_runtime_registry_runtimeregistry_get]]
- [[assistant_tests_unit_test_communication_runtime]] → `contains` → [[assistant_tests_unit_test_communication_runtime_mockprovider]]
- [[assistant_tests_unit_test_communication_runtime]] → `contains` → [[assistant_tests_unit_test_communication_runtime_test_communication_runtime_routing]]
- [[assistant_tests_unit_test_communication_runtime_mockprovider]] → `method` → [[assistant_tests_unit_test_communication_runtime_mockprovider_authenticate]]
- [[assistant_tests_unit_test_communication_runtime_mockprovider]] → `method` → [[assistant_tests_unit_test_communication_runtime_mockprovider_connect]]
- [[assistant_tests_unit_test_communication_runtime_mockprovider]] → `method` → [[assistant_tests_unit_test_communication_runtime_mockprovider_disconnect]]
- [[assistant_tests_unit_test_communication_runtime_mockprovider]] → `method` → [[assistant_tests_unit_test_communication_runtime_mockprovider_health]]
- [[assistant_tests_unit_test_communication_runtime_mockprovider]] → `method` → [[assistant_tests_unit_test_communication_runtime_mockprovider_receive]]
- [[assistant_tests_unit_test_communication_runtime_mockprovider]] → `method` → [[assistant_tests_unit_test_communication_runtime_mockprovider_refresh]]
- [[assistant_tests_unit_test_communication_runtime_mockprovider]] → `method` → [[assistant_tests_unit_test_communication_runtime_mockprovider_send]]
- [[assistant_tests_unit_test_communication_runtime_test_communication_runtime_routing]] → `calls` → [[assistant_tests_unit_test_communication_runtime_mockprovider]]
- [[assistant_tests_unit_test_communication_runtime_test_communication_runtime_routing]] → `calls` → [[assistant_tests_unit_test_communication_runtime_mockprovider_send]]