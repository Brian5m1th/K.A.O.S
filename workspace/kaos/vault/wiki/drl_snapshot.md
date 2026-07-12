# assistant\app\audit\drl_snapshot.py

## Símbolos

- [[assistant_app_audit_drl_snapshot]] — code: drl_snapshot.py
- [[assistant_app_audit_drl_snapshot_graphsummary]] — code: GraphSummary
- [[assistant_app_audit_drl_snapshot_drlsnapshot]] — code: DRLSnapshot
- [[assistant_app_audit_drl_snapshot_drlsnapshot_to_dict]] — code: .to_dict()
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] — code: DRLSnapshotManager
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_build_snapshot]] — code: .build_snapshot()
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_persist]] — code: ._persist()
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_load]] — code: .load()
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_update_graph_summary]] — code: .update_graph_summary()
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_get_features_for_frontend]] — code: .get_features_for_frontend()
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_get_coverage]] — code: .get_coverage()
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_get_drift_level]] — code: .get_drift_level()

## Dependências

- [[assistant_app_audit_drl_snapshot_drlsnapshot]] → `uses` → [[assistant_app_audit_audit_engine_driftreport]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `uses` → [[assistant_app_audit_audit_engine_driftreport]]
- [[assistant_app_audit_drl_snapshot_graphsummary]] → `uses` → [[assistant_app_audit_audit_engine_driftreport]]
- [[assistant_app_audit_drl_snapshot_drlsnapshot]] → `uses` → [[assistant_app_audit_audit_engine_auditengine]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `uses` → [[assistant_app_audit_audit_engine_auditengine]]
- [[assistant_app_audit_drl_snapshot_graphsummary]] → `uses` → [[assistant_app_audit_audit_engine_auditengine]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_build_snapshot]] → `calls` → [[assistant_app_audit_audit_engine_auditengine_load_latest_report]]
- [[assistant_app_audit_drl_snapshot_drlsnapshot]] → `uses` → [[assistant_app_audit_commit_mapper_commitmapper]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `uses` → [[assistant_app_audit_commit_mapper_commitmapper]]
- [[assistant_app_audit_drl_snapshot_graphsummary]] → `uses` → [[assistant_app_audit_commit_mapper_commitmapper]]
- [[assistant_app_audit_drl_snapshot]] → `contains` → [[assistant_app_audit_drl_snapshot_drlsnapshot]]
- [[assistant_app_audit_drl_snapshot]] → `contains` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]]
- [[assistant_app_audit_drl_snapshot]] → `contains` → [[assistant_app_audit_drl_snapshot_graphsummary]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_build_snapshot]] → `calls` → [[assistant_app_audit_drl_snapshot_graphsummary]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_load]] → `calls` → [[assistant_app_audit_drl_snapshot_graphsummary]]
- [[assistant_app_audit_drl_snapshot_graphsummary]] → `uses` → [[assistant_app_audit_feature_registry_featureentry]]
- [[assistant_app_audit_drl_snapshot_graphsummary]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_audit_drl_snapshot_drlsnapshot]] → `method` → [[assistant_app_audit_drl_snapshot_drlsnapshot_to_dict]]
- [[assistant_app_audit_drl_snapshot_drlsnapshot]] → `uses` → [[assistant_app_audit_feature_registry_featureentry]]
- [[assistant_app_audit_drl_snapshot_drlsnapshot]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_build_snapshot]] → `references` → [[assistant_app_audit_drl_snapshot_drlsnapshot]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_load]] → `references` → [[assistant_app_audit_drl_snapshot_drlsnapshot]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_persist]] → `references` → [[assistant_app_audit_drl_snapshot_drlsnapshot]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_get_features_for_frontend]] → `calls` → [[assistant_app_audit_drl_snapshot_drlsnapshot_to_dict]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_persist]] → `calls` → [[assistant_app_audit_drl_snapshot_drlsnapshot_to_dict]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `method` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_build_snapshot]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `method` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_get_coverage]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `method` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_get_drift_level]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `method` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_get_features_for_frontend]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `method` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_load]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `method` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_persist]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `method` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_update_graph_summary]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `uses` → [[assistant_app_audit_feature_registry_featureentry]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager]] → `uses` → [[assistant_app_audit_feature_registry_featureregistry]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_build_snapshot]] → `calls` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_persist]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_build_snapshot]] → `references` → [[assistant_app_audit_drl_snapshot_py_driftreport]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_build_snapshot]] → `calls` → [[assistant_app_audit_feature_registry_featureregistry_load_from_json]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_update_graph_summary]] → `calls` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_persist]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_get_coverage]] → `calls` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_load]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_get_drift_level]] → `calls` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_load]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_get_features_for_frontend]] → `calls` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_load]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_load]] → `calls` → [[assistant_app_audit_feature_registry_featureentry_from_dict]]
- [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_update_graph_summary]] → `calls` → [[assistant_app_audit_drl_snapshot_drlsnapshotmanager_load]]