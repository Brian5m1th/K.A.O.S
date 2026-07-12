# assistant\app\ai\vault_analyzer\vault_reader.py

## Símbolos

- [[assistant_app_ai_vault_analyzer_vault_reader]] — code: vault_reader.py
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultnode]] — code: VaultNode
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] — code: VaultReader
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_scan_dirs]] — code: .get_scan_dirs()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]] — code: .scan_all()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_dir]] — code: .scan_dir()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_single]] — code: .scan_single()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_file]] — code: ._parse_file()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_frontmatter]] — code: ._parse_frontmatter()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_extract_wikilinks]] — code: ._extract_wikilinks()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_node_by_id]] — code: .get_node_by_id()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_nodes_by_type]] — code: .get_nodes_by_type()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_orphan_nodes]] — code: .get_orphan_nodes()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_node_count_by_type]] — code: .get_node_count_by_type()
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_total_links]] — code: .get_total_links()
- [[assistant_app_ai_vault_analyzer_vault_reader_rationale_33]] — code: Retorna diretorios para scan, usando EnvironmentService.

## Dependências

- [[assistant_app_ai_vault_analyzer_vault_reader]] → `contains` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultnode]]
- [[assistant_app_ai_vault_analyzer_vault_reader]] → `contains` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultnode]] → `uses` → [[assistant_app_core_environment_service_environmentservice]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_node_by_id]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultnode]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_nodes_by_type]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultnode]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_orphan_nodes]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultnode]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_file]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultnode]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultnode]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_dir]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultnode]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_single]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultnode]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_extract_wikilinks]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_node_by_id]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_node_count_by_type]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_nodes_by_type]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_orphan_nodes]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_scan_dirs]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_total_links]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_file]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_frontmatter]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_dir]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `method` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_single]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader]] → `uses` → [[assistant_app_core_environment_service_environmentservice]]
- [[assistant_app_ai_vault_analyzer_vault_reader_rationale_33]] → `rationale_for` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_scan_dirs]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_scan_dirs]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_py_path]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_scan_dirs]] → `calls` → [[assistant_app_core_environment_service_environmentservice_detect]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_scan_dirs]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_file]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_py_path]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_dir]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_py_path]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_single]] → `references` → [[assistant_app_ai_vault_analyzer_vault_reader_py_path]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_node_by_id]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_node_count_by_type]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_nodes_by_type]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_orphan_nodes]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_get_total_links]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_all]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_file]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_dir]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_file]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_scan_single]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_file]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_file]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_extract_wikilinks]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_file]] → `calls` → [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_frontmatter]]
- [[assistant_app_ai_vault_analyzer_vault_reader_vaultreader_parse_file]] → `calls` → [[assistant_app_core_environment_service_environmentservice_detect]]