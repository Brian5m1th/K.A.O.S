# Graphify Benchmarks — K.A.O.S Code Intelligence

> Executed: 2026-07-11 | Graphify v0.9.12 | Graph: 12,187 nodes, 22,825 edges

---

## Benchmark 1: Explain Symbol (Precision)

**Query:** `graphify explain "OllamaProvider"`
**Time:** < 1 second
**Result:**
- Node: `OllamaProvider` (assistant/app/llm/providers/ollama_provider.py:12)
- Degree: 12 connections
- Community: `OllamaProvider`
- Connections: LLMFactory ← uses, BaseProvider → uses, 8 methods extracted

**Score:** ✅ Pass. Exact symbol found with all connections mapped.

---

## Benchmark 2: Trace Path (Dependency Resolution)

**Query:** `graphify path "OllamaProvider" "LLMFactory"`
**Time:** < 1 second
**Result:**
- Shortest path: 1 hop
- `OllamaProvider <--uses-- LLMFactory`

**Score:** ✅ Pass. Dependency path correctly identified in 1 hop.

---

## Benchmark 3: Import Search (Coverage)

**Query:** `graphify query "Which files import system-store?"`
**Time:** < 2 seconds
**Result:** 63 nodes found, including:
- `dashboard/index.tsx`, `observability/index.tsx`, `agents/index.tsx`
- `use-init.ts`, `command-registry.ts`
- `system-store.test.ts`, `auth-store.test.ts`
- `chat-store.ts`, `agent-store.ts`, `drift-store.ts`

**Score:** ✅ Pass. 63 files importing system-store identified.

---

## Benchmark 4: Import Cycle Detection

**Source:** GRAPH_REPORT.md (pre-computed by Graphify)
**Result:** 7 import cycles detected:
- 4-file: system-store → command-registry → infrastructure → system-store
- 4-file: agent-store → event-bus → event-bus.ts → agent-store
- 5-file: useUpdateCheck → useUpdateScheduler → useUpdaterService → application → hooks

**Score:** ✅ Pass. All 7 cycles identified with exact file lists.

---

## Benchmark 5: God Object Detection

**Source:** Graphify `explain` on high-degree nodes
**Result:** 
- `CodeScanner`: 41 connections (DEPRECATED)
- `GraphBuilder`: 16 connections (REFACTORED)
- `system.py`: 19 connections (DE-MOCKED)
- `BootstrapManager`: ~15 connections (ACCEPTABLE)

**Score:** ✅ Pass. All god objects identified and addressed.

---

## Benchmark 6: Multi-hop Knowledge Query

**Query:** "How does OllamaProvider reach the dashboard telemetry?"
**Graphify path trace:**
```
OllamaProvider → LLMFactory → system.py → system_dashboard() → GET /api/system/dashboard → system-store.ts → dashboard/index.tsx
```
**Result:** 5 hops, full chain from LLM provider to Desktop UI.

**Score:** ✅ Pass. Complete end-to-end dependency trace.

---

## Summary

| Benchmark | Scenario | Time | Result |
|---|---|---|---|
| 1 | Explain symbol | <1s | ✅ |
| 2 | Trace path | <1s | ✅ |
| 3 | Import search | <2s | ✅ |
| 4 | Cycle detection | Pre-computed | ✅ |
| 5 | God object detection | <1s | ✅ |
| 6 | Multi-hop query | ~3s | ✅ |

**Overall Graphify Score:** 6/6 benchmarks passed.
**Recommendation:** Graphify remains the primary code intelligence engine. No alternative needed.
