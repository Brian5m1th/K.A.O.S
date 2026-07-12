# assistant\tests\unit\test_desktop_apis.py

## Símbolos

- [[assistant_tests_unit_test_desktop_apis]] — code: test_desktop_apis.py
- [[assistant_tests_unit_test_desktop_apis_client]] — code: client()
- [[assistant_tests_unit_test_desktop_apis_test_get_user_exists]] — code: test_get_user_exists()
- [[assistant_tests_unit_test_desktop_apis_test_get_user_not_found]] — code: test_get_user_not_found()
- [[assistant_tests_unit_test_desktop_apis_test_upsert_user]] — code: test_upsert_user()
- [[assistant_tests_unit_test_desktop_apis_test_list_models]] — code: test_list_models()
- [[assistant_tests_unit_test_desktop_apis_test_get_model]] — code: test_get_model()
- [[assistant_tests_unit_test_desktop_apis_test_list_capability_policies]] — code: test_list_capability_policies()
- [[assistant_tests_unit_test_desktop_apis_test_create_capability_policy]] — code: test_create_capability_policy()
- [[assistant_tests_unit_test_desktop_apis_test_list_feature_flags]] — code: test_list_feature_flags()
- [[assistant_tests_unit_test_desktop_apis_test_get_feature_flag]] — code: test_get_feature_flag()
- [[assistant_tests_unit_test_desktop_apis_test_list_user_model_profiles]] — code: test_list_user_model_profiles()

## Dependências

- [[assistant_tests_unit_test_desktop_apis]] → `imports_from` → [[assistant_app_database]]
- [[assistant_tests_unit_test_desktop_apis]] → `imports_from` → [[assistant_app_main]]
- [[assistant_tests_unit_test_desktop_apis_test_list_capability_policies]] → `calls` → [[assistant_app_repositories_capability_policy_repository_capabilitypolicyrecord]]
- [[assistant_tests_unit_test_desktop_apis_test_list_feature_flags]] → `calls` → [[assistant_app_repositories_feature_flag_repository_featureflagrecord]]
- [[assistant_tests_unit_test_desktop_apis_test_get_model]] → `calls` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_tests_unit_test_desktop_apis_test_list_models]] → `calls` → [[assistant_app_repositories_model_repository_modelrecord]]
- [[assistant_tests_unit_test_desktop_apis_test_list_user_model_profiles]] → `calls` → [[assistant_app_repositories_user_model_profile_repository_usermodelprofilerecord]]
- [[assistant_tests_unit_test_desktop_apis_test_get_user_exists]] → `calls` → [[assistant_app_repositories_user_profile_repository_userprofilerecord]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_client]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_test_create_capability_policy]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_test_get_feature_flag]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_test_get_model]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_test_get_user_exists]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_test_get_user_not_found]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_test_list_capability_policies]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_test_list_feature_flags]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_test_list_models]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_test_list_user_model_profiles]]
- [[assistant_tests_unit_test_desktop_apis]] → `contains` → [[assistant_tests_unit_test_desktop_apis_test_upsert_user]]
- [[assistant_tests_unit_test_desktop_apis_client]] → `calls` → [[graphify_worked_httpx_raw_client_asyncclient]]