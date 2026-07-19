"""
Shared fixtures and helpers for KAOS Research tests.

Loads each source module via importlib so tests can exercise the actual
functions without relying on package-level imports.  All four experiment
files are standalone scripts (not packages), so ``import`` would fail
without this loader.
"""

import importlib.util
from pathlib import Path

import pytest

# Root of kaos-research/  (parent of tests/)
RESEARCH_ROOT = Path(__file__).resolve().parent.parent


# ---------------------------------------------------------------------------
# Internal helper
# ---------------------------------------------------------------------------

def _load_source_module(name: str, rel_path: str):
    """Load a Python source file as a module by its filesystem path.

    Parameters
    ----------
    name : str
        Dotted name used to register the module in ``sys.modules``.
    rel_path : str
        Relative path from ``kaos-research/`` to the source file
        (e.g. ``"technology-observatory/observatory.py"``).

    Returns
    -------
    module
        The executed module object.
    """
    filepath = (RESEARCH_ROOT / rel_path).resolve()
    spec = importlib.util.spec_from_file_location(name, filepath)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {filepath}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Module-level fixtures  (one per source file)
# ---------------------------------------------------------------------------

@pytest.fixture
def observatory():
    """Return the loaded ``technology-observatory/observatory.py`` module."""
    return _load_source_module(
        "kaos_observatory",
        "technology-observatory/observatory.py",
    )


@pytest.fixture
def graphrag_experiment():
    """Return the loaded ``experiments/graphrag/experiment.py`` module."""
    return _load_source_module(
        "kaos_graphrag_experiment",
        "experiments/graphrag/experiment.py",
    )


@pytest.fixture
def mem0_experiment():
    """Return the loaded ``experiments/mem0/experiment.py`` module."""
    return _load_source_module(
        "kaos_mem0_experiment",
        "experiments/mem0/experiment.py",
    )


@pytest.fixture
def airllm_experiment():
    """Return the loaded ``experiments/airllm/experiment.py`` module."""
    return _load_source_module(
        "kaos_airllm_experiment",
        "experiments/airllm/experiment.py",
    )
