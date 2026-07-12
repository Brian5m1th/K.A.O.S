# assistant\tests\test_chat.py

## Símbolos

- [[assistant_tests_test_chat]] — code: test_chat.py
- [[assistant_tests_test_chat_client]] — code: client()
- [[assistant_tests_test_chat_test_send_message_streams_response]] — code: test_send_message_streams_response()
- [[assistant_tests_test_chat_test_send_message_empty_content_returns_422]] — code: test_send_message_empty_content_returns_422()
- [[assistant_tests_test_chat_test_readiness_degraded_when_ollama_unavailable]] — code: test_readiness_degraded_when_ollama_unavailable()
- [[assistant_tests_test_chat_test_readiness_ready_when_ollama_available]] — code: test_readiness_ready_when_ollama_available()

## Dependências

- [[assistant_tests_test_chat_test_send_message_streams_response]] → `calls` → [[assistant_app_domain_intent_intentresult]]
- [[assistant_tests_test_chat]] → `imports_from` → [[assistant_app_main]]
- [[assistant_tests_test_chat]] → `contains` → [[assistant_tests_test_chat_client]]
- [[assistant_tests_test_chat]] → `contains` → [[assistant_tests_test_chat_test_readiness_degraded_when_ollama_unavailable]]
- [[assistant_tests_test_chat]] → `contains` → [[assistant_tests_test_chat_test_readiness_ready_when_ollama_available]]
- [[assistant_tests_test_chat]] → `contains` → [[assistant_tests_test_chat_test_send_message_empty_content_returns_422]]
- [[assistant_tests_test_chat]] → `contains` → [[assistant_tests_test_chat_test_send_message_streams_response]]
- [[assistant_tests_test_chat_client]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_chat_test_send_message_streams_response]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_chat_test_send_message_empty_content_returns_422]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_chat_test_readiness_degraded_when_ollama_unavailable]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]
- [[assistant_tests_test_chat_test_readiness_ready_when_ollama_available]] → `references` → [[graphify_worked_httpx_raw_client_asyncclient]]