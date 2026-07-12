# graphify\tests\test_semantic_similarity.py

## Símbolos

- [[graphify_tests_test_semantic_similarity]] — code: test_semantic_similarity.py
- [[graphify_tests_test_semantic_similarity_make_extraction_with_semantic_edge]] — code: _make_extraction_with_semantic_edge()
- [[graphify_tests_test_semantic_similarity_make_graph_with_semantic_edge]] — code: _make_graph_with_semantic_edge()
- [[graphify_tests_test_semantic_similarity_make_two_edge_graph]] — code: _make_two_edge_graph()
- [[graphify_tests_test_semantic_similarity_test_semantic_edge_survives_build_from_json]] — code: test_semantic_edge_survives_build_from_json()
- [[graphify_tests_test_semantic_similarity_test_semantic_edge_nodes_present]] — code: test_semantic_edge_nodes_present()
- [[graphify_tests_test_semantic_similarity_test_semantic_edge_confidence_score_preserved]] — code: test_semantic_edge_confidence_score_preserved()
- [[graphify_tests_test_semantic_similarity_test_semantic_edge_scores_higher_than_references]] — code: test_semantic_edge_scores_higher_than_references()
- [[graphify_tests_test_semantic_similarity_test_semantic_edge_reason_mentions_similarity]] — code: test_semantic_edge_reason_mentions_similarity()
- [[graphify_tests_test_semantic_similarity_make_report_with_semantic_surprise]] — code: _make_report_with_semantic_surprise()
- [[graphify_tests_test_semantic_similarity_test_report_renders_semantically_similar_tag]] — code: test_report_renders_semantically_similar_tag()
- [[graphify_tests_test_semantic_similarity_test_report_semantic_tag_on_correct_line]] — code: test_report_semantic_tag_on_correct_line()
- [[graphify_tests_test_semantic_similarity_test_report_no_semantic_tag_for_other_relations]] — code: test_report_no_semantic_tag_for_other_relations()
- [[graphify_tests_test_semantic_similarity_rationale_1]] — code: Tests for semantically_similar_to edge support.
- [[graphify_tests_test_semantic_similarity_rationale_14]] — code: Two nodes in separate files connected by a semantically_similar_to edge.
- [[graphify_tests_test_semantic_similarity_rationale_44]] — code: Graph with one semantically_similar_to edge and one references edge, both cross-
- [[graphify_tests_test_semantic_similarity_rationale_167]] — code: Non-semantic edges must not get the [semantically similar] tag.

## Dependências

- [[graphify_tests_test_semantic_similarity]] → `imports_from` → [[graphify_graphify_analyze]]
- [[graphify_tests_test_semantic_similarity]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_semantic_similarity]] → `imports_from` → [[graphify_graphify_report]]
- [[graphify_tests_test_semantic_similarity_make_report_with_semantic_surprise]] → `calls` → [[graphify_graphify_report_generate]]
- [[graphify_tests_test_semantic_similarity_test_report_no_semantic_tag_for_other_relations]] → `calls` → [[graphify_graphify_report_generate]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_make_extraction_with_semantic_edge]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_make_graph_with_semantic_edge]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_make_report_with_semantic_surprise]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_make_two_edge_graph]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_test_report_no_semantic_tag_for_other_relations]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_test_report_renders_semantically_similar_tag]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_test_report_semantic_tag_on_correct_line]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_test_semantic_edge_confidence_score_preserved]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_test_semantic_edge_nodes_present]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_test_semantic_edge_reason_mentions_similarity]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_test_semantic_edge_scores_higher_than_references]]
- [[graphify_tests_test_semantic_similarity]] → `contains` → [[graphify_tests_test_semantic_similarity_test_semantic_edge_survives_build_from_json]]
- [[graphify_tests_test_semantic_similarity_rationale_1]] → `rationale_for` → [[graphify_tests_test_semantic_similarity]]
- [[graphify_tests_test_semantic_similarity_make_graph_with_semantic_edge]] → `calls` → [[graphify_tests_test_semantic_similarity_make_extraction_with_semantic_edge]]
- [[graphify_tests_test_semantic_similarity_rationale_14]] → `rationale_for` → [[graphify_tests_test_semantic_similarity_make_extraction_with_semantic_edge]]
- [[graphify_tests_test_semantic_similarity_make_report_with_semantic_surprise]] → `calls` → [[graphify_tests_test_semantic_similarity_make_graph_with_semantic_edge]]
- [[graphify_tests_test_semantic_similarity_test_semantic_edge_confidence_score_preserved]] → `calls` → [[graphify_tests_test_semantic_similarity_make_graph_with_semantic_edge]]
- [[graphify_tests_test_semantic_similarity_test_semantic_edge_nodes_present]] → `calls` → [[graphify_tests_test_semantic_similarity_make_graph_with_semantic_edge]]
- [[graphify_tests_test_semantic_similarity_test_semantic_edge_survives_build_from_json]] → `calls` → [[graphify_tests_test_semantic_similarity_make_graph_with_semantic_edge]]
- [[graphify_tests_test_semantic_similarity_rationale_44]] → `rationale_for` → [[graphify_tests_test_semantic_similarity_make_two_edge_graph]]
- [[graphify_tests_test_semantic_similarity_test_semantic_edge_reason_mentions_similarity]] → `calls` → [[graphify_tests_test_semantic_similarity_make_two_edge_graph]]
- [[graphify_tests_test_semantic_similarity_test_semantic_edge_scores_higher_than_references]] → `calls` → [[graphify_tests_test_semantic_similarity_make_two_edge_graph]]
- [[graphify_tests_test_semantic_similarity_test_report_renders_semantically_similar_tag]] → `calls` → [[graphify_tests_test_semantic_similarity_make_report_with_semantic_surprise]]
- [[graphify_tests_test_semantic_similarity_test_report_semantic_tag_on_correct_line]] → `calls` → [[graphify_tests_test_semantic_similarity_make_report_with_semantic_surprise]]
- [[graphify_tests_test_semantic_similarity_rationale_167]] → `rationale_for` → [[graphify_tests_test_semantic_similarity_test_report_no_semantic_tag_for_other_relations]]