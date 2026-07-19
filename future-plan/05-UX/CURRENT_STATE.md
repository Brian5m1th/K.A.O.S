# UX Epic - CURRENT STATE: Existing Tauri Interface

## 1. Page Bloat Analysis

The current Tauri frontend (`desktop/src/pages/`) contains 21 distinct page files:

```text
desktop/src/pages/
├── Dashboard/         # Observability metrics (Prometheus graphs)
├── Chat/              # Standard conversation interface
├── RAG/               # Semantic search query inputs
├── Graphify/          # Architectural nodes graph visualizer
├── Events/            # Real-time event bus logs
├── Audit/             # Document drift tables (KIRL)
├── Settings/          # Technical parameters setup
└── [Other Pages]      # Pipelines, costs, prompt editors, etc.
```

---

## 2. Usability Failures in Current Layout

- **High Navigation Friction:** Users must leave the Chat page to check Prometheus metrics, open the RAG page to index files, and navigate to the Audit page to view drift results.
- **Cognitive Load:** Exposing raw event JSON logs directly in the main interface overwhelms non-developer users.
- **No Background feedback:** If the user is on the Settings page, they cannot see if an active agent is executing a command in the background unless they click back to the Chat page.
- **Lacks Cohesive Style System:** Layout components have inconsistent button styling, border radii, and HSL transparency coefficients.
