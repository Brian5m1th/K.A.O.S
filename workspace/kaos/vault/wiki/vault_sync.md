# assistant\app\audit\vault_sync.py

## Símbolos

- [[assistant_app_audit_vault_sync]] — code: vault_sync.py
- [[assistant_app_audit_vault_sync_vaultsync]] — code: VaultSync
- [[assistant_app_audit_vault_sync_vaultsync_set_vault_base]] — code: .set_vault_base()
- [[assistant_app_audit_vault_sync_vaultsync_sync_to_vault]] — code: .sync_to_vault()
- [[assistant_app_audit_vault_sync_vaultsync_sync_from_vault]] — code: .sync_from_vault()
- [[assistant_app_audit_vault_sync_vaultsync_validate_frontmatter]] — code: ._validate_frontmatter()
- [[assistant_app_audit_vault_sync_vaultsync_ensure_vault_structure]] — code: .ensure_vault_structure()
- [[assistant_app_audit_vault_sync_vaultsync_is_vault_mounted]] — code: .is_vault_mounted()

## Dependências

- [[assistant_app_audit_vault_sync_vaultsync]] → `uses` → [[assistant_app_audit_frontmatter_parser_frontmatterparser]]
- [[assistant_app_audit_vault_sync_vaultsync_validate_frontmatter]] → `calls` → [[assistant_app_audit_frontmatter_parser_frontmatterparser_parse]]
- [[assistant_app_audit_vault_sync]] → `contains` → [[assistant_app_audit_vault_sync_vaultsync]]
- [[assistant_app_audit_vault_sync_vaultsync]] → `method` → [[assistant_app_audit_vault_sync_vaultsync_ensure_vault_structure]]
- [[assistant_app_audit_vault_sync_vaultsync]] → `method` → [[assistant_app_audit_vault_sync_vaultsync_is_vault_mounted]]
- [[assistant_app_audit_vault_sync_vaultsync]] → `method` → [[assistant_app_audit_vault_sync_vaultsync_set_vault_base]]
- [[assistant_app_audit_vault_sync_vaultsync]] → `method` → [[assistant_app_audit_vault_sync_vaultsync_sync_from_vault]]
- [[assistant_app_audit_vault_sync_vaultsync]] → `method` → [[assistant_app_audit_vault_sync_vaultsync_sync_to_vault]]
- [[assistant_app_audit_vault_sync_vaultsync]] → `method` → [[assistant_app_audit_vault_sync_vaultsync_validate_frontmatter]]
- [[assistant_app_audit_vault_sync_vaultsync_set_vault_base]] → `references` → [[assistant_app_audit_vault_sync_py_path]]
- [[assistant_app_audit_vault_sync_vaultsync_sync_from_vault]] → `references` → [[assistant_app_audit_vault_sync_py_path]]
- [[assistant_app_audit_vault_sync_vaultsync_sync_to_vault]] → `references` → [[assistant_app_audit_vault_sync_py_path]]
- [[assistant_app_audit_vault_sync_vaultsync_validate_frontmatter]] → `references` → [[assistant_app_audit_vault_sync_py_path]]
- [[assistant_app_audit_vault_sync_vaultsync_sync_from_vault]] → `calls` → [[assistant_app_audit_vault_sync_vaultsync_validate_frontmatter]]