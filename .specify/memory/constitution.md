# K.A.O.S Constitution

## Core Principles

### I. Zero Tolerance for Fabricated Data
Every metric, log line, or alert rendered in production mode must be backed by real, live, and traceable operational data. The system must display Loading, Offline, Unknown, or Error states when data is unready or unreachable. Fabricated mocks (like fake logs seeds, default hardcoded alerts, or random values) are prohibited.

### II. Dynamic Hardware Detection (CPU/VRAM)
VRAM usage and capacity metrics must query real GPU hardware interfaces (like `nvidia-smi`). In environments without dedicated GPU accelerators, the backend must report values as `null` and the frontend must display `VRAM: CPU Mode`. Fabricating fake VRAM allocations (e.g. `0.0/16GB`) on CPU-only machines is prohibited.

### III. Single Source of Truth Telemetry
All dashboard telemetry metrics must be consolidated into a single aggregated endpoint (`GET /api/system/dashboard`) executing sub-queries in parallel using `asyncio.gather`. The frontend must query from a single state store (`useSystemStore`) protected by a cache TTL. Parallel individual polls are restricted to avoid server resource starvation.

### IV. Offline Blocking Gate
The application boot and navigation flows must verify backend readiness (`GET /api/system/readiness`). If the backend server is unreachable or degraded, the routing gate must display a full-screen offline overlay blocking normal page navigation and preventing unhandled "Failed to fetch" errors.

### V. Silent Execution
All desktop updates, subprocess runs, and system daemon checks executed by Rust/Tauri under Windows environments must run invisibly without opening visible CMD or terminal command windows on the user's screen.

## Quality and Compliance

- **Architecture Fitness**: Pre-commit triggers verify boundary constraints (e.g. frontend files must not import backend modules, and workflows must not perform raw SQL database transactions).
- **Test coverage**: All feature pull requests must maintain at least 80% test line coverage and verify contract consistency against mock integrations.

## Governance

- Any change to core configuration parameters, database schemas, or provider endpoints must be accompanied by a new or updated Architecture Decision Record (ADR) file inside `docs/adr/`.
- The backlog and roadmap must be synchronized after each implementation milestone.

**Version**: 1.0.0 | **Ratified**: 2026-07-11 | **Last Amended**: 2026-07-11
