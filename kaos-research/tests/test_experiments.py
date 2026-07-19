"""
Tests for the three experiment scripts:

- ``experiments/graphrag/experiment.py``  — Microsoft GraphRAG
- ``experiments/mem0/experiment.py``      — Mem0 persistent memory
- ``experiments/airllm/experiment.py``    — AirLLM layer-wise inference

All external library imports (``graphrag``, ``mem0``, ``airllm``) are mocked
so tests never need GPU, network, or installed third-party packages.
File I/O is redirected to ``tmp_path`` to prevent side effects.
"""

import json
from unittest import mock

import pytest

# ===================================================================
# GRAPHRAG EXPERIMENT
# ===================================================================

class TestGraphRAGCreateDataset:
    """``create_dataset()`` — creates the benchmark question set."""

    def test_creates_json_with_five_questions(self, graphrag_experiment, tmp_path):
        """The dataset file must contain exactly 5 benchmark questions."""
        graphrag_experiment.DATASET = tmp_path

        result_path = graphrag_experiment.create_dataset()

        assert result_path == tmp_path / "kaos_questions.json"
        assert result_path.exists()

        with open(result_path) as f:
            questions = json.load(f)

        assert len(questions) == 5
        assert questions[0]["id"] == "q1"
        assert questions[0]["type"] == "code_structure"
        assert questions[4]["id"] == "q5"

    def test_questions_have_required_fields(self, graphrag_experiment, tmp_path):
        """Each question must have id, question, expected_answer, and type."""
        graphrag_experiment.DATASET = tmp_path

        result_path = graphrag_experiment.create_dataset()
        with open(result_path) as f:
            questions = json.load(f)

        for q in questions:
            assert "id" in q
            assert "question" in q
            assert "expected_answer" in q
            assert "type" in q


class TestGraphRAGIndex:
    """``test_graphrag_index()`` — indexing phase."""

    def test_returns_not_installed_when_library_missing(
        self, graphrag_experiment, tmp_path,
    ):
        """Gracefully report ``not_installed`` when ``graphrag`` is absent."""
        graphrag_experiment.RESULTS = tmp_path / "results.json"

        result = graphrag_experiment.test_graphrag_index()

        assert result["status"] == "not_installed"
        assert "error" in result
        assert "graphrag" in result["error"].lower()

    def test_indexes_successfully_with_mock_library(
        self, graphrag_experiment, tmp_path,
    ):
        """Return a measured index time when ``graphrag`` is available."""
        graphrag_experiment.RESULTS = tmp_path / "results.json"

        mock_graphrag = mock.MagicMock()
        with mock.patch.dict("sys.modules", {"graphrag": mock_graphrag}):
            result = graphrag_experiment.test_graphrag_index()

        assert result["framework"] == "graphrag"
        assert result["status"] in ("indexed", "slow")
        assert "index_time_ms" in result


class TestGraphRAGQuery:
    """``test_graphrag_query()`` — multi-hop querying phase."""

    def test_creates_dataset_if_missing(self, graphrag_experiment, tmp_path):
        """When the dataset file does not exist it is created first."""
        graphrag_experiment.DATASET = tmp_path
        graphrag_experiment.RESULTS = tmp_path / "results.json"

        # The dataset file does NOT exist yet; query should trigger creation
        mock_graphrag = mock.MagicMock()
        mock_query = mock.MagicMock()
        mock_graphrag.query = mock_query

        with mock.patch.dict("sys.modules", {"graphrag": mock_graphrag}):
            graphrag_experiment.test_graphrag_query()

        # Dataset should now exist
        assert (tmp_path / "kaos_questions.json").exists()

    def test_handles_import_error_gracefully(
        self, graphrag_experiment, tmp_path,
    ):
        """Return a result dict with error info when graphrag is missing."""
        graphrag_experiment.DATASET = tmp_path
        graphrag_experiment.RESULTS = tmp_path / "results.json"

        # Pre-create dataset so we reach the import line
        graphrag_experiment.create_dataset()

        result = graphrag_experiment.test_graphrag_query()

        assert "error" in result
        assert "graphrag" in result["error"].lower()


# ===================================================================
# MEM0 EXPERIMENT
# ===================================================================

class TestMem0Basic:
    """``test_mem0_basic()`` — store, retrieve and cross-session memory."""

    def test_returns_not_installed_when_library_missing(
        self, mem0_experiment, tmp_path,
    ):
        """Gracefully report a skipped import when ``mem0`` is absent."""
        mem0_experiment.RESULTS = tmp_path / "results.json"

        result = mem0_experiment.test_mem0_basic()

        assert "error" in result
        assert "mem0" in result["error"].lower()
        # Should have at least the skipped import test
        assert len(result["tests"]) >= 1
        assert result["tests"][0]["status"] in ("skip", "error")

    def test_all_tests_pass_with_mock_library(
        self, mem0_experiment, tmp_path,
    ):
        """Execute all three memory tests successfully when mem0 is mocked."""
        mem0_experiment.RESULTS = tmp_path / "results.json"

        # Build a mock Memory that returns results for search queries
        mock_memory_instance = mock.MagicMock()
        mock_memory_instance.add.return_value = None
        mock_memory_instance.search.return_value = [{"text": "result"}]  # non-empty

        mock_mem0 = mock.MagicMock()
        mock_mem0.Memory.return_value = mock_memory_instance

        with mock.patch.dict("sys.modules", {"mem0": mock_mem0}):
            result = mem0_experiment.test_mem0_basic()

        assert "error" not in result, (
            f"Unexpected error: {result.get('error')}"
        )
        assert len(result["tests"]) == 3
        for test in result["tests"]:
            assert test["status"] == "pass", (
                f"Test '{test['name']}' did not pass: {test}"
            )

        # Verify summary counts
        assert result["summary"]["passed"] == 3
        assert result["summary"]["total"] == 3


class TestMem0Performance:
    """``test_mem0_performance()`` — benchmark with 100 entries."""

    def test_returns_error_when_library_missing(
        self, mem0_experiment, tmp_path,
    ):
        """Gracefully report an error when ``mem0`` is not installed."""
        mem0_experiment.RESULTS = tmp_path / "results.json"

        result = mem0_experiment.test_mem0_performance()

        assert "error" in result
        assert "mem0" in result["error"].lower()

    def test_benchmark_runs_with_mock_library(
        self, mem0_experiment, tmp_path,
    ):
        """Collect timing metrics for 100 entries when mem0 is mocked."""
        mem0_experiment.RESULTS = tmp_path / "results.json"

        mock_memory_instance = mock.MagicMock()
        mock_memory_instance.add.return_value = None
        mock_memory_instance.search.return_value = [{"text": "hit"}] * 10

        mock_mem0 = mock.MagicMock()
        mock_mem0.Memory.return_value = mock_memory_instance

        with mock.patch.dict("sys.modules", {"mem0": mock_mem0}):
            result = mem0_experiment.test_mem0_performance()

        assert "error" not in result, (
            f"Unexpected error: {result.get('error')}"
        )
        assert "add_100_entries_ms" in result
        assert "add_per_entry_ms" in result
        assert "search_time_ms" in result
        assert "search_results" in result
        assert result["search_results"] == 10

        # Memory.add should have been called 100 times
        assert mock_memory_instance.add.call_count == 100


# ===================================================================
# AIRLLM EXPERIMENT
# ===================================================================

class TestAirLLMLoading:
    """``test_airllm_loading()`` — model import, loading and inference."""

    def test_returns_not_installed_when_library_missing(
        self, airllm_experiment, tmp_path,
    ):
        """Gracefully report ``import_status == 'not_installed'``."""
        airllm_experiment.RESULTS = tmp_path / "results.json"

        result = airllm_experiment.test_airllm_loading()

        assert result.get("import_status") == "not_installed"
        assert "error" in result
        assert "airllm" in result["error"].lower()


class TestAirLLMProviderIntegration:
    """``test_airllm_provider_integration()`` — K.A.O.S adapter."""

    def test_returns_false_when_provider_missing(
        self, airllm_experiment, tmp_path,
    ):
        """Gracefully report ``provider_loaded == False`` on ImportError."""
        airllm_experiment.RESULTS = tmp_path / "results.json"

        result = airllm_experiment.test_airllm_provider_integration()

        assert result.get("provider_loaded") is False
        assert "error" in result

    def test_provider_loads_successfully_with_mock(
        self, airllm_experiment, tmp_path,
    ):
        """Return provider metadata when the adapter module is mocked."""
        airllm_experiment.RESULTS = tmp_path / "results.json"

        # Mock the K.A.O.S provider module
        mock_provider = mock.MagicMock()
        mock_provider.AirLLMProvider.return_value = mock.MagicMock(
            provider_name="airllm",
            model_name="test-model",
        )

        with mock.patch.dict(
            "sys.modules",
            {"app.llm.providers.airllm_provider": mock_provider},
        ):
            result = airllm_experiment.test_airllm_provider_integration()

        assert result.get("provider_loaded") is True
        assert result.get("provider_name") == "airllm"
        assert result.get("model_name") == "test-model"
        assert "error" not in result


# ===================================================================
# CROSS-CUTTING: result file output
# ===================================================================

class TestResultFileOutput:
    """Verify that each experiment writes its result file correctly."""

    def test_graphrag_index_writes_results_json(self, graphrag_experiment, tmp_path):
        """``test_graphrag_index()`` writes JSON to the configured RESULTS path."""
        dest = tmp_path / "results.json"
        graphrag_experiment.RESULTS = dest

        graphrag_experiment.test_graphrag_index()

        assert dest.exists(), "RESULTS file was not written"
        with open(dest) as f:
            data = json.load(f)
        assert "hypothesis" in data
        assert data["framework"] == "graphrag"

    def test_mem0_basic_writes_results_json(self, mem0_experiment, tmp_path):
        """``test_mem0_basic()`` writes JSON to the configured RESULTS path."""
        dest = tmp_path / "results.json"
        mem0_experiment.RESULTS = dest

        mem0_experiment.test_mem0_basic()

        assert dest.exists(), "RESULTS file was not written"
        with open(dest) as f:
            data = json.load(f)
        assert data["framework"] == "mem0"
        assert "hypothesis" in data

    def test_airllm_loading_writes_results_json(self, airllm_experiment, tmp_path):
        """``test_airllm_loading()`` writes JSON to the configured RESULTS path."""
        dest = tmp_path / "results.json"
        airllm_experiment.RESULTS = dest

        airllm_experiment.test_airllm_loading()

        assert dest.exists(), "RESULTS file was not written"
        with open(dest) as f:
            data = json.load(f)
        assert data["framework"] == "airllm"
        assert "hypothesis" in data
