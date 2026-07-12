# assistant\tests\unit\test_model_registry.py

## Símbolos

- [[assistant_tests_unit_test_model_registry]] — code: test_model_registry.py
- [[assistant_tests_unit_test_model_registry_mock_session]] — code: mock_session()
- [[assistant_tests_unit_test_model_registry_test_get_model]] — code: test_get_model()
- [[assistant_tests_unit_test_model_registry_test_get_model_not_found]] — code: test_get_model_not_found()
- [[assistant_tests_unit_test_model_registry_test_list_by_capability]] — code: test_list_by_capability()
- [[assistant_tests_unit_test_model_registry_test_list_all]] — code: test_list_all()

## Dependências

- [[assistant_tests_unit_test_model_registry_test_get_model]] → `calls` → [[assistant_app_models_model_registry_modelregistry]]
- [[assistant_tests_unit_test_model_registry_test_get_model_not_found]] → `calls` → [[assistant_app_models_model_registry_modelregistry]]
- [[assistant_tests_unit_test_model_registry_test_list_all]] → `calls` → [[assistant_app_models_model_registry_modelregistry]]
- [[assistant_tests_unit_test_model_registry_test_list_by_capability]] → `calls` → [[assistant_app_models_model_registry_modelregistry]]
- [[assistant_tests_unit_test_model_registry_test_get_model]] → `calls` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_tests_unit_test_model_registry]] → `contains` → [[assistant_tests_unit_test_model_registry_mock_session]]
- [[assistant_tests_unit_test_model_registry]] → `contains` → [[assistant_tests_unit_test_model_registry_test_get_model]]
- [[assistant_tests_unit_test_model_registry]] → `contains` → [[assistant_tests_unit_test_model_registry_test_get_model_not_found]]
- [[assistant_tests_unit_test_model_registry]] → `contains` → [[assistant_tests_unit_test_model_registry_test_list_all]]
- [[assistant_tests_unit_test_model_registry]] → `contains` → [[assistant_tests_unit_test_model_registry_test_list_by_capability]]