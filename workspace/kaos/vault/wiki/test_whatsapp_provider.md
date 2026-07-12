# assistant\tests\unit\test_whatsapp_provider.py

## Símbolos

- [[assistant_tests_unit_test_whatsapp_provider]] — code: test_whatsapp_provider.py
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider]] — code: TestWhatsAppProvider
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_not_configured]] — code: .test_not_configured()
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_send_message_not_configured]] — code: .test_send_message_not_configured()
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_send_message_success]] — code: .test_send_message_success()
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_send_message_http_error]] — code: .test_send_message_http_error()
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsapptool]] — code: TestWhatsAppTool
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsapptool_test_tool_not_configured]] — code: .test_tool_not_configured()
- [[assistant_tests_unit_test_whatsapp_provider_rationale_1]] — code: Testes do provedor WhatsApp.

## Dependências

- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider]] → `uses` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]]
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_not_configured]] → `calls` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]]
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_send_message_http_error]] → `calls` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]]
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_send_message_not_configured]] → `calls` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]]
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_send_message_success]] → `calls` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]]
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsapptool]] → `uses` → [[assistant_app_providers_whatsapp_whatsapp_provider_whatsappprovider]]
- [[assistant_tests_unit_test_whatsapp_provider]] → `contains` → [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider]]
- [[assistant_tests_unit_test_whatsapp_provider]] → `contains` → [[assistant_tests_unit_test_whatsapp_provider_testwhatsapptool]]
- [[assistant_tests_unit_test_whatsapp_provider_rationale_1]] → `rationale_for` → [[assistant_tests_unit_test_whatsapp_provider]]
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider]] → `method` → [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_not_configured]]
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider]] → `method` → [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_send_message_http_error]]
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider]] → `method` → [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_send_message_not_configured]]
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider]] → `method` → [[assistant_tests_unit_test_whatsapp_provider_testwhatsappprovider_test_send_message_success]]
- [[assistant_tests_unit_test_whatsapp_provider_testwhatsapptool]] → `method` → [[assistant_tests_unit_test_whatsapp_provider_testwhatsapptool_test_tool_not_configured]]