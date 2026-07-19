# MEMORY Epic - IMPLEMENTATION PLAN: Memory Systems Refactor

This plan schedules database and vector schema migrations for memory compartments.

---

## 1. Milestones

```text
Phase 1: DB Migration ──► Phase 2: Keyring Sync ──► Phase 3: Consolidator Svc
(Create identity/logs)   (E2EE Sync Engine)       (Summarize chat threads)
```

### Phase 1: Database Schemas (Sprint 1)
- Write Alembic migrations to create `user_identity` and `episodic_execution_logs` tables.
- Add SQLAlchemy Models in `capabilities/memory/models.py`.
- Run pytest integration scripts to verify Postgres writes.

### Phase 2: E2EE Sync Gateway (Sprint 2-3)
- Write encryption and decryption utils utilizing AES-256-GCM.
- Connect sync relays in `capabilities/memory/adapters/sync_relay.py`.
- Verify database backups can be recovered using only the local user key.

### Phase 3: Memory Consolidator (Sprint 4)
- Write background task runners in FastAPI to trigger after a 15-minute chat inactivity timeout.
- Implement the summarization prompt and index the results in Qdrant.
