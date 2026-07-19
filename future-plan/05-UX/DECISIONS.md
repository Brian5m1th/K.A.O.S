# UX Epic - DECISIONS: Front-End Design Choices

This document logs front-end framework and UI design decisions.

---

## 1. ADR-UX-001: Consolidated Navigation Architecture

### Context
With 21 pages, navigating the Tauri desktop application feels cluttered and requires high cognitive overhead.

### Decision
Consolidate the application layout into three key views:
- **Mission Control** (Action/Goals/Chat)
- **Memory Vault** (Knowledge search/Graphify)
- **Control Center** (Config/Logs/Monitoring)

### Consequences
- Dramatically simplifies the sidebar.
- Keeps users focused on active tasks instead of technical settings.

---

## 2. ADR-UX-002: React Router 7 Migration

### Context
We need clean transitions and sub-layouts inside the Consolidated Navigation views.

### Decision
Migrate the project from React Router v6 to v7 to take advantage of nested routing layouts, simplified loader data caching, and native transition hooks.

### Consequences
- Speeds up route loading.
- Simplifies breadcrumb components.
