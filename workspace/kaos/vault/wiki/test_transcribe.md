# graphify\tests\test_transcribe.py

## Símbolos

- [[graphify_tests_test_transcribe]] — code: test_transcribe.py
- [[graphify_tests_test_transcribe_test_video_extensions_set]] — code: test_video_extensions_set()
- [[graphify_tests_test_transcribe_test_build_whisper_prompt_no_nodes]] — code: test_build_whisper_prompt_no_nodes()
- [[graphify_tests_test_transcribe_test_build_whisper_prompt_env_override]] — code: test_build_whisper_prompt_env_override()
- [[graphify_tests_test_transcribe_test_build_whisper_prompt_returns_topic_string]] — code: test_build_whisper_prompt_returns_topic_string()
- [[graphify_tests_test_transcribe_test_build_whisper_prompt_nodes_without_labels]] — code: test_build_whisper_prompt_nodes_without_labels()
- [[graphify_tests_test_transcribe_test_transcribe_uses_cache]] — code: test_transcribe_uses_cache()
- [[graphify_tests_test_transcribe_test_transcribe_force_reruns]] — code: test_transcribe_force_reruns()
- [[graphify_tests_test_transcribe_test_transcribe_missing_faster_whisper]] — code: test_transcribe_missing_faster_whisper()
- [[graphify_tests_test_transcribe_test_transcribe_all_empty]] — code: test_transcribe_all_empty()
- [[graphify_tests_test_transcribe_test_transcribe_all_uses_cache]] — code: test_transcribe_all_uses_cache()
- [[graphify_tests_test_transcribe_test_transcribe_all_skips_failed]] — code: test_transcribe_all_skips_failed()
- [[graphify_tests_test_transcribe_rationale_1]] — code: Tests for graphify.transcribe — video/audio transcription support.
- [[graphify_tests_test_transcribe_rationale_35]] — code: Empty god_nodes returns fallback prompt.
- [[graphify_tests_test_transcribe_rationale_41]] — code: GRAPHIFY_WHISPER_PROMPT env var short-circuits LLM call.
- [[graphify_tests_test_transcribe_rationale_48]] — code: Returns a topic-based prompt from god node labels — no LLM call.
- [[graphify_tests_test_transcribe_rationale_58]] — code: Nodes missing 'label' keys are safely skipped.
- [[graphify_tests_test_transcribe_rationale_69]] — code: If transcript already exists, transcribe() returns cached path without running W
- [[graphify_tests_test_transcribe_rationale_82]] — code: force=True re-transcribes even when cache exists.
- [[graphify_tests_test_transcribe_rationale_104]] — code: ImportError propagates when faster_whisper is not installed.
- [[graphify_tests_test_transcribe_rationale_118]] — code: Empty input returns empty list without error.
- [[graphify_tests_test_transcribe_rationale_123]] — code: transcribe_all() returns cached paths for already-transcribed files.
- [[graphify_tests_test_transcribe_rationale_137]] — code: transcribe_all() warns and skips files that fail to transcribe.

## Dependências

- [[graphify_tests_test_transcribe]] → `imports_from` → [[graphify_graphify_transcribe]]
- [[graphify_tests_test_transcribe_test_build_whisper_prompt_env_override]] → `calls` → [[graphify_graphify_transcribe_build_whisper_prompt]]
- [[graphify_tests_test_transcribe_test_build_whisper_prompt_no_nodes]] → `calls` → [[graphify_graphify_transcribe_build_whisper_prompt]]
- [[graphify_tests_test_transcribe_test_build_whisper_prompt_nodes_without_labels]] → `calls` → [[graphify_graphify_transcribe_build_whisper_prompt]]
- [[graphify_tests_test_transcribe_test_build_whisper_prompt_returns_topic_string]] → `calls` → [[graphify_graphify_transcribe_build_whisper_prompt]]
- [[graphify_tests_test_transcribe_test_transcribe_force_reruns]] → `calls` → [[graphify_graphify_transcribe_transcribe]]
- [[graphify_tests_test_transcribe_test_transcribe_missing_faster_whisper]] → `calls` → [[graphify_graphify_transcribe_transcribe]]
- [[graphify_tests_test_transcribe_test_transcribe_uses_cache]] → `calls` → [[graphify_graphify_transcribe_transcribe]]
- [[graphify_tests_test_transcribe_test_transcribe_all_empty]] → `calls` → [[graphify_graphify_transcribe_transcribe_all]]
- [[graphify_tests_test_transcribe_test_transcribe_all_skips_failed]] → `calls` → [[graphify_graphify_transcribe_transcribe_all]]
- [[graphify_tests_test_transcribe_test_transcribe_all_uses_cache]] → `calls` → [[graphify_graphify_transcribe_transcribe_all]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_build_whisper_prompt_env_override]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_build_whisper_prompt_no_nodes]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_build_whisper_prompt_nodes_without_labels]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_build_whisper_prompt_returns_topic_string]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_transcribe_all_empty]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_transcribe_all_skips_failed]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_transcribe_all_uses_cache]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_transcribe_force_reruns]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_transcribe_missing_faster_whisper]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_transcribe_uses_cache]]
- [[graphify_tests_test_transcribe]] → `contains` → [[graphify_tests_test_transcribe_test_video_extensions_set]]
- [[graphify_tests_test_transcribe_rationale_1]] → `rationale_for` → [[graphify_tests_test_transcribe]]
- [[graphify_tests_test_transcribe_rationale_35]] → `rationale_for` → [[graphify_tests_test_transcribe_test_build_whisper_prompt_no_nodes]]
- [[graphify_tests_test_transcribe_rationale_41]] → `rationale_for` → [[graphify_tests_test_transcribe_test_build_whisper_prompt_env_override]]
- [[graphify_tests_test_transcribe_rationale_48]] → `rationale_for` → [[graphify_tests_test_transcribe_test_build_whisper_prompt_returns_topic_string]]
- [[graphify_tests_test_transcribe_rationale_58]] → `rationale_for` → [[graphify_tests_test_transcribe_test_build_whisper_prompt_nodes_without_labels]]
- [[graphify_tests_test_transcribe_rationale_69]] → `rationale_for` → [[graphify_tests_test_transcribe_test_transcribe_uses_cache]]
- [[graphify_tests_test_transcribe_rationale_82]] → `rationale_for` → [[graphify_tests_test_transcribe_test_transcribe_force_reruns]]
- [[graphify_tests_test_transcribe_rationale_104]] → `rationale_for` → [[graphify_tests_test_transcribe_test_transcribe_missing_faster_whisper]]
- [[graphify_tests_test_transcribe_rationale_118]] → `rationale_for` → [[graphify_tests_test_transcribe_test_transcribe_all_empty]]
- [[graphify_tests_test_transcribe_rationale_123]] → `rationale_for` → [[graphify_tests_test_transcribe_test_transcribe_all_uses_cache]]
- [[graphify_tests_test_transcribe_rationale_137]] → `rationale_for` → [[graphify_tests_test_transcribe_test_transcribe_all_skips_failed]]