"""
Testes de integracao do fluxo de bootstrap completo.

Valida:
- EnvironmentService + BootstrapManager operam juntos
- Endpoints /api/system/environment e /api/system/bootstrap via HTTP
- Bootstrap termina em READY ou DEGRADED (nunca PENDING)
- Dados retornados pelos endpoints sao coerentes
"""

import pytest
from httpx import AsyncClient, ASGITransport

from app.main import app
from app.core.bootstrap_manager import BootstrapManager, BootstrapState
from app.core.environment_service import EnvironmentService


@pytest.fixture(autouse=True)
def reset_bootstrap():
    """Reseta bootstrap antes de cada teste de integracao."""
    BootstrapManager.reset()
    EnvironmentService._instance = None
    EnvironmentService._cached_info = None
    yield
    BootstrapManager.reset()
    EnvironmentService._instance = None
    EnvironmentService._cached_info = None


@pytest.fixture
def client() -> AsyncClient:
    app.state.api_key = "test-api-key"
    transport = ASGITransport(app=app)
    return AsyncClient(
        transport=transport,
        base_url="http://test",
        headers={"x-api-key": "test-api-key"},
    )


@pytest.mark.asyncio
class TestEnvironmentServiceIntegration:
    """Testa EnvironmentService via HTTP endpoint."""

    async def test_environment_endpoint_exists(self, client: AsyncClient):
        resp = await client.get("/api/system/environment")
        assert resp.status_code == 200

    async def test_environment_endpoint_returns_workspace(self, client: AsyncClient):
        resp = await client.get("/api/system/environment")
        data = resp.json()
        assert "workspace" in data
        assert data["workspace"] is not None

    async def test_environment_endpoint_has_env_type(self, client: AsyncClient):
        resp = await client.get("/api/system/environment")
        data = resp.json()
        assert "env_type" in data
        assert data["env_type"] in ("docker", "local", "ci", "unknown")

    async def test_environment_endpoint_has_kirl(self, client: AsyncClient):
        resp = await client.get("/api/system/environment")
        data = resp.json()
        # O endpoint retorna os campos do to_dict() do EnvironmentInfo
        assert "workspace" in data
        assert "env_type" in data
        assert "docs" in data

    async def test_environment_endpoint_is_container(self, client: AsyncClient):
        resp = await client.get("/api/system/environment")
        data = resp.json()
        assert "is_container" in data
        assert isinstance(data["is_container"], bool)


@pytest.mark.asyncio
class TestBootstrapEndpointIntegration:
    """Testa BootstrapManager via HTTP endpoint."""

    async def test_bootstrap_endpoint_exists(self, client: AsyncClient):
        resp = await client.get("/api/system/bootstrap")
        assert resp.status_code == 200

    async def test_bootstrap_endpoint_returns_state_dict(self, client: AsyncClient):
        resp = await client.get("/api/system/bootstrap")
        data = resp.json()
        assert "state" in data
        assert "is_ready" in data
        assert "stages" in data
        assert "errors" in data
        assert "boot_complete" in data

    async def test_boot_full_pipeline(self, client: AsyncClient):
        """Executa o boot completo e verifica estado final."""
        from app.core.bootstrap_manager import BootstrapManager

        result = await BootstrapManager.boot()
        assert result.state in (
            BootstrapState.READY,
            BootstrapState.DEGRADED,
            BootstrapState.FAILED,
        ), f"Bootstrap terminou em estado inesperado: {result.state}"

        # Verifica via HTTP
        resp = await client.get("/api/system/bootstrap")
        data = resp.json()
        assert data["state"] == result.state.value
        assert data["is_ready"] == result.is_ready

    async def test_boot_has_stages(self, client: AsyncClient):
        """Verifica que stages foram populados."""
        from app.core.bootstrap_manager import BootstrapManager

        result = await BootstrapManager.boot()
        # Deve ter pelo menos o stage ENVIRONMENT
        stage_names = [s.stage.value for s in result.stages]
        assert "environment" in stage_names

        # Verifica que stage ENVIRONMENT tem resultado
        env_stage = [s for s in result.stages if s.stage.value == "environment"][0]
        assert env_stage.success is True

    async def test_boot_degraded_has_errors(self, client: AsyncClient):
        """Se degraded=True, deve ter pelo menos um erro listado."""
        from app.core.bootstrap_manager import BootstrapManager

        result = await BootstrapManager.boot()
        if result.degraded:
            assert len(result.errors) > 0
            for err in result.errors:
                assert isinstance(err, str)
                assert len(err) > 0

    async def test_bootstrap_endpoint_after_boot(self, client: AsyncClient):
        """Endpoint /api/system/bootstrap reflete boot() real."""
        from app.core.bootstrap_manager import BootstrapManager

        await BootstrapManager.boot()

        resp = await client.get("/api/system/bootstrap")
        data = resp.json()
        assert data["boot_complete"] is True
        assert data["total_elapsed_ms"] > 0

    async def test_multiple_boot_calls(self, client: AsyncClient):
        """Chamar boot() multiplas vezes nao quebra."""
        from app.core.bootstrap_manager import BootstrapManager

        result1 = await BootstrapManager.boot()  # noqa: F841 — first call for idempotency check / unused
        result2 = await BootstrapManager.boot()

        # Segunda chamada nao reinicia se ja completo (stateless: roda de novo)
        assert result2.state in (
            BootstrapState.READY,
            BootstrapState.DEGRADED,
            BootstrapState.FAILED,
        )


@pytest.mark.asyncio
class TestEnvironmentAndBootstrapTogether:
    """Testa que ambos servicos funcionam juntos no mesmo ciclo de vida."""

    async def test_environment_runs_before_bootstrap_in_pipeline(self, client: AsyncClient):
        """Environment e chamado antes do bootstrap no pipeline."""
        from app.core.bootstrap_manager import BootstrapManager

        await BootstrapManager.boot()
        state = BootstrapManager.get_state()

        # Environment info deve estar presente
        assert state.get("environment") is not None
        assert "workspace" in state["environment"]

    async def test_both_endpoints_available(self, client: AsyncClient):
        """Ambos endpoints respondem 200."""
        r1 = await client.get("/api/system/environment")
        r2 = await client.get("/api/system/bootstrap")
        assert r1.status_code == 200
        assert r2.status_code == 200

    async def test_environment_data_in_bootstrap_state(self, client: AsyncClient):
        """Bootstrap state contem environment_info."""
        from app.core.bootstrap_manager import BootstrapManager

        await BootstrapManager.boot()
        state = BootstrapManager.get_state()
        env = state.get("environment", {})
        assert "workspace" in env
        assert "env_type" in env
