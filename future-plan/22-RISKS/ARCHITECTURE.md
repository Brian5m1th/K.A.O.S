# RISKS Epic - ARCHITECTURE: Safety Boundaries

## 1. Safety Gate Topology

K.A.O.S implements an interception-based safety layer (The Guardian) that wraps the execution engine.

```text
  ┌────────────────────────────────────────────────────────┐
  │                    EXECUTION INITIATED                 │
  │                  (Plan / Action Request)               │
  └───────────────────────────┬────────────────────────────┘
                              │
  ┌───────────────────────────▼────────────────────────────┐
  │                   THE GUARDIAN GATEWAY                 │
  │                                                        │
  │  ┌───────────────┐   ┌───────────────┐  ┌───────────┐  │
  │  │ Cost Budget   │   │  Permission   │  │ Resource  │  │
  │  │ Check         │   │  Validator    │  │ Supervisor│  │
  │  └───────┬───────┘   └───────┬───────┘  └─────┬─────┘  │
  │          │                   │                │        │
  │          ▼                   ▼                ▼        │
  │    Is under $2.00?     Is command safe?  Is CPU < 80%? │
  └──────────┼───────────────────┼────────────────┼────────┘
             │ Yes               │ Yes            │ Yes
             └───────────┬───────┴────────────────┘
                         ▼
  ┌────────────────────────────────────────────────────────┐
  │                   ALLOW TOOL EXECUTION                 │
  └────────────────────────────────────────────────────────┘
```

- **Cost Budget Check:** Compares execution history against the Mission budget before calling cloud APIs.
- **Permission Validator:** Analyzes command strings against blacklists (e.g. `rm -rf`, `format`, `del`) and requires user confirmation dialogs.
- **Resource Supervisor:** Halts background audits if local CPU temperature or usage spike above safety limits.
