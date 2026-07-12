# assistant\app\runtime\communication\whatsapp_evolution.py

## Símbolos

- [[assistant_app_runtime_communication_whatsapp_evolution]] — code: whatsapp_evolution.py
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] — code: EvolutionWhatsAppAdapter
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_init]] — code: .__init__()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_get_api_key]] — code: ._get_api_key()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_connect]] — code: .connect()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_disconnect]] — code: .disconnect()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_health]] — code: .health()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_send]] — code: .send()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_receive]] — code: .receive()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_authenticate]] — code: .authenticate()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_refresh]] — code: .refresh()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_init_registration]] — code: ._init_registration()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_activate_license]] — code: ._activate_license()
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_send_heartbeat]] — code: .send_heartbeat()
- [[assistant_app_runtime_communication_whatsapp_evolution_rationale_1]] — code: Evolution API Adapter for WhatsApp Communication Channel.  SDD-KAOS-EVOLUTION-
- [[assistant_app_runtime_communication_whatsapp_evolution_rationale_22]] — code: Adapter for WhatsApp channel powered by Evolution API.
- [[assistant_app_runtime_communication_whatsapp_evolution_rationale_100]] — code: Runs the registration/polling/activation flow.          Credentials can includ

## Dependências

- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `uses` → [[assistant_app_core_credential_service_credentialmanager]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_get_api_key]] → `calls` → [[assistant_app_core_credential_service_credentialmanager_get_credential]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_activate_license]] → `calls` → [[assistant_app_core_credential_service_credentialmanager_set_credential]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `inherits` → [[assistant_app_runtime_communication_base_communicationprovider]]
- [[assistant_app_runtime_communication_whatsapp_evolution]] → `contains` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]]
- [[assistant_app_runtime_communication_whatsapp_evolution_rationale_1]] → `rationale_for` → [[assistant_app_runtime_communication_whatsapp_evolution]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_activate_license]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_authenticate]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_connect]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_disconnect]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_get_api_key]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_health]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_init]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_init_registration]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_receive]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_refresh]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_send]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]] → `method` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_send_heartbeat]]
- [[assistant_app_runtime_communication_whatsapp_evolution_rationale_22]] → `rationale_for` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_connect]] → `calls` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_get_api_key]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_health]] → `calls` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_get_api_key]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_refresh]] → `calls` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_get_api_key]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_send]] → `calls` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_get_api_key]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_health]] → `references` → [[assistant_app_runtime_communication_whatsapp_evolution_py_any]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_health]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_authenticate]] → `references` → [[assistant_app_runtime_communication_whatsapp_evolution_py_any]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_init_registration]] → `references` → [[assistant_app_runtime_communication_whatsapp_evolution_py_any]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_receive]] → `references` → [[assistant_app_runtime_communication_whatsapp_evolution_py_any]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_send]] → `references` → [[assistant_app_runtime_communication_whatsapp_evolution_py_any]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_send]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_authenticate]] → `calls` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_activate_license]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_authenticate]] → `calls` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_init_registration]]
- [[assistant_app_runtime_communication_whatsapp_evolution_rationale_100]] → `rationale_for` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_authenticate]]
- [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_refresh]] → `calls` → [[assistant_app_runtime_communication_whatsapp_evolution_evolutionwhatsappadapter_send_heartbeat]]