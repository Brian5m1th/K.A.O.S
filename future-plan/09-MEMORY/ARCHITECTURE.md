# MEMORY Epic - ARCHITECTURE: The Nine Compartments

## 1. Memory Topologies

Memory is stored across different databases and schemas based on retrieval speed and data structure:

```text
                  ┌────────────────────────┐
                  │    MEMORY MANAGER      │
                  └───────────┬────────────┘
                              │
       ┌──────────────────────┼──────────────────────┐
       ▼                      ▼                      ▼
  [Volatile/Fast]      [Relational/SQL]       [Semantic/Vector]
  (RAM / Redis)        (PostgreSQL)           (Qdrant DB)
       │                      │                      │
       ├─ Working Memory      ├─ Conversation Logs   ├─ Obsidian Notes
       └─ active context      ├─ Preferences         ├─ Identity Twin
                              ├─ Mission Checklists  └─ Code Semantics
                              └─ People & Projects
```

---

## 2. Dynamic Memory Consolidator

At the end of a Mission, the **Reflection** stage triggers a memory consolidation run:
1. Gathers working memory chat threads and tool execution logs.
2. Summarizes key decisions, errors, and lessons learned.
3. Generates vector embeddings of the summary and saves them to the **Semantic Memory** space in Qdrant.
4. Truncates the active conversation history to reduce context window load.
