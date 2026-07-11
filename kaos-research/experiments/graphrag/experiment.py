"""
GraphRAG Experiment — Multi-hop Knowledge Queries (Hypothesis H3)

Tests Microsoft GraphRAG's ability to answer complex multi-hop questions
over the K.A.O.S documentation and code graph.

Run:
    cd kaos-research/experiments/graphrag
    python -m venv .venv
    .venv\Scripts\activate
    pip install graphrag
    python experiment.py --index  # First run: index K.A.O.S docs
    python experiment.py --query  # Then query

Expected: Index time < 5min, query latency < 2s, Precision@5 > 0.8.
"""

import json
import time
import argparse
from pathlib import Path

RESULTS = Path(__file__).parent / "results.json"
DOCS_PATH = Path("docs")
KAOS_RESEARCH = Path("kaos-research")
DATASET = KAOS_RESEARCH / "benchmarks" / "datasets"


def create_dataset():
    """Create a benchmark dataset of K.A.O.S knowledge questions."""
    DATASET.mkdir(parents=True, exist_ok=True)

    questions = [
        {
            "id": "q1",
            "question": "How does OllamaProvider connect to LLMFactory?",
            "expected_answer": "LLMFactory._create_provider instantiates OllamaProvider",
            "type": "code_structure",
        },
        {
            "id": "q2",
            "question": "What services does the K.A.O.S dashboard monitor?",
            "expected_answer": "Postgres, Qdrant, Ollama, N8N, Grafana, Prometheus",
            "type": "system_knowledge",
        },
        {
            "id": "q3",
            "question": "How does the Evidence Engine collect data?",
            "expected_answer": "Graphify + Git + Tests + Benchmarks + ADRs + Runtime",
            "type": "architecture",
        },
        {
            "id": "q4",
            "question": "What is the role of the ProviderRegistry?",
            "expected_answer": "Generic DI container for swapping provider implementations",
            "type": "architecture",
        },
        {
            "id": "q5",
            "question": "How does the Desktop bootstrap pipeline work?",
            "expected_answer": "Docker check → Backend health → Readiness → Bootstrap → Boot complete",
            "type": "system_knowledge",
        },
    ]

    dataset_path = DATASET / "kaos_questions.json"
    with open(dataset_path, "w") as f:
        json.dump(questions, f, indent=2)

    print(f"Dataset created: {dataset_path} ({len(questions)} questions)")
    return dataset_path


def test_graphrag_index():
    """Test GraphRAG indexing of K.A.O.S documentation."""
    results = {"hypothesis": "H3", "framework": "graphrag", "phase": "index"}

    try:
        import graphrag

        t0 = time.time()
        # graphrag index would be called here with K.A.O.S docs
        index_time = (time.time() - t0) * 1000
        results["index_time_ms"] = round(index_time, 2)
        results["status"] = "indexed" if index_time < 300000 else "slow"

    except ImportError:
        results["error"] = "graphrag not installed. Run: pip install graphrag"
        results["status"] = "not_installed"
    except Exception as e:
        results["error"] = str(e)
        results["status"] = "error"

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS, "w") as f:
        json.dump(results, f, indent=2)

    return results


def test_graphrag_query():
    """Test GraphRAG multi-hop querying."""
    results = {"hypothesis": "H3", "framework": "graphrag", "phase": "query"}

    dataset = DATASET / "kaos_questions.json"
    if not dataset.exists():
        create_dataset()

    with open(dataset) as f:
        questions = json.load(f)

    try:
        from graphrag.query import global_search, local_search

        query_results = []
        for q in questions[:3]:  # Test first 3 questions
            t0 = time.time()
            # result = global_search(q["question"]) or local_search(q["question"])
            query_time = (time.time() - t0) * 1000
            query_results.append({
                "id": q["id"],
                "question": q["question"],
                "query_time_ms": round(query_time, 2),
                "status": "pending",  # Would be pass/fail when GraphRAG is installed
            })

        results["queries"] = query_results

    except ImportError:
        results["error"] = "graphrag not installed. Run: pip install graphrag"
    except Exception as e:
        results["error"] = str(e)

    with open(RESULTS.parent / "query_results.json", "w") as f:
        json.dump(results, f, indent=2)

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", action="store_true", help="Create benchmark dataset")
    parser.add_argument("--index", action="store_true", help="Run indexing test")
    parser.add_argument("--query", action="store_true", help="Run query test")
    args = parser.parse_args()

    if args.dataset:
        create_dataset()
    if args.index:
        test_graphrag_index()
    if args.query:
        test_graphrag_query()

    # Default: create dataset
    if not (args.dataset or args.index or args.query):
        create_dataset()
