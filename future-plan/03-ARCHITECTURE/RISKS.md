# ARCHITECTURE Epic - RISKS: Technical Architect Risks

This document analyzes technical system risks.

---

## 1. Risk: Circular Imports & Coupling

### Description
Since python doesn't enforce module boundaries at build time, developers might bypass ports and import between capabilities directly (e.g. importing `capabilities.memory.services` directly inside `capabilities.chat`).

### Impact
- **High:** Re-introduces coupling and defeats the capability-first architecture.

### Mitigation
- Implement a static lint check in the CI/CD pipeline and the KIRL engine to analyze imports.
- Block PRs that contain direct cross-capability imports.

---

## 2. Risk: Event Queue Overflow

### Description
An in-memory event bus (using `asyncio.Queue`) can lose events if the server crashes or if the queue is overloaded with file changes/observability metrics.

### Impact
- **Medium:** Loss of observability data or missing file watcher updates.

### Mitigation
- Integrate a database-backed transaction outbox pattern for critical events (like billing, credential changes, or mission updates).
- Non-critical events (like UI status changes) can fail gracefully.
