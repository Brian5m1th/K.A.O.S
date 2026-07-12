# Tasks: K.A.O.S Production Readiness & Mock Elimination

**Input**: Design documents from `.specify/memory/`

**Prerequisites**: plan.md (required), spec.md (required)

---

## Phase 1: Setup (Shared Infrastructure)
**Purpose**: Project initialization and Spec Kit hooks integration

- [ ] T001 Initialize Spec Kit directories and verify `.specify/memory/` configuration files.
- [ ] T002 Configure local linting rules for both backend (`ruff`) and frontend.
- [ ] T003 [P] Add the `verify-no-mocks.ps1` audit script to check for static indicators on build time.

---

## Phase 2: Foundational (Blocking Prerequisites)
**Purpose**: Core backend readiness APIs and metrics configurations

- [ ] T004 Implement `GET /api/system/readiness` inside `assistant/app/api/system.py` querying Postgres and Qdrant states.
- [ ] T005 Implement `GET /api/system/dashboard` combining services, telemetry metrics, cost breakdowns, and notifications via `asyncio.gather`.
- [ ] T006 [P] Update `ProviderMetrics` inside `assistant/app/llm/metrics.py` to use class-level `_global_entries` to log average LLM request latencies.
- [ ] T007 [P] Configure Ollama local tags check inside `/provider/active` to check if default models exist before returning names.
- [ ] T008 [P] Refactor `GraphBuilder` inside `assistant/app/ai/vault_analyzer/graph_builder.py` to load `graphify-out/graph.json`, aggregate and cluster nodes at the file/component level, and deprecate `CodeScanner.py`.
- [ ] T022 Implement AirLLMProvider wrapping lyogavin/airllm library, mapping settings, and routing keys in LLMFactory.

---

## Phase 3: User Story 1 - De-mocking Dashboard & Observability (Priority: P1)
**Goal**: Remove all mock logs, hardcoded alerts, and dummy arrays from frontend screens.

- [ ] T009 [P] [US1] Remove `fallbackAlerts`, static logs seed, and simulated agent status logic from `desktop/src/pages/dashboard/index.tsx`.
- [ ] T010 [P] [US1] Clean out static alerts array and mock log states from `desktop/src/pages/observability/index.tsx`.
- [ ] T011 [US1] Retarget all store imports under `desktop/src/pages/documentation/index.tsx` and the test files to remove duplicate folder files in `@/shared/lib/stores`.

---

## Phase 4: User Story 2 - Consolidated Dashboard Telemetry (Priority: P1)
**Goal**: Integrate the unified dashboard endpoint with the client system store and implement SWR TTL caching.

- [ ] T012 [US2] Update `fetchAll` in `desktop/src/application/stores/system-store.ts` to call `GET /api/system/dashboard` and parse aggregated payloads.
- [ ] T013 [US2] Add a 3-second throttle cache using timestamp checks to skip redundant requests.
- [ ] T014 [P] [US2] Add the contract validation test suite in `desktop/src/__tests__/integration/contract-validation.test.ts`.

---

## Phase 5: User Story 3 - Offline Boot Gate & Readiness check (Priority: P1)
**Goal**: Block access to protected routes on backend failures or timeouts.

- [ ] T015 [US3] Update bootstrap pipeline in `desktop/src/shared/lib/use-init.ts` to poll `GET /api/system/readiness` and track timings.
- [ ] T016 [US3] Add the visual offline overlay to `AuthGate` in `desktop/src/app/routes/index.tsx` triggered by store offline state.

---

## Phase 6: User Story 4 - Silent Subprocess Execution (Priority: P2)
**Goal**: Prevent command prompt windows on Windows.

- [ ] T017 [US4] Configure `creation_flags(0x08000000)` on all Rust Tauri command executions inside `desktop/src-tauri/src/updater.rs`.

---

## Phase 7: Polish & Validation
**Purpose**: Final check and backlog review.

- [ ] T018 Execute `npm run test` (vitest) and `uv run pytest` to check test compliance.
- [ ] T019 Execute the `verify-no-mocks.ps1` scan script.
- [ ] T020 Update the backlog document and ADR records to reflect completion status.
- [ ] T021 Implement a "Graphify Path Inspector" tab in the Desktop explorer UI calling backend wrapper for `graphify path` queries.

---

## Phase 8: Advanced Tools Integration & System-Wide Audit
**Purpose**: Setup, configuration, and comparative audit of state-of-the-art developer and memory tools.

- [ ] T023 Clone/Install the target library suite (Microsoft GraphRAG, Graphiti, Mem0, Letta, LlamaIndex, FalkorDB, OpenTelemetry, Langfuse, MCP, SCIP, Semgrep, Aider, OpenHands).
- [ ] T024 Execute active behavioral test scripts to audit execution costs, latency, memory footprints, and interface bounds for all target libraries.
- [ ] T025 Document findings in `tool_integration_audit_report.md`, determining codebase deprecation/adaptation decisions and structural code changes.
