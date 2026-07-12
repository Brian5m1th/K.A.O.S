# assistant\app\api\health.py

## Símbolos

- [[assistant_app_api_health]] — code: health.py
- [[assistant_app_api_health_healthresponse]] — code: HealthResponse
- [[assistant_app_api_health_readinessresponse]] — code: ReadinessResponse
- [[assistant_app_api_health_get_llm_service]] — code: get_llm_service()
- [[assistant_app_api_health_health_check]] — code: health_check()
- [[assistant_app_api_health_readiness_check]] — code: readiness_check()

## Dependências

- [[assistant_app_api_health]] → `contains` → [[assistant_app_api_health_get_llm_service]]
- [[assistant_app_api_health]] → `contains` → [[assistant_app_api_health_health_check]]
- [[assistant_app_api_health]] → `contains` → [[assistant_app_api_health_healthresponse]]
- [[assistant_app_api_health]] → `contains` → [[assistant_app_api_health_readiness_check]]
- [[assistant_app_api_health]] → `contains` → [[assistant_app_api_health_readinessresponse]]
- [[assistant_app_api_health]] → `imports_from` → [[fastapi]]
- [[assistant_app_api_health_health_check]] → `references` → [[assistant_app_api_health_healthresponse]]
- [[assistant_app_api_health_healthresponse]] → `inherits` → [[assistant_app_api_health_py_basemodel]]
- [[assistant_app_api_health_healthresponse]] → `uses` → [[assistant_app_service_llm_service_llmservice]]
- [[assistant_app_api_health_readinessresponse]] → `inherits` → [[assistant_app_api_health_py_basemodel]]
- [[assistant_app_api_health_readiness_check]] → `references` → [[assistant_app_api_health_readinessresponse]]
- [[assistant_app_api_health_readinessresponse]] → `uses` → [[assistant_app_service_llm_service_llmservice]]
- [[assistant_app_api_health_get_llm_service]] → `references` → [[assistant_app_service_llm_service_llmservice]]
- [[assistant_app_api_health_readiness_check]] → `references` → [[assistant_app_service_llm_service_llmservice]]