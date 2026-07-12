# graphify\tests\test_confidence.py

## Símbolos

- [[graphify_tests_test_confidence]] — code: test_confidence.py
- [[graphify_tests_test_confidence_make_extraction]] — code: _make_extraction()
- [[graphify_tests_test_confidence_test_extracted_edges_have_score_1]] — code: test_extracted_edges_have_score_1()
- [[graphify_tests_test_confidence_test_inferred_edges_score_in_range]] — code: test_inferred_edges_score_in_range()
- [[graphify_tests_test_confidence_test_ambiguous_edges_score_at_most_04]] — code: test_ambiguous_edges_score_at_most_04()
- [[graphify_tests_test_confidence_test_confidence_score_round_trip]] — code: test_confidence_score_round_trip()
- [[graphify_tests_test_confidence_test_to_json_defaults_missing_confidence_score]] — code: test_to_json_defaults_missing_confidence_score()
- [[graphify_tests_test_confidence_test_report_shows_avg_confidence_for_inferred]] — code: test_report_shows_avg_confidence_for_inferred()
- [[graphify_tests_test_confidence_test_report_inferred_tag_with_score]] — code: test_report_inferred_tag_with_score()
- [[graphify_tests_test_confidence_rationale_1]] — code: Tests for confidence_score on edges.
- [[graphify_tests_test_confidence_rationale_18]] — code: Return a minimal extraction dict with one edge of each confidence type.
- [[graphify_tests_test_confidence_rationale_41]] — code: EXTRACTED edges must have confidence_score == 1.0.
- [[graphify_tests_test_confidence_rationale_51]] — code: INFERRED edges must have confidence_score between 0.0 and 1.0.
- [[graphify_tests_test_confidence_rationale_66]] — code: AMBIGUOUS edges must have confidence_score <= 0.4.
- [[graphify_tests_test_confidence_rationale_81]] — code: confidence_score survives build_from_json → to_json → JSON parse round-trip.
- [[graphify_tests_test_confidence_rationale_102]] — code: Edges lacking confidence_score get sensible defaults in to_json.
- [[graphify_tests_test_confidence_rationale_137]] — code: Report summary line should include avg confidence for INFERRED edges.
- [[graphify_tests_test_confidence_rationale_155]] — code: Surprising connections section shows confidence score next to INFERRED edges.

## Dependências

- [[graphify_tests_test_confidence]] → `imports_from` → [[graphify_graphify_analyze]]
- [[graphify_tests_test_confidence]] → `imports_from` → [[graphify_graphify_build]]
- [[graphify_tests_test_confidence]] → `imports_from` → [[graphify_graphify_cluster]]
- [[graphify_tests_test_confidence]] → `imports_from` → [[graphify_graphify_export]]
- [[graphify_tests_test_confidence_test_confidence_score_round_trip]] → `calls` → [[graphify_graphify_export_to_json]]
- [[graphify_tests_test_confidence_test_to_json_defaults_missing_confidence_score]] → `calls` → [[graphify_graphify_export_to_json]]
- [[graphify_tests_test_confidence]] → `imports_from` → [[graphify_graphify_report]]
- [[graphify_tests_test_confidence_test_report_inferred_tag_with_score]] → `calls` → [[graphify_graphify_report_generate]]
- [[graphify_tests_test_confidence_test_report_shows_avg_confidence_for_inferred]] → `calls` → [[graphify_graphify_report_generate]]
- [[graphify_tests_test_confidence]] → `contains` → [[graphify_tests_test_confidence_make_extraction]]
- [[graphify_tests_test_confidence]] → `contains` → [[graphify_tests_test_confidence_test_ambiguous_edges_score_at_most_04]]
- [[graphify_tests_test_confidence]] → `contains` → [[graphify_tests_test_confidence_test_confidence_score_round_trip]]
- [[graphify_tests_test_confidence]] → `contains` → [[graphify_tests_test_confidence_test_extracted_edges_have_score_1]]
- [[graphify_tests_test_confidence]] → `contains` → [[graphify_tests_test_confidence_test_inferred_edges_score_in_range]]
- [[graphify_tests_test_confidence]] → `contains` → [[graphify_tests_test_confidence_test_report_inferred_tag_with_score]]
- [[graphify_tests_test_confidence]] → `contains` → [[graphify_tests_test_confidence_test_report_shows_avg_confidence_for_inferred]]
- [[graphify_tests_test_confidence]] → `contains` → [[graphify_tests_test_confidence_test_to_json_defaults_missing_confidence_score]]
- [[graphify_tests_test_confidence_rationale_1]] → `rationale_for` → [[graphify_tests_test_confidence]]
- [[graphify_tests_test_confidence_rationale_18]] → `rationale_for` → [[graphify_tests_test_confidence_make_extraction]]
- [[graphify_tests_test_confidence_test_ambiguous_edges_score_at_most_04]] → `calls` → [[graphify_tests_test_confidence_make_extraction]]
- [[graphify_tests_test_confidence_test_confidence_score_round_trip]] → `calls` → [[graphify_tests_test_confidence_make_extraction]]
- [[graphify_tests_test_confidence_test_extracted_edges_have_score_1]] → `calls` → [[graphify_tests_test_confidence_make_extraction]]
- [[graphify_tests_test_confidence_test_inferred_edges_score_in_range]] → `calls` → [[graphify_tests_test_confidence_make_extraction]]
- [[graphify_tests_test_confidence_test_report_shows_avg_confidence_for_inferred]] → `calls` → [[graphify_tests_test_confidence_make_extraction]]
- [[graphify_tests_test_confidence_rationale_41]] → `rationale_for` → [[graphify_tests_test_confidence_test_extracted_edges_have_score_1]]
- [[graphify_tests_test_confidence_rationale_51]] → `rationale_for` → [[graphify_tests_test_confidence_test_inferred_edges_score_in_range]]
- [[graphify_tests_test_confidence_rationale_66]] → `rationale_for` → [[graphify_tests_test_confidence_test_ambiguous_edges_score_at_most_04]]
- [[graphify_tests_test_confidence_rationale_81]] → `rationale_for` → [[graphify_tests_test_confidence_test_confidence_score_round_trip]]
- [[graphify_tests_test_confidence_rationale_102]] → `rationale_for` → [[graphify_tests_test_confidence_test_to_json_defaults_missing_confidence_score]]
- [[graphify_tests_test_confidence_rationale_137]] → `rationale_for` → [[graphify_tests_test_confidence_test_report_shows_avg_confidence_for_inferred]]
- [[graphify_tests_test_confidence_rationale_155]] → `rationale_for` → [[graphify_tests_test_confidence_test_report_inferred_tag_with_score]]