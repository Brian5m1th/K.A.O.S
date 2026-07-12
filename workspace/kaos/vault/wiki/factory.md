# assistant\app\llm\factory.py

## Símbolos

- [[assistant_app_llm_factory]] — code: factory.py
- [[assistant_app_llm_factory_llmfactory]] — code: LLMFactory
- [[assistant_app_llm_factory_llmfactory_init]] — code: .__init__()
- [[assistant_app_llm_factory_llmfactory_parse_fallback_chain]] — code: ._parse_fallback_chain()
- [[assistant_app_llm_factory_llmfactory_build]] — code: .build()
- [[assistant_app_llm_factory_llmfactory_resolve_model_config]] — code: ._resolve_model_config()
- [[assistant_app_llm_factory_llmfactory_create_provider]] — code: ._create_provider()
- [[assistant_app_llm_factory_llmfactory_ainvoke_with_fallback]] — code: .ainvoke_with_fallback()
- [[assistant_app_llm_factory_llmfactory_chain_invoke]] — code: ._chain_invoke()
- [[assistant_app_llm_factory_llmfactory_metrics]] — code: .metrics()

## Dependências

- [[assistant_app_llm_factory]] → `contains` → [[assistant_app_llm_factory_llmfactory]]
- [[assistant_app_llm_factory_llmfactory]] → `method` → [[assistant_app_llm_factory_llmfactory_ainvoke_with_fallback]]
- [[assistant_app_llm_factory_llmfactory]] → `method` → [[assistant_app_llm_factory_llmfactory_build]]
- [[assistant_app_llm_factory_llmfactory]] → `method` → [[assistant_app_llm_factory_llmfactory_chain_invoke]]
- [[assistant_app_llm_factory_llmfactory]] → `method` → [[assistant_app_llm_factory_llmfactory_create_provider]]
- [[assistant_app_llm_factory_llmfactory]] → `method` → [[assistant_app_llm_factory_llmfactory_init]]
- [[assistant_app_llm_factory_llmfactory]] → `method` → [[assistant_app_llm_factory_llmfactory_metrics]]
- [[assistant_app_llm_factory_llmfactory]] → `method` → [[assistant_app_llm_factory_llmfactory_parse_fallback_chain]]
- [[assistant_app_llm_factory_llmfactory]] → `method` → [[assistant_app_llm_factory_llmfactory_resolve_model_config]]
- [[assistant_app_llm_factory_llmfactory]] → `uses` → [[assistant_app_llm_metrics_providermetrics]]
- [[assistant_app_llm_factory_llmfactory]] → `uses` → [[assistant_app_llm_provider_baseprovider]]
- [[assistant_app_llm_factory_llmfactory]] → `uses` → [[assistant_app_llm_providers_airllm_provider_airllmprovider]]
- [[assistant_app_llm_factory_llmfactory]] → `uses` → [[assistant_app_llm_providers_claude_provider_claudeprovider]]
- [[assistant_app_llm_factory_llmfactory]] → `uses` → [[assistant_app_llm_providers_gemini_provider_geminiprovider]]
- [[assistant_app_llm_factory_llmfactory]] → `uses` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider]]
- [[assistant_app_llm_factory_llmfactory]] → `uses` → [[assistant_app_llm_providers_openai_provider_openaiprovider]]
- [[assistant_app_llm_factory_llmfactory_init]] → `calls` → [[assistant_app_llm_factory_llmfactory_parse_fallback_chain]]
- [[assistant_app_llm_factory_llmfactory_init]] → `calls` → [[assistant_app_llm_metrics_providermetrics]]
- [[assistant_app_llm_factory_llmfactory_build]] → `calls` → [[assistant_app_llm_factory_llmfactory_create_provider]]
- [[assistant_app_llm_factory_llmfactory_build]] → `calls` → [[assistant_app_llm_factory_llmfactory_resolve_model_config]]
- [[assistant_app_llm_factory_llmfactory_build]] → `references` → [[assistant_app_llm_provider_baseprovider]]
- [[assistant_app_llm_factory_llmfactory_chain_invoke]] → `calls` → [[assistant_app_llm_factory_llmfactory_build]]
- [[assistant_app_llm_factory_llmfactory_resolve_model_config]] → `calls` → [[assistant_app_setup_provider_config_get_active_provider_config]]
- [[assistant_app_llm_factory_llmfactory_chain_invoke]] → `calls` → [[assistant_app_llm_factory_llmfactory_create_provider]]
- [[assistant_app_llm_factory_llmfactory_create_provider]] → `references` → [[assistant_app_llm_provider_baseprovider]]
- [[assistant_app_llm_factory_llmfactory_create_provider]] → `calls` → [[assistant_app_llm_providers_airllm_provider_airllmprovider]]
- [[assistant_app_llm_factory_llmfactory_create_provider]] → `calls` → [[assistant_app_llm_providers_claude_provider_claudeprovider]]
- [[assistant_app_llm_factory_llmfactory_create_provider]] → `calls` → [[assistant_app_llm_providers_gemini_provider_geminiprovider]]
- [[assistant_app_llm_factory_llmfactory_create_provider]] → `calls` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider]]
- [[assistant_app_llm_factory_llmfactory_create_provider]] → `calls` → [[assistant_app_llm_providers_openai_provider_openaiprovider]]
- [[assistant_app_llm_factory_llmfactory_ainvoke_with_fallback]] → `calls` → [[assistant_app_llm_factory_llmfactory_chain_invoke]]
- [[assistant_app_llm_factory_llmfactory_metrics]] → `references` → [[assistant_app_llm_metrics_providermetrics]]