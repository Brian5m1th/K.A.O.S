import pytest
from unittest.mock import MagicMock
from app.runtime.runtime_selector import RuntimeSelector
from app.runtime.runtime_layer import AIRuntime


class TestRuntimeSelector:
    def test_select_by_objectives(self) -> None:
        selector = RuntimeSelector()

        # Mock three test runtimes with different capabilities
        local_run = MagicMock(spec=AIRuntime)
        local_run.name = "local-model"
        local_run.type = "local"
        local_run.capabilities = {
            "offline": True,
            "reasoning": False,
            "cost": 0.0,
            "latency": 3.0,
            "context_window": 8192,
        }

        cloud_run = MagicMock(spec=AIRuntime)
        cloud_run.name = "cloud-model"
        cloud_run.type = "cloud"
        cloud_run.capabilities = {
            "offline": False,
            "reasoning": True,
            "cost": 0.005,
            "latency": 1.5,
            "context_window": 128000,
        }

        # Override Selector's runtimes with our isolated mocks
        selector._runtimes = [local_run, cloud_run]

        # Test selecting offline/privacidade -> should select local
        run_offline = selector.select("privacidade")
        assert run_offline.type == "local"

        # Test selecting raciocinio/qualidade -> should select cloud
        run_quality = selector.select("raciocinio")
        assert run_quality.type == "cloud"
