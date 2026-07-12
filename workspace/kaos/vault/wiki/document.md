# assistant\app\domain\document.py

## Símbolos

- [[assistant_app_domain_document]] — code: document.py
- [[assistant_app_domain_document_notecreaterequest]] — code: NoteCreateRequest
- [[assistant_app_domain_document_noteupdaterequest]] — code: NoteUpdateRequest
- [[assistant_app_domain_document_noteresponse]] — code: NoteResponse
- [[assistant_app_domain_document_notereadresult]] — code: NoteReadResult
- [[assistant_app_domain_document_searchresult]] — code: SearchResult
- [[assistant_app_domain_document_searchresponse]] — code: SearchResponse

## Dependências

- [[assistant_app_domain_document]] → `contains` → [[assistant_app_domain_document_notecreaterequest]]
- [[assistant_app_domain_document]] → `contains` → [[assistant_app_domain_document_notereadresult]]
- [[assistant_app_domain_document]] → `contains` → [[assistant_app_domain_document_noteresponse]]
- [[assistant_app_domain_document]] → `contains` → [[assistant_app_domain_document_noteupdaterequest]]
- [[assistant_app_domain_document]] → `contains` → [[assistant_app_domain_document_searchresponse]]
- [[assistant_app_domain_document]] → `contains` → [[assistant_app_domain_document_searchresult]]
- [[assistant_app_domain_document_notecreaterequest]] → `inherits` → [[assistant_app_domain_document_py_basemodel]]
- [[assistant_app_domain_document_notereadresult]] → `inherits` → [[assistant_app_domain_document_py_basemodel]]
- [[assistant_app_domain_document_noteresponse]] → `inherits` → [[assistant_app_domain_document_py_basemodel]]
- [[assistant_app_domain_document_noteupdaterequest]] → `inherits` → [[assistant_app_domain_document_py_basemodel]]
- [[assistant_app_domain_document_searchresponse]] → `inherits` → [[assistant_app_domain_document_py_basemodel]]
- [[assistant_app_domain_document_searchresult]] → `inherits` → [[assistant_app_domain_document_py_basemodel]]