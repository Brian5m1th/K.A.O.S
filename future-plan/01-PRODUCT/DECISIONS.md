# PRODUCT Epic - DECISIONS: Product Design Choices

This document logs the product design choices made for K.A.O.S during the transition to a Cognitive OS.

---

## 1. ADR-PROD-001: Move from Chat to Mission Control

### Context
Users open K.A.O.S and see a chat prompt. This suggests that the system's primary interface is chat conversations, mimicking ChatGPT. This hides the background execution, scheduling, and RAG capabilities of the platform.

### Decision
Make **Mission Control** the default view in the Tauri Desktop App. The Chat page will be moved inside a specific Mission as a communication channel. If no mission is active, a default "General Mission" will represent the global chat context.

### Consequences
- Clarifies the product's identity as a task/goal manager.
- Forces the user to specify context (workspace path) to enable agent execution.

---

## 2. ADR-PROD-002: Hide Technology Names behind Capability Labels

### Context
Exposing words like Qdrant, LangGraph, Promtail, and Ollama in the primary navigation tabs forces the user to understand the technology stack to navigate the app.

### Decision
Rename navigation tabs and features to clean, human-readable capability words (e.g., Think, Remember, Observe, Act, Protect).

### Consequences
- Simplifies UX and makes it accessible to power users who are not AI engineers.
- Keeps configuration decoupled: changes to the backend (e.g., swapping Qdrant for PostgreSQL PGVector) do not affect user interface labels.
