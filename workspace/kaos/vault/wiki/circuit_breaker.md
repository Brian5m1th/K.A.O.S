# assistant\app\orchestrator\circuit_breaker.py

## Símbolos

- [[assistant_app_orchestrator_circuit_breaker]] — code: circuit_breaker.py
- [[assistant_app_orchestrator_circuit_breaker_circuitstate]] — code: CircuitState
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]] — code: CircuitBreaker
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_init]] — code: .__init__()
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_name]] — code: .name()
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_state]] — code: .state()
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_failure_count]] — code: .failure_count()
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_call]] — code: .call()
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_on_success]] — code: ._on_success()
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_on_failure]] — code: ._on_failure()
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_reset]] — code: .reset()
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_to_dict]] — code: .to_dict()

## Dependências

- [[assistant_app_orchestrator_circuit_breaker]] → `contains` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]]
- [[assistant_app_orchestrator_circuit_breaker]] → `contains` → [[assistant_app_orchestrator_circuit_breaker_circuitstate]]
- [[assistant_app_orchestrator_circuit_breaker]] → `imports_from` → [[assistant_app_orchestrator_circuit_breaker_py_enum]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_state]] → `references` → [[assistant_app_orchestrator_circuit_breaker_circuitstate]]
- [[assistant_app_orchestrator_circuit_breaker_circuitstate]] → `inherits` → [[assistant_app_orchestrator_circuit_breaker_py_enum]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]] → `method` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_call]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]] → `method` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_failure_count]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]] → `method` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_init]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]] → `method` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_name]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]] → `method` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_on_failure]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]] → `method` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_on_success]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]] → `method` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_reset]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]] → `method` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_state]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker]] → `method` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_to_dict]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_call]] → `calls` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_on_failure]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_call]] → `calls` → [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_on_success]]
- [[assistant_app_orchestrator_circuit_breaker_circuitbreaker_call]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]