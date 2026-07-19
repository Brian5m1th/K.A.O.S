# RISKS Epic - IMPLEMENTATION PLAN: Security Milestones

This plan describes the implementation sequence for security and safety gates.

---

## 1. Security Roadmap

```text
Phase 1: Credentials ───► Phase 2: Cost Limits ───► Phase 3: Sandbox Runs
(OS Keyring migration)    (FastAPI budget check)   (Tool command interceptor)
```

### Phase 1: Credential Migration (Sprint 1)
- Install the `keyring` package in the Python virtual environment.
- Implement `app/core/credential_service.py` to retrieve and write keys via OS API calls.
- Refactor the startup boot process to request API keys from the Keyring service, removing plaintext strings from `.env`.

### Phase 2: Cost Limiting Middleware (Sprint 2)
- Write the cost limit database tables in PostgreSQL.
- Implement the FastAPI `cost_guard_middleware` checking transaction history.
- Add standard error handling on the Tauri UI to capture `402 Payment Required` states.

### Phase 3: Shell Interceptor (Sprint 3)
- Refactor the LangGraph tool runner to intercept all shell command requests.
- Parse script arguments for blacklisted command substrings.
- Integrate Tauri IPC prompts asking for explicit execution permission before running terminal tasks.
