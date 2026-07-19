# RISKS Epic - PROPOSAL: Security & Guard System

## 1. Credential Service Refactoring

We propose replacing the standard `.env` configuration file with a pluggable **Credential Service** that requests keys from the OS Keyring.

- **Windows:** Integrates with Windows Credential Manager via the `keyring` Python library.
- **Fallbacks:** Encrypted JSON file saved inside the `.gemini` directory if the OS keyring is unavailable.

---

## 2. Sandboxed Shell Executions

All shell tools are redirected through a validation middleware:
- **Blacklists:** Prevents commands containing sub-strings like `rm -rf /`, `format`, `Diskpart`, or registry manipulation.
- **Execution Folder Lock:** The engine enforces that all file reads and writes are restricted to the active Mission workspace directory.
- **User Prompt Dialogs:** High-risk actions (e.g., executing a newly created Python script) trigger a Tauri pop-up asking the user to click "Approve" or "Reject".

---

## 3. Cost-Tracking Guard

A FastAPI middleware evaluates cumulative mission costs:
```python
async def cost_guard_middleware(request: Request, call_next):
    mission_id = request.headers.get("x-mission-id")
    if mission_id:
        current_cost = get_mission_cost(mission_id)
        if current_cost > BUDGET_LIMIT:
            return JSONResponse(
                status_code=402, 
                content={"error": "Mission budget exceeded. Please approve addition balance."}
            )
    return await call_next(request)
```
