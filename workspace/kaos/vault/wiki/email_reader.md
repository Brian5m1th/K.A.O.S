# assistant\app\providers\email\email_reader.py

## Símbolos

- [[assistant_app_providers_email_email_reader]] — code: email_reader.py
- [[assistant_app_providers_email_email_reader_emailmessage]] — code: EmailMessage
- [[assistant_app_providers_email_email_reader_emailreader]] — code: EmailReader
- [[assistant_app_providers_email_email_reader_emailreader_init]] — code: .__init__()
- [[assistant_app_providers_email_email_reader_emailreader_decode_mime_header]] — code: ._decode_mime_header()
- [[assistant_app_providers_email_email_reader_emailreader_get_email_body]] — code: ._get_email_body()
- [[assistant_app_providers_email_email_reader_emailreader_fetch_inbox]] — code: .fetch_inbox()
- [[assistant_app_providers_email_email_reader_emailreader_is_configured]] — code: .is_configured()
- [[assistant_app_providers_email_email_reader_rationale_1]] — code: Email Reader — Leitura e triagem de mensagens via IMAP.
- [[assistant_app_providers_email_email_reader_rationale_18]] — code: Representa uma mensagem de email.
- [[assistant_app_providers_email_email_reader_rationale_29]] — code: Leitor de email via protocolo IMAP.      Responsavel por conectar ao servidor
- [[assistant_app_providers_email_email_reader_rationale_49]] — code: Decodifica cabecalho MIME para string legivel.
- [[assistant_app_providers_email_email_reader_rationale_65]] — code: Extrai o corpo do email (text/plain优先).
- [[assistant_app_providers_email_email_reader_rationale_84]] — code: Busca os emails mais recentes da caixa de entrada.          Args:
- [[assistant_app_providers_email_email_reader_rationale_140]] — code: Verifica se o servico de email esta configurado.

## Dependências

- [[assistant_app_providers_email_email_reader]] → `contains` → [[assistant_app_providers_email_email_reader_emailmessage]]
- [[assistant_app_providers_email_email_reader]] → `contains` → [[assistant_app_providers_email_email_reader_emailreader]]
- [[assistant_app_providers_email_email_reader_rationale_1]] → `rationale_for` → [[assistant_app_providers_email_email_reader]]
- [[assistant_app_providers_email_email_reader_emailreader_fetch_inbox]] → `references` → [[assistant_app_providers_email_email_reader_emailmessage]]
- [[assistant_app_providers_email_email_reader_rationale_18]] → `rationale_for` → [[assistant_app_providers_email_email_reader_emailmessage]]
- [[assistant_app_providers_email_email_reader_emailreader]] → `method` → [[assistant_app_providers_email_email_reader_emailreader_decode_mime_header]]
- [[assistant_app_providers_email_email_reader_emailreader]] → `method` → [[assistant_app_providers_email_email_reader_emailreader_fetch_inbox]]
- [[assistant_app_providers_email_email_reader_emailreader]] → `method` → [[assistant_app_providers_email_email_reader_emailreader_get_email_body]]
- [[assistant_app_providers_email_email_reader_emailreader]] → `method` → [[assistant_app_providers_email_email_reader_emailreader_init]]
- [[assistant_app_providers_email_email_reader_emailreader]] → `method` → [[assistant_app_providers_email_email_reader_emailreader_is_configured]]
- [[assistant_app_providers_email_email_reader_rationale_29]] → `rationale_for` → [[assistant_app_providers_email_email_reader_emailreader]]
- [[assistant_app_providers_email_email_reader_emailreader_fetch_inbox]] → `calls` → [[assistant_app_providers_email_email_reader_emailreader_decode_mime_header]]
- [[assistant_app_providers_email_email_reader_rationale_49]] → `rationale_for` → [[assistant_app_providers_email_email_reader_emailreader_decode_mime_header]]
- [[assistant_app_providers_email_email_reader_emailreader_fetch_inbox]] → `calls` → [[assistant_app_providers_email_email_reader_emailreader_get_email_body]]
- [[assistant_app_providers_email_email_reader_emailreader_get_email_body]] → `references` → [[assistant_app_providers_email_email_reader_py_message]]
- [[assistant_app_providers_email_email_reader_rationale_65]] → `rationale_for` → [[assistant_app_providers_email_email_reader_emailreader_get_email_body]]
- [[assistant_app_providers_email_email_reader_emailreader_fetch_inbox]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[assistant_app_providers_email_email_reader_rationale_84]] → `rationale_for` → [[assistant_app_providers_email_email_reader_emailreader_fetch_inbox]]
- [[assistant_app_providers_email_email_reader_rationale_140]] → `rationale_for` → [[assistant_app_providers_email_email_reader_emailreader_is_configured]]