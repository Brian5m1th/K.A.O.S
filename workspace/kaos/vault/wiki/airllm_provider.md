# assistant\app\llm\providers\airllm_provider.py

## Símbolos

- [[assistant_app_llm_providers_airllm_provider]] — code: airllm_provider.py
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] — code: AirLLMProvider
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_init]] — code: .__init__()
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_get_model]] — code: ._get_model()
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_messages_to_prompt]] — code: ._messages_to_prompt()
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_sync_generate]] — code: ._sync_generate()
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_invoke]] — code: .invoke()
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_ainvoke]] — code: .ainvoke()
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_stream]] — code: .stream()
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_astream]] — code: .astream()
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_model_name]] — code: .model_name()
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_provider_name]] — code: .provider_name()
- [[assistant_app_llm_providers_airllm_provider_rationale_18]] — code: Lazy-load AirLLM AutoModel to save memory during startup.
- [[assistant_app_llm_providers_airllm_provider_rationale_31]] — code: Translate LangChain messages list to a formatted text prompt.
- [[assistant_app_llm_providers_airllm_provider_rationale_44]] — code: Run blocking model generation synchronously.

## Dependências

- [[assistant_app_llm_providers_airllm_provider_airllmprovider_get_model]] → `calls` → [[airllm_air_llm_airllm_auto_model_automodel]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `uses` → [[assistant_app_llm_provider_baseprovider]]
- [[assistant_app_llm_providers_airllm_provider]] → `contains` → [[assistant_app_llm_providers_airllm_provider_airllmprovider]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `method` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_ainvoke]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `method` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_astream]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `method` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_get_model]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `method` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_init]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `method` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_invoke]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `method` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_messages_to_prompt]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `method` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_model_name]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `method` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_provider_name]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `method` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_stream]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider]] → `method` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_sync_generate]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_sync_generate]] → `calls` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_get_model]]
- [[assistant_app_llm_providers_airllm_provider_rationale_18]] → `rationale_for` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_get_model]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_ainvoke]] → `calls` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_messages_to_prompt]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_invoke]] → `calls` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_messages_to_prompt]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_messages_to_prompt]] → `references` → [[assistant_app_llm_providers_airllm_provider_py_basemessage]]
- [[assistant_app_llm_providers_airllm_provider_rationale_31]] → `rationale_for` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_messages_to_prompt]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_ainvoke]] → `references` → [[assistant_app_llm_providers_airllm_provider_py_basemessage]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_astream]] → `references` → [[assistant_app_llm_providers_airllm_provider_py_basemessage]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_invoke]] → `references` → [[assistant_app_llm_providers_airllm_provider_py_basemessage]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_stream]] → `references` → [[assistant_app_llm_providers_airllm_provider_py_basemessage]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_invoke]] → `calls` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_sync_generate]]
- [[assistant_app_llm_providers_airllm_provider_rationale_44]] → `rationale_for` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_sync_generate]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_stream]] → `calls` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_invoke]]
- [[assistant_app_llm_providers_airllm_provider_airllmprovider_astream]] → `calls` → [[assistant_app_llm_providers_airllm_provider_airllmprovider_ainvoke]]