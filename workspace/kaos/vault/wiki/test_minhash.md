# graphify\tests\test_minhash.py

## Símbolos

- [[graphify_tests_test_minhash]] — code: test_minhash.py
- [[graphify_tests_test_minhash_minhash_for]] — code: _minhash_for()
- [[graphify_tests_test_minhash_test_identical_texts_produce_identical_hashvalues]] — code: test_identical_texts_produce_identical_hashvalues()
- [[graphify_tests_test_minhash_test_similar_texts_share_most_hashvalues]] — code: test_similar_texts_share_most_hashvalues()
- [[graphify_tests_test_minhash_test_unrelated_texts_share_few_hashvalues]] — code: test_unrelated_texts_share_few_hashvalues()
- [[graphify_tests_test_minhash_test_update_mutates_hashvalues]] — code: test_update_mutates_hashvalues()
- [[graphify_tests_test_minhash_test_near_duplicates_are_candidates]] — code: test_near_duplicates_are_candidates()
- [[graphify_tests_test_minhash_test_unrelated_strings_not_candidates]] — code: test_unrelated_strings_not_candidates()
- [[graphify_tests_test_minhash_test_query_always_returns_self]] — code: test_query_always_returns_self()
- [[graphify_tests_test_minhash_test_duplicate_insert_raises]] — code: test_duplicate_insert_raises()
- [[graphify_tests_test_minhash_test_optimal_params_within_budget]] — code: test_optimal_params_within_budget()
- [[graphify_tests_test_minhash_test_optimal_params_cached]] — code: test_optimal_params_cached()
- [[graphify_tests_test_minhash_test_dedup_import_does_not_pull_scipy_or_numpy_testing]] — code: test_dedup_import_does_not_pull_scipy_or_numpy_testing()
- [[graphify_tests_test_minhash_rationale_1]] — code: Tests for graphify/_minhash.py — MinHash sketch and band-LSH.

## Dependências

- [[graphify_tests_test_minhash]] → `imports_from` → [[graphify_graphify_minhash]]
- [[graphify_tests_test_minhash_minhash_for]] → `references` → [[graphify_graphify_minhash_minhash]]
- [[graphify_tests_test_minhash_test_update_mutates_hashvalues]] → `calls` → [[graphify_graphify_minhash_minhash]]
- [[graphify_tests_test_minhash_test_optimal_params_cached]] → `calls` → [[graphify_graphify_minhash_optimal_lsh_params]]
- [[graphify_tests_test_minhash_test_optimal_params_within_budget]] → `calls` → [[graphify_graphify_minhash_optimal_lsh_params]]
- [[graphify_tests_test_minhash_test_duplicate_insert_raises]] → `calls` → [[graphify_graphify_minhash_minhashlsh]]
- [[graphify_tests_test_minhash_test_near_duplicates_are_candidates]] → `calls` → [[graphify_graphify_minhash_minhashlsh]]
- [[graphify_tests_test_minhash_test_query_always_returns_self]] → `calls` → [[graphify_graphify_minhash_minhashlsh]]
- [[graphify_tests_test_minhash_test_unrelated_strings_not_candidates]] → `calls` → [[graphify_graphify_minhash_minhashlsh]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_minhash_for]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_dedup_import_does_not_pull_scipy_or_numpy_testing]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_duplicate_insert_raises]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_identical_texts_produce_identical_hashvalues]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_near_duplicates_are_candidates]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_optimal_params_cached]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_optimal_params_within_budget]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_query_always_returns_self]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_similar_texts_share_most_hashvalues]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_unrelated_strings_not_candidates]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_unrelated_texts_share_few_hashvalues]]
- [[graphify_tests_test_minhash]] → `contains` → [[graphify_tests_test_minhash_test_update_mutates_hashvalues]]
- [[graphify_tests_test_minhash_rationale_1]] → `rationale_for` → [[graphify_tests_test_minhash]]
- [[graphify_tests_test_minhash_test_duplicate_insert_raises]] → `calls` → [[graphify_tests_test_minhash_minhash_for]]
- [[graphify_tests_test_minhash_test_identical_texts_produce_identical_hashvalues]] → `calls` → [[graphify_tests_test_minhash_minhash_for]]
- [[graphify_tests_test_minhash_test_near_duplicates_are_candidates]] → `calls` → [[graphify_tests_test_minhash_minhash_for]]
- [[graphify_tests_test_minhash_test_query_always_returns_self]] → `calls` → [[graphify_tests_test_minhash_minhash_for]]
- [[graphify_tests_test_minhash_test_similar_texts_share_most_hashvalues]] → `calls` → [[graphify_tests_test_minhash_minhash_for]]
- [[graphify_tests_test_minhash_test_unrelated_strings_not_candidates]] → `calls` → [[graphify_tests_test_minhash_minhash_for]]
- [[graphify_tests_test_minhash_test_unrelated_texts_share_few_hashvalues]] → `calls` → [[graphify_tests_test_minhash_minhash_for]]