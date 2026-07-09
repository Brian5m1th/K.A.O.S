"""
Testes unitarios do BootstrapManager.

Valida:
- BootstrapState enum
- StageResult e BootstrapResult dataclasses
- get_state() antes/durante/depois do boot
- reset()
- _run_stage com timeout e erro
- Pipeline boot em modo offline (sem DB)
"""

import asyncio

import pytest

from app.core.bootstrap_manager import (
    BootstrapManager,
    BootstrapState,
    BootstrapStage,
    StageResult,
    BootstrapResult,
)


@pytest.fixture(autouse=True)
def reset_bootstrap():
    """Reseta o BootstrapManager antes de cada teste unitario."""
    BootstrapManager.reset()
    yield


class TestBootstrapState:
    def test_all_states_present(self):
        assert BootstrapState.PENDING.value == "pending"
        assert BootstrapState.ENVIRONMENT_DETECTING.value == "environment_detecting"
        assert BootstrapState.DOCKER_CHECKING.value == "docker_checking"
        assert BootstrapState.DATABASE_INITIALIZING.value == "database_initializing"
        assert BootstrapState.WORKSPACE_SCANNING.value == "workspace_scanning"
        assert BootstrapState.VAULT_INDEXING.value == "vault_indexing"
        assert (
            BootstrapState.KNOWLEDGE_GRAPH_BUILDING.value == "knowledge_graph_building"
        )
        assert (
            BootstrapState.ARCHITECTURE_GRAPH_BUILDING.value
            == "architecture_graph_building"
        )
        assert BootstrapState.AUDIT_SCANNING.value == "audit_scanning"
        assert BootstrapState.READY.value == "ready"
        assert BootstrapState.FAILED.value == "failed"
        assert BootstrapState.DEGRADED.value == "degraded"


class TestBootstrapStage:
    def test_all_stages_present(self):
        assert BootstrapStage.ENVIRONMENT.value == "environment"
        assert BootstrapStage.DOCKER.value == "docker"
        assert BootstrapStage.DATABASE.value == "database"
        assert BootstrapStage.WORKSPACE.value == "workspace"
        assert BootstrapStage.VAULT.value == "vault"
        assert BootstrapStage.KNOWLEDGE_GRAPH.value == "knowledge_graph"
        assert BootstrapStage.ARCHITECTURE_GRAPH.value == "architecture_graph"
        assert BootstrapStage.AUDIT.value == "audit"

    def test_total_stages(self):
        assert len(BootstrapStage) == 8


class TestStageResult:
    def test_default_values(self):
        result = StageResult(stage=BootstrapStage.ENVIRONMENT, success=True)
        assert result.elapsed_ms == 0.0
        assert result.error is None
        assert result.details == {}

    def test_label_property(self):
        result = StageResult(stage=BootstrapStage.DATABASE, success=False)
        assert result.label == "database"

    def test_with_error(self):
        result = StageResult(
            stage=BootstrapStage.VAULT,
            success=False,
            elapsed_ms=1500.5,
            error="Connection refused",
        )
        assert result.elapsed_ms == 1500.5
        assert "Connection refused" in str(result.error)

    def test_with_details(self):
        details = {"nodes": 10, "edges": 5}
        result = StageResult(
            stage=BootstrapStage.KNOWLEDGE_GRAPH,
            success=True,
            details=details,
        )
        assert result.details["nodes"] == 10


class TestBootstrapResult:
    def test_default_state_pending(self):
        result = BootstrapResult(state=BootstrapState.PENDING)
        assert result.state == BootstrapState.PENDING
        assert result.is_ready is False

    def test_ready_state(self):
        result = BootstrapResult(state=BootstrapState.READY)
        assert result.is_ready is True

    def test_degraded_is_also_ready(self):
        result = BootstrapResult(state=BootstrapState.DEGRADED)
        assert result.is_ready is True

    def test_started_at_isoformat(self):
        result = BootstrapResult(state=BootstrapState.PENDING)
        assert result.started_at  # nao vazio
        assert "T" in result.started_at  # ISO format

    def test_to_dict_keys(self):
        result = BootstrapResult(
            state=BootstrapState.READY,
            stages=[StageResult(stage=BootstrapStage.ENVIRONMENT, success=True)],
            errors=[],
            degraded=False,
        )
        d = result.to_dict()
        assert "state" in d
        assert "is_ready" in d
        assert "stages" in d
        assert "errors" in d
        assert "total_elapsed_ms" in d
        assert d["state"] == "ready"
        assert d["is_ready"] is True

    def test_to_dict_stages(self):
        result = BootstrapResult(
            state=BootstrapState.DEGRADED,
            stages=[
                StageResult(
                    stage=BootstrapStage.ENVIRONMENT, success=True, elapsed_ms=100.0
                ),
                StageResult(
                    stage=BootstrapStage.DATABASE,
                    success=False,
                    elapsed_ms=5000.0,
                    error="Timeout",
                ),
            ],
        )
        d = result.to_dict()
        assert len(d["stages"]) == 2
        assert d["stages"][0]["stage"] == "environment"
        assert d["stages"][0]["success"] is True
        assert d["stages"][1]["error"] == "Timeout"


@pytest.mark.asyncio
class TestBootstrapManagerState:
    async def test_initial_state(self):
        """Antes do boot, state = PENDING."""
        state = BootstrapManager.get_state()
        assert state["state"] == "pending"
        assert state["is_ready"] is False

    async def test_reset_clears_state(self):
        """reset() volta ao estado PENDING."""
        BootstrapManager._state = BootstrapState.READY
        BootstrapManager._boot_complete = True
        BootstrapManager.reset()
        assert BootstrapManager._state == BootstrapState.PENDING
        assert BootstrapManager._boot_complete is False
        assert BootstrapManager._stages == []

    async def test_get_state_after_partial_boot(self):
        """Estado com stages parciais e refletido."""
        BootstrapManager._state = BootstrapState.DATABASE_INITIALIZING
        BootstrapManager._stages = [
            StageResult(
                stage=BootstrapStage.ENVIRONMENT, success=True, elapsed_ms=200.0
            ),
        ]
        BootstrapManager._started_at = __import__("time").monotonic()
        state = BootstrapManager.get_state()
        assert state["state"] == "database_initializing"
        assert len(state["stages"]) == 1

    async def test_boot_returns_bootstrap_result(self):
        """boot() retorna BootstrapResult."""
        # Vai falhar porque nao tem DB, mas retorna resultado
        result = await BootstrapManager.boot()
        assert isinstance(result, BootstrapResult)
        assert result.state in (
            BootstrapState.READY,
            BootstrapState.DEGRADED,
            BootstrapState.FAILED,
        )


class TestRunStage:
    @pytest.mark.asyncio
    async def test_successful_stage(self):
        """Stage que sucede retorna StageResult com success=True."""

        async def good_stage():
            return {"ok": True}

        result = await BootstrapManager._run_stage(
            BootstrapStage.ENVIRONMENT, good_stage
        )
        assert result.success is True
        assert result.error is None
        assert result.elapsed_ms >= 0

    @pytest.mark.asyncio
    async def test_failing_stage(self):
        """Stage que falha retorna StageResult com success=False e error."""

        async def bad_stage():
            raise ValueError("Algo deu errado")

        result = await BootstrapManager._run_stage(BootstrapStage.VAULT, bad_stage)
        assert result.success is False
        assert "Algo deu errado" in (result.error or "")

    @pytest.mark.asyncio
    async def test_stage_timeout(self):
        """Stage que excede timeout retorna StageResult com error Timeout."""

        async def slow_stage():
            await asyncio.sleep(100)  # muito lento
            return {}

        # Timeout curto para forçar timeout
        original = BootstrapManager.STAGE_TIMEOUTS[BootstrapStage.DOCKER]
        BootstrapManager.STAGE_TIMEOUTS[BootstrapStage.DOCKER] = 1  # 1 segundo
        result = await BootstrapManager._run_stage(BootstrapStage.DOCKER, slow_stage)
        BootstrapManager.STAGE_TIMEOUTS[BootstrapStage.DOCKER] = original

        assert result.success is False
        assert "Timeout" in (result.error or "")

    @pytest.mark.asyncio
    async def test_stage_with_details(self):
        """Stage pode retornar detalhes no dicionario."""

        async def detailed_stage():
            return {"nodes": 42, "edges": 17}

        result = await BootstrapManager._run_stage(BootstrapStage.AUDIT, detailed_stage)
        assert result.success is True
        assert result.details.get("nodes") == 42


class TestStageTimeouts:
    def test_all_stages_have_timeout(self):
        for stage in BootstrapStage:
            assert stage in BootstrapManager.STAGE_TIMEOUTS
            assert BootstrapManager.STAGE_TIMEOUTS[stage] > 0

    def test_environment_fast(self):
        assert BootstrapManager.STAGE_TIMEOUTS[BootstrapStage.ENVIRONMENT] <= 10

    def test_vault_longest(self):
        assert BootstrapManager.STAGE_TIMEOUTS[BootstrapStage.VAULT] >= 60
