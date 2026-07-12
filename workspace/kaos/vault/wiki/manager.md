# assistant\app\runtime\communication\manager.py

## Símbolos

- [[assistant_app_runtime_communication_manager]] — code: manager.py
- [[assistant_app_runtime_communication_manager_communicationruntime]] — code: CommunicationRuntime
- [[assistant_app_runtime_communication_manager_communicationruntime_init]] — code: .__init__()
- [[assistant_app_runtime_communication_manager_communicationruntime_register_channel]] — code: .register_channel()
- [[assistant_app_runtime_communication_manager_communicationruntime_get_channel]] — code: .get_channel()
- [[assistant_app_runtime_communication_manager_communicationruntime_send]] — code: .send()
- [[assistant_app_runtime_communication_manager_communicationruntime_health]] — code: .health()
- [[assistant_app_runtime_communication_manager_rationale_1]] — code: Communication Runtime Manager.  SDD-KAOS-EVOLUTION-001: Orchestrates and expos
- [[assistant_app_runtime_communication_manager_rationale_15]] — code: Manages and routes messages through pluggable communication channels.
- [[assistant_app_runtime_communication_manager_rationale_23]] — code: Register a new channel provider (e.g. Email, Slack).
- [[assistant_app_runtime_communication_manager_rationale_28]] — code: Get provider for a channel.
- [[assistant_app_runtime_communication_manager_rationale_34]] — code: Routes the message send request to the appropriate provider.
- [[assistant_app_runtime_communication_manager_rationale_44]] — code: Returns health status of the provider.

## Dependências

- [[assistant_app_runtime_communication_manager_communicationruntime_get_channel]] → `references` → [[assistant_app_runtime_communication_base_communicationprovider]]
- [[assistant_app_runtime_communication_manager_communicationruntime_register_channel]] → `references` → [[assistant_app_runtime_communication_base_communicationprovider]]
- [[assistant_app_runtime_communication_manager]] → `contains` → [[assistant_app_runtime_communication_manager_communicationruntime]]
- [[assistant_app_runtime_communication_manager_rationale_1]] → `rationale_for` → [[assistant_app_runtime_communication_manager]]
- [[assistant_app_runtime_communication_manager_communicationruntime]] → `method` → [[assistant_app_runtime_communication_manager_communicationruntime_get_channel]]
- [[assistant_app_runtime_communication_manager_communicationruntime]] → `method` → [[assistant_app_runtime_communication_manager_communicationruntime_health]]
- [[assistant_app_runtime_communication_manager_communicationruntime]] → `method` → [[assistant_app_runtime_communication_manager_communicationruntime_init]]
- [[assistant_app_runtime_communication_manager_communicationruntime]] → `method` → [[assistant_app_runtime_communication_manager_communicationruntime_register_channel]]
- [[assistant_app_runtime_communication_manager_communicationruntime]] → `method` → [[assistant_app_runtime_communication_manager_communicationruntime_send]]
- [[assistant_app_runtime_communication_manager_communicationruntime]] → `uses` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]]
- [[assistant_app_runtime_communication_manager_rationale_15]] → `rationale_for` → [[assistant_app_runtime_communication_manager_communicationruntime]]
- [[assistant_app_runtime_communication_manager_communicationruntime_init]] → `calls` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]]
- [[assistant_app_runtime_communication_manager_rationale_23]] → `rationale_for` → [[assistant_app_runtime_communication_manager_communicationruntime_register_channel]]
- [[assistant_app_runtime_communication_manager_communicationruntime_health]] → `calls` → [[assistant_app_runtime_communication_manager_communicationruntime_get_channel]]
- [[assistant_app_runtime_communication_manager_communicationruntime_send]] → `calls` → [[assistant_app_runtime_communication_manager_communicationruntime_get_channel]]
- [[assistant_app_runtime_communication_manager_rationale_28]] → `rationale_for` → [[assistant_app_runtime_communication_manager_communicationruntime_get_channel]]
- [[assistant_app_runtime_communication_manager_communicationruntime_send]] → `references` → [[assistant_app_runtime_communication_manager_py_any]]
- [[assistant_app_runtime_communication_manager_rationale_34]] → `rationale_for` → [[assistant_app_runtime_communication_manager_communicationruntime_send]]
- [[assistant_app_runtime_communication_manager_communicationruntime_health]] → `references` → [[assistant_app_runtime_communication_manager_py_any]]
- [[assistant_app_runtime_communication_manager_rationale_44]] → `rationale_for` → [[assistant_app_runtime_communication_manager_communicationruntime_health]]