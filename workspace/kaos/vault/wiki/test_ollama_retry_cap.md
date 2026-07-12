# graphify\tests\test_ollama_retry_cap.py

## Símbolos

- [[graphify_tests_test_ollama_retry_cap]] — code: test_ollama_retry_cap.py
- [[graphify_tests_test_ollama_retry_cap_capture_client_kwargs]] — code: _capture_client_kwargs()
- [[graphify_tests_test_ollama_retry_cap_test_ollama_defaults_to_zero_sdk_retries]] — code: test_ollama_defaults_to_zero_sdk_retries()
- [[graphify_tests_test_ollama_retry_cap_test_ollama_honors_explicit_max_retries]] — code: test_ollama_honors_explicit_max_retries()
- [[graphify_tests_test_ollama_retry_cap_test_cloud_backend_keeps_default_retries]] — code: test_cloud_backend_keeps_default_retries()
- [[graphify_tests_test_ollama_retry_cap_test_api_timeout_is_passed_to_client]] — code: test_api_timeout_is_passed_to_client()
- [[graphify_tests_test_ollama_retry_cap_rationale_1]] — code: #1686 - a wedged local Ollama request must not multiply --api-timeout by the SD

## Dependências

- [[graphify_tests_test_ollama_retry_cap]] → `imports` → [[graphify_graphify_llm]]
- [[graphify_tests_test_ollama_retry_cap]] → `contains` → [[graphify_tests_test_ollama_retry_cap_capture_client_kwargs]]
- [[graphify_tests_test_ollama_retry_cap]] → `contains` → [[graphify_tests_test_ollama_retry_cap_test_api_timeout_is_passed_to_client]]
- [[graphify_tests_test_ollama_retry_cap]] → `contains` → [[graphify_tests_test_ollama_retry_cap_test_cloud_backend_keeps_default_retries]]
- [[graphify_tests_test_ollama_retry_cap]] → `contains` → [[graphify_tests_test_ollama_retry_cap_test_ollama_defaults_to_zero_sdk_retries]]
- [[graphify_tests_test_ollama_retry_cap]] → `contains` → [[graphify_tests_test_ollama_retry_cap_test_ollama_honors_explicit_max_retries]]
- [[graphify_tests_test_ollama_retry_cap_rationale_1]] → `rationale_for` → [[graphify_tests_test_ollama_retry_cap]]
- [[graphify_tests_test_ollama_retry_cap_test_api_timeout_is_passed_to_client]] → `calls` → [[graphify_tests_test_ollama_retry_cap_capture_client_kwargs]]
- [[graphify_tests_test_ollama_retry_cap_test_cloud_backend_keeps_default_retries]] → `calls` → [[graphify_tests_test_ollama_retry_cap_capture_client_kwargs]]
- [[graphify_tests_test_ollama_retry_cap_test_ollama_defaults_to_zero_sdk_retries]] → `calls` → [[graphify_tests_test_ollama_retry_cap_capture_client_kwargs]]
- [[graphify_tests_test_ollama_retry_cap_test_ollama_honors_explicit_max_retries]] → `calls` → [[graphify_tests_test_ollama_retry_cap_capture_client_kwargs]]