# assistant\app\providers\inference\ollama_adapter.py

## Símbolos

- [[assistant_app_providers_inference_ollama_adapter]] — code: ollama_adapter.py
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] — code: OllamaAdapter
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_provider_name]] — code: .provider_name()
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_invoke]] — code: .invoke()
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_stream]] — code: .stream()
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_health]] — code: .health()
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_list_models]] — code: .list_models()
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_to_langchain]] — code: ._to_langchain()
- [[assistant_app_providers_inference_ollama_adapter_rationale_1]] — code: OllamaAdapter — Wraps OllamaProvider for InferencePort.  Provides local LLM infe
- [[assistant_app_providers_inference_ollama_adapter_rationale_15]] — code: Local Ollama inference adapter.

## Dependências

- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] → `uses` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_invoke]] → `references` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_stream]] → `references` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] → `uses` → [[assistant_app_domain_ports_inference_port_inferenceresult]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] → `uses` → [[assistant_app_domain_ports_inference_port_inferenceport]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] → `uses` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_invoke]] → `calls` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_stream]] → `calls` → [[assistant_app_llm_providers_ollama_provider_ollamaprovider]]
- [[assistant_app_providers_inference_ollama_adapter]] → `contains` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]]
- [[assistant_app_providers_inference_ollama_adapter_rationale_1]] → `rationale_for` → [[assistant_app_providers_inference_ollama_adapter]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] → `method` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_health]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] → `method` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_invoke]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] → `method` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_list_models]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] → `method` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_provider_name]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] → `method` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_stream]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]] → `method` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_to_langchain]]
- [[assistant_app_providers_inference_ollama_adapter_rationale_15]] → `rationale_for` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_invoke]] → `calls` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_to_langchain]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_invoke]] → `references` → [[assistant_app_providers_inference_ollama_adapter_py_inferenceresult]]
- [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_stream]] → `calls` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter_to_langchain]]