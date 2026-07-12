# assistant\tests\test_openai.py

## Símbolos

- [[assistant_tests_test_openai]] — code: test_openai.py
- [[assistant_tests_test_openai_client]] — code: client()
- [[assistant_tests_test_openai_read_sse]] — code: _read_sse()
- [[assistant_tests_test_openai_test_openai_chat_completions]] — code: test_openai_chat_completions()
- [[assistant_tests_test_openai_test_openai_chat_completions_no_user_message]] — code: test_openai_chat_completions_no_user_message()
- [[assistant_tests_test_openai_test_openai_chat_completions_empty_body_returns_422]] — code: test_openai_chat_completions_empty_body_returns_422()

## Dependências

- [[assistant_tests_test_openai_test_openai_chat_completions]] → `calls` → [[assistant_app_domain_intent_intentresult]]
- [[assistant_tests_test_openai_test_openai_chat_completions_no_user_message]] → `calls` → [[assistant_app_domain_intent_intentresult]]
- [[assistant_tests_test_openai]] → `imports_from` → [[assistant_app_main]]
- [[assistant_tests_test_openai]] → `contains` → [[assistant_tests_test_openai_client]]
- [[assistant_tests_test_openai]] → `contains` → [[assistant_tests_test_openai_read_sse]]
- [[assistant_tests_test_openai]] → `contains` → [[assistant_tests_test_openai_test_openai_chat_completions]]
- [[assistant_tests_test_openai]] → `contains` → [[assistant_tests_test_openai_test_openai_chat_completions_empty_body_returns_422]]
- [[assistant_tests_test_openai]] → `contains` → [[assistant_tests_test_openai_test_openai_chat_completions_no_user_message]]
- [[assistant_tests_test_openai_client]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_openai_test_openai_chat_completions]] → `calls` → [[assistant_tests_test_openai_read_sse]]
- [[assistant_tests_test_openai_test_openai_chat_completions_no_user_message]] → `calls` → [[assistant_tests_test_openai_read_sse]]
- [[assistant_tests_test_openai_test_openai_chat_completions]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_openai_test_openai_chat_completions_no_user_message]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_openai_test_openai_chat_completions_empty_body_returns_422]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]