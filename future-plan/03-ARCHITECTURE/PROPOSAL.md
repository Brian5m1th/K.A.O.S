# ARCHITECTURE Epic - PROPOSAL: Capability-First System Restructuring

## 1. Modular Directory Blueprint

We propose refactoring the FastAPI backend (`assistant/app/`) to group code by capability domain:

```text
assistant/app/
├── capabilities/
│   ├── chat/                  # Chat api, service, models
│   ├── memory/                # Context serialization, database connections
│   ├── workspace/             # Code logic, Note parser, KIRL audits
│   └── communication/         # Email, WhatsApp adapters
├── core/                      # System Kernel (EventBus, Config, Manifest Engine)
└── main.py                    # Gateway Loader (dynamically boots capability folders)
```

Each folder under `capabilities/` is a self-contained unit holding:
- `manifest.yaml`
- `api/` (Routers)
- `services/` (Core Logic)
- `adapters/` (Technology Implementations: e.g., Qdrant, Postgres, SMTP)
- `events/` (Subscribers)
- `tests/` (Dedicated Unit/Integration files)

---

## 2. Manifest Autodiscovery Engine

The application startup is refactored to parse files at boot:

```python
import os
import yaml
from fastapi import FastAPI

def load_capabilities(app: FastAPI):
    cap_dir = "./app/capabilities"
    for cap_name in os.listdir(cap_dir):
        manifest_path = os.path.join(cap_dir, cap_name, "manifest.yaml")
        if os.path.exists(manifest_path):
            with open(manifest_path, "r") as f:
                manifest = yaml.safe_load(f)
                
            # 1. Dynamically mount routes
            mount_routes(app, cap_name, manifest.get("routes", []))
            
            # 2. Register event subscribers
            register_subscribers(cap_name, manifest.get("events_subscribed", []))
```

---

## 3. Rejected Alternatives

### Alternative A: Microservices (running each capability in a separate Docker container)
- **Why Rejected:** Too heavy for a local-first Windows environment. Memory consumption would exceed the target threshold (< 100MB RAM when idle). Keeping a monolithic codebase with modular runtime separation is optimal.
