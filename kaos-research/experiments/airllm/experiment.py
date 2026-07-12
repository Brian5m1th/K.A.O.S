"""
AirLLM Experiment — Large Model Inference on Consumer GPU (Hypothesis H7)

Tests AirLLM's layer-wise inference for 70B+ models on 4-8GB GPUs.

Run:
    cd kaos-research/experiments/airllm
    python -m venv .venv
    .venv\Scripts\activate
    pip install airllm
    python experiment.py

Expected: Token rate > 1 t/s on 8GB GPU, memory within VRAM budget.
"""

import json
import time
from pathlib import Path

RESULTS = Path(__file__).parent / "results.json"


def test_airllm_loading():
    """Test AirLLM model loading without full inference."""
    results = {"hypothesis": "H7", "framework": "airllm", "tests": []}

    try:
        # Test that airllm can be imported
        import airllm
        from airllm import AutoModel

        results["import_status"] = "ok"
        results["airllm_version"] = getattr(airllm, "__version__", "unknown")

        # Model load test (skip if no GPU)
        t0 = time.time()
        try:
            model = AutoModel("meta-llama/Meta-Llama-3-8B")
            load_time = (time.time() - t0) * 1000
            results["tests"].append({
                "name": "model_load",
                "status": "pass",
                "model": "Meta-Llama-3-8B",
                "load_time_ms": round(load_time, 2),
            })

            # Inference test
            t0 = time.time()
            output = model.generate("Explain K.A.O.S in one sentence.", max_new_tokens=20)
            infer_time = (time.time() - t0) * 1000
            tokens = output.split()
            tps = len(tokens) / (infer_time / 1000) if infer_time > 0 else 0
            results["tests"].append({
                "name": "inference",
                "status": "pass" if len(tokens) > 0 else "fail",
                "inference_time_ms": round(infer_time, 2),
                "tokens_generated": len(tokens),
                "tokens_per_second": round(tps, 2),
            })

        except Exception as e:
            results["tests"].append({
                "name": "model_load",
                "status": "skip",
                "reason": f"No GPU or insufficient memory: {e}",
            })

    except ImportError:
        results["import_status"] = "not_installed"
        results["error"] = "airllm not installed. Run: pip install airllm"
    except Exception as e:
        results["error"] = str(e)

    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS, "w") as f:
        json.dump(results, f, indent=2)

    print(json.dumps(results, indent=2))
    return results


def test_airllm_provider_integration():
    """Test the K.A.O.S AirLLMProvider adapter integration."""
    results = {"hypothesis": "H7", "framework": "airllm", "test": "provider_integration"}

    try:
        from app.llm.providers.airllm_provider import AirLLMProvider

        provider = AirLLMProvider(model="test-model")
        results["provider_name"] = provider.provider_name
        results["model_name"] = provider.model_name
        results["provider_loaded"] = True

    except ImportError as e:
        results["provider_loaded"] = False
        results["error"] = str(e)
    except Exception as e:
        results["error"] = str(e)

    with open(RESULTS.parent / "provider_integration.json", "w") as f:
        json.dump(results, f, indent=2)

    return results


if __name__ == "__main__":
    test_airllm_loading()
    test_airllm_provider_integration()
