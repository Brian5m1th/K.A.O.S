# assistant\app\providers\chat\ollama.py

## Símbolos

- [[assistant_app_providers_chat_ollama]] — code: ollama.py
- [[assistant_app_providers_chat_ollama_ollamachatprovider]] — code: OllamaChatProvider
- [[assistant_app_providers_chat_ollama_ollamachatprovider_init]] — code: .__init__()
- [[assistant_app_providers_chat_ollama_ollamachatprovider_chat]] — code: .chat()
- [[assistant_app_providers_chat_ollama_ollamachatprovider_stream]] — code: .stream()
- [[assistant_app_providers_chat_ollama_ollamachatprovider_models]] — code: .models()
- [[assistant_app_providers_chat_ollama_ollamachatprovider_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_providers_chat_ollama_ollamachatprovider]] → `uses` → [[assistant_app_domain_chat_message]]
- [[assistant_app_providers_chat_ollama_ollamachatprovider]] → `inherits` → [[assistant_app_providers_base_chat_basechatprovider]]
- [[assistant_app_providers_chat_ollama]] → `contains` → [[assistant_app_providers_chat_ollama_ollamachatprovider]]
- [[assistant_app_providers_chat_ollama_ollamachatprovider]] → `method` → [[assistant_app_providers_chat_ollama_ollamachatprovider_chat]]
- [[assistant_app_providers_chat_ollama_ollamachatprovider]] → `method` → [[assistant_app_providers_chat_ollama_ollamachatprovider_healthcheck]]
- [[assistant_app_providers_chat_ollama_ollamachatprovider]] → `method` → [[assistant_app_providers_chat_ollama_ollamachatprovider_init]]
- [[assistant_app_providers_chat_ollama_ollamachatprovider]] → `method` → [[assistant_app_providers_chat_ollama_ollamachatprovider_models]]
- [[assistant_app_providers_chat_ollama_ollamachatprovider]] → `method` → [[assistant_app_providers_chat_ollama_ollamachatprovider_stream]]
- [[assistant_app_providers_chat_ollama_ollamachatprovider_chat]] → `references` → [[assistant_app_providers_chat_ollama_py_message]]
- [[assistant_app_providers_chat_ollama_ollamachatprovider_stream]] → `references` → [[assistant_app_providers_chat_ollama_py_message]]