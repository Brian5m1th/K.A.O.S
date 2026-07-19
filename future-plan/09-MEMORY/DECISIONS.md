# MEMORY Epic - DECISIONS: Database & Vector Configurations

This document logs critical choices made for data storage.

---

## 1. ADR-MEM-001: Consolidate configuration into Database

### Context
Using filesystem JSON files (like `kaos.config.json`) makes it difficult to run concurrent updates or rollback changes.

### Decision
Migrate system configuration and environment profiles into a `system_settings` relational table in PostgreSQL. The settings will be queried at boot and cached in-memory with hot-reload triggers.

### Consequences
- Prevents file access race conditions.
- Simplifies multi-device syncing (only sync the database rather than random config files).

---

## 2. ADR-MEM-002: Local Vector Index Selection

### Context
Qdrant runs as a Docker container. For community/non-developer tiers, running a docker container is a high barrier to entry.

### Decision
For local community setups, allow the memory engine to fallback from Qdrant to an embedded HNSW library (e.g. `faiss` or `hnswlib` in python) saving vector indexes directly as a local bin file (`~/.kaos/vectors.bin`).

### Consequences
- Allows K.A.O.S to run completely without Docker Desktop on standard Windows laptops.
- Maintain Qdrant as the primary adapter for developer and enterprise tiers.
