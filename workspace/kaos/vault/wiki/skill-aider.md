# graphify\graphify\skill-aider.md

## Símbolos

- [[graphify_graphify_skill_aider]] — code: skill-aider.md
- [[graphify_graphify_skill_aider_graphify]] — code: /graphify
- [[graphify_graphify_skill_aider_usage]] — code: Usage
- [[graphify_graphify_skill_aider_what_graphify_is_for]] — code: What graphify is for
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] — code: What You Must Do When Invoked
- [[graphify_graphify_skill_aider_step_1_ensure_graphify_is_installed]] — code: Step 1 - Ensure graphify is installed
- [[graphify_graphify_skill_aider_step_2_detect_files]] — code: Step 2 - Detect files
- [[graphify_graphify_skill_aider_step_2_5_transcribe_video_audio_files_only_if_video_files_detected]] — code: Step 2.5 - Transcribe video / audio files (only if video files detected)
- [[graphify_graphify_skill_aider_step_3_extract_entities_and_relationships]] — code: Step 3 - Extract entities and relationships
- [[graphify_graphify_skill_aider_part_a_structural_extraction_for_code_files]] — code: Part A - Structural extraction for code files
- [[graphify_graphify_skill_aider_part_b_semantic_extraction_parallel_subagents]] — code: Part B - Semantic extraction (parallel subagents)
- [[graphify_graphify_skill_aider_part_c_merge_ast_semantic_into_final_extraction]] — code: Part C - Merge AST + semantic into final extraction
- [[graphify_graphify_skill_aider_step_4_build_graph_cluster_analyze_generate_outputs]] — code: Step 4 - Build graph, cluster, analyze, generate outputs
- [[graphify_graphify_skill_aider_step_5_label_communities]] — code: Step 5 - Label communities
- [[graphify_graphify_skill_aider_step_6_generate_obsidian_vault_opt_in_html]] — code: Step 6 - Generate Obsidian vault (opt-in) + HTML
- [[graphify_graphify_skill_aider_step_7_neo4j_export_only_if_neo4j_or_neo4j_push_flag]] — code: Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag)
- [[graphify_graphify_skill_aider_step_7b_svg_export_only_if_svg_flag]] — code: Step 7b - SVG export (only if --svg flag)
- [[graphify_graphify_skill_aider_step_7c_graphml_export_only_if_graphml_flag]] — code: Step 7c - GraphML export (only if --graphml flag)
- [[graphify_graphify_skill_aider_step_7d_mcp_server_only_if_mcp_flag]] — code: Step 7d - MCP server (only if --mcp flag)
- [[graphify_graphify_skill_aider_step_8_token_reduction_benchmark_only_if_total_words_5000]] — code: Step 8 - Token reduction benchmark (only if total_words > 5000)
- [[graphify_graphify_skill_aider_step_9_save_manifest_update_cost_tracker_clean_up_and_report]] — code: Step 9 - Save manifest, update cost tracker, clean up, and report
- [[graphify_graphify_skill_aider_for_update_incremental_re_extraction]] — code: For --update (incremental re-extraction)
- [[graphify_graphify_skill_aider_for_cluster_only]] — code: For --cluster-only
- [[graphify_graphify_skill_aider_for_graphify_query]] — code: For /graphify query
- [[graphify_graphify_skill_aider_for_graphify_path]] — code: For /graphify path
- [[graphify_graphify_skill_aider_for_graphify_explain]] — code: For /graphify explain
- [[graphify_graphify_skill_aider_for_graphify_add]] — code: For /graphify add
- [[graphify_graphify_skill_aider_for_watch]] — code: For --watch
- [[graphify_graphify_skill_aider_for_git_commit_hook]] — code: For git commit hook
- [[graphify_graphify_skill_aider_for_native_claude_md_integration]] — code: For native CLAUDE.md integration
- [[graphify_graphify_skill_aider_honesty_rules]] — code: Honesty Rules

## Dependências

- [[graphify_graphify_skill_aider]] → `contains` → [[graphify_graphify_skill_aider_graphify]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_for_cluster_only]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_for_git_commit_hook]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_for_graphify_add]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_for_graphify_explain]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_for_graphify_path]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_for_graphify_query]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_for_native_claude_md_integration]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_for_update_incremental_re_extraction]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_for_watch]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_honesty_rules]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_usage]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_what_graphify_is_for]]
- [[graphify_graphify_skill_aider_graphify]] → `contains` → [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_1_ensure_graphify_is_installed]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_2_5_transcribe_video_audio_files_only_if_video_files_detected]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_2_detect_files]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_3_extract_entities_and_relationships]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_4_build_graph_cluster_analyze_generate_outputs]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_5_label_communities]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_6_generate_obsidian_vault_opt_in_html]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_7_neo4j_export_only_if_neo4j_or_neo4j_push_flag]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_7b_svg_export_only_if_svg_flag]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_7c_graphml_export_only_if_graphml_flag]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_7d_mcp_server_only_if_mcp_flag]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_8_token_reduction_benchmark_only_if_total_words_5000]]
- [[graphify_graphify_skill_aider_what_you_must_do_when_invoked]] → `contains` → [[graphify_graphify_skill_aider_step_9_save_manifest_update_cost_tracker_clean_up_and_report]]
- [[graphify_graphify_skill_aider_step_3_extract_entities_and_relationships]] → `contains` → [[graphify_graphify_skill_aider_part_a_structural_extraction_for_code_files]]
- [[graphify_graphify_skill_aider_step_3_extract_entities_and_relationships]] → `contains` → [[graphify_graphify_skill_aider_part_b_semantic_extraction_parallel_subagents]]
- [[graphify_graphify_skill_aider_step_3_extract_entities_and_relationships]] → `contains` → [[graphify_graphify_skill_aider_part_c_merge_ast_semantic_into_final_extraction]]