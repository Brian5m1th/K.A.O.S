# graphify\tests\test_llm_parser.py

## Símbolos

- [[graphify_tests_test_llm_parser]] — code: test_llm_parser.py
- [[graphify_tests_test_llm_parser_test_preamble_then_fence_is_parsed]] — code: test_preamble_then_fence_is_parsed()
- [[graphify_tests_test_llm_parser_test_prose_wrapped_json_without_fence_is_parsed]] — code: test_prose_wrapped_json_without_fence_is_parsed()
- [[graphify_tests_test_llm_parser_test_raw_json_still_works]] — code: test_raw_json_still_works()
- [[graphify_tests_test_llm_parser_test_total_refusal_returns_empty_fragment]] — code: test_total_refusal_returns_empty_fragment()
- [[graphify_tests_test_llm_parser_test_fence_with_uppercase_language_tag]] — code: test_fence_with_uppercase_language_tag()
- [[graphify_tests_test_llm_parser_test_fence_without_closing_backticks]] — code: test_fence_without_closing_backticks()
- [[graphify_tests_test_llm_parser_test_empty_response_returns_empty_fragment]] — code: test_empty_response_returns_empty_fragment()
- [[graphify_tests_test_llm_parser_make_envelope]] — code: _make_envelope()
- [[graphify_tests_test_llm_parser_test_instructions_ride_in_user_turn_not_system_prompt]] — code: test_instructions_ride_in_user_turn_not_system_prompt()
- [[graphify_tests_test_llm_parser_test_model_env_var_adds_model_flag]] — code: test_model_env_var_adds_model_flag()
- [[graphify_tests_test_llm_parser_test_no_model_flag_when_env_var_unset]] — code: test_no_model_flag_when_env_var_unset()
- [[graphify_tests_test_llm_parser_rationale_1]] — code: Tests for `_parse_llm_json` robustness and the `_call_claude_cli` subprocess ar
- [[graphify_tests_test_llm_parser_rationale_23]] — code: Claude often prefixes the JSON with a short preamble before the     ```json fen
- [[graphify_tests_test_llm_parser_rationale_38]] — code: Some models return prose around bare JSON with no markdown fence.     The balan
- [[graphify_tests_test_llm_parser_rationale_49]] — code: Regression: clean JSON input (the original happy path) must keep     parsing ex
- [[graphify_tests_test_llm_parser_rationale_57]] — code: When the model refuses or returns unrelated prose, the parser     must degrade
- [[graphify_tests_test_llm_parser_rationale_75]] — code: Truncated response: the model started the fence but ran out of     tokens befor
- [[graphify_tests_test_llm_parser_rationale_105]] — code: Extraction instructions must be delivered in the user turn, not via     --syste
- [[graphify_tests_test_llm_parser_rationale_133]] — code: GRAPHIFY_CLAUDE_CLI_MODEL must be forwarded to claude -p --model.
- [[graphify_tests_test_llm_parser_rationale_147]] — code: Default behaviour: when the env var is not set, --model is not     added so cla

## Dependências

- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_make_envelope]]
- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_test_empty_response_returns_empty_fragment]]
- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_test_fence_with_uppercase_language_tag]]
- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_test_fence_without_closing_backticks]]
- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_test_instructions_ride_in_user_turn_not_system_prompt]]
- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_test_model_env_var_adds_model_flag]]
- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_test_no_model_flag_when_env_var_unset]]
- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_test_preamble_then_fence_is_parsed]]
- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_test_prose_wrapped_json_without_fence_is_parsed]]
- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_test_raw_json_still_works]]
- [[graphify_tests_test_llm_parser]] → `contains` → [[graphify_tests_test_llm_parser_test_total_refusal_returns_empty_fragment]]
- [[graphify_tests_test_llm_parser_rationale_1]] → `rationale_for` → [[graphify_tests_test_llm_parser]]
- [[graphify_tests_test_llm_parser_rationale_23]] → `rationale_for` → [[graphify_tests_test_llm_parser_test_preamble_then_fence_is_parsed]]
- [[graphify_tests_test_llm_parser_rationale_38]] → `rationale_for` → [[graphify_tests_test_llm_parser_test_prose_wrapped_json_without_fence_is_parsed]]
- [[graphify_tests_test_llm_parser_rationale_49]] → `rationale_for` → [[graphify_tests_test_llm_parser_test_raw_json_still_works]]
- [[graphify_tests_test_llm_parser_rationale_57]] → `rationale_for` → [[graphify_tests_test_llm_parser_test_total_refusal_returns_empty_fragment]]
- [[graphify_tests_test_llm_parser_rationale_75]] → `rationale_for` → [[graphify_tests_test_llm_parser_test_fence_without_closing_backticks]]
- [[graphify_tests_test_llm_parser_test_instructions_ride_in_user_turn_not_system_prompt]] → `calls` → [[graphify_tests_test_llm_parser_make_envelope]]
- [[graphify_tests_test_llm_parser_test_model_env_var_adds_model_flag]] → `calls` → [[graphify_tests_test_llm_parser_make_envelope]]
- [[graphify_tests_test_llm_parser_test_no_model_flag_when_env_var_unset]] → `calls` → [[graphify_tests_test_llm_parser_make_envelope]]
- [[graphify_tests_test_llm_parser_rationale_105]] → `rationale_for` → [[graphify_tests_test_llm_parser_test_instructions_ride_in_user_turn_not_system_prompt]]
- [[graphify_tests_test_llm_parser_rationale_133]] → `rationale_for` → [[graphify_tests_test_llm_parser_test_model_env_var_adds_model_flag]]
- [[graphify_tests_test_llm_parser_rationale_147]] → `rationale_for` → [[graphify_tests_test_llm_parser_test_no_model_flag_when_env_var_unset]]