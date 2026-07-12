# graphify\worked\example\raw\storage.py

## Símbolos

- [[graphify_worked_example_raw_storage]] — code: storage.py
- [[graphify_worked_example_raw_storage_ensure_storage]] — code: _ensure_storage()
- [[graphify_worked_example_raw_storage_load_index]] — code: load_index()
- [[graphify_worked_example_raw_storage_save_index]] — code: save_index()
- [[graphify_worked_example_raw_storage_save_parsed]] — code: save_parsed()
- [[graphify_worked_example_raw_storage_save_processed]] — code: save_processed()
- [[graphify_worked_example_raw_storage_load_record]] — code: load_record()
- [[graphify_worked_example_raw_storage_delete_record]] — code: delete_record()
- [[graphify_worked_example_raw_storage_list_records]] — code: list_records()
- [[graphify_worked_example_raw_storage_rationale_1]] — code: Storage module - persists documents to disk and maintains the search index. All
- [[graphify_worked_example_raw_storage_rationale_21]] — code: Load the full document index from disk.
- [[graphify_worked_example_raw_storage_rationale_27]] — code: Persist the index to disk.
- [[graphify_worked_example_raw_storage_rationale_33]] — code: Write a parsed document to storage. Returns the assigned record ID.
- [[graphify_worked_example_raw_storage_rationale_50]] — code: Write an enriched document to storage, updating the index with keywords.
- [[graphify_worked_example_raw_storage_rationale_66]] — code: Fetch a single document by ID.
- [[graphify_worked_example_raw_storage_rationale_75]] — code: Remove a document and its index entry. Returns True if it existed.
- [[graphify_worked_example_raw_storage_rationale_88]] — code: Return all record IDs currently in storage.

## Dependências

- [[graphify_worked_example_raw_storage]] → `contains` → [[graphify_worked_example_raw_storage_delete_record]]
- [[graphify_worked_example_raw_storage]] → `contains` → [[graphify_worked_example_raw_storage_ensure_storage]]
- [[graphify_worked_example_raw_storage]] → `contains` → [[graphify_worked_example_raw_storage_list_records]]
- [[graphify_worked_example_raw_storage]] → `contains` → [[graphify_worked_example_raw_storage_load_index]]
- [[graphify_worked_example_raw_storage]] → `contains` → [[graphify_worked_example_raw_storage_load_record]]
- [[graphify_worked_example_raw_storage]] → `contains` → [[graphify_worked_example_raw_storage_save_index]]
- [[graphify_worked_example_raw_storage]] → `contains` → [[graphify_worked_example_raw_storage_save_parsed]]
- [[graphify_worked_example_raw_storage]] → `contains` → [[graphify_worked_example_raw_storage_save_processed]]
- [[graphify_worked_example_raw_storage_rationale_1]] → `rationale_for` → [[graphify_worked_example_raw_storage]]
- [[graphify_worked_example_raw_storage_delete_record]] → `calls` → [[graphify_worked_example_raw_storage_ensure_storage]]
- [[graphify_worked_example_raw_storage_load_index]] → `calls` → [[graphify_worked_example_raw_storage_ensure_storage]]
- [[graphify_worked_example_raw_storage_load_record]] → `calls` → [[graphify_worked_example_raw_storage_ensure_storage]]
- [[graphify_worked_example_raw_storage_save_index]] → `calls` → [[graphify_worked_example_raw_storage_ensure_storage]]
- [[graphify_worked_example_raw_storage_save_parsed]] → `calls` → [[graphify_worked_example_raw_storage_ensure_storage]]
- [[graphify_worked_example_raw_storage_save_processed]] → `calls` → [[graphify_worked_example_raw_storage_ensure_storage]]
- [[graphify_worked_example_raw_storage_delete_record]] → `calls` → [[graphify_worked_example_raw_storage_load_index]]
- [[graphify_worked_example_raw_storage_list_records]] → `calls` → [[graphify_worked_example_raw_storage_load_index]]
- [[graphify_worked_example_raw_storage_rationale_21]] → `rationale_for` → [[graphify_worked_example_raw_storage_load_index]]
- [[graphify_worked_example_raw_storage_save_parsed]] → `calls` → [[graphify_worked_example_raw_storage_load_index]]
- [[graphify_worked_example_raw_storage_save_processed]] → `calls` → [[graphify_worked_example_raw_storage_load_index]]
- [[graphify_worked_example_raw_storage_delete_record]] → `calls` → [[graphify_worked_example_raw_storage_save_index]]
- [[graphify_worked_example_raw_storage_rationale_27]] → `rationale_for` → [[graphify_worked_example_raw_storage_save_index]]
- [[graphify_worked_example_raw_storage_save_parsed]] → `calls` → [[graphify_worked_example_raw_storage_save_index]]
- [[graphify_worked_example_raw_storage_save_processed]] → `calls` → [[graphify_worked_example_raw_storage_save_index]]
- [[graphify_worked_example_raw_storage_rationale_33]] → `rationale_for` → [[graphify_worked_example_raw_storage_save_parsed]]
- [[graphify_worked_example_raw_storage_rationale_50]] → `rationale_for` → [[graphify_worked_example_raw_storage_save_processed]]
- [[graphify_worked_example_raw_storage_rationale_66]] → `rationale_for` → [[graphify_worked_example_raw_storage_load_record]]
- [[graphify_worked_example_raw_storage_rationale_75]] → `rationale_for` → [[graphify_worked_example_raw_storage_delete_record]]
- [[graphify_worked_example_raw_storage_rationale_88]] → `rationale_for` → [[graphify_worked_example_raw_storage_list_records]]