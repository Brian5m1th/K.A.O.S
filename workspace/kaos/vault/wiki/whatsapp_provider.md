# assistant\app\providers\whatsapp\whatsapp_provider.py

## Símbolos

- [[assistant_app_providers_whatsapp_whatsapp_provider]] — code: whatsapp_provider.py
- [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]] — code: WhatsAppProvider
- [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider_init]] — code: .__init__()
- [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider_send_message]] — code: .send_message()
- [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider_is_configured]] — code: .is_configured()
- [[assistant_app_providers_whatsapp_whatsapp_provider_rationale_1]] — code: WhatsApp Provider — Envio de mensagens via Evolution API / N8N.
- [[assistant_app_providers_whatsapp_whatsapp_provider_rationale_14]] — code: Provedor de mensagens WhatsApp via Evolution API.      Utiliza a Evolution API
- [[assistant_app_providers_whatsapp_whatsapp_provider_rationale_30]] — code: Envia uma mensagem WhatsApp.          Args:             to: Numero de telefon

## Dependências

- [[assistant_app_providers_whatsapp_whatsapp_provider]] → `contains` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]]
- [[assistant_app_providers_whatsapp_whatsapp_provider_rationale_1]] → `rationale_for` → [[assistant_app_providers_whatsapp_whatsapp_provider]]
- [[assistant_app_providers_whatsapp_whatsapp_provider_rationale_14]] → `rationale_for` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]]
- [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]] → `method` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider_init]]
- [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]] → `method` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider_is_configured]]
- [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]] → `method` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider_send_message]]
- [[assistant_app_providers_whatsapp_whatsapp_provider_rationale_30]] → `rationale_for` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider_send_message]]
- [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider_send_message]] → `references` → [[assistant_app_providers_whatsapp_whatsapp_provider_py_any]]
- [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider_send_message]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]