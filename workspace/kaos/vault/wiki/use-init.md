# desktop\src\shared\lib\use-init.ts

## Símbolos

- [[desktop_src_shared_lib_use_init]] — code: use-init.ts
- [[desktop_src_shared_lib_use_init_bootstrapstep]] — code: BootstrapStep
- [[desktop_src_shared_lib_use_init_bootstrapprogress]] — code: BootstrapProgress
- [[desktop_src_shared_lib_use_init_currentprogress]] — code: _currentProgress
- [[desktop_src_shared_lib_use_init_bootstraplisteners]] — code: _bootstrapListeners
- [[desktop_src_shared_lib_use_init_notifylisteners]] — code: notifyListeners()
- [[desktop_src_shared_lib_use_init_onbootstrapprogress]] — code: onBootstrapProgress()
- [[desktop_src_shared_lib_use_init_getbootstrapprogress]] — code: getBootstrapProgress()
- [[desktop_src_shared_lib_use_init_runbootstrappipeline]] — code: runBootstrapPipeline()
- [[desktop_src_shared_lib_use_init_useappinit]] — code: useAppInit()

## Dependências

- [[desktop_src_shared_lib_use_init]] → `imports_from` → [[desktop_src_application_index]]
- [[desktop_src_shared_lib_use_init]] → `imports` → [[desktop_src_application_stores_auth_store_useauthstore]]
- [[desktop_src_shared_lib_use_init_useappinit]] → `calls` → [[desktop_src_application_stores_auth_store_useauthstore]]
- [[desktop_src_shared_lib_use_init_runbootstrappipeline]] → `imports_from` → [[desktop_src_application_stores_system_store]]
- [[desktop_src_shared_lib_use_init]] → `imports` → [[desktop_src_application_stores_update_store_useupdatestore]]
- [[desktop_src_shared_lib_use_init]] → `imports_from` → [[desktop_src_features_auto_update_hooks_useupdatecheck]]
- [[desktop_src_shared_lib_use_init]] → `imports` → [[desktop_src_features_auto_update_hooks_useupdatecheck_useupdatecheck]]
- [[desktop_src_shared_lib_use_init_useappinit]] → `calls` → [[desktop_src_features_auto_update_hooks_useupdatecheck_useupdatecheck]]
- [[desktop_src_shared_lib_use_init]] → `imports_from` → [[desktop_src_features_documentation_audit_auto_doc_doc_sync_engine]]
- [[desktop_src_shared_lib_use_init]] → `imports` → [[desktop_src_features_documentation_audit_auto_doc_doc_sync_engine_docsyncengine]]
- [[desktop_src_shared_lib_use_init_useappinit]] → `calls` → [[desktop_src_features_documentation_audit_auto_doc_doc_sync_engine_docsyncengine_start]]
- [[desktop_src_shared_lib_use_init_useappinit]] → `calls` → [[desktop_src_features_documentation_audit_auto_doc_doc_sync_engine_docsyncengine_stop]]
- [[desktop_src_shared_lib_use_init]] → `imports_from` → [[desktop_src_infrastructure_index]]
- [[desktop_src_shared_lib_use_init]] → `imports` → [[desktop_src_infrastructure_ipc_ipc_bridge_invokeipc]]
- [[desktop_src_shared_lib_use_init]] → `contains` → [[desktop_src_shared_lib_use_init_bootstraplisteners]]
- [[desktop_src_shared_lib_use_init]] → `contains` → [[desktop_src_shared_lib_use_init_bootstrapprogress]]
- [[desktop_src_shared_lib_use_init]] → `contains` → [[desktop_src_shared_lib_use_init_bootstrapstep]]
- [[desktop_src_shared_lib_use_init]] → `contains` → [[desktop_src_shared_lib_use_init_currentprogress]]
- [[desktop_src_shared_lib_use_init]] → `contains` → [[desktop_src_shared_lib_use_init_getbootstrapprogress]]
- [[desktop_src_shared_lib_use_init]] → `contains` → [[desktop_src_shared_lib_use_init_notifylisteners]]
- [[desktop_src_shared_lib_use_init]] → `contains` → [[desktop_src_shared_lib_use_init_onbootstrapprogress]]
- [[desktop_src_shared_lib_use_init]] → `contains` → [[desktop_src_shared_lib_use_init_runbootstrappipeline]]
- [[desktop_src_shared_lib_use_init]] → `contains` → [[desktop_src_shared_lib_use_init_useappinit]]
- [[desktop_src_shared_lib_use_init_runbootstrappipeline]] → `calls` → [[desktop_src_shared_lib_use_init_notifylisteners]]
- [[desktop_src_shared_lib_use_init_useappinit]] → `calls` → [[desktop_src_shared_lib_use_init_onbootstrapprogress]]
- [[desktop_src_shared_lib_use_init_useappinit]] → `indirect_call` → [[desktop_src_shared_lib_use_init_getbootstrapprogress]]
- [[desktop_src_shared_lib_use_init_useappinit]] → `calls` → [[desktop_src_shared_lib_use_init_runbootstrappipeline]]