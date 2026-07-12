# graphify\tests\test_long_path_hashing.py

## Símbolos

- [[graphify_tests_test_long_path_hashing]] — code: test_long_path_hashing.py
- [[graphify_tests_test_long_path_hashing_test_os_path_noop_on_posix]] — code: test_os_path_noop_on_posix()
- [[graphify_tests_test_long_path_hashing_test_os_path_adds_prefix_on_win32]] — code: test_os_path_adds_prefix_on_win32()
- [[graphify_tests_test_long_path_hashing_test_os_path_idempotent_on_win32]] — code: test_os_path_idempotent_on_win32()
- [[graphify_tests_test_long_path_hashing_test_hashing_still_works_and_stabilizes]] — code: test_hashing_still_works_and_stabilizes()
- [[graphify_tests_test_long_path_hashing_rationale_1]] — code: r"""#1655 — files whose absolute path exceeds Windows MAX_PATH (260) must still

## Dependências

- [[graphify_tests_test_long_path_hashing]] → `contains` → [[graphify_tests_test_long_path_hashing_test_hashing_still_works_and_stabilizes]]
- [[graphify_tests_test_long_path_hashing]] → `contains` → [[graphify_tests_test_long_path_hashing_test_os_path_adds_prefix_on_win32]]
- [[graphify_tests_test_long_path_hashing]] → `contains` → [[graphify_tests_test_long_path_hashing_test_os_path_idempotent_on_win32]]
- [[graphify_tests_test_long_path_hashing]] → `contains` → [[graphify_tests_test_long_path_hashing_test_os_path_noop_on_posix]]
- [[graphify_tests_test_long_path_hashing_rationale_1]] → `rationale_for` → [[graphify_tests_test_long_path_hashing]]