# K.A.O.S Architectural Evolution Laboratory

> **Purpose:** Isolated environment for evidence-driven technology evaluation.
> **Principle:** Never install frameworks in the main system without evidence.
> **Method:** Capability First → Hypotheses → Research → Benchmarks → ADRs → Adapt (if valid).

---

## Rules

1. **No framework touches the K.A.O.S main codebase** until an ADR is approved.
2. **Every experiment must be reproducible** — include script, dataset, and results.
3. **Hypotheses before installation** — never `pip install` without a stated hypothesis.
4. **All decisions require evidence** — Graphify queries, benchmarks, or experiments.
5. **Prefer composition over replacement** — adapters wrap frameworks; never rewrite.
6. **Technology Observatory runs continuously** — not a one-time scan.
7. **Document everything** — every query, every benchmark run, every decision rationale.

---

## Scientific Method (10 Steps)

```
1. Inventory     → Map current state & capabilities (Graphify + Evidence Engine)
2. Identify      → Gaps, overlaps, pain points (with evidence)
3. Formulate     → Hypothesis: "Framework X can solve capability Y better than Z"
4. Research      → README + Issues + Papers + Benchmarks + Community
5. Compare       → Capability matrix (not popularity matrix)
6. Experiment    → Run in kaos-research/experiments/, controlled dataset
7. Measure       → Performance, quality, cost, architectural impact
8. Validate      → Hypothesis confirmed or rejected (with evidence)
9. Decide        → ADR + Incremental plan + Rollback
10. Integrate    → Via adapters + ports. Never direct coupling.
```

---

## Directory Structure

```
kaos-research/
├── README.md                    ← This file
├── catalog/                     ← Knowledge Catalog
│   └── framework-catalog.json   ← All registered frameworks
├── experiments/                 ← Isolated experiments
│   ├── graphrag/
│   ├── graphiti/
│   ├── mem0/
│   ├── cognee/
│   ├── letta/
│   └── langgraph/
├── benchmarks/                  ← Functional benchmarks
│   ├── benchmark-plan.md
│   ├── datasets/
│   ├── scenarios/
│   └── results/
├── evidence/                    ← Collected evidence
│   ├── graphify-queries/
│   ├── research-notes/
│   └── decisions/
├── adrs/                        ← Architecture Decision Records
├── reports/                     ← Consolidated reports
├── evaluation/                  ← Scoring engine & metrics
└── technology-observatory/      ← Continuous tech monitoring
```

---

## Current Phase: State Audit + Hypothesis Formulation

Next deliverables:
1. State audit report (Graphify evidence)
2. Hypothesis list
3. Framework research dossiers
4. Capability comparison matrix
5. Technology Observatory MVP
6. Knowledge Catalog initial population
7. Research phase ADRs
