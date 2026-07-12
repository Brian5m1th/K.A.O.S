# assistant\app\providers\whatsapp\whatsapp_tool.py

## Símbolos

- [[assistant_app_providers_whatsapp_whatsapp_tool]] — code: whatsapp_tool.py
- [[assistant_app_providers_whatsapp_whatsapp_tool_send_whatsapp]] — code: send_whatsapp()
- [[assistant_app_providers_whatsapp_whatsapp_tool_register_whatsapp_tools]] — code: register_whatsapp_tools()
- [[assistant_app_providers_whatsapp_whatsapp_tool_rationale_1]] — code: WhatsApp Tools — Ferramentas LangChain para integracao WhatsApp.
- [[assistant_app_providers_whatsapp_whatsapp_tool_rationale_13]] — code: Envia uma mensagem WhatsApp.      Args:         to: Numero de telefone do des
- [[assistant_app_providers_whatsapp_whatsapp_tool_rationale_40]] — code: Registra as ferramentas WhatsApp no TOOL_REGISTRY global.

## Dependências

- [[assistant_app_providers_whatsapp_whatsapp_tool_send_whatsapp]] → `calls` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]]
- [[assistant_app_providers_whatsapp_whatsapp_tool]] → `contains` → [[assistant_app_providers_whatsapp_whatsapp_tool_register_whatsapp_tools]]
- [[assistant_app_providers_whatsapp_whatsapp_tool]] → `contains` → [[assistant_app_providers_whatsapp_whatsapp_tool_send_whatsapp]]
- [[assistant_app_providers_whatsapp_whatsapp_tool_rationale_1]] → `rationale_for` → [[assistant_app_providers_whatsapp_whatsapp_tool]]
- [[assistant_app_providers_whatsapp_whatsapp_tool_rationale_13]] → `rationale_for` → [[assistant_app_providers_whatsapp_whatsapp_tool_send_whatsapp]]
- [[assistant_app_providers_whatsapp_whatsapp_tool_register_whatsapp_tools]] → `indirect_call` → [[assistant_app_providers_whatsapp_whatsapp_tool_send_whatsapp]]
- [[assistant_app_providers_whatsapp_whatsapp_tool_rationale_40]] → `rationale_for` → [[assistant_app_providers_whatsapp_whatsapp_tool_register_whatsapp_tools]]