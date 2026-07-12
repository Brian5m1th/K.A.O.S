# graphify\worked\example\raw\parser.py

## Símbolos

- [[graphify_worked_example_raw_parser]] — code: parser.py
- [[graphify_worked_example_raw_parser_parse_file]] — code: parse_file()
- [[graphify_worked_example_raw_parser_parse_markdown]] — code: parse_markdown()
- [[graphify_worked_example_raw_parser_parse_json]] — code: parse_json()
- [[graphify_worked_example_raw_parser_parse_plaintext]] — code: parse_plaintext()
- [[graphify_worked_example_raw_parser_parse_and_save]] — code: parse_and_save()
- [[graphify_worked_example_raw_parser_batch_parse]] — code: batch_parse()
- [[graphify_worked_example_raw_parser_rationale_1]] — code: Parser module - reads raw input documents and converts them into a structured f
- [[graphify_worked_example_raw_parser_rationale_13]] — code: Read a file from disk and return a structured document.
- [[graphify_worked_example_raw_parser_rationale_30]] — code: Extract title, sections, and links from markdown.
- [[graphify_worked_example_raw_parser_rationale_50]] — code: Parse a JSON document into a structured dict.
- [[graphify_worked_example_raw_parser_rationale_57]] — code: Split plaintext into paragraphs.
- [[graphify_worked_example_raw_parser_rationale_63]] — code: Full pipeline: parse, validate, save. Returns the saved record ID.
- [[graphify_worked_example_raw_parser_rationale_71]] — code: Parse a list of files and return their record IDs.

## Dependências

- [[graphify_worked_example_raw_parser_batch_parse]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_worked_example_raw_parser]] → `contains` → [[graphify_worked_example_raw_parser_batch_parse]]
- [[graphify_worked_example_raw_parser]] → `contains` → [[graphify_worked_example_raw_parser_parse_and_save]]
- [[graphify_worked_example_raw_parser]] → `contains` → [[graphify_worked_example_raw_parser_parse_file]]
- [[graphify_worked_example_raw_parser]] → `contains` → [[graphify_worked_example_raw_parser_parse_json]]
- [[graphify_worked_example_raw_parser]] → `contains` → [[graphify_worked_example_raw_parser_parse_markdown]]
- [[graphify_worked_example_raw_parser]] → `contains` → [[graphify_worked_example_raw_parser_parse_plaintext]]
- [[graphify_worked_example_raw_parser]] → `imports_from` → [[graphify_worked_example_raw_storage]]
- [[graphify_worked_example_raw_parser]] → `imports_from` → [[graphify_worked_example_raw_validator]]
- [[graphify_worked_example_raw_parser_rationale_1]] → `rationale_for` → [[graphify_worked_example_raw_parser]]
- [[graphify_worked_example_raw_parser_parse_and_save]] → `calls` → [[graphify_worked_example_raw_parser_parse_file]]
- [[graphify_worked_example_raw_parser_parse_file]] → `calls` → [[graphify_worked_example_raw_parser_parse_json]]
- [[graphify_worked_example_raw_parser_parse_file]] → `calls` → [[graphify_worked_example_raw_parser_parse_markdown]]
- [[graphify_worked_example_raw_parser_parse_file]] → `calls` → [[graphify_worked_example_raw_parser_parse_plaintext]]
- [[graphify_worked_example_raw_parser_rationale_13]] → `rationale_for` → [[graphify_worked_example_raw_parser_parse_file]]
- [[graphify_worked_example_raw_parser_rationale_30]] → `rationale_for` → [[graphify_worked_example_raw_parser_parse_markdown]]
- [[graphify_worked_example_raw_parser_rationale_50]] → `rationale_for` → [[graphify_worked_example_raw_parser_parse_json]]
- [[graphify_worked_example_raw_parser_rationale_57]] → `rationale_for` → [[graphify_worked_example_raw_parser_parse_plaintext]]
- [[graphify_worked_example_raw_parser_batch_parse]] → `calls` → [[graphify_worked_example_raw_parser_parse_and_save]]
- [[graphify_worked_example_raw_parser_parse_and_save]] → `calls` → [[graphify_worked_example_raw_storage_save_parsed]]
- [[graphify_worked_example_raw_parser_parse_and_save]] → `calls` → [[graphify_worked_example_raw_validator_validate_document]]
- [[graphify_worked_example_raw_parser_rationale_63]] → `rationale_for` → [[graphify_worked_example_raw_parser_parse_and_save]]
- [[graphify_worked_example_raw_parser_rationale_71]] → `rationale_for` → [[graphify_worked_example_raw_parser_batch_parse]]