# assistant\app\core\services\inference_service.py

## Símbolos

- [[assistant_app_core_services_inference_service]] — code: inference_service.py
- [[assistant_app_core_services_inference_service_inferenceservice]] — code: InferenceService
- [[assistant_app_core_services_inference_service_inferenceservice_init]] — code: .__init__()
- [[assistant_app_core_services_inference_service_inferenceservice_invoke]] — code: .invoke()
- [[assistant_app_core_services_inference_service_inferenceservice_stream]] — code: .stream()
- [[assistant_app_core_services_inference_service_inferenceservice_list_models]] — code: .list_models()
- [[assistant_app_core_services_inference_service_inferenceservice_health]] — code: .health()
- [[assistant_app_core_services_inference_service_inferenceservice_resolve_provider]] — code: ._resolve_provider()
- [[assistant_app_core_services_inference_service_rationale_1]] — code: InferenceService — LLM inference orchestrator.  Routes inference requests to the
- [[assistant_app_core_services_inference_service_rationale_14]] — code: Service for LLM model inference across multiple providers.

## Dependências

- [[assistant_app_core_services_inference_service_inferenceservice]] → `uses` → [[assistant_app_core_provider_registry_providerregistry]]
- [[assistant_app_core_services_inference_service]] → `contains` → [[assistant_app_core_services_inference_service_inferenceservice]]
- [[assistant_app_core_services_inference_service_rationale_1]] → `rationale_for` → [[assistant_app_core_services_inference_service]]
- [[assistant_app_core_services_inference_service_inferenceservice]] → `method` → [[assistant_app_core_services_inference_service_inferenceservice_health]]
- [[assistant_app_core_services_inference_service_inferenceservice]] → `method` → [[assistant_app_core_services_inference_service_inferenceservice_init]]
- [[assistant_app_core_services_inference_service_inferenceservice]] → `method` → [[assistant_app_core_services_inference_service_inferenceservice_invoke]]
- [[assistant_app_core_services_inference_service_inferenceservice]] → `method` → [[assistant_app_core_services_inference_service_inferenceservice_list_models]]
- [[assistant_app_core_services_inference_service_inferenceservice]] → `method` → [[assistant_app_core_services_inference_service_inferenceservice_resolve_provider]]
- [[assistant_app_core_services_inference_service_inferenceservice]] → `method` → [[assistant_app_core_services_inference_service_inferenceservice_stream]]
- [[assistant_app_core_services_inference_service_inferenceservice]] → `uses` → [[assistant_app_domain_ports_inference_port_inferenceport]]
- [[assistant_app_core_services_inference_service_inferenceservice]] → `uses` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_core_services_inference_service_inferenceservice]] → `uses` → [[assistant_app_domain_ports_inference_port_inferenceresult]]
- [[assistant_app_core_services_inference_service_rationale_14]] → `rationale_for` → [[assistant_app_core_services_inference_service_inferenceservice]]
- [[assistant_app_core_services_inference_service_inferenceservice_invoke]] → `calls` → [[assistant_app_core_services_inference_service_inferenceservice_resolve_provider]]
- [[assistant_app_core_services_inference_service_inferenceservice_invoke]] → `references` → [[assistant_app_core_services_inference_service_py_inferenceresult]]
- [[assistant_app_core_services_inference_service_inferenceservice_invoke]] → `references` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_core_services_inference_service_inferenceservice_stream]] → `calls` → [[assistant_app_core_services_inference_service_inferenceservice_resolve_provider]]
- [[assistant_app_core_services_inference_service_inferenceservice_stream]] → `references` → [[assistant_app_domain_ports_inference_port_inferencerequest]]
- [[assistant_app_core_services_inference_service_inferenceservice_resolve_provider]] → `references` → [[assistant_app_domain_ports_inference_port_inferenceport]]