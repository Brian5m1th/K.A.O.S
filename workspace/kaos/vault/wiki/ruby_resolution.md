# graphify\graphify\ruby_resolution.py

## Símbolos

- [[graphify_graphify_ruby_resolution]] — code: ruby_resolution.py
- [[graphify_graphify_ruby_resolution_key]] — code: _key()
- [[graphify_graphify_ruby_resolution_ruby_raw_calls]] — code: _ruby_raw_calls()
- [[graphify_graphify_ruby_resolution_resolve_ruby_member_calls]] — code: resolve_ruby_member_calls()
- [[graphify_graphify_ruby_resolution_rationale_1]] — code: Type-aware cross-file resolution for Ruby member calls.  Ruby has no type anno
- [[graphify_graphify_ruby_resolution_rationale_27]] — code: Normalize a class/method label to a comparison key (drop punctuation).
- [[graphify_graphify_ruby_resolution_rationale_57]] — code: Resolve Ruby ``Class.new`` and typed ``var.method`` calls by receiver type.

## Dependências

- [[graphify_graphify_ruby_resolution]] → `contains` → [[graphify_graphify_ruby_resolution_key]]
- [[graphify_graphify_ruby_resolution]] → `contains` → [[graphify_graphify_ruby_resolution_resolve_ruby_member_calls]]
- [[graphify_graphify_ruby_resolution]] → `contains` → [[graphify_graphify_ruby_resolution_ruby_raw_calls]]
- [[graphify_graphify_ruby_resolution_rationale_1]] → `rationale_for` → [[graphify_graphify_ruby_resolution]]
- [[graphify_graphify_ruby_resolution_rationale_27]] → `rationale_for` → [[graphify_graphify_ruby_resolution_key]]
- [[graphify_graphify_ruby_resolution_resolve_ruby_member_calls]] → `calls` → [[graphify_graphify_ruby_resolution_key]]
- [[graphify_graphify_ruby_resolution_resolve_ruby_member_calls]] → `calls` → [[graphify_graphify_ruby_resolution_ruby_raw_calls]]
- [[graphify_graphify_ruby_resolution_rationale_57]] → `rationale_for` → [[graphify_graphify_ruby_resolution_resolve_ruby_member_calls]]