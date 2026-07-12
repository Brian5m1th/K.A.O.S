# graphify\worked\example\raw\processor.py

## Símbolos

- [[graphify_worked_example_raw_processor]] — code: processor.py
- [[graphify_worked_example_raw_processor_normalize_text]] — code: normalize_text()
- [[graphify_worked_example_raw_processor_extract_keywords]] — code: extract_keywords()
- [[graphify_worked_example_raw_processor_enrich_document]] — code: enrich_document()
- [[graphify_worked_example_raw_processor_find_cross_references]] — code: find_cross_references()
- [[graphify_worked_example_raw_processor_process_and_save]] — code: process_and_save()
- [[graphify_worked_example_raw_processor_reprocess_all]] — code: reprocess_all()
- [[graphify_worked_example_raw_processor_rationale_1]] — code: Processor module - transforms validated documents into enriched records ready f
- [[graphify_worked_example_raw_processor_rationale_13]] — code: Lowercase, strip extra whitespace, remove control characters.
- [[graphify_worked_example_raw_processor_rationale_21]] — code: Pull non-stopword tokens from text, deduplicated.
- [[graphify_worked_example_raw_processor_rationale_33]] — code: Add keyword index and cross-references to a validated document.
- [[graphify_worked_example_raw_processor_rationale_45]] — code: Look up the index and return IDs of related documents by keyword overlap.
- [[graphify_worked_example_raw_processor_rationale_58]] — code: Enrich a validated document and persist it. Returns the record ID.
- [[graphify_worked_example_raw_processor_rationale_65]] — code: Re-enrich all records in the index. Returns count of records updated.

## Dependências

- [[graphify_worked_example_raw_processor]] → `contains` → [[graphify_worked_example_raw_processor_enrich_document]]
- [[graphify_worked_example_raw_processor]] → `contains` → [[graphify_worked_example_raw_processor_extract_keywords]]
- [[graphify_worked_example_raw_processor]] → `contains` → [[graphify_worked_example_raw_processor_find_cross_references]]
- [[graphify_worked_example_raw_processor]] → `contains` → [[graphify_worked_example_raw_processor_normalize_text]]
- [[graphify_worked_example_raw_processor]] → `contains` → [[graphify_worked_example_raw_processor_process_and_save]]
- [[graphify_worked_example_raw_processor]] → `contains` → [[graphify_worked_example_raw_processor_reprocess_all]]
- [[graphify_worked_example_raw_processor]] → `imports_from` → [[graphify_worked_example_raw_storage]]
- [[graphify_worked_example_raw_processor_rationale_1]] → `rationale_for` → [[graphify_worked_example_raw_processor]]
- [[graphify_worked_example_raw_processor_extract_keywords]] → `calls` → [[graphify_worked_example_raw_processor_normalize_text]]
- [[graphify_worked_example_raw_processor_rationale_13]] → `rationale_for` → [[graphify_worked_example_raw_processor_normalize_text]]
- [[graphify_worked_example_raw_processor_enrich_document]] → `calls` → [[graphify_worked_example_raw_processor_extract_keywords]]
- [[graphify_worked_example_raw_processor_rationale_21]] → `rationale_for` → [[graphify_worked_example_raw_processor_extract_keywords]]
- [[graphify_worked_example_raw_processor_enrich_document]] → `calls` → [[graphify_worked_example_raw_processor_find_cross_references]]
- [[graphify_worked_example_raw_processor_process_and_save]] → `calls` → [[graphify_worked_example_raw_processor_enrich_document]]
- [[graphify_worked_example_raw_processor_rationale_33]] → `rationale_for` → [[graphify_worked_example_raw_processor_enrich_document]]
- [[graphify_worked_example_raw_processor_find_cross_references]] → `calls` → [[graphify_worked_example_raw_storage_load_index]]
- [[graphify_worked_example_raw_processor_rationale_45]] → `rationale_for` → [[graphify_worked_example_raw_processor_find_cross_references]]
- [[graphify_worked_example_raw_processor_process_and_save]] → `calls` → [[graphify_worked_example_raw_storage_save_processed]]
- [[graphify_worked_example_raw_processor_rationale_58]] → `rationale_for` → [[graphify_worked_example_raw_processor_process_and_save]]
- [[graphify_worked_example_raw_processor_reprocess_all]] → `calls` → [[graphify_worked_example_raw_processor_process_and_save]]
- [[graphify_worked_example_raw_processor_rationale_65]] → `rationale_for` → [[graphify_worked_example_raw_processor_reprocess_all]]
- [[graphify_worked_example_raw_processor_reprocess_all]] → `calls` → [[graphify_worked_example_raw_storage_load_index]]