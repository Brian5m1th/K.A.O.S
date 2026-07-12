# Implementation Plan: K.A.O.S Production Readiness & Advanced Tool Integration

**Branch**: `sdd-kaos-production-readiness` | **Date**: 2026-07-11 | **Spec**: [.specify/memory/specification.md](file:///c:/workspace/Freelancer/K.A.O.S/.specify/memory/specification.md)

## Summary
The goal is to prepare K.A.O.S Desktop and backend for production use by:
1. Eliminating simulated/mock data sources and unifiying telemetry APIs.
2. Implementing an offline gate in the frontend boot pipeline.
3. Integrating a robust suite of industry-standard engineering tools:
   - **Spec Kit & Graphify**: Structured SDD execution and code-level AST knowledge indexing.
   - **AirLLM**: Local layer-wise inference execution.
   - **Microsoft GraphRAG, Graphiti, Mem0 & Letta**: Layered cognitive architecture for multi-agent workflows, temporal knowledge, and virtual persistent memory.
   - **LlamaIndex, FalkorDB & NetworkX**: Structured property graphs and graph analysis.
   - **OpenTelemetry & Langfuse**: Advanced tracing, telemetry diagnostics, and cost analysis.

## Technical Context
- **Language/Version**: Python 3.13 (backend) & TypeScript/TSX (frontend/Tauri app).
- **Primary Dependencies**: FastAPI (backend), React, Zustand (frontend), Tauri (desktop shell), Qdrant (vector index), LangGraph, FalkorDB, and OpenTelemetry.
- **Storage**: PostgreSQL, Qdrant, FalkorDB, and local JSON graphs.
- **Testing**: pytest (backend) and vitest (frontend).
- **Target Platform**: Windows 10/11 native.
- **Constraints**: zero fabricated variables, offline-first boot readiness, and silent Tauri executions.

## Constitution Check
- **Zero Mocks**: Passed. All static array metrics in `dashboard/index.tsx` and `observability/index.tsx` are deleted.
- **Hardware Mode**: Passed. If no GPU is found, VRAM total/used is returned as `null` (CPU Mode).
- **Consolidated Telemetry**: Passed. Consolidated 12 telemetry calls into `GET /api/system/dashboard` running parallelized sub-queries.

## Project Structure

### Source Code
```text
assistant/
├── app/
│   ├── api/
│   │   ├── system.py       # Exposes /dashboard and /readiness
│   │   └── setup.py        # Validates model active status
│   ├── llm/
│   │   ├── providers/
│   │   │   └── airllm_provider.py # AirLLM layer-wise provider
│   │   └── metrics.py      # Tracks latency average
│   ├── providers/
│   │   ├── memory/
│   │   │   ├── mem0.py     # Mem0 persistent agent memory adapter
│   │   │   └── graphiti.py # Graphiti temporal evolution adapter
│   │   └── rag/
│   │       └── graphrag.py # Microsoft GraphRAG integration
│   └── main.py             # App route bindings
└── tests/                  # Backend unit/integration tests

desktop/
├── src/
│   ├── application/
│   │   └── stores/         # Canonical stores (consolidated)
│   ├── shared/
│   │   └── lib/
│   │       ├── use-init.ts # Boot readiness gate & telemetry timer
│   │       └── stores/     # Deleted duplicate stores
│   ├── app/
│   │   └── routes/         # AuthGate connection overlay
│   └── pages/
│       ├── dashboard/      # Unified telemetry rendering
│       └── welcome/        # Welcome/Onboarding steps
└── package.json            # Vitest script configs
```

**Structure Decision**: Consolidate frontend state management strictly under `desktop/src/application/stores/` to enforce Feature-Sliced Design (FSD) architecture. Implement external cognitive libraries under specialized subfolders inside `assistant/app/providers/`.
