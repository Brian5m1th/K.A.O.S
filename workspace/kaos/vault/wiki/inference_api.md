# assistant\app\api\inference_api.py

## Símbolos

- [[assistant_app_api_inference_api]] — code: inference_api.py
- [[assistant_app_api_inference_api_invokerequest]] — code: InvokeRequest
- [[assistant_app_api_inference_api_get_inference_service]] — code: get_inference_service()
- [[assistant_app_api_inference_api_invoke_inference]] — code: invoke_inference()
- [[assistant_app_api_inference_api_stream_inference]] — code: stream_inference()
- [[assistant_app_api_inference_api_list_models]] — code: list_models()
- [[assistant_app_api_inference_api_inference_health]] — code: inference_health()
- [[assistant_app_api_inference_api_rationale_1]] — code: Inference REST API — LLM model inference and provider management.  Endpoints:
- [[assistant_app_api_inference_api_rationale_50]] — code: Non-streaming LLM inference.
- [[assistant_app_api_inference_api_rationale_73]] — code: Streaming LLM inference via Server-Sent Events.
- [[assistant_app_api_inference_api_rationale_93]] — code: List available models grouped by provider.

## Dependências

- [[assistant_app_api_inference_api]] → `contains` → [[assistant_app_api_inference_api_get_inference_service]]
- [[assistant_app_api_inference_api]] → `contains` → [[assistant_app_api_inference_api_inference_health]]
- [[assistant_app_api_inference_api]] → `contains` → [[assistant_app_api_inference_api_invoke_inference]]
- [[assistant_app_api_inference_api]] → `contains` → [[assistant_app_api_inference_api_invokerequest]]
- [[assistant_app_api_inference_api]] → `contains` → [[assistant_app_api_inference_api_list_models]]
- [[assistant_app_api_inference_api]] → `contains` → [[assistant_app_api_inference_api_stream_inference]]
- [[assistant_app_api_inference_api]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_inference_api_rationale_1]] → `rationale_for` → [[assistant_app_api_inference_api]]
- [[assistant_app_api_inference_api_invoke_inference]] → `references` → [[assistant_app_api_inference_api_invokerequest]]
- [[assistant_app_api_inference_api_invokerequest]] → `inherits` → [[assistant_app_api_inference_api_py_basemodel]]
- [[assistant_app_api_inference_api_invokerequest]] → `uses` → [[assistant_app_core_services_inference_service_inferenceservice]]
- [[assistant_app_api_inference_api_invokerequest]] → `uses` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_api_inference_api_invokerequest]] → `uses` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter]]
- [[assistant_app_api_inference_api_invokerequest]] → `uses` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]]
- [[assistant_app_api_inference_api_invokerequest]] → `uses` → [[assistant_app_providers_inference_openai_adapter_claudeadapter]]
- [[assistant_app_api_inference_api_invokerequest]] → `uses` → [[assistant_app_providers_inference_openai_adapter_geminiadapter]]
- [[assistant_app_api_inference_api_invokerequest]] → `uses` → [[assistant_app_providers_inference_openai_adapter_openaiadapter]]
- [[assistant_app_api_inference_api_stream_inference]] → `references` → [[assistant_app_api_inference_api_invokerequest]]
- [[assistant_app_api_inference_api_get_inference_service]] → `references` → [[assistant_app_core_services_inference_service_inferenceservice]]
- [[assistant_app_api_inference_api_get_inference_service]] → `calls` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter]]
- [[assistant_app_api_inference_api_get_inference_service]] → `calls` → [[assistant_app_providers_inference_ollama_adapter_ollamaadapter]]
- [[assistant_app_api_inference_api_get_inference_service]] → `calls` → [[assistant_app_providers_inference_openai_adapter_claudeadapter]]
- [[assistant_app_api_inference_api_get_inference_service]] → `calls` → [[assistant_app_providers_inference_openai_adapter_geminiadapter]]
- [[assistant_app_api_inference_api_get_inference_service]] → `calls` → [[assistant_app_providers_inference_openai_adapter_openaiadapter]]
- [[assistant_app_api_inference_api_invoke_inference]] → `references` → [[assistant_app_core_services_inference_service_inferenceservice]]
- [[assistant_app_api_inference_api_invoke_inference]] → `calls` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_api_inference_api_rationale_50]] → `rationale_for` → [[assistant_app_api_inference_api_invoke_inference]]
- [[assistant_app_api_inference_api_rationale_73]] → `rationale_for` → [[assistant_app_api_inference_api_stream_inference]]
- [[assistant_app_api_inference_api_stream_inference]] → `references` → [[assistant_app_core_services_inference_service_inferenceservice]]
- [[assistant_app_api_inference_api_stream_inference]] → `calls` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_api_inference_api_stream_inference]] → `calls` → [[assistant_app_memory_summarizer_conversationsummarizer_generate]]
- [[assistant_app_api_inference_api_list_models]] → `references` → [[assistant_app_core_services_inference_service_inferenceservice]]
- [[assistant_app_api_inference_api_rationale_93]] → `rationale_for` → [[assistant_app_api_inference_api_list_models]]
- [[assistant_app_api_inference_api_inference_health]] → `references` → [[assistant_app_core_services_inference_service_inferenceservice]]