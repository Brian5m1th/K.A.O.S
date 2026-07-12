# assistant\app\providers\inference\airllm_adapter.py

## Símbolos

- [[assistant_app_providers_inference_airllm_adapter]] — code: airllm_adapter.py
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] — code: AirLLMAdapter
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_provider_name]] — code: .provider_name()
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_invoke]] — code: .invoke()
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_stream]] — code: .stream()
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_health]] — code: .health()
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_list_models]] — code: .list_models()
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_to_langchain]] — code: ._to_langchain()
- [[assistant_app_providers_inference_airllm_adapter_rationale_1]] — code: AirLLMAdapter — Wraps AirLLMProvider for InferencePort.  Layer-wise inference fo
- [[assistant_app_providers_inference_airllm_adapter_rationale_15]] — code: Local AirLLM layer-wise inference adapter.

## Dependências

- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] → `uses` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_invoke]] → `references` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_stream]] → `references` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] → `uses` → [[assistant_app_domain_ports_inference_port_inferenceresult]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] → `uses` → [[assistant_app_domain_ports_inference_port_inferenceport]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] → `uses` → [[assistant_app_llm_providers_airllm_provider_airllmprovider]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_invoke]] → `calls` → [[assistant_app_llm_providers_airllm_provider_airllmprovider]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_stream]] → `calls` → [[assistant_app_llm_providers_airllm_provider_airllmprovider]]
- [[assistant_app_providers_inference_airllm_adapter]] → `contains` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter]]
- [[assistant_app_providers_inference_airllm_adapter_rationale_1]] → `rationale_for` → [[assistant_app_providers_inference_airllm_adapter]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] → `method` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter_health]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] → `method` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter_invoke]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] → `method` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter_list_models]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] → `method` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter_provider_name]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] → `method` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter_stream]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter]] → `method` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter_to_langchain]]
- [[assistant_app_providers_inference_airllm_adapter_rationale_15]] → `rationale_for` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_invoke]] → `calls` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter_to_langchain]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_invoke]] → `references` → [[assistant_app_providers_inference_airllm_adapter_py_inferenceresult]]
- [[assistant_app_providers_inference_airllm_adapter_airllmadapter_stream]] → `calls` → [[assistant_app_providers_inference_airllm_adapter_airllmadapter_to_langchain]]