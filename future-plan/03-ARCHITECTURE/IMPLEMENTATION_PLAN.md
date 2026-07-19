# ARCHITECTURE Epic - IMPLEMENTATION PLAN: Domain Restructuring Steps

This document outlines the step-by-step refactoring needed to transition the backend codebase.

---

## 1. Migration Plan

```text
Step 1: Manifest Engine ──► Step 2: Migrate Chat ──► Step 3: Migrate Memory ──► Step 4: Cleanup
(Build Loader in Core)     (Move Chat APIs/Svc)     (Move DB/Vectors)          (Remove old dirs)
```

### Step 1: Core Manifest Engine
- Implement `app/core/manifest_parser.py`.
- Refactor `app/main.py` to use dynamic loader instead of static imports.
- Validate that the server boots with zero capabilities registered (empty gateway).

### Step 2: Migrate Chat Module
- Create `app/capabilities/chat/` directory structure.
- Move Chat endpoints from `app/api/chat.py` to `app/capabilities/chat/api/routes.py`.
- Move Chat reasoning services from `app/service/llm.py` to `app/capabilities/chat/services/`.
- Declare `app/capabilities/chat/manifest.yaml`.
- Run `pytest tests/unit/test_chat.py` to verify routing compatibility.

### Step 3: Migrate Memory & RAG Modules
- Create `app/capabilities/memory/`.
- Relocate Qdrant/PostgreSQL database connections and migrations into memory adapters.
- Validate indices and connections dynamically.

### Step 4: System Cleanup
- Once all domains are migrated, delete original `app/api/`, `app/service/`, and `app/providers/` folders.
- Run the full test suite to guarantee 100% functional parity.
