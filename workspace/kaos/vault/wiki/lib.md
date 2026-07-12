# graphify\tests\fixtures\crate_b\src\lib.rs

## Símbolos

- [[graphify_tests_fixtures_crate_b_src_lib]] — code: lib.rs
- [[graphify_tests_fixtures_crate_b_src_lib_server]] — code: Server
- [[graphify_tests_fixtures_crate_b_src_lib_server_run]] — code: .run()
- [[graphify_tests_fixtures_crate_b_src_lib_server_start]] — code: .start()

## Dependências

- [[graphify_tests_fixtures_crate_b_src_lib]] → `contains` → [[graphify_tests_fixtures_crate_b_src_lib_server]]
- [[graphify_tests_fixtures_crate_b_src_lib_server]] → `method` → [[graphify_tests_fixtures_crate_b_src_lib_server_run]]
- [[graphify_tests_fixtures_crate_b_src_lib_server]] → `method` → [[graphify_tests_fixtures_crate_b_src_lib_server_start]]
- [[graphify_tests_fixtures_crate_b_src_lib_server_run]] → `calls` → [[graphify_tests_fixtures_crate_b_src_lib_server_start]]