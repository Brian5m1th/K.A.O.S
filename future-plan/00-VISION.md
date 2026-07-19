# 00-VISION: K.A.O.S Cognitive Operating System

## 1. Executive Summary

This document establishes the strategic vision for **K.A.O.S (Knowledge & Agentic Orchestration System)**. It details a paradigm shift: transitioning K.A.O.S from a reactive, chat-centric application into a **Cognitive Operating System (Cognitive OS)**.

In this paradigm, the system ceases to be an on-demand chatbot interface. Instead, it becomes a persistent, autonomous background service—a digital mind that models the user, proactively manages goals, runs scheduled operations, observes digital environments, and uses interfaces (Chat, CLI, APIs) simply as terminal points of interaction.

---

## 2. The Paradigm Shift: Chat-Centric vs. Cognitive OS

Historically, personal AI assistants are reactive loop frameworks (User Input ➔ Prompt ➔ Tool Call ➔ LLM Response). The Cognitive OS treats intelligence as a state-management machine that operates continuously, even in the absence of user interaction.

| Dimension | Reactive Chat-Centric App | Cognitive Operating System |
| :--- | :--- | :--- |
| **Core Entity** | A Chat Session (Conversation) | The Cognitive Kernel (The Mind) |
| **Initiative** | Reactive (Waiting for user prompt) | Proactive (Triggered by events, goals, or time) |
| **Primary Interface**| Text Chat UI / Command Input | Background daemon with multi-modal boundary adapters |
| **Mental Model** | Short-term prompt engineering | A living, humanized "Personal Digital Twin" |
| **Execution Mode** | Transient scripts / Linear tools | Continuous goal-driven "Missions" |
| **Scheduling** | User runs commands manually | Headless Scheduler running automated workflows |

---

## 3. High-Level Architecture (The Cognitive Kernel)

The Cognitive OS separates the core reasoning engine (The Kernel) from interfaces and integrations.

```text
                           ┌───────────────────────────┐
                           │        INTERFACES         │
                           │ Desktop │ CLI │ API │ Voice│
                           └─────────────┬─────────────┘
                                         │
                        ┌────────────────┴────────────────┐
                        │        COGNITIVE KERNEL         │
                        │                                 │
                        │  ┌───────────┐   ┌───────────┐  │
                        │  │Perception │ ◄─┤ Guardian  │  │
                        │  └─────┬─────┘   └───────────┘  │
                        │        ▼                        │
                        │  ┌───────────┐                  │
                        │  │Understndg │                  │
                        │  └─────┬─────┘                  │
                        │        ▼                        │
                        │  ┌───────────┐   ┌───────────┐  │
                        │  │   Goals   │ ──►  Memory   │  │
                        │  └─────┬─────┘   └───────────┘  │
                        │        ▼                        │
                        │  ┌───────────┐                  │
                        │  │ Planning  │                  │
                        │  └─────┬─────┘                  │
                        │        ▼                        │
                        │  ┌───────────┐   ┌───────────┐  │
                        │  │ Execution │ ──►Reflection │  │
                        │  └─────┬─────┘   └─────┬─────┘  │
                        │        │               ▼        │
                        │        │         ┌───────────┐  │
                        │        │         │ Learning  │  │
                        │        │         └───────────┘  │
                        └────────┼────────────────────────┘
                                 │
                        ┌────────▼────────────────────────┐
                        │          INTEGRATIONS           │
                        │ LLMs │ MCP │ Filesystem │ n8n   │
                        │ GitHub │ Email │ Calendar │ OS   │
                        └─────────────────────────────────┘
```

### The 10 Cognitive Pipeline Stages

1. **Perception:** Listens to the environment. Ingests Windows events, git commits, file updates, emails, calendar notifications, system metrics (CPU/RAM), and messenger logs.
2. **Understanding:** Translates unstructured environment events into semantic relationships and impacts. (e.g., *Event: Docker container down* ➔ *Impact: Nextcloud database unavailable* ➔ *Priority: High*).
3. **Goals:** Maintains a nested hierarchy of user-defined long-term and short-term objectives (e.g., "Build Cognitive OS" ➔ Subgoals: "Structure 09-MEMORY", "Refactor LangGraph loop").
4. **Memory:** Manages 9 humanized subdivisions of data: Working, Conversation, Semantic, Episodic, Procedural, Identity, Preferences, Projects, and People.
5. **Reasoning:** Runs evaluation protocols, cognitive fallbacks, and checks safety policies before proposing actions.
6. **Planning:** Maps out multi-day, multi-step actions ("Missions") to resolve goal dependencies rather than simple single-prompt completions.
7. **Execution:** Dispatches tools, executes shell scripts, posts to webhooks, interacts with MCP servers, and generates files.
8. **Reflection:** Evaluates whether the execution was successful and why (e.g., *Check: Did compiling succeed? No, because of missing import*).
9. **Learning:** Updates Procedural and Semantic memories with findings from reflection, refining future plans.
10. **Response:** Sends stream responses, summaries, or OS notifications to the user interface.

---

## 4. The Jarvis Paradigm: Initiative & Windows Guardian

A true personal AI must possess initiative. Under Windows, the **Guardian** and **Perception** layers monitor system state continuously.

### Windows OS-Level Integration Points
- **Process & Resource Monitoring:** Watches Windows Performance Counters (CPU, RAM, Disk I/O) and Docker service states.
- **Filesystem Watcher:** Monitored via Windows Directory Change Notifications (`ReadDirectoryChangesW`) to track changes in workspace folders and Obsidian vaults.
- **Headless Execution:** Runs as a Windows Service (`kaosd.exe`) starting on boot, with zero visible console windows, using named pipes or HTTP for communicating with Tauri.

### Scenario Example:
1. **Perception:** File watcher detects a git pull with conflicting package dependencies.
2. **Understanding:** Understands this will break local compilation of the project.
3. **Goals:** Aligns with the active project mission: "Deliver stable release".
4. **Planning:** Schedules a background check.
5. **Execution:** Performs a dry run compile in the background.
6. **Reflection:** Identifies the precise file and line causing compilation failure.
7. **Response:** Proactively notifies the user via desktop toast: *"Brian, a recent commit has broken the build. I've analyzed the conflict and prepared a plan to resolve it. Double-click here to view."*

---

## 5. Mental States

To make interaction natural and context-aware, K.A.O.S implements **Mental States** which alter resource allocation, LLM selection, and communication urgency.

- **Sleeping:** Low-power state. Minimal filesystem auditing, no active LLM processing. Wakes on schedule or IPC interrupt.
- **Idle:** Idle loop. Periodically scans system state (Guardian), checks emails, audits memory.
- **Listening:** Interactive phase. Ingesting user prompt or stream.
- **Thinking:** Active reasoning. Processing embeddings, executing vector searches, evaluating logic.
- **Executing:** Active tool use. Running shell commands, calling APIs, modifying files.
- **Observing:** Tracking background execution status (e.g., waiting for docker build or n8n workflow).
- **Learning:** Post-execution cleanup. Saving vectors, consolidating memory logs.
- **Reflecting:** Validating outcome metrics and analyzing faults.
- **Planning:** Mapping multi-task workflows for new goals.
- **Emergency:** Critical fault detected (e.g., server down, database corrupted, disk full). Pauses non-critical agents, sends alert, waits for immediate human action.

---

## 6. The Concept of "Missions"

To replace transient "Chats", the Cognitive OS structures work into **Missions**.
A Mission is a stateful folder/database object containing:
- **Core Goal:** The desired outcome (e.g., "Migrate Qdrant to Cloud").
- **Sub-tasks:** Checklists tracked like a JIRA board.
- **Active Context:** Related project files, technical specs (SDDs), and documentation.
- **History log:** Decisions taken, errors encountered, and solutions discovered.
- **Execution state:** Live background tasks or scheduled scripts.

This turns every project into a persistent, living workspace that can be picked up by human developers or AI agents at any time.
