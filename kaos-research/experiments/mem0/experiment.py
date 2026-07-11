"""
Mem0 Experiment — Persistent User/Agent Memory (Hypothesis H2)

Tests Mem0's ability to store and retrieve user preferences across sessions.
Uses an isolated virtual environment to avoid polluting the main project.

Run:
    cd kaos-research/experiments/mem0
    python -m venv .venv
    .venv\Scripts\activate
    pip install mem0ai
    python experiment.py

Expected: Memory retrieval < 50ms, profile consistency across sessions.
"""

import json
import time
from pathlib import Path

RESULTS = Path(__file__).parent / "results.json"


def test_mem0_basic():
    """Test basic Mem0 memory storage and retrieval."""
    results = {"hypothesis": "H2", "framework": "mem0", "tests": []}

    try:
        from mem0 import Memory

        mem = Memory()

        # Test 1: Store user preference
        t0 = time.time()
        mem.add("User prefers dark mode and 24-hour time format.", user_id="test_user")
        store_time = (time.time() - t0) * 1000
        results["tests"].append({
            "name": "store_preference",
            "status": "pass",
            "latency_ms": round(store_time, 2),
        })

        # Test 2: Retrieve preference
        t0 = time.time()
        results_query = mem.search("dark mode preferences", user_id="test_user")
        query_time = (time.time() - t0) * 1000
        results["tests"].append({
            "name": "retrieve_preference",
            "status": "pass" if len(results_query) > 0 else "fail",
            "latency_ms": round(query_time, 2),
            "matches": len(results_query),
        })

        # Test 3: Cross-session memory (simulated)
        mem2 = Memory()
        t0 = time.time()
        results_query2 = mem2.search("time format", user_id="test_user")
        cross_session_time = (time.time() - t0) * 1000
        results["tests"].append({
            "name": "cross_session_memory",
            "status": "pass" if len(results_query2) > 0 else "fail",
            "latency_ms": round(cross_session_time, 2),
            "matches": len(results_query2),
        })

        results["summary"] = {
            "passed": sum(1 for t in results["tests"] if t["status"] == "pass"),
            "total": len(results["tests"]),
        }

    except ImportError:
        results["error"] = "mem0ai not installed. Run: pip install mem0ai"
        results["tests"] = [{"name": "import", "status": "skip", "reason": "not installed"}]
    except Exception as e:
        results["error"] = str(e)
        results["tests"] = [{"name": "general", "status": "error", "reason": str(e)}]

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS, "w") as f:
        json.dump(results, f, indent=2)

    print(json.dumps(results, indent=2))
    return results


def test_mem0_performance():
    """Benchmark Mem0 with 100 entries."""
    results = {"hypothesis": "H2", "framework": "mem0", "benchmark": "performance"}

    try:
        from mem0 import Memory
        mem = Memory()

        # Add 100 entries
        t0 = time.time()
        for i in range(100):
            mem.add(f"K.A.O.S task {i}: Process document batch {i}", user_id="bench_user")
        add_time = (time.time() - t0) * 1000
        results["add_100_entries_ms"] = round(add_time, 2)
        results["add_per_entry_ms"] = round(add_time / 100, 2)

        # Search
        t0 = time.time()
        hits = mem.search("document batch", user_id="bench_user", limit=10)
        search_time = (time.time() - t0) * 1000
        results["search_time_ms"] = round(search_time, 2)
        results["search_results"] = len(hits)

        results["passed"] = search_time < 100  # Target: < 100ms

    except ImportError:
        results["error"] = "mem0ai not installed"
    except Exception as e:
        results["error"] = str(e)

    with open(RESULTS.parent / "performance.json", "w") as f:
        json.dump(results, f, indent=2)

    return results


if __name__ == "__main__":
    test_mem0_basic()
    test_mem0_performance()
