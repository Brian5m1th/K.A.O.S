# graphify\tests\fixtures\sample_php_config.php

## Símbolos

- [[graphify_tests_fixtures_sample_php_config]] — code: sample_php_config.php
- [[graphify_tests_fixtures_sample_php_config_throttle]] — code: Throttle
- [[graphify_tests_fixtures_sample_php_config_ratelimiter]] — code: RateLimiter
- [[graphify_tests_fixtures_sample_php_config_ratelimiter_persecond]] — code: .perSecond()
- [[graphify_tests_fixtures_sample_php_config_ratelimiter_perday]] — code: .perDay()

## Dependências

- [[graphify_tests_fixtures_sample_php_config]] → `contains` → [[graphify_tests_fixtures_sample_php_config_ratelimiter]]
- [[graphify_tests_fixtures_sample_php_config]] → `contains` → [[graphify_tests_fixtures_sample_php_config_throttle]]
- [[graphify_tests_fixtures_sample_php_config_ratelimiter_perday]] → `uses_config` → [[graphify_tests_fixtures_sample_php_config_throttle]]
- [[graphify_tests_fixtures_sample_php_config_ratelimiter_persecond]] → `uses_config` → [[graphify_tests_fixtures_sample_php_config_throttle]]
- [[graphify_tests_fixtures_sample_php_config_ratelimiter]] → `method` → [[graphify_tests_fixtures_sample_php_config_ratelimiter_perday]]
- [[graphify_tests_fixtures_sample_php_config_ratelimiter]] → `method` → [[graphify_tests_fixtures_sample_php_config_ratelimiter_persecond]]