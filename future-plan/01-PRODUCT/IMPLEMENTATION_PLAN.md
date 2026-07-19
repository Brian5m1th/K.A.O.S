# PRODUCT Epic - IMPLEMENTATION PLAN: K.A.O.S Product Migration

This plan details the phases of the product refactor. Code changes will be executed by other technical epics, while this document serves as the product roadmap.

---

## 1. Phases & Milestones

```text
Phase 1: Relabeling UI ──► Phase 2: Mission Control ──► Phase 3: Goal Integration
(Rename tech labels)      (Introduce Mission view)      (Real-time Goals graph)
```

### Phase 1: Relabeling UI (Milestone 1)
- Rename pages and sidebars to match capabilities:
  - "RAG search" ➔ "Remember"
  - "MCP Tools" ➔ "Act"
  - "LangGraph Logs" ➔ "Think Logs"
  - "Event Bus" ➔ "Observe"
- Simplify Settings page: abstract Ollama/OpenAI behind "Model Profile".

### Phase 2: Mission Control UI (Milestone 2)
- Build the **Mission Control Dashboard** in the Tauri frontend.
- Allow users to "Create a Mission" by binding a path (folder) and describing the goal.
- Embed a JIRA-style task list inside the Mission view.

### Phase 3: Goal Integration (Milestone 3)
- Connect the frontend to the backend's Goal Engine.
- Show live subgoal trees that check items off automatically as the planner executes tasks.
- Enable desktop toasts for proactive notifications (e.g., compile issues, server status alerts).

---

## 2. Acceptance Criteria

- [ ] Users can create a Mission with a target directory and description.
- [ ] Technical terms like Ollama/Qdrant are hidden from the primary workspace views.
- [ ] Active subgoals are represented in a visual hierarchy tree in the UI.
- [ ] Background alerts trigger system notifications on Windows without opening the Tauri UI window.
