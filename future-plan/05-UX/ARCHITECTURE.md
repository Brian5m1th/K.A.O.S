# UX Epic - ARCHITECTURE: Front-End UI Layout Blueprint

## 1. UI Grid & Framework

The Tauri interface uses **Feature-Sliced Design (FSD)** to structure component hierarchies, dividing pages into standalone widgets.

```text
┌──────────────────────────────────────────────────────────────┐
│  TOP BAR:  [Mental State]        [Mind Stats]  [Notification]│
├─────────────┬────────────────────────────────────────────────┤
│             │                                                │
│  SIDEBAR    │                MAIN WORKSPACE                  │
│             │                                                │
│  [Missions] │  ┌──────────────────────────────────────────┐  │
│  - M-01     │  │           Active Mission Panel           │  │
│  - M-02     │  │                                          │  │
│             │  │  ┌──────────────┐      ┌──────────────┐  │  │
│  [Settings] │  │  │  Goal Tree   │      │  Chat & Logs │  │  │
│  - Prompts  │  │  └──────────────┘      └──────────────┘  │  │
│  - Models   │  └──────────────────────────────────────────┘  │
│             │                                                │
└─────────────┴────────────────────────────────────────────────┘
```

- **Sidebar (Global Navigation):** Lists active Missions, custom Model Profiles, and Configuration Settings.
- **Top Bar (Mind Status):** Exposes current mental states, local system metrics (Guardian), and connection indicators.
- **Main Workspace:** Shows active Mission details (Goal trees, notes, execution logs, Chat box).

---

## 2. Command Palette Architecture

Pressing `CTRL+K` opens a global Command Palette modal that intercepts actions:
- **Navigation:** `/go [mission-name]`
- **Actions:** `/act [tool-name] [params]`
- **Search:** `/search [query]` (runs semantic RAG retrieve)
- **State override:** `/state [sleeping/idle/thinking]`
