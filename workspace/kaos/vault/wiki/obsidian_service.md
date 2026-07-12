# assistant\app\obsidian\services\obsidian_service.py

## Símbolos

- [[assistant_app_obsidian_services_obsidian_service]] — code: obsidian_service.py
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] — code: ObsidianService
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_init]] — code: .__init__()
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_resolve_path]] — code: ._resolve_path()
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_create_note]] — code: .create_note()
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_read_note]] — code: .read_note()
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_update_note]] — code: .update_note()
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_delete_note]] — code: .delete_note()
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_list_notes]] — code: .list_notes()
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_search_text]] — code: .search_text()

## Dependências

- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] → `uses` → [[assistant_app_domain_document_notereadresult]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_read_note]] → `references` → [[assistant_app_domain_document_notereadresult]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] → `uses` → [[assistant_app_domain_document_searchresult]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_search_text]] → `references` → [[assistant_app_domain_document_searchresult]]
- [[assistant_app_obsidian_services_obsidian_service]] → `contains` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] → `method` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_create_note]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] → `method` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_delete_note]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] → `method` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_init]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] → `method` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_list_notes]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] → `method` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_read_note]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] → `method` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_resolve_path]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] → `method` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_search_text]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice]] → `method` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_update_note]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_init]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_py_path]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_delete_note]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_resolve_path]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_read_note]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_resolve_path]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_resolve_path]] → `references` → [[assistant_app_obsidian_services_obsidian_service_py_path]]
- [[assistant_app_obsidian_services_obsidian_service_obsidianservice_update_note]] → `calls` → [[assistant_app_obsidian_services_obsidian_service_obsidianservice_resolve_path]]