"""
Contract validation tests for K.A.O.S system dashboard endpoint.

Ensures /api/system/dashboard returns correct schema and values
conforming to Constitution Article I: Zero fabricated data.
"""

import pytest
from unittest.mock import AsyncMock, patch


class TestDashboardContract:
    """Validate /api/system/dashboard response schema."""

    @pytest.mark.asyncio
    async def test_dashboard_returns_required_fields(self):
        """Dashboard must include services, runtime, metrics, costs, dlq, alerts."""
        from app.api.system import system_dashboard

        # Mock all sub-resolvers to return minimal valid data
        with (
            patch(
                "app.api.system._get_services_status", new_callable=AsyncMock
            ) as mock_svc,
            patch(
                "app.api.system._get_runtime_info", new_callable=AsyncMock
            ) as mock_rt,
            patch("app.api.system._get_metrics_data", new_callable=AsyncMock) as mock_m,
            patch("app.api.system._get_costs_data", new_callable=AsyncMock) as mock_c,
            patch("app.api.system._get_dlq_data", new_callable=AsyncMock) as mock_d,
            patch("app.api.system._get_alerts_data", new_callable=AsyncMock) as mock_a,
        ):
            mock_svc.return_value = {"backend": True, "postgres": True, "qdrant": True}
            mock_rt.return_value = {
                "activeModel": "qwen3",
                "latency": 42.0,
                "cpu": 10.0,
                "ram": {"used": 2.0, "total": 16.0},
                "vram": {"used": None, "total": None},
            }
            mock_m.return_value = {"vectorCount": 100, "tokenRate": 25.0}
            mock_c.return_value = {"total_usd": 1.50, "total_tokens": 5000}
            mock_d.return_value = {"failed": [], "count": 0}
            mock_a.return_value = {"notifications": []}

            result = await system_dashboard()

        assert "services" in result
        assert "runtime" in result
        assert "metrics" in result
        assert "costs" in result
        assert "dlq" in result
        assert "alerts" in result
        assert result["status"] == "ready"

    @pytest.mark.asyncio
    async def test_dashboard_returns_null_on_failure_not_fabricated(self):
        """When sub-resolver fails, dashboard must return None, not fabricated zeros."""
        from app.api.system import system_dashboard

        with (
            patch(
                "app.api.system._get_services_status",
                side_effect=RuntimeError("DB down"),
            ),
            patch(
                "app.api.system._get_runtime_info",
                side_effect=RuntimeError("CPU error"),
            ),
            patch(
                "app.api.system._get_metrics_data",
                side_effect=RuntimeError("Qdrant down"),
            ),
            patch("app.api.system._get_costs_data", new_callable=AsyncMock) as mock_c,
            patch("app.api.system._get_dlq_data", new_callable=AsyncMock) as mock_d,
            patch("app.api.system._get_alerts_data", new_callable=AsyncMock) as mock_a,
        ):
            mock_c.return_value = {"total_usd": 0.0, "total_tokens": 0}
            mock_d.return_value = {"failed": [], "count": 0}
            mock_a.return_value = {"notifications": []}

            result = await system_dashboard()

        # Failed resolvers must return None for values, not fabricated data
        assert result["services"]["postgres"] is None
        assert result["services"]["qdrant"] is None
        assert result["runtime"]["cpu"] is None
        assert result["runtime"]["activeModel"] is None
        assert result["metrics"]["vectorCount"] is None
        # Must include error information
        assert "error" in result["services"]

    @pytest.mark.asyncio
    async def test_dashboard_services_structure(self):
        """Services object must have all expected keys."""
        from app.api.system import system_dashboard

        with (
            patch(
                "app.api.system._get_services_status", new_callable=AsyncMock
            ) as mock_svc,
            patch(
                "app.api.system._get_runtime_info", new_callable=AsyncMock
            ) as mock_rt,
            patch("app.api.system._get_metrics_data", new_callable=AsyncMock) as mock_m,
            patch("app.api.system._get_costs_data", new_callable=AsyncMock) as mock_c,
            patch("app.api.system._get_dlq_data", new_callable=AsyncMock) as mock_d,
            patch("app.api.system._get_alerts_data", new_callable=AsyncMock) as mock_a,
        ):
            mock_svc.return_value = {
                "backend": True,
                "postgres": True,
                "qdrant": True,
                "ollama": True,
                "n8n": False,
                "grafana": False,
                "prometheus": False,
            }
            mock_rt.return_value = {
                "activeModel": "test",
                "latency": 0,
                "cpu": 0,
                "ram": {"used": 0, "total": 0},
                "vram": {"used": None, "total": None},
            }
            mock_m.return_value = {"vectorCount": 0, "tokenRate": 0}
            mock_c.return_value = {"total_usd": 0, "total_tokens": 0}
            mock_d.return_value = {"failed": [], "count": 0}
            mock_a.return_value = {"notifications": []}

            result = await system_dashboard()

        svc = result["services"]
        expected_keys = [
            "backend",
            "postgres",
            "qdrant",
            "ollama",
            "n8n",
            "grafana",
            "prometheus",
        ]
        for key in expected_keys:
            assert key in svc, f"Missing key '{key}' in services"

    @pytest.mark.asyncio
    async def test_dashboard_runtime_vram_null_on_cpu_mode(self):
        """VRAM must be null when no GPU detected (Constitution Article I)."""
        from app.api.system import system_dashboard

        with (
            patch(
                "app.api.system._get_services_status", new_callable=AsyncMock
            ) as mock_svc,
            patch(
                "app.api.system._get_runtime_info", new_callable=AsyncMock
            ) as mock_rt,
            patch("app.api.system._get_metrics_data", new_callable=AsyncMock) as mock_m,
            patch("app.api.system._get_costs_data", new_callable=AsyncMock) as mock_c,
            patch("app.api.system._get_dlq_data", new_callable=AsyncMock) as mock_d,
            patch("app.api.system._get_alerts_data", new_callable=AsyncMock) as mock_a,
        ):
            mock_svc.return_value = {"backend": True}
            # Simulate CPU Mode: VRAM is null
            mock_rt.return_value = {
                "activeModel": "test",
                "latency": 0,
                "cpu": 5,
                "ram": {"used": 1.0, "total": 8.0},
                "vram": {"used": None, "total": None},
            }
            mock_m.return_value = {"vectorCount": 0, "tokenRate": 0}
            mock_c.return_value = {"total_usd": 0, "total_tokens": 0}
            mock_d.return_value = {"failed": [], "count": 0}
            mock_a.return_value = {"notifications": []}

            result = await system_dashboard()

        vram = result["runtime"]["vram"]
        assert vram["used"] is None, "VRAM used must be null in CPU mode"
        assert vram["total"] is None, "VRAM total must be null in CPU mode"


class TestReadinessContract:
    """Validate /api/system/readiness response schema."""

    @pytest.mark.asyncio
    async def test_readiness_returns_required_fields(self):
        """Readiness must include ready, degraded, message, services, vectors."""
        from app.api.system import system_readiness

        with (
            patch("app.api.system._check_postgres", new_callable=AsyncMock) as mock_pg,
            patch("app.api.system._check", new_callable=AsyncMock) as mock_check,
        ):
            mock_pg.return_value = True
            mock_check.return_value = True

            result = await system_readiness()

        assert "ready" in result
        assert "degraded" in result
        assert "message" in result
        assert "services" in result
        assert "vectors" in result
        assert "postgres" in result["services"]
        assert "qdrant" in result["services"]
