# PRODUCT Epic - PROPOSAL: K.A.O.S Cognitive Product Redesign

## 1. The Core Proposal: Mission Control & Goals

We propose redesigning the user interface and product experience to focus on a **Mission Control Panel** instead of a single Chat UI.

```text
┌────────────────────────────────────────────────────────┐
│                      MISSION CONTROL                   │
│                                                        │
│  Active Mission: "Migrate Server Database"             │
│  State: EXECUTING                 Urgency: NORMAL      │
│                                                        │
│  ┌───────────────────────┐   ┌──────────────────────┐  │
│  │ Goal Tree             │   │ Activity log (Mind)  │  │
│  │ [x] Stop Postgres     │   │ - Observed Git push  │  │
│  │ [/] Backup SQL        │   │ - Running dry run    │  │
│  │ [ ] Transfer Data     │   │ - Reflecting on log  │  │
│  └───────────────────────┘   └──────────────────────┘  │
│                                                        │
│  [Ask Assistant / Issue Command...]                    │
└────────────────────────────────────────────────────────┘
```

- **Missions as Folders:** Every project is mapped as a Mission. The Mission folder keeps track of files, logs, commits, notes, and task lists.
- **Goal Tree UI:** A hierarchy showing active, pending, and completed subgoals.
- **Mind Activity Log:** Instead of simple chat messages, the system streams its background thoughts (Perceptions, Reflections, and Decisions).

---

## 2. Re-labeling Technical Assets to Humanized Capabilities

To clean up the UI, technical features will be presented under clean, capability-based labels:

- **RAG / Qdrant search** ➔ **Remember** (Search semantic vault)
- **LangGraph loop / Ollama** ➔ **Think** (Formulate response)
- **Tauri / OS commands** ➔ **Act** (Execute shell tool)
- **Windows File Watcher** ➔ **Observe** (Process events)

---

## 3. Rejected Alternatives

### Alternative A: Keep the Chat interface as the center, and add "Agent Panels" on the side.
- **Why Rejected:** This doesn't resolve the identity crisis. The system still looks like a ChatGPT clone with side features. It doesn't convey the "Cognitive OS" architecture.

### Alternative B: Direct terminal emulation as the main page.
- **Why Rejected:** Too complex for power users who are not software developers. Focuses too heavily on CLI and not enough on knowledge and goals.
