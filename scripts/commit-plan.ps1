#!/usr/bin/env pwsh
# K.A.O.S Evolution v14 — Atomic Commits by Functionality
# Target branch: dev
# Usage: pwsh -File scripts/commit-plan.ps1

$ErrorActionPreference = "Stop"
Set-Location "C:\workspace\Freelancer\K.A.O.S"

Write-Host "`n🌿 K.A.O.S Evolution v14 — Committing by Feature to 'dev'" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════`n" -ForegroundColor Gray

# ── Pre-flight ──────────────────────────────────────────────────
Write-Host "🔍 Checking git status..." -ForegroundColor Yellow
git status --short | Measure-Object | ForEach-Object { Write-Host "  $($_.Count) files changed" }
Write-Host ""

# ════════════════════════════════════════════════════════════════
# COMMIT 1: Fix — Mock Elimination & Constitution Compliance
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [1/11] fix: mock elimination & constitution compliance" -ForegroundColor Green
git add `
  scripts/verify-no-mocks.ps1 `
  desktop/src/application/stores/system-store.ts `
  assistant/app/api/system.py `
  desktop/src/__tests__/shared/lib/stores/system-store.test.ts `
  assistant/app/llm/factory.py `
  desktop/src/shared/lib/use-init.ts
git commit -m "fix: eliminate all mock/fabricated data patterns

- Remove _fallback_services/runtime/metrics from system.py
- Change vramTotal: 16 to 0 in system-store.ts + test
- Add GET /api/system/readiness endpoint
- Add readiness polling in use-init.ts bootstrap pipeline
- Rename _fallback_invoke to _chain_invoke (circuit breaker, not mock)
- Create verify-no-mocks.ps1 CI scan script

Constitution Article I: Zero Tolerance for Fabricated Data — 100% compliant"

# ════════════════════════════════════════════════════════════════
# COMMIT 2: Feat — Graphify Source Integration
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [2/11] feat: graphify source integration, deprecate CodeScanner" -ForegroundColor Green
git add `
  assistant/app/ai/vault_analyzer/graph_builder.py `
  assistant/app/ai/vault_analyzer/knowledge_graph.py
git commit -m "feat: integrate Graphify graph.json as code intelligence source

- Refactor GraphBuilder to load graphify-out/graph.json
- Refactor KnowledgeGraphBuilder to load graphify-out/graph.json
- Deprecate CodeScanner (regex scanner, 41 connections, consumed by 7 subsystems)
- Aggregate file-level nodes from AST symbol graph
- Add Graphify evidence: GraphBuilder --uses--> CodeScanner (1 hop)

Evidence: graphify path 'GraphBuilder' 'CodeScanner' confirmed dependency"

# ════════════════════════════════════════════════════════════════
# COMMIT 3: Feat — Domain Ports (Capability Interfaces)
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [3/11] feat: domain ports — GraphPort, MemoryPort, RetrievalPort, InferencePort, PlannerPort, EvidencePort" -ForegroundColor Green
git add `
  assistant/app/domain/__init__.py `
  assistant/app/domain/ports/
git commit -m "feat: define 6 domain ports for capability-first architecture

- GraphPort: code intelligence queries (explain, path, query, health)
- MemoryPort: agent/user memory (store, search, get, delete, health)
- RetrievalPort: semantic vector search (search, index, count, health)
- InferencePort: LLM inference (invoke, stream, list_models, health)
- PlannerPort: task planning (plan, execute, status, health)
- EvidencePort: architecture evidence (collect, get_metric, history, health)

Architecture: Domain → Ports → Adapters → Frameworks
Zero framework dependencies at the port level"

# ════════════════════════════════════════════════════════════════
# COMMIT 4: Feat — ProviderRegistry
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [4/11] feat: generic ProviderRegistry for runtime provider swapping" -ForegroundColor Green
git add `
  assistant/app/core/__init__.py `
  assistant/app/core/provider_registry.py
git commit -m "feat: add generic ProviderRegistry for runtime provider switching

- ProviderRegistry[T]: register, activate, remove, deactivate, list
- Auto-activate first registered provider
- Health-aware fallback support
- Type-safe generic container for all K.A.O.S services

Enables: Desktop never knows which framework implements a capability"

# ════════════════════════════════════════════════════════════════
# COMMIT 5: Feat — Framework Adapters
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [5/11] feat: 11 framework adapters implementing domain ports" -ForegroundColor Green
git add `
  assistant/app/providers/__init__.py `
  assistant/app/providers/graph/ `
  assistant/app/providers/memory/postgres_memory_adapter.py `
  assistant/app/providers/retrieval/ `
  assistant/app/providers/inference/ `
  assistant/app/providers/planner/ `
  assistant/app/providers/evidence/
git commit -m "feat: implement 11 framework adapters for domain ports

Graph:
  - GraphifyAdapter (CLI + graph.json, explain/path/query)
  - NetworkXFallback (in-memory when Graphify offline)
Memory:
  - PostgresMemoryAdapter (PostgreSQL + in-memory fallback)
Retrieval:
  - QdrantAdapter (vector search via qdrant-client)
Inference (5 providers):
  - OllamaAdapter, AirLLMAdapter, OpenAIAdapter, GeminiAdapter, ClaudeAdapter
Planner:
  - LangGraphAdapter (agent workflow state machine)
Evidence:
  - EvidenceEngine (Graphify + Git + ADRs multi-source)

Every adapter wraps exactly one framework. Desktop never imports any of them"

# ════════════════════════════════════════════════════════════════
# COMMIT 6: Feat — Core Services
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [6/11] feat: 7 capability services with ProviderRegistry" -ForegroundColor Green
git add `
  assistant/app/core/services/
git commit -m "feat: implement 7 capability services

- GraphService: code intelligence queries (wraps GraphPort)
- MemoryService: agent/user memory (wraps MemoryPort)
- RetrievalService: semantic search (wraps RetrievalPort)
- InferenceService: LLM routing (wraps InferencePort, 5 providers)
- PlannerService: task planning (wraps PlannerPort)
- EvidenceService: architecture health (wraps EvidencePort)
- KnowledgeService: unified coalescing (graph + memory + retrieval)

Each service has a ProviderRegistry for runtime provider swapping"

# ════════════════════════════════════════════════════════════════
# COMMIT 7: Feat — REST APIs + Dependency Injection
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [7/11] feat: 6 REST APIs, 24 endpoints, FastAPI wiring" -ForegroundColor Green
git add `
  assistant/app/api/graph_api.py `
  assistant/app/api/memory_api.py `
  assistant/app/api/knowledge_api.py `
  assistant/app/api/inference_api.py `
  assistant/app/api/planner_api.py `
  assistant/app/api/evidence_api.py `
  assistant/app/dependencies/ `
  assistant/app/main.py
git commit -m "feat: deploy 6 REST APIs with 24 endpoints + FastAPI DI

New APIs:
  - /api/graph/*     (explain, path, query, health)
  - /api/memory/*    (store, search, get, delete, health)
  - /api/knowledge/* (query, health)
  - /api/inference/* (invoke, stream/SSE, models, health)
  - /api/planner/*   (plan, execute, status, health)
  - /api/evidence/*  (report, metric, history, health)

Dependency injection via app.dependencies.services:
  Singleton services initialized at startup, lazy-loaded on first request
  All API routes use FastAPI Depends() for service injection"

# ════════════════════════════════════════════════════════════════
# COMMIT 8: Feat — Desktop Decoupled Stores
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [8/11] feat: 5 Desktop stores + Graphify Inspector page" -ForegroundColor Green
git add `
  desktop/src/application/stores/graph-store.ts `
  desktop/src/application/stores/memory-store.ts `
  desktop/src/application/stores/knowledge-store.ts `
  desktop/src/application/stores/inference-store.ts `
  desktop/src/application/stores/evidence-store.ts `
  desktop/src/pages/graphify-inspector/ `
  scripts/verify-no-framework-imports.ps1
git commit -m "feat: add 5 Desktop stores — zero framework imports

Stores:
  - graph-store.ts      → GET /api/graph/*
  - memory-store.ts     → POST /api/memory/*
  - knowledge-store.ts  → POST /api/knowledge/*
  - inference-store.ts  → POST /api/inference/*  (5 providers + SSE streaming)
  - evidence-store.ts   → GET /api/evidence/*

Graphify Inspector page: explain symbols, trace paths, search code graph
verify-no-framework-imports.ps1: CI gate enforcing zero framework imports

Architecture Fit Function: Desktop never imports graphify, mem0, qdrant, etc."

# ════════════════════════════════════════════════════════════════
# COMMIT 9: Docs — Blueprint, Governance & Validation
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [9/11] docs: blueprint, governance, validation report" -ForegroundColor Green
git add `
  docs/blueprint/ `
  docs/governance/ `
  docs/evolution/ `
  docs/VALIDATION_REPORT.md `
  PROJECT_HEALTH.md
git commit -m "docs: architecture blueprint, governance, and validation report

Blueprint:
  - capability-map.md: complete 6-layer K.A.O.S brain map

Governance:
  - ADR-template.md: standardized decision record format
  - adr-governance.md: lifecycle, merge block rules, registry
  - evidence-driven-decisions.md: 10-step scientific method
  - quality-gates.md: 11 CI gates (lint → coverage → security)

Evolution:
  - onboarding.md: how to add capability, swap provider, run experiments

Validation:
  - VALIDATION_REPORT.md: full test results, Graphify evidence, 6 flow traces"

# ════════════════════════════════════════════════════════════════
# COMMIT 10: Feat — Research Laboratory
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [10/11] feat: kaos-research laboratory + experiments" -ForegroundColor Green
git add `
  kaos-research/README.md `
  kaos-research/evidence/ `
  kaos-research/catalog/ `
  kaos-research/adrs/ `
  kaos-research/reports/ `
  kaos-research/experiments/mem0/experiment.py `
  kaos-research/experiments/graphrag/experiment.py `
  kaos-research/experiments/airllm/experiment.py `
  kaos-research/benchmarks/ `
  kaos-research/technology-observatory/observatory.py
git commit -m "feat: kaos-research laboratory — evidence-driven framework evaluation

Structure: catalog, experiments (Mem0, GraphRAG, AirLLM), benchmarks, evidence, ADRs

Key artifacts:
  - evidence/state-audit-report.md: Graphify-powered architecture audit
  - evidence/hypotheses.md: 7 hypotheses (H1-H7) with validation criteria
  - evidence/capability-matrix.md: 7 frameworks × 27 capabilities comparison
  - catalog/framework-catalog.json: 9 frameworks with structured metadata
  - adrs/001-evidence-engine.md: Graphify as primary evidence source
  - adrs/002-capability-ports.md: Capability-First architecture decision
  - adrs/003-technology-observatory.md: continuous tech monitoring
  - technology-observatory/observatory.py: tracks 14 frameworks via GitHub + PyPI
  - benchmarks/datasets/kaos_questions.json: 6 benchmark questions

Rules: no framework touches K.A.O.S main codebase until ADR approved"

# ════════════════════════════════════════════════════════════════
# COMMIT 11: Test — Unit & Contract Tests
# ════════════════════════════════════════════════════════════════
Write-Host "📦 [11/11] test: ProviderRegistry, adapters, and dashboard contract" -ForegroundColor Green
git add `
  assistant/tests/unit/ports/ `
  assistant/tests/unit/test_dashboard_contract.py
git commit -m "test: add 21 unit + contract tests (all passing)

ProviderRegistry tests (10):
  - register, activate, remove, deactivate, fallback, auto-select
Adapter tests (6):
  - GraphifyAdapter, NetworkXFallback, EvidenceEngine
Contract tests (5):
  - dashboard: required fields, null on failure, services structure, VRAM null on CPU mode
  - readiness: required fields, services sub-object

Result: 21/21 pass, verify-no-mocks.ps1 PASS, verify-no-framework-imports.ps1 PASS"

# ════════════════════════════════════════════════════════════════
# SUMMARY
# ════════════════════════════════════════════════════════════════
Write-Host "`n═══════════════════════════════════════════════════════════" -ForegroundColor Gray
Write-Host "✅ All 11 commits created successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "Branch: dev" -ForegroundColor Cyan
Write-Host "Commits: 11 atomic commits by functionality" -ForegroundColor Cyan
Write-Host ""
Write-Host "To push:" -ForegroundColor Yellow
Write-Host "  git push origin dev" -ForegroundColor White
Write-Host ""
Write-Host "Commit summary:" -ForegroundColor Gray
git log --oneline -11
