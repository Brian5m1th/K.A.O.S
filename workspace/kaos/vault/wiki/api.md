# graphify\worked\example\raw\api.py

## Símbolos

- [[graphify_worked_example_raw_api]] — code: api.py
- [[graphify_worked_example_raw_api_handle_upload]] — code: handle_upload()
- [[graphify_worked_example_raw_api_handle_get]] — code: handle_get()
- [[graphify_worked_example_raw_api_handle_delete]] — code: handle_delete()
- [[graphify_worked_example_raw_api_handle_list]] — code: handle_list()
- [[graphify_worked_example_raw_api_handle_search]] — code: handle_search()
- [[graphify_worked_example_raw_api_handle_enrich]] — code: handle_enrich()
- [[graphify_worked_example_raw_api_rationale_1]] — code: API module - exposes the document pipeline over HTTP. Thin layer over parser, v
- [[graphify_worked_example_raw_api_rationale_12]] — code: Accept a list of file paths, run the full pipeline on each,     and return a su
- [[graphify_worked_example_raw_api_rationale_28]] — code: Fetch a document by ID and return it.
- [[graphify_worked_example_raw_api_rationale_36]] — code: Delete a document by ID.
- [[graphify_worked_example_raw_api_rationale_44]] — code: List all document IDs in storage.
- [[graphify_worked_example_raw_api_rationale_49]] — code: Simple keyword search over the index.     Returns documents whose keyword list
- [[graphify_worked_example_raw_api_rationale_68]] — code: Re-enrich a document to pick up new cross-references.

## Dependências

- [[graphify_worked_example_raw_api_handle_enrich]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_worked_example_raw_api]] → `imports_from` → [[processor]]
- [[graphify_worked_example_raw_api]] → `contains` → [[graphify_worked_example_raw_api_handle_delete]]
- [[graphify_worked_example_raw_api]] → `contains` → [[graphify_worked_example_raw_api_handle_enrich]]
- [[graphify_worked_example_raw_api]] → `contains` → [[graphify_worked_example_raw_api_handle_get]]
- [[graphify_worked_example_raw_api]] → `contains` → [[graphify_worked_example_raw_api_handle_list]]
- [[graphify_worked_example_raw_api]] → `contains` → [[graphify_worked_example_raw_api_handle_search]]
- [[graphify_worked_example_raw_api]] → `contains` → [[graphify_worked_example_raw_api_handle_upload]]
- [[graphify_worked_example_raw_api]] → `imports_from` → [[graphify_worked_example_raw_parser]]
- [[graphify_worked_example_raw_api]] → `imports_from` → [[graphify_worked_example_raw_storage]]
- [[graphify_worked_example_raw_api]] → `imports_from` → [[graphify_worked_example_raw_validator]]
- [[graphify_worked_example_raw_api_rationale_1]] → `rationale_for` → [[graphify_worked_example_raw_api]]
- [[graphify_worked_example_raw_api_handle_upload]] → `calls` → [[graphify_worked_example_raw_parser_batch_parse]]
- [[graphify_worked_example_raw_api_rationale_12]] → `rationale_for` → [[graphify_worked_example_raw_api_handle_upload]]
- [[graphify_worked_example_raw_api_handle_get]] → `calls` → [[graphify_worked_example_raw_storage_load_record]]
- [[graphify_worked_example_raw_api_rationale_28]] → `rationale_for` → [[graphify_worked_example_raw_api_handle_get]]
- [[graphify_worked_example_raw_api_handle_delete]] → `calls` → [[graphify_worked_example_raw_storage_delete_record]]
- [[graphify_worked_example_raw_api_rationale_36]] → `rationale_for` → [[graphify_worked_example_raw_api_handle_delete]]
- [[graphify_worked_example_raw_api_handle_list]] → `calls` → [[graphify_worked_example_raw_storage_list_records]]
- [[graphify_worked_example_raw_api_rationale_44]] → `rationale_for` → [[graphify_worked_example_raw_api_handle_list]]
- [[graphify_worked_example_raw_api_handle_search]] → `calls` → [[graphify_worked_example_raw_storage_load_index]]
- [[graphify_worked_example_raw_api_rationale_49]] → `rationale_for` → [[graphify_worked_example_raw_api_handle_search]]
- [[graphify_worked_example_raw_api_handle_enrich]] → `calls` → [[graphify_worked_example_raw_processor_process_and_save]]
- [[graphify_worked_example_raw_api_handle_enrich]] → `calls` → [[graphify_worked_example_raw_storage_load_record]]
- [[graphify_worked_example_raw_api_handle_enrich]] → `calls` → [[graphify_worked_example_raw_validator_validate_document]]
- [[graphify_worked_example_raw_api_rationale_68]] → `rationale_for` → [[graphify_worked_example_raw_api_handle_enrich]]