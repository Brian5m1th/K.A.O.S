# ARCHITECTURE Epic - GAPS: Architectural Backlog

The following architectural modifications are required to achieve the Cognitive OS model:

| Architectural Gap | Impact | Technical Debt Rating | Resolution Strategy |
| :--- | :--- | :--- | :--- |
| **Layered Packaging** | High | High | Restructure codebase under `app/capabilities/` subdirectories. |
| **Static Router Mounting** | Medium | Medium | Implement dynamic directory parsing and route injection in FastAPI gateway. |
| **Tightly Coupled Classes** | High | High | Introduce abstract base classes (Ports) and load drivers dynamically. |
| **Synchronous Event Bus** | Critical | Medium | Refactor Event Bus to use `asyncio.Queue` background tasks with Postgres/Celery fallback. |
| **Static Credential Storage** | High | High | Replace plaintext env vars with a platform-agnostic Credential Service. |
