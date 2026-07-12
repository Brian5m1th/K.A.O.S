# ADR-003: Technology Observatory as Continuous Monitoring System

- **Status:** Accepted
- **Decision Owner:** KAOS Architect (System)
- **Review Date:** 2027-01-11 (6 months)
- **Date:** 2026-07-11

---

## Context

The K.A.O.S ecosystem evolves continuously: new framework versions, breaking changes, emerging alternatives, security advisories, and community shifts. Currently, technology decisions are made through one-time research with no systematic tracking.

## Decision

**A Technology Observatory will track all frameworks in the K.A.O.S Knowledge Catalog continuously** through:

1. GitHub repository monitoring (stars, forks, releases, issues)
2. PyPI version tracking (new releases, breaking changes)
3. License compliance checks
4. Security advisory monitoring
5. Community health metrics (maintainer activity, response time)

The Observatory runs weekly via scheduled script and produces JSON reports stored in `kaos-research/technology-observatory/reports/`.

## Evidence

- State Audit identified 5 frameworks to evaluate (GraphRAG, Mem0, Graphiti, Cognee, LangGraph)
- Knowledge Catalog has 9 registered frameworks with structured metadata
- Without continuous tracking, framework decisions become stale within weeks

## Implementation

```python
# technology-observatory/observatory.py
# Tracks 14 frameworks:
# Graphify, GraphRAG, Graphiti, Mem0, Cognee, Letta, LangGraph,
# Qdrant, AirLLM, LlamaIndex, DSPy, CrewAI, AutoGen, FalkorDB, Neo4j
```

Output: `reports/observatory-YYYY-MM-DD.json` + `reports/latest.json`

## Consequences

- **Positive:** Informed technology decisions, early warning on breaking changes, community health visibility
- **Negative:** Requires `gh` CLI auth for GitHub API, scheduled execution infrastructure
- **Mitigation:** Fallback to PyPI-only tracking without GitHub data

## Alternatives Considered

- **Manual periodic review:** Rejected — inconsistent, not scalable
- **Third-party dependency scanner (Dependabot):** Partial — only tracks Python packages, not GitHub health
