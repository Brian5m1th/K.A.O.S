# assistant\app\obsidian\watcher\vault_watcher.py

## Símbolos

- [[assistant_app_obsidian_watcher_vault_watcher]] — code: vault_watcher.py
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]] — code: _VaultEventHandler
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_init]] — code: .__init__()
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_is_markdown]] — code: ._is_markdown()
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_created]] — code: .on_created()
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_modified]] — code: .on_modified()
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_deleted]] — code: .on_deleted()
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_moved]] — code: .on_moved()
- [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]] — code: VaultWatcher
- [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher_init]] — code: .__init__()
- [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher_start]] — code: .start()
- [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher_stop]] — code: .stop()

## Dependências

- [[assistant_app_obsidian_watcher_vault_watcher]] → `contains` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]]
- [[assistant_app_obsidian_watcher_vault_watcher]] → `contains` → [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]] → `inherits` → [[assistant_app_obsidian_watcher_vault_watcher_py_filesystemeventhandler]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]] → `method` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_init]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]] → `method` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_is_markdown]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]] → `method` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_created]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]] → `method` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_deleted]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]] → `method` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_modified]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]] → `method` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_moved]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]] → `uses` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher_start]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_init]] → `references` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_created]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_is_markdown]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_deleted]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_is_markdown]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_modified]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_is_markdown]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_moved]] → `calls` → [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_is_markdown]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_created]] → `references` → [[filesystemevent]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_deleted]] → `references` → [[filesystemevent]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_modified]] → `references` → [[filesystemevent]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaulteventhandler_on_moved]] → `references` → [[filesystemevent]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]] → `method` → [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher_init]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]] → `method` → [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher_start]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]] → `method` → [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher_stop]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher]] → `uses` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer]]
- [[assistant_app_obsidian_watcher_vault_watcher_vaultwatcher_init]] → `calls` → [[assistant_app_rag_indexer_vault_indexer_vaultindexer]]