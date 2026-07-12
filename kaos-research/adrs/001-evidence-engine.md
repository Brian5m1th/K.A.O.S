# ADR-001: Graphify as Evidence Engine Source

- **Status:** Accepted
- **Decision Owner:** KAOS Architect (System)
- **Review Date:** 2027-01-11 (6 months)
- **Date:** 2026-07-11

---

## Context

The K.A.O.S platform needs an Evidence Engine to drive architectural decisions with data instead of intuition. Currently, architecture decisions are made ad-hoc with no systematic collection of evidence.

Graphify provides AST-level code graph with 12,187 nodes and 22,825 edges, including dependency paths, import cycles, god object detection, and community clustering.

## Decision

**Graphify will serve as the primary code intelligence source for the K.A.O.S Evidence Engine.** It will be one of multiple sources (alongside Git history, test results, coverage data, benchmarks, ADR history, and runtime metrics). No single source (including Graphify) is the sole authority.

## Evidence Supporting This Decision

1. **Graphify path query confirmed `GraphBuilder --uses--> CodeScanner` (1 hop)** — used to validate the deprecation decision.
2. **Graphify explain `CodeScanner` returned 41 connections** — identified as god object, triggering refactoring.
3. **Graphify GRAPH_REPORT.md detected 7 import cycles** — provided concrete evidence for architectural fit violations.
4. **Graphify explain `system.py` revealed `_fallback_*` functions** — validated mock elimination.
5. **Graphify explain `system-store.ts` confirmed `vramTotal: 16` hardcoded** — validated data fabrication removal.

## Consequences

- **Positive:** Evidence-driven decisions, automated architecture audit, continuous quality tracking
- **Negative:** Graphify CLI dependency for queries (mitigated by fallback to direct graph.json parsing)
- **Risk:** Graphify graph becomes stale between updates (mitigated by `graphify update .` in CI pipeline)

## Implementation

1. Phase 1: GraphBuilder and KnowledgeGraphBuilder refactored to load graphify-out/graph.json (done)
2. Phase 2: EvidencePort + EvidenceService created with Graphify as first source (done)
3. Phase 3: Git history, test results, benchmarks added as additional sources (pending)
4. Phase 4: Technology Observatory provides continuous framework evolution tracking (pending)

## Alternatives Considered

- **CodeScanner (regex):** Rejected — error-prone, ignores actual imports, hardcoded patterns
- **Manual review:** Rejected — does not scale, subjective
- **SCIP/LSIF:** Deferred — Graphify covers current needs; SCIP adds complexity
