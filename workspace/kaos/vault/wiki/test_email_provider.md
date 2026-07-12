# assistant\tests\unit\test_email_provider.py

## Símbolos

- [[assistant_tests_unit_test_email_provider]] — code: test_email_provider.py
- [[assistant_tests_unit_test_email_provider_testemailreader]] — code: TestEmailReader
- [[assistant_tests_unit_test_email_provider_testemailreader_test_not_configured]] — code: .test_not_configured()
- [[assistant_tests_unit_test_email_provider_testemailreader_test_fetch_inbox]] — code: .test_fetch_inbox()
- [[assistant_tests_unit_test_email_provider_testemailreader_test_decode_mime_header]] — code: .test_decode_mime_header()
- [[assistant_tests_unit_test_email_provider_testemailreader_test_decode_mime_header_none]] — code: .test_decode_mime_header_none()
- [[assistant_tests_unit_test_email_provider_testemailsender]] — code: TestEmailSender
- [[assistant_tests_unit_test_email_provider_testemailsender_test_not_configured]] — code: .test_not_configured()
- [[assistant_tests_unit_test_email_provider_testemailsender_test_send_success]] — code: .test_send_success()
- [[assistant_tests_unit_test_email_provider_testemailtools]] — code: TestEmailTools
- [[assistant_tests_unit_test_email_provider_testemailtools_test_read_emails_not_configured]] — code: .test_read_emails_not_configured()
- [[assistant_tests_unit_test_email_provider_testemailtools_test_send_email_not_configured]] — code: .test_send_email_not_configured()
- [[assistant_tests_unit_test_email_provider_rationale_1]] — code: Testes do provedor de Email.

## Dependências

- [[assistant_tests_unit_test_email_provider_testemailreader]] → `uses` → [[assistant_app_providers_email_email_reader_emailreader]]
- [[assistant_tests_unit_test_email_provider_testemailreader_test_decode_mime_header]] → `calls` → [[assistant_app_providers_email_email_reader_emailreader]]
- [[assistant_tests_unit_test_email_provider_testemailreader_test_decode_mime_header_none]] → `calls` → [[assistant_app_providers_email_email_reader_emailreader]]
- [[assistant_tests_unit_test_email_provider_testemailreader_test_fetch_inbox]] → `calls` → [[assistant_app_providers_email_email_reader_emailreader]]
- [[assistant_tests_unit_test_email_provider_testemailreader_test_not_configured]] → `calls` → [[assistant_app_providers_email_email_reader_emailreader]]
- [[assistant_tests_unit_test_email_provider_testemailsender]] → `uses` → [[assistant_app_providers_email_email_reader_emailreader]]
- [[assistant_tests_unit_test_email_provider_testemailtools]] → `uses` → [[assistant_app_providers_email_email_reader_emailreader]]
- [[assistant_tests_unit_test_email_provider_testemailreader]] → `uses` → [[assistant_app_providers_email_email_sender_emailsender]]
- [[assistant_tests_unit_test_email_provider_testemailsender]] → `uses` → [[assistant_app_providers_email_email_sender_emailsender]]
- [[assistant_tests_unit_test_email_provider_testemailsender_test_not_configured]] → `calls` → [[assistant_app_providers_email_email_sender_emailsender]]
- [[assistant_tests_unit_test_email_provider_testemailsender_test_send_success]] → `calls` → [[assistant_app_providers_email_email_sender_emailsender]]
- [[assistant_tests_unit_test_email_provider_testemailtools]] → `uses` → [[assistant_app_providers_email_email_sender_emailsender]]
- [[assistant_tests_unit_test_email_provider]] → `contains` → [[assistant_tests_unit_test_email_provider_testemailreader]]
- [[assistant_tests_unit_test_email_provider]] → `contains` → [[assistant_tests_unit_test_email_provider_testemailsender]]
- [[assistant_tests_unit_test_email_provider]] → `contains` → [[assistant_tests_unit_test_email_provider_testemailtools]]
- [[assistant_tests_unit_test_email_provider_rationale_1]] → `rationale_for` → [[assistant_tests_unit_test_email_provider]]
- [[assistant_tests_unit_test_email_provider_testemailreader]] → `method` → [[assistant_tests_unit_test_email_provider_testemailreader_test_decode_mime_header]]
- [[assistant_tests_unit_test_email_provider_testemailreader]] → `method` → [[assistant_tests_unit_test_email_provider_testemailreader_test_decode_mime_header_none]]
- [[assistant_tests_unit_test_email_provider_testemailreader]] → `method` → [[assistant_tests_unit_test_email_provider_testemailreader_test_fetch_inbox]]
- [[assistant_tests_unit_test_email_provider_testemailreader]] → `method` → [[assistant_tests_unit_test_email_provider_testemailreader_test_not_configured]]
- [[assistant_tests_unit_test_email_provider_testemailsender]] → `method` → [[assistant_tests_unit_test_email_provider_testemailsender_test_not_configured]]
- [[assistant_tests_unit_test_email_provider_testemailsender]] → `method` → [[assistant_tests_unit_test_email_provider_testemailsender_test_send_success]]
- [[assistant_tests_unit_test_email_provider_testemailtools]] → `method` → [[assistant_tests_unit_test_email_provider_testemailtools_test_read_emails_not_configured]]
- [[assistant_tests_unit_test_email_provider_testemailtools]] → `method` → [[assistant_tests_unit_test_email_provider_testemailtools_test_send_email_not_configured]]