# graphify\tests\test_ollama.py

## Símbolos

- [[graphify_tests_test_ollama]] — code: test_ollama.py
- [[graphify_tests_test_ollama_test_ollama_blocks_link_local_and_metadata]] — code: test_ollama_blocks_link_local_and_metadata()
- [[graphify_tests_test_ollama_test_ollama_loopback_and_lan_do_not_raise]] — code: test_ollama_loopback_and_lan_do_not_raise()
- [[graphify_tests_test_ollama_test_ollama_alias_resolving_to_link_local_blocked]] — code: test_ollama_alias_resolving_to_link_local_blocked()
- [[graphify_tests_test_ollama_test_ollama_warn_false_still_hard_blocks_but_stays_quiet]] — code: test_ollama_warn_false_still_hard_blocks_but_stays_quiet()
- [[graphify_tests_test_ollama_test_ollama_in_backends]] — code: test_ollama_in_backends()
- [[graphify_tests_test_ollama_test_detect_backend_ollama]] — code: test_detect_backend_ollama()
- [[graphify_tests_test_ollama_test_detect_backend_kimi_beats_ollama]] — code: test_detect_backend_kimi_beats_ollama()
- [[graphify_tests_test_ollama_test_detect_backend_claude_beats_ollama]] — code: test_detect_backend_claude_beats_ollama()
- [[graphify_tests_test_ollama_test_detect_backend_none_without_envvars]] — code: test_detect_backend_none_without_envvars()
- [[graphify_tests_test_ollama_test_ollama_api_key_sentinel]] — code: test_ollama_api_key_sentinel()
- [[graphify_tests_test_ollama_rationale_1]] — code: Tests for the Ollama backend additions in graphify/llm.py.
- [[graphify_tests_test_ollama_rationale_16]] — code: Link-local / cloud-metadata Ollama targets fail closed (F3).
- [[graphify_tests_test_ollama_rationale_22]] — code: Loopback is silent; a general LAN host warns but is allowed (F3).
- [[graphify_tests_test_ollama_rationale_30]] — code: A hostname that RESOLVES to a link-local IP is blocked, not just literals (F3).
- [[graphify_tests_test_ollama_rationale_42]] — code: warn=False suppresses the LAN warning but never the metadata hard-block (F3).
- [[graphify_tests_test_ollama_rationale_91]] — code: extract_files_direct with backend=ollama and no OLLAMA_API_KEY should use sentin

## Dependências

- [[graphify_tests_test_ollama]] → `imports_from` → [[graphify_graphify_llm]]
- [[graphify_tests_test_ollama_test_ollama_api_key_sentinel]] → `calls` → [[graphify_graphify_llm_extract_files_direct]]
- [[graphify_tests_test_ollama_test_ollama_blocks_link_local_and_metadata]] → `calls` → [[graphify_graphify_llm_validate_ollama_base_url]]
- [[graphify_tests_test_ollama_test_ollama_loopback_and_lan_do_not_raise]] → `calls` → [[graphify_graphify_llm_validate_ollama_base_url]]
- [[graphify_tests_test_ollama_test_ollama_warn_false_still_hard_blocks_but_stays_quiet]] → `calls` → [[graphify_graphify_llm_validate_ollama_base_url]]
- [[graphify_tests_test_ollama_test_detect_backend_claude_beats_ollama]] → `calls` → [[graphify_graphify_llm_detect_backend]]
- [[graphify_tests_test_ollama_test_detect_backend_kimi_beats_ollama]] → `calls` → [[graphify_graphify_llm_detect_backend]]
- [[graphify_tests_test_ollama_test_detect_backend_none_without_envvars]] → `calls` → [[graphify_graphify_llm_detect_backend]]
- [[graphify_tests_test_ollama_test_detect_backend_ollama]] → `calls` → [[graphify_graphify_llm_detect_backend]]
- [[graphify_tests_test_ollama]] → `contains` → [[graphify_tests_test_ollama_test_detect_backend_claude_beats_ollama]]
- [[graphify_tests_test_ollama]] → `contains` → [[graphify_tests_test_ollama_test_detect_backend_kimi_beats_ollama]]
- [[graphify_tests_test_ollama]] → `contains` → [[graphify_tests_test_ollama_test_detect_backend_none_without_envvars]]
- [[graphify_tests_test_ollama]] → `contains` → [[graphify_tests_test_ollama_test_detect_backend_ollama]]
- [[graphify_tests_test_ollama]] → `contains` → [[graphify_tests_test_ollama_test_ollama_alias_resolving_to_link_local_blocked]]
- [[graphify_tests_test_ollama]] → `contains` → [[graphify_tests_test_ollama_test_ollama_api_key_sentinel]]
- [[graphify_tests_test_ollama]] → `contains` → [[graphify_tests_test_ollama_test_ollama_blocks_link_local_and_metadata]]
- [[graphify_tests_test_ollama]] → `contains` → [[graphify_tests_test_ollama_test_ollama_in_backends]]
- [[graphify_tests_test_ollama]] → `contains` → [[graphify_tests_test_ollama_test_ollama_loopback_and_lan_do_not_raise]]
- [[graphify_tests_test_ollama]] → `contains` → [[graphify_tests_test_ollama_test_ollama_warn_false_still_hard_blocks_but_stays_quiet]]
- [[graphify_tests_test_ollama_rationale_1]] → `rationale_for` → [[graphify_tests_test_ollama]]
- [[graphify_tests_test_ollama_rationale_16]] → `rationale_for` → [[graphify_tests_test_ollama_test_ollama_blocks_link_local_and_metadata]]
- [[graphify_tests_test_ollama_rationale_22]] → `rationale_for` → [[graphify_tests_test_ollama_test_ollama_loopback_and_lan_do_not_raise]]
- [[graphify_tests_test_ollama_rationale_30]] → `rationale_for` → [[graphify_tests_test_ollama_test_ollama_alias_resolving_to_link_local_blocked]]
- [[graphify_tests_test_ollama_rationale_42]] → `rationale_for` → [[graphify_tests_test_ollama_test_ollama_warn_false_still_hard_blocks_but_stays_quiet]]
- [[graphify_tests_test_ollama_rationale_91]] → `rationale_for` → [[graphify_tests_test_ollama_test_ollama_api_key_sentinel]]