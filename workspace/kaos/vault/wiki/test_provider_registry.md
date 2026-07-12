# graphify\tests\test_provider_registry.py

## Símbolos

- [[graphify_tests_test_provider_registry]] — code: test_provider_registry.py
- [[graphify_tests_test_provider_registry_test_custom_provider_add_list_show_remove]] — code: test_custom_provider_add_list_show_remove()
- [[graphify_tests_test_provider_registry_test_custom_provider_pricing_defaults_to_zero]] — code: test_custom_provider_pricing_defaults_to_zero()
- [[graphify_tests_test_provider_registry_test_custom_provider_cannot_shadow_builtin]] — code: test_custom_provider_cannot_shadow_builtin()
- [[graphify_tests_test_provider_registry_test_project_local_providers_ignored_without_optin]] — code: test_project_local_providers_ignored_without_optin()
- [[graphify_tests_test_provider_registry_test_project_local_providers_loaded_with_optin]] — code: test_project_local_providers_loaded_with_optin()
- [[graphify_tests_test_provider_registry_test_non_http_provider_base_url_rejected]] — code: test_non_http_provider_base_url_rejected()
- [[graphify_tests_test_provider_registry_test_provider_base_url_ok_scheme_and_warnings]] — code: test_provider_base_url_ok_scheme_and_warnings()
- [[graphify_tests_test_provider_registry_test_detect_backend_custom_provider_after_builtins]] — code: test_detect_backend_custom_provider_after_builtins()
- [[graphify_tests_test_provider_registry_rationale_7]] — code: Full round-trip: add → list → show → remove via providers.json.
- [[graphify_tests_test_provider_registry_rationale_31]] — code: Missing pricing field defaults to zero so estimate_cost doesn't blow up.
- [[graphify_tests_test_provider_registry_rationale_53]] — code: Built-in provider names are protected from being overridden.
- [[graphify_tests_test_provider_registry_rationale_73]] — code: A project-local ./.graphify/providers.json is NOT loaded by default (F1).
- [[graphify_tests_test_provider_registry_rationale_95]] — code: With explicit opt-in the project-local file is honoured (F1).
- [[graphify_tests_test_provider_registry_rationale_113]] — code: A provider whose base_url uses a non-http(s) scheme is skipped on load (F1).
- [[graphify_tests_test_provider_registry_rationale_129]] — code: provider_base_url_ok rejects bad schemes and warns on plaintext-http egress (F1)
- [[graphify_tests_test_provider_registry_rationale_142]] — code: Custom providers appear after all built-ins in detect_backend() priority.

## Dependências

- [[graphify_tests_test_provider_registry]] → `contains` → [[graphify_tests_test_provider_registry_test_custom_provider_add_list_show_remove]]
- [[graphify_tests_test_provider_registry]] → `contains` → [[graphify_tests_test_provider_registry_test_custom_provider_cannot_shadow_builtin]]
- [[graphify_tests_test_provider_registry]] → `contains` → [[graphify_tests_test_provider_registry_test_custom_provider_pricing_defaults_to_zero]]
- [[graphify_tests_test_provider_registry]] → `contains` → [[graphify_tests_test_provider_registry_test_detect_backend_custom_provider_after_builtins]]
- [[graphify_tests_test_provider_registry]] → `contains` → [[graphify_tests_test_provider_registry_test_non_http_provider_base_url_rejected]]
- [[graphify_tests_test_provider_registry]] → `contains` → [[graphify_tests_test_provider_registry_test_project_local_providers_ignored_without_optin]]
- [[graphify_tests_test_provider_registry]] → `contains` → [[graphify_tests_test_provider_registry_test_project_local_providers_loaded_with_optin]]
- [[graphify_tests_test_provider_registry]] → `contains` → [[graphify_tests_test_provider_registry_test_provider_base_url_ok_scheme_and_warnings]]
- [[graphify_tests_test_provider_registry_rationale_7]] → `rationale_for` → [[graphify_tests_test_provider_registry_test_custom_provider_add_list_show_remove]]
- [[graphify_tests_test_provider_registry_rationale_31]] → `rationale_for` → [[graphify_tests_test_provider_registry_test_custom_provider_pricing_defaults_to_zero]]
- [[graphify_tests_test_provider_registry_rationale_53]] → `rationale_for` → [[graphify_tests_test_provider_registry_test_custom_provider_cannot_shadow_builtin]]
- [[graphify_tests_test_provider_registry_rationale_73]] → `rationale_for` → [[graphify_tests_test_provider_registry_test_project_local_providers_ignored_without_optin]]
- [[graphify_tests_test_provider_registry_rationale_95]] → `rationale_for` → [[graphify_tests_test_provider_registry_test_project_local_providers_loaded_with_optin]]
- [[graphify_tests_test_provider_registry_rationale_113]] → `rationale_for` → [[graphify_tests_test_provider_registry_test_non_http_provider_base_url_rejected]]
- [[graphify_tests_test_provider_registry_rationale_129]] → `rationale_for` → [[graphify_tests_test_provider_registry_test_provider_base_url_ok_scheme_and_warnings]]
- [[graphify_tests_test_provider_registry_rationale_142]] → `rationale_for` → [[graphify_tests_test_provider_registry_test_detect_backend_custom_provider_after_builtins]]