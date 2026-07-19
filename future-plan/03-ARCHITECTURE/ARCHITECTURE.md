# ARCHITECTURE Epic - ARCHITECTURE: Core System Blueprint

## 1. System Topology

K.A.O.S is structured into three distinct execution layers: Boundary Interfaces, the Cognitive Kernel, and Adapter Drivers.

```text
  ┌────────────────────────────────────────────────────────┐
  │                   BOUNDARY INTERFACES                  │
  │     Tauri UI (React)  ◄──►  CLI  ◄──►  Web API Gateway │
  └───────────────────────────┬────────────────────────────┘
                              │ IPC / WebSocket / HTTP
  ┌───────────────────────────▼────────────────────────────┐
  │                    COGNITIVE KERNEL                    │
  │  ┌──────────────────────────────────────────────────┐  │
  │  │                     Event Bus                    │  │
  │  └───────▲───────────────────▲──────────────────▲───┘  │
  │          │                   │                  │      │
  │    ┌─────▼─────┐       ┌─────▼─────┐      ┌─────▼─────┐│
  │    │  MEMORY   │       │ PLANNING  │      │ GOAL ENG. ││
  │    │Capability │       │Capability │      │Capability ││
  │    └─────▲─────┘       └─────▲─────┘      └─────▲─────┘│
  └──────────┼───────────────────┼──────────────────┼──────┘
             │ Dependency Inversion Ports           │
  ┌──────────▼───────────────────▼──────────────────▼──────┐
  │                    ADAPTER DRIVERS                     │
  │  Postgres DB │ Qdrant Vector │ Ollama Local │ MCP Bridge│
  └────────────────────────────────────────────────────────┘
```

---

## 2. Dynamic Registration & Autodiscovery

On startup, the system initializes through an 8-stage boot program.
Instead of importing FastAPI routers statically, the system scans `app/capabilities/*/manifest.yaml` files and automatically mounts:
1. **HTTP/SSE Routes:** Mapped to FastAPI.
2. **Event Subscribers:** Linked to the system's asynchronous Event Bus.
3. **MCP Tools:** Exported to the active planning agent loop.

### Contract Sample (`app/core/manifest_parser.py`):
```python
class CapabilityManifest(BaseModel):
    id: str
    version: str
    routes: list[dict[str, str]]
    events_subscribed: list[str]
    commands_exposed: list[str]
```
