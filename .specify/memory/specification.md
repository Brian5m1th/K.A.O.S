# Feature Specification: K.A.O.S Production Readiness & Mock Elimination

**Feature Branch**: `sdd-kaos-production-readiness`

**Created**: 2026-07-11

**Status**: Active

**Input**: User description: "Eliminar mocks, unificar endpoints do dashboard, criar gates de boot e readiness, corrigir subprocessos com popups de terminal, retargetar e consolidar stores do frontend."

## User Scenarios & Testing

### User Story 1 - De-mocking Dashboard & Observability (Priority: P1)
As a workspace operator, I want to see only real operational metrics on my dashboard, so that I don't confuse simulated logs or alerts with actual system events.

**Why this priority**: Zero tolerance for fabricated data is the core architectural rule. Accurate observability is critical to prevent false-positives.

**Independent Test**: Remove static seeds and verify that the dashboard renders empty states ("No active alerts", empty log viewport) when the backend database holds no events.

**Acceptance Scenarios**:
1. **Given** no active system notifications, **When** loading the dashboard, **Then** display "No active alerts" and zero active counts.
2. **Given** no streamed SSE events, **When** loading the observability logs, **Then** show a clean empty viewport with a connection status indicator.

---

### User Story 2 - Consolidated Dashboard telemetry (Priority: P1)
As a desktop client, I want to retrieve all dashboard metrics in a single network roundtrip, so that parallel requests do not saturate my local backend or timeout.

**Why this priority**: Consolidating 12 requests into 1 reduces communication bottlenecks and prevents "Failed to fetch" connection errors.

**Independent Test**: Mock a single `/api/system/dashboard` endpoint and verify the frontend `useSystemStore` populates metrics, services, and VRAM with 1 fetch request.

**Acceptance Scenarios**:
1. **Given** a healthy backend, **When** the dashboard polls for updates, **Then** invoke `GET /api/system/dashboard` once per interval cycle.
2. **Given** rapid navigation between pages, **When** fetchAll is triggered, **Then** leverage the 3-second cache TTL to skip redundant requests.

---

### User Story 3 - Offline Boot Gate & Readiness Check (Priority: P1)
As a Tauri desktop user, I want the client app to verify the backend database and vector status on startup, so that I am blocked from entering the main application routes if the backend is offline.

**Why this priority**: Gracefully handling connection failures prevents routing to broken interfaces.

**Independent Test**: Stop the backend process and verify the application displays a full-screen offline overlay with a retry option.

**Acceptance Scenarios**:
1. **Given** the backend is uninitialized, **When** the application starts, **Then** display the boot readiness step as loading.
2. **Given** the readiness check times out (30s), **When** loading the router, **Then** redirect to the offline overlay displaying `https://api.kaostech.com.br` and block page access.

---

### User Story 4 - Silent Subprocess Execution (Priority: P2)
As a Windows user, I want Tauri update checks and migration tasks to execute silently, so that command prompt windows do not pop up on my screen.

**Why this priority**: Enhances desktop UX by running system diagnostics in the background.

**Independent Test**: Trigger a docker engine availability check and verify no console host or shell process creates a visible window.

**Acceptance Scenarios**:
1. **Given** update check starts on Windows, **When** invoking Tauri commands, **Then** set creation flags `0x08000000` (CREATE_NO_WINDOW).

---

### Edge Cases
- **No GPU Present**: System must report VRAM as `null` and show `VRAM: CPU Mode` instead of fake gigabytes allocation.
- **Out of Sync Store**: All direct references to `@/shared/lib/stores` are cleaned and consolidated in `@/application/stores` to prevent state drift.

## Requirements

### Functional Requirements
- **FR-001**: The backend MUST expose `GET /api/system/dashboard` parallelizing database, vector count, and active provider metrics.
- **FR-002**: The backend MUST expose `GET /api/system/readiness` assessing Postgres and Qdrant connectivity states.
- **FR-003**: The frontend MUST redirect to an offline blocking screen if `GET /api/system/readiness` fails during app bootstrap.
- **FR-004**: The frontend MUST enforce a 3-second cache throttle on dashboard telemetry polls.
- **FR-005**: The Rust updater MUST execute checks using `CREATE_NO_WINDOW` flags on Windows.
- **FR-006**: The CI build pipeline MUST execute `verify-no-mocks.ps1` to prevent mock regressions.

## Success Criteria

### Measurable Outcomes
- **SC-001**: Average network request count during dashboard polling is reduced from 12 parallel requests to 1 aggregated call.
- **SC-002**: Visual audits prove that zero hardcoded mock alerts (`fallbackAlerts`) or static logs are bundled in the production release.
- **SC-003**: In GPU-less environments, top bar renders `VRAM: CPU Mode`.
- **SC-004**: The pre-commit/CI script validates 100% compliance with mock exclusions.

## Assumptions
- The default remote URL is `https://api.kaostech.com.br` as configured in the store.
- Host system runs Windows, requiring `CREATE_NO_WINDOW` subprocess adjustments.
