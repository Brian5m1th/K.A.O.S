# graphify\graphify\extractors\terraform.py

## Símbolos

- [[graphify_graphify_extractors_terraform]] — code: terraform.py
- [[graphify_graphify_extractors_terraform_extract_terraform]] — code: extract_terraform()
- [[graphify_graphify_extractors_terraform_rationale_1]] — code: Terraform extractor. Moved verbatim from graphify/extract.py.
- [[graphify_graphify_extractors_terraform_rationale_12]] — code: Extract Terraform/HCL blocks and the references between them via tree-sitter.

## Dependências

- [[graphify_graphify_extractors_terraform_extract_terraform]] → `calls` → [[graphify_graphify_extractors_base_make_id]]
- [[graphify_graphify_extractors_terraform]] → `contains` → [[graphify_graphify_extractors_terraform_extract_terraform]]
- [[graphify_graphify_extractors_terraform_rationale_1]] → `rationale_for` → [[graphify_graphify_extractors_terraform]]
- [[graphify_graphify_extractors_terraform_extract_terraform]] → `references` → [[graphify_graphify_extractors_terraform_py_path]]
- [[graphify_graphify_extractors_terraform_extract_terraform]] → `calls` → [[graphify_graphify_mcp_ingest_add_node]]
- [[graphify_graphify_extractors_terraform_extract_terraform]] → `indirect_call` → [[graphify_scripts_gen_demo_path_e]]
- [[graphify_graphify_extractors_terraform_rationale_12]] → `rationale_for` → [[graphify_graphify_extractors_terraform_extract_terraform]]