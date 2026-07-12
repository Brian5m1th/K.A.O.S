# graphify\tests\test_word_count_cache.py

## Símbolos

- [[graphify_tests_test_word_count_cache]] — code: test_word_count_cache.py
- [[graphify_tests_test_word_count_cache_test_word_count_cached_until_file_changes]] — code: test_word_count_cached_until_file_changes()
- [[graphify_tests_test_word_count_cache_test_word_count_augments_existing_hash_entry]] — code: test_word_count_augments_existing_hash_entry()
- [[graphify_tests_test_word_count_cache_rationale_1]] — code: #1656 — word counts are cached against each file's stat signature so detect() d

## Dependências

- [[graphify_tests_test_word_count_cache_test_word_count_augments_existing_hash_entry]] → `indirect_call` → [[assistant_tests_unit_rag_test_embeddings_cache_testembeddingcache_cache]]
- [[graphify_tests_test_word_count_cache_test_word_count_cached_until_file_changes]] → `indirect_call` → [[assistant_tests_unit_rag_test_embeddings_cache_testembeddingcache_cache]]
- [[graphify_tests_test_word_count_cache]] → `contains` → [[graphify_tests_test_word_count_cache_test_word_count_augments_existing_hash_entry]]
- [[graphify_tests_test_word_count_cache]] → `contains` → [[graphify_tests_test_word_count_cache_test_word_count_cached_until_file_changes]]
- [[graphify_tests_test_word_count_cache_rationale_1]] → `rationale_for` → [[graphify_tests_test_word_count_cache]]