# assistant\app\audit\sdd_watcher.py

## Símbolos

- [[assistant_app_audit_sdd_watcher]] — code: sdd_watcher.py
- [[assistant_app_audit_sdd_watcher_sddwatcher]] — code: SDDWatcher
- [[assistant_app_audit_sdd_watcher_sddwatcher_set_interval]] — code: .set_interval()
- [[assistant_app_audit_sdd_watcher_sddwatcher_start]] — code: .start()
- [[assistant_app_audit_sdd_watcher_sddwatcher_stop]] — code: .stop()
- [[assistant_app_audit_sdd_watcher_sddwatcher_detect_changes]] — code: ._detect_changes()

## Dependências

- [[assistant_app_audit_sdd_watcher_sddwatcher]] → `uses` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]]
- [[assistant_app_audit_sdd_watcher_sddwatcher_start]] → `calls` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_build_snapshot]]
- [[assistant_app_audit_sdd_watcher]] → `contains` → [[assistant_app_audit_sdd_watcher_sddwatcher]]
- [[assistant_app_audit_sdd_watcher_sddwatcher]] → `method` → [[assistant_app_audit_sdd_watcher_sddwatcher_detect_changes]]
- [[assistant_app_audit_sdd_watcher_sddwatcher]] → `method` → [[assistant_app_audit_sdd_watcher_sddwatcher_set_interval]]
- [[assistant_app_audit_sdd_watcher_sddwatcher]] → `method` → [[assistant_app_audit_sdd_watcher_sddwatcher_start]]
- [[assistant_app_audit_sdd_watcher_sddwatcher]] → `method` → [[assistant_app_audit_sdd_watcher_sddwatcher_stop]]
- [[assistant_app_audit_sdd_watcher_sddwatcher]] → `uses` → [[assistant_app_audit_vault_sync_vaultsync]]
- [[assistant_app_audit_sdd_watcher_sddwatcher_start]] → `calls` → [[assistant_app_audit_sdd_watcher_sddwatcher_detect_changes]]
- [[assistant_app_audit_sdd_watcher_sddwatcher_start]] → `calls` → [[assistant_app_audit_vault_sync_vaultsync_sync_to_vault]]
- [[assistant_app_audit_sdd_watcher_sddwatcher_detect_changes]] → `references` → [[assistant_app_audit_sdd_watcher_py_path]]