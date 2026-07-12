# assistant\app\providers\base\vector_store.py

## Símbolos

- [[assistant_app_providers_base_vector_store]] — code: vector_store.py
- [[assistant_app_providers_base_vector_store_basevectorstore]] — code: BaseVectorStore
- [[assistant_app_providers_base_vector_store_basevectorstore_upsert]] — code: .upsert()
- [[assistant_app_providers_base_vector_store_basevectorstore_search]] — code: .search()
- [[assistant_app_providers_base_vector_store_basevectorstore_delete]] — code: .delete()
- [[assistant_app_providers_base_vector_store_basevectorstore_healthcheck]] — code: .healthcheck()

## Dependências

- [[assistant_app_providers_base_vector_store_basevectorstore]] → `uses` → [[assistant_app_domain_document_searchresult]]
- [[assistant_app_providers_base_vector_store_basevectorstore_search]] → `references` → [[assistant_app_domain_document_searchresult]]
- [[assistant_app_providers_base_vector_store]] → `contains` → [[assistant_app_providers_base_vector_store_basevectorstore]]
- [[assistant_app_providers_base_vector_store]] → `imports_from` → [[assistant_app_providers_base_vector_store_py_abc]]
- [[assistant_app_providers_base_vector_store_basevectorstore]] → `method` → [[assistant_app_providers_base_vector_store_basevectorstore_delete]]
- [[assistant_app_providers_base_vector_store_basevectorstore]] → `method` → [[assistant_app_providers_base_vector_store_basevectorstore_healthcheck]]
- [[assistant_app_providers_base_vector_store_basevectorstore]] → `method` → [[assistant_app_providers_base_vector_store_basevectorstore_search]]
- [[assistant_app_providers_base_vector_store_basevectorstore]] → `method` → [[assistant_app_providers_base_vector_store_basevectorstore_upsert]]
- [[assistant_app_providers_base_vector_store_basevectorstore]] → `inherits` → [[assistant_app_providers_base_vector_store_py_abc]]