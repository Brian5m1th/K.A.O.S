# graphify\tests\fixtures\sample_php_static_prop.php

## Símbolos

- [[graphify_tests_fixtures_sample_php_static_prop]] — code: sample_php_static_prop.php
- [[graphify_tests_fixtures_sample_php_static_prop_defaultpalette]] — code: DefaultPalette
- [[graphify_tests_fixtures_sample_php_static_prop_colorresolver]] — code: ColorResolver
- [[graphify_tests_fixtures_sample_php_static_prop_colorresolver_primary]] — code: .primary()
- [[graphify_tests_fixtures_sample_php_static_prop_colorresolver_accent]] — code: .accent()

## Dependências

- [[graphify_tests_fixtures_sample_php_static_prop]] → `contains` → [[graphify_tests_fixtures_sample_php_static_prop_colorresolver]]
- [[graphify_tests_fixtures_sample_php_static_prop]] → `contains` → [[graphify_tests_fixtures_sample_php_static_prop_defaultpalette]]
- [[graphify_tests_fixtures_sample_php_static_prop_colorresolver_accent]] → `uses_static_prop` → [[graphify_tests_fixtures_sample_php_static_prop_defaultpalette]]
- [[graphify_tests_fixtures_sample_php_static_prop_colorresolver_primary]] → `uses_static_prop` → [[graphify_tests_fixtures_sample_php_static_prop_defaultpalette]]
- [[graphify_tests_fixtures_sample_php_static_prop_colorresolver]] → `method` → [[graphify_tests_fixtures_sample_php_static_prop_colorresolver_accent]]
- [[graphify_tests_fixtures_sample_php_static_prop_colorresolver]] → `method` → [[graphify_tests_fixtures_sample_php_static_prop_colorresolver_primary]]