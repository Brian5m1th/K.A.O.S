# graphify\tests\test_obsidian_dangling_member.py

## Símbolos

- [[graphify_tests_test_obsidian_dangling_member]] — code: test_obsidian_dangling_member.py
- [[graphify_tests_test_obsidian_dangling_member_graph_with_dangling_member]] — code: _graph_with_dangling_member()
- [[graphify_tests_test_obsidian_dangling_member_test_obsidian_dangling_community_member_does_not_crash]] — code: test_obsidian_dangling_community_member_does_not_crash()
- [[graphify_tests_test_obsidian_dangling_member_test_obsidian_community_of_only_dangling_members]] — code: test_obsidian_community_of_only_dangling_members()
- [[graphify_tests_test_obsidian_dangling_member_test_canvas_dangling_community_member_does_not_crash]] — code: test_canvas_dangling_community_member_does_not_crash()
- [[graphify_tests_test_obsidian_dangling_member_rationale_1]] — code: Regression test for issue #1236: to_obsidian must not crash with KeyError when
- [[graphify_tests_test_obsidian_dangling_member_rationale_11]] — code: Two real nodes plus a community that references a third, non-existent id.
- [[graphify_tests_test_obsidian_dangling_member_rationale_42]] — code: A community whose members are all dangling should still not crash.
- [[graphify_tests_test_obsidian_dangling_member_rationale_54]] — code: #1236 follow-up: the fix landed in to_obsidian but not to_canvas, so     `graph

## Dependências

- [[graphify_tests_test_obsidian_dangling_member]] → `imports_from` → [[graphify_graphify_export]]
- [[graphify_tests_test_obsidian_dangling_member_test_obsidian_community_of_only_dangling_members]] → `calls` → [[graphify_graphify_export_to_obsidian]]
- [[graphify_tests_test_obsidian_dangling_member_test_obsidian_dangling_community_member_does_not_crash]] → `calls` → [[graphify_graphify_export_to_obsidian]]
- [[graphify_tests_test_obsidian_dangling_member_test_canvas_dangling_community_member_does_not_crash]] → `calls` → [[graphify_graphify_export_to_canvas]]
- [[graphify_tests_test_obsidian_dangling_member]] → `contains` → [[graphify_tests_test_obsidian_dangling_member_graph_with_dangling_member]]
- [[graphify_tests_test_obsidian_dangling_member]] → `contains` → [[graphify_tests_test_obsidian_dangling_member_test_canvas_dangling_community_member_does_not_crash]]
- [[graphify_tests_test_obsidian_dangling_member]] → `contains` → [[graphify_tests_test_obsidian_dangling_member_test_obsidian_community_of_only_dangling_members]]
- [[graphify_tests_test_obsidian_dangling_member]] → `contains` → [[graphify_tests_test_obsidian_dangling_member_test_obsidian_dangling_community_member_does_not_crash]]
- [[graphify_tests_test_obsidian_dangling_member_rationale_1]] → `rationale_for` → [[graphify_tests_test_obsidian_dangling_member]]
- [[graphify_tests_test_obsidian_dangling_member_rationale_11]] → `rationale_for` → [[graphify_tests_test_obsidian_dangling_member_graph_with_dangling_member]]
- [[graphify_tests_test_obsidian_dangling_member_test_canvas_dangling_community_member_does_not_crash]] → `calls` → [[graphify_tests_test_obsidian_dangling_member_graph_with_dangling_member]]
- [[graphify_tests_test_obsidian_dangling_member_test_obsidian_dangling_community_member_does_not_crash]] → `calls` → [[graphify_tests_test_obsidian_dangling_member_graph_with_dangling_member]]
- [[graphify_tests_test_obsidian_dangling_member_rationale_42]] → `rationale_for` → [[graphify_tests_test_obsidian_dangling_member_test_obsidian_community_of_only_dangling_members]]
- [[graphify_tests_test_obsidian_dangling_member_rationale_54]] → `rationale_for` → [[graphify_tests_test_obsidian_dangling_member_test_canvas_dangling_community_member_does_not_crash]]