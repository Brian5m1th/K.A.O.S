# assistant\app\llm\providers\ollama_provider.py

## Símbolos

- [[assistant_app_llm_providers_ollama_provider]] — code: ollama_provider.py
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider]] — code: OllamaProvider
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_init]] — code: .__init__()
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_rebuild]] — code: ._rebuild()
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_invoke]] — code: .invoke()
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_ainvoke]] — code: .ainvoke()
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_stream]] — code: .stream()
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_astream]] — code: .astream()
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_model_name]] — code: .model_name()
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_provider_name]] — code: .provider_name()

## Dependências

- [[assistant_app_llm_providers_ollama_provider_ollamaprovider]] → `uses` → [[assistant_app_llm_provider_baseprovider]]
- [[assistant_app_llm_providers_ollama_provider]] → `contains` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider]] → `method` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider_ainvoke]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider]] → `method` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider_astream]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider]] → `method` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider_init]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider]] → `method` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider_invoke]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider]] → `method` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider_model_name]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider]] → `method` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider_provider_name]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider]] → `method` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider_rebuild]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider]] → `method` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider_stream]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_astream]] → `calls` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider_rebuild]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_invoke]] → `references` → [[assistant_app_llm_providers_ollama_provider_py_basemessage]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_ainvoke]] → `references` → [[assistant_app_llm_providers_ollama_provider_py_basemessage]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_astream]] → `references` → [[assistant_app_llm_providers_ollama_provider_py_basemessage]]
- [[assistant_app_llm_providers_ollama_provider_ollamaprovider_stream]] → `references` → [[assistant_app_llm_providers_ollama_provider_py_basemessage]]