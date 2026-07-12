# assistant\app\providers\email\email_sender.py

## Símbolos

- [[assistant_app_providers_email_email_sender]] — code: email_sender.py
- [[assistant_app_providers_email_email_sender_emailsender]] — code: EmailSender
- [[assistant_app_providers_email_email_sender_emailsender_init]] — code: .__init__()
- [[assistant_app_providers_email_email_sender_emailsender_send]] — code: .send()
- [[assistant_app_providers_email_email_sender_emailsender_is_configured]] — code: .is_configured()
- [[assistant_app_providers_email_email_sender_rationale_1]] — code: Email Sender — Envio de mensagens via SMTP.
- [[assistant_app_providers_email_email_sender_rationale_16]] — code: Envio de email via protocolo SMTP.      Responsavel por enviar mensagens de em
- [[assistant_app_providers_email_email_sender_rationale_43]] — code: Envia um email.          Args:             to: Endereco de email do destinata

## Dependências

- [[assistant_app_providers_email_email_sender]] → `contains` → [[assistant_app_providers_email_email_sender_emailsender]]
- [[assistant_app_providers_email_email_sender_rationale_1]] → `rationale_for` → [[assistant_app_providers_email_email_sender]]
- [[assistant_app_providers_email_email_sender_emailsender]] → `method` → [[assistant_app_providers_email_email_sender_emailsender_init]]
- [[assistant_app_providers_email_email_sender_emailsender]] → `method` → [[assistant_app_providers_email_email_sender_emailsender_is_configured]]
- [[assistant_app_providers_email_email_sender_emailsender]] → `method` → [[assistant_app_providers_email_email_sender_emailsender_send]]
- [[assistant_app_providers_email_email_sender_rationale_16]] → `rationale_for` → [[assistant_app_providers_email_email_sender_emailsender]]
- [[assistant_app_providers_email_email_sender_emailsender_send]] → `references` → [[assistant_app_providers_email_email_sender_py_any]]
- [[assistant_app_providers_email_email_sender_emailsender_send]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_providers_email_email_sender_rationale_43]] → `rationale_for` → [[assistant_app_providers_email_email_sender_emailsender_send]]