# graphify\tests\test_validate.py

## Símbolos

- [[graphify_tests_test_validate]] — code: test_validate.py
- [[graphify_tests_test_validate_test_valid_passes]] — code: test_valid_passes()
- [[graphify_tests_test_validate_test_missing_nodes_key]] — code: test_missing_nodes_key()
- [[graphify_tests_test_validate_test_missing_edges_key]] — code: test_missing_edges_key()
- [[graphify_tests_test_validate_test_not_a_dict]] — code: test_not_a_dict()
- [[graphify_tests_test_validate_test_invalid_file_type]] — code: test_invalid_file_type()
- [[graphify_tests_test_validate_test_invalid_confidence]] — code: test_invalid_confidence()
- [[graphify_tests_test_validate_test_dangling_edge_source]] — code: test_dangling_edge_source()
- [[graphify_tests_test_validate_test_dangling_edge_target]] — code: test_dangling_edge_target()
- [[graphify_tests_test_validate_test_missing_node_field]] — code: test_missing_node_field()
- [[graphify_tests_test_validate_test_assert_valid_raises_on_errors]] — code: test_assert_valid_raises_on_errors()
- [[graphify_tests_test_validate_test_assert_valid_passes_silently]] — code: test_assert_valid_passes_silently()
- [[graphify_tests_test_validate_test_non_hashable_node_id_reported_not_raised]] — code: test_non_hashable_node_id_reported_not_raised()
- [[graphify_tests_test_validate_test_non_hashable_edge_endpoint_reported_not_raised]] — code: test_non_hashable_edge_endpoint_reported_not_raised()
- [[graphify_tests_test_validate_test_non_hashable_node_id_does_not_mask_valid_ids]] — code: test_non_hashable_node_id_does_not_mask_valid_ids()

## Dependências

- [[graphify_tests_test_validate]] → `imports_from` → [[graphify_graphify_validate]]
- [[graphify_tests_test_validate_test_dangling_edge_source]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_dangling_edge_target]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_invalid_confidence]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_invalid_file_type]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_missing_edges_key]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_missing_node_field]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_missing_nodes_key]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_non_hashable_edge_endpoint_reported_not_raised]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_non_hashable_node_id_does_not_mask_valid_ids]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_non_hashable_node_id_reported_not_raised]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_not_a_dict]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_valid_passes]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_tests_test_validate_test_assert_valid_passes_silently]] → `calls` → [[graphify_graphify_validate_assert_valid]]
- [[graphify_tests_test_validate_test_assert_valid_raises_on_errors]] → `calls` → [[graphify_graphify_validate_assert_valid]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_assert_valid_passes_silently]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_assert_valid_raises_on_errors]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_dangling_edge_source]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_dangling_edge_target]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_invalid_confidence]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_invalid_file_type]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_missing_edges_key]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_missing_node_field]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_missing_nodes_key]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_non_hashable_edge_endpoint_reported_not_raised]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_non_hashable_node_id_does_not_mask_valid_ids]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_non_hashable_node_id_reported_not_raised]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_not_a_dict]]
- [[graphify_tests_test_validate]] → `contains` → [[graphify_tests_test_validate_test_valid_passes]]