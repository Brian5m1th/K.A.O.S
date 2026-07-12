# graphify\graphify\validate.py

## Símbolos

- [[graphify_graphify_validate]] — code: validate.py
- [[graphify_graphify_validate_validate_extraction]] — code: validate_extraction()
- [[graphify_graphify_validate_assert_valid]] — code: assert_valid()
- [[graphify_graphify_validate_rationale_11]] — code: Validate an extraction JSON dict against the graphify schema.     Returns a lis
- [[graphify_graphify_validate_rationale_91]] — code: Raise ValueError with all errors if extraction is invalid.

## Dependências

- [[graphify_graphify_validate]] → `contains` → [[graphify_graphify_validate_assert_valid]]
- [[graphify_graphify_validate]] → `contains` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_graphify_validate_assert_valid]] → `calls` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_graphify_validate_rationale_11]] → `rationale_for` → [[graphify_graphify_validate_validate_extraction]]
- [[graphify_graphify_validate_rationale_91]] → `rationale_for` → [[graphify_graphify_validate_assert_valid]]