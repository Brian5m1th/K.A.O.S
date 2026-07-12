# graphify\worked\example\raw\validator.py

## Símbolos

- [[graphify_worked_example_raw_validator]] — code: validator.py
- [[graphify_worked_example_raw_validator_validationerror]] — code: ValidationError
- [[graphify_worked_example_raw_validator_validate_document]] — code: validate_document()
- [[graphify_worked_example_raw_validator_check_required_fields]] — code: check_required_fields()
- [[graphify_worked_example_raw_validator_check_format]] — code: check_format()
- [[graphify_worked_example_raw_validator_normalize_fields]] — code: normalize_fields()
- [[graphify_worked_example_raw_validator_validate_batch]] — code: validate_batch()
- [[graphify_worked_example_raw_validator_rationale_1]] — code: Validator module - checks that parsed documents meet schema requirements before
- [[graphify_worked_example_raw_validator_rationale_18]] — code: Run all validation checks on a parsed document. Raises ValidationError on failur
- [[graphify_worked_example_raw_validator_rationale_26]] — code: Raise if any required field is missing.
- [[graphify_worked_example_raw_validator_rationale_33]] — code: Raise if the format is not in the allowed list.
- [[graphify_worked_example_raw_validator_rationale_40]] — code: Clean up text fields using the processor.
- [[graphify_worked_example_raw_validator_rationale_53]] — code: Validate a list of documents. Returns (valid_docs, errors).

## Dependências

- [[graphify_worked_example_raw_validator_validate_batch]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_worked_example_raw_validator]] → `imports_from` → [[processor]]
- [[graphify_worked_example_raw_validator_normalize_fields]] → `calls` → [[graphify_worked_example_raw_processor_normalize_text]]
- [[graphify_worked_example_raw_validator]] → `contains` → [[graphify_worked_example_raw_validator_check_format]]
- [[graphify_worked_example_raw_validator]] → `contains` → [[graphify_worked_example_raw_validator_check_required_fields]]
- [[graphify_worked_example_raw_validator]] → `contains` → [[graphify_worked_example_raw_validator_normalize_fields]]
- [[graphify_worked_example_raw_validator]] → `contains` → [[graphify_worked_example_raw_validator_validate_batch]]
- [[graphify_worked_example_raw_validator]] → `contains` → [[graphify_worked_example_raw_validator_validate_document]]
- [[graphify_worked_example_raw_validator]] → `contains` → [[graphify_worked_example_raw_validator_validationerror]]
- [[graphify_worked_example_raw_validator_rationale_1]] → `rationale_for` → [[graphify_worked_example_raw_validator]]
- [[graphify_worked_example_raw_validator_check_format]] → `calls` → [[graphify_worked_example_raw_validator_validationerror]]
- [[graphify_worked_example_raw_validator_check_required_fields]] → `calls` → [[graphify_worked_example_raw_validator_validationerror]]
- [[graphify_worked_example_raw_validator_validationerror]] → `inherits` → [[graphify_worked_example_raw_validator_py_exception]]
- [[graphify_worked_example_raw_validator_rationale_18]] → `rationale_for` → [[graphify_worked_example_raw_validator_validate_document]]
- [[graphify_worked_example_raw_validator_validate_batch]] → `calls` → [[graphify_worked_example_raw_validator_validate_document]]
- [[graphify_worked_example_raw_validator_validate_document]] → `calls` → [[graphify_worked_example_raw_validator_check_format]]
- [[graphify_worked_example_raw_validator_validate_document]] → `calls` → [[graphify_worked_example_raw_validator_check_required_fields]]
- [[graphify_worked_example_raw_validator_validate_document]] → `calls` → [[graphify_worked_example_raw_validator_normalize_fields]]
- [[graphify_worked_example_raw_validator_rationale_26]] → `rationale_for` → [[graphify_worked_example_raw_validator_check_required_fields]]
- [[graphify_worked_example_raw_validator_rationale_33]] → `rationale_for` → [[graphify_worked_example_raw_validator_check_format]]
- [[graphify_worked_example_raw_validator_rationale_40]] → `rationale_for` → [[graphify_worked_example_raw_validator_normalize_fields]]
- [[graphify_worked_example_raw_validator_rationale_53]] → `rationale_for` → [[graphify_worked_example_raw_validator_validate_batch]]