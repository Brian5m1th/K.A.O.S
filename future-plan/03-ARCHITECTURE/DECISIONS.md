# ARCHITECTURE Epic - DECISIONS: Architectural Choices

This document lists the Architectural Decision Records (ADRs) for the backend kernel layout.

---

## 1. ADR-ARCH-001: Monolithic Process with Package Isolation

### Context
We want isolation between domains to prevent code tangling. However, microservices introduce network latency, serialization overhead, and run complex container loops that are too heavy for a local Windows PC.

### Decision
Keep the backend running as a single Python process, but enforce package isolation. Capabilities must not import from other capabilities directly. If communication is needed, it must run through the EventBus or via Dependency Inversion interfaces (Ports) registered in `app/core/ports.py`.

### Consequences
- Maintains lightweight performance (< 100MB idle RAM).
- Prevents spaghetti dependencies while avoiding microservice networking costs.

---

## 2. ADR-ARCH-002: Auto-Routing via FastAPI Router Prefixes

### Context
FastAPI requires explicit routes. Dynamic route mounting can make API documentation (Swagger) generation difficult if routes are not registered correctly before the app starts.

### Decision
Each capability manifest defines a list of route prefixes and module paths. During the startup sequence (specifically, Phase 4 of the boot manager), the system imports these routers and mounts them under the specified prefix.

### Consequences
- Keeps Swagger docs complete and fully functional.
- Allows zero-effort feature toggling: deleting a capability folder automatically removes its routes from the API gateway on next launch.
