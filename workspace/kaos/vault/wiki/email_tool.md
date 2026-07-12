# assistant\app\providers\email\email_tool.py

## Símbolos

- [[assistant_app_providers_email_email_tool]] — code: email_tool.py
- [[assistant_app_providers_email_email_tool_read_emails]] — code: read_emails()
- [[assistant_app_providers_email_email_tool_send_email]] — code: send_email()
- [[assistant_app_providers_email_email_tool_register_email_tools]] — code: register_email_tools()
- [[assistant_app_providers_email_email_tool_rationale_1]] — code: Email Tools — Ferramentas LangChain para integracao de email.
- [[assistant_app_providers_email_email_tool_rationale_14]] — code: Le os emails mais recentes da caixa de entrada.      Args:         limit: Num
- [[assistant_app_providers_email_email_tool_rationale_49]] — code: Envia um email.      Args:         to: Endereco de email do destinatario.
- [[assistant_app_providers_email_email_tool_rationale_70]] — code: Registra as ferramentas de email no TOOL_REGISTRY global.

## Dependências

- [[assistant_app_providers_email_email_tool_read_emails]] → `calls` → [[assistant_app_providers_email_email_reader_emailreader]]
- [[assistant_app_providers_email_email_tool_send_email]] → `calls` → [[assistant_app_providers_email_email_sender_emailsender]]
- [[assistant_app_providers_email_email_tool]] → `contains` → [[assistant_app_providers_email_email_tool_read_emails]]
- [[assistant_app_providers_email_email_tool]] → `contains` → [[assistant_app_providers_email_email_tool_register_email_tools]]
- [[assistant_app_providers_email_email_tool]] → `contains` → [[assistant_app_providers_email_email_tool_send_email]]
- [[assistant_app_providers_email_email_tool_rationale_1]] → `rationale_for` → [[assistant_app_providers_email_email_tool]]
- [[assistant_app_providers_email_email_tool_rationale_14]] → `rationale_for` → [[assistant_app_providers_email_email_tool_read_emails]]
- [[assistant_app_providers_email_email_tool_register_email_tools]] → `indirect_call` → [[assistant_app_providers_email_email_tool_read_emails]]
- [[assistant_app_providers_email_email_tool_rationale_49]] → `rationale_for` → [[assistant_app_providers_email_email_tool_send_email]]
- [[assistant_app_providers_email_email_tool_register_email_tools]] → `indirect_call` → [[assistant_app_providers_email_email_tool_send_email]]
- [[assistant_app_providers_email_email_tool_rationale_70]] → `rationale_for` → [[assistant_app_providers_email_email_tool_register_email_tools]]