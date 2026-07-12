# assistant\app\service\llm_service.py

## Símbolos

- [[assistant_app_service_llm_service]] — code: llm_service.py
- [[assistant_app_service_llm_service_llmservice]] — code: LLMService
- [[assistant_app_service_llm_service_llmservice_init]] — code: .__init__()
- [[assistant_app_service_llm_service_llmservice_stream_chat]] — code: .stream_chat()
- [[assistant_app_service_llm_service_llmservice_check_availability]] — code: .check_availability()

## Dependências

- [[assistant_app_service_llm_service_llmservice]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_service_llm_service]] → `contains` → [[assistant_app_service_llm_service_llmservice]]
- [[assistant_app_service_llm_service_llmservice]] → `method` → [[assistant_app_service_llm_service_llmservice_check_availability]]
- [[assistant_app_service_llm_service_llmservice]] → `method` → [[assistant_app_service_llm_service_llmservice_init]]
- [[assistant_app_service_llm_service_llmservice]] → `method` → [[assistant_app_service_llm_service_llmservice_stream_chat]]
- [[assistant_app_service_llm_service_llmservice_stream_chat]] → `references` → [[assistant_app_service_llm_service_py_message]]