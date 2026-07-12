# graphify\tests\fixtures\sample_php_container.php

## Símbolos

- [[graphify_tests_fixtures_sample_php_container]] — code: sample_php_container.php
- [[graphify_tests_fixtures_sample_php_container_paymentgateway]] — code: PaymentGateway
- [[graphify_tests_fixtures_sample_php_container_stripegateway]] — code: StripeGateway
- [[graphify_tests_fixtures_sample_php_container_cashiergateway]] — code: CashierGateway
- [[graphify_tests_fixtures_sample_php_container_appserviceprovider]] — code: AppServiceProvider
- [[graphify_tests_fixtures_sample_php_container_appserviceprovider_register]] — code: .register()

## Dependências

- [[graphify_tests_fixtures_sample_php_container]] → `contains` → [[graphify_tests_fixtures_sample_php_container_appserviceprovider]]
- [[graphify_tests_fixtures_sample_php_container]] → `contains` → [[graphify_tests_fixtures_sample_php_container_cashiergateway]]
- [[graphify_tests_fixtures_sample_php_container]] → `contains` → [[graphify_tests_fixtures_sample_php_container_paymentgateway]]
- [[graphify_tests_fixtures_sample_php_container]] → `contains` → [[graphify_tests_fixtures_sample_php_container_stripegateway]]
- [[graphify_tests_fixtures_sample_php_container_appserviceprovider_register]] → `references_constant` → [[graphify_tests_fixtures_sample_php_container_paymentgateway]]
- [[graphify_tests_fixtures_sample_php_container_paymentgateway]] → `bound_to` → [[graphify_tests_fixtures_sample_php_container_stripegateway]]
- [[graphify_tests_fixtures_sample_php_container_appserviceprovider_register]] → `references_constant` → [[graphify_tests_fixtures_sample_php_container_stripegateway]]
- [[graphify_tests_fixtures_sample_php_container_cashiergateway]] → `bound_to` → [[graphify_tests_fixtures_sample_php_container_stripegateway]]
- [[graphify_tests_fixtures_sample_php_container_appserviceprovider_register]] → `references_constant` → [[graphify_tests_fixtures_sample_php_container_cashiergateway]]
- [[graphify_tests_fixtures_sample_php_container_appserviceprovider]] → `method` → [[graphify_tests_fixtures_sample_php_container_appserviceprovider_register]]