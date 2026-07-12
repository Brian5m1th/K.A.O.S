# assistant\app\domain\ports\inference_port.py

## Símbolos

- [[assistant_app_domain_ports_inference_port]] — code: inference_port.py
- [[assistant_app_domain_ports_inference_port_inferencerequest]] — code: InferenceRequest
- [[assistant_app_domain_ports_inference_port_inferenceresult]] — code: InferenceResult
- [[assistant_app_domain_ports_inference_port_inferenceport]] — code: InferencePort
- [[assistant_app_domain_ports_inference_port_inferenceport_provider_name]] — code: .provider_name()
- [[assistant_app_domain_ports_inference_port_inferenceport_invoke]] — code: .invoke()
- [[assistant_app_domain_ports_inference_port_inferenceport_stream]] — code: .stream()
- [[assistant_app_domain_ports_inference_port_inferenceport_health]] — code: .health()
- [[assistant_app_domain_ports_inference_port_inferenceport_list_models]] — code: .list_models()
- [[assistant_app_domain_ports_inference_port_rationale_1]] — code: InferencePort — LLM inference and model routing capability.  Provides a unified
- [[assistant_app_domain_ports_inference_port_rationale_20]] — code: Unified inference request.
- [[assistant_app_domain_ports_inference_port_rationale_31]] — code: Unified inference result.
- [[assistant_app_domain_ports_inference_port_rationale_41]] — code: Interface for LLM model inference.      Concrete implementations:       - Ollama
- [[assistant_app_domain_ports_inference_port_rationale_59]] — code: Non-streaming inference call.
- [[assistant_app_domain_ports_inference_port_rationale_64]] — code: Streaming inference call. Yields content chunks.
- [[assistant_app_domain_ports_inference_port_rationale_69]] — code: Check if the provider is reachable and models are available.
- [[assistant_app_domain_ports_inference_port_rationale_74]] — code: List available models for this provider.

## Dependências

- [[assistant_app_domain_ports_inference_port]] → `contains` → [[assistant_app_domain_ports_inference_port_inferenceport]]
- [[assistant_app_domain_ports_inference_port]] → `contains` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_domain_ports_inference_port]] → `contains` → [[assistant_app_domain_ports_inference_port_inferenceresult]]
- [[assistant_app_domain_ports_inference_port]] → `imports_from` → [[assistant_app_domain_ports_inference_port_py_abc]]
- [[assistant_app_domain_ports_inference_port_rationale_1]] → `rationale_for` → [[assistant_app_domain_ports_inference_port]]
- [[assistant_app_domain_ports_inference_port_inferenceport_invoke]] → `references` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_domain_ports_inference_port_inferenceport_stream]] → `references` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_domain_ports_inference_port_rationale_20]] → `rationale_for` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_domain_ports_inference_port_inferenceport_invoke]] → `references` → [[assistant_app_domain_ports_inference_port_inferenceresult]]
- [[assistant_app_domain_ports_inference_port_rationale_31]] → `rationale_for` → [[assistant_app_domain_ports_inference_port_inferenceresult]]
- [[assistant_app_domain_ports_inference_port_inferenceport]] → `method` → [[assistant_app_domain_ports_inference_port_inferenceport_health]]
- [[assistant_app_domain_ports_inference_port_inferenceport]] → `method` → [[assistant_app_domain_ports_inference_port_inferenceport_invoke]]
- [[assistant_app_domain_ports_inference_port_inferenceport]] → `method` → [[assistant_app_domain_ports_inference_port_inferenceport_list_models]]
- [[assistant_app_domain_ports_inference_port_inferenceport]] → `method` → [[assistant_app_domain_ports_inference_port_inferenceport_provider_name]]
- [[assistant_app_domain_ports_inference_port_inferenceport]] → `method` → [[assistant_app_domain_ports_inference_port_inferenceport_stream]]
- [[assistant_app_domain_ports_inference_port_inferenceport]] → `inherits` → [[assistant_app_domain_ports_inference_port_py_abc]]
- [[assistant_app_domain_ports_inference_port_rationale_41]] → `rationale_for` → [[assistant_app_domain_ports_inference_port_inferenceport]]
- [[assistant_app_domain_ports_inference_port_rationale_59]] → `rationale_for` → [[assistant_app_domain_ports_inference_port_inferenceport_invoke]]
- [[assistant_app_domain_ports_inference_port_rationale_64]] → `rationale_for` → [[assistant_app_domain_ports_inference_port_inferenceport_stream]]
- [[assistant_app_domain_ports_inference_port_rationale_69]] → `rationale_for` → [[assistant_app_domain_ports_inference_port_inferenceport_health]]
- [[assistant_app_domain_ports_inference_port_rationale_74]] → `rationale_for` → [[assistant_app_domain_ports_inference_port_inferenceport_list_models]]