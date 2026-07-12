# graphify\tests\fixtures\sample_php_listen.php

## Símbolos

- [[graphify_tests_fixtures_sample_php_listen]] — code: sample_php_listen.php
- [[graphify_tests_fixtures_sample_php_listen_userregistered]] — code: UserRegistered
- [[graphify_tests_fixtures_sample_php_listen_orderplaced]] — code: OrderPlaced
- [[graphify_tests_fixtures_sample_php_listen_sendwelcomeemail]] — code: SendWelcomeEmail
- [[graphify_tests_fixtures_sample_php_listen_notifyadmins]] — code: NotifyAdmins
- [[graphify_tests_fixtures_sample_php_listen_shiporder]] — code: ShipOrder
- [[graphify_tests_fixtures_sample_php_listen_eventserviceprovider]] — code: EventServiceProvider

## Dependências

- [[graphify_tests_fixtures_sample_php_listen]] → `contains` → [[graphify_tests_fixtures_sample_php_listen_eventserviceprovider]]
- [[graphify_tests_fixtures_sample_php_listen]] → `contains` → [[graphify_tests_fixtures_sample_php_listen_notifyadmins]]
- [[graphify_tests_fixtures_sample_php_listen]] → `contains` → [[graphify_tests_fixtures_sample_php_listen_orderplaced]]
- [[graphify_tests_fixtures_sample_php_listen]] → `contains` → [[graphify_tests_fixtures_sample_php_listen_sendwelcomeemail]]
- [[graphify_tests_fixtures_sample_php_listen]] → `contains` → [[graphify_tests_fixtures_sample_php_listen_shiporder]]
- [[graphify_tests_fixtures_sample_php_listen]] → `contains` → [[graphify_tests_fixtures_sample_php_listen_userregistered]]
- [[graphify_tests_fixtures_sample_php_listen_userregistered]] → `listened_by` → [[graphify_tests_fixtures_sample_php_listen_notifyadmins]]
- [[graphify_tests_fixtures_sample_php_listen_userregistered]] → `listened_by` → [[graphify_tests_fixtures_sample_php_listen_sendwelcomeemail]]
- [[graphify_tests_fixtures_sample_php_listen_orderplaced]] → `listened_by` → [[graphify_tests_fixtures_sample_php_listen_shiporder]]