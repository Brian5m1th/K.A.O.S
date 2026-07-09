"""
K.A.O.S Bootstrap Manager
===========================
Orquestrador do startup completo do backend.

Maquina de estados explicita que substitui watchers avulsos por um
pipeline ordenado: Environment → Docker → Database → Workspace →
Vault → Knowledge Graph → Architecture Graph → Audit.

Falha em uma etapa NAO quebra o boot — o sistema continua em estado degradado
mas funcional, com erros registrados para diagnostico.
"""

from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Optional

from loguru import logger


class BootstrapState(Enum):
    PENDING = "pending"
    ENVIRONMENT_DETECTING = "environment_detecting"
    DOCKER_CHECKING = "docker_checking"
    DATABASE_INITIALIZING = "database_initializing"
    WORKSPACE_SCANNING = "workspace_scanning"
    VAULT_INDEXING = "vault_indexing"
    KNOWLEDGE_GRAPH_BUILDING = "knowledge_graph_building"
    ARCHITECTURE_GRAPH_BUILDING = "architecture_graph_building"
    AUDIT_SCANNING = "audit_scanning"
    READY = "ready"
    FAILED = "failed"
    DEGRADED = "degraded"  # Iniciou com erros nao-criticos


class BootstrapStage(Enum):
    """Etapas individuais com timeout e criticidade."""

    ENVIRONMENT = "environment"
    DOCKER = "docker"
    DATABASE = "database"
    WORKSPACE = "workspace"
    VAULT = "vault"
    KNOWLEDGE_GRAPH = "knowledge_graph"
    ARCHITECTURE_GRAPH = "architecture_graph"
    AUDIT = "audit"


@dataclass
class StageResult:
    """Resultado de uma etapa do bootstrap."""

    stage: BootstrapStage
    success: bool
    elapsed_ms: float = 0.0
    error: Optional[str] = None
    details: dict[str, Any] = field(default_factory=dict)

    @property
    def label(self) -> str:
        return self.stage.value


@dataclass
class BootstrapResult:
    """Resultado completo do bootstrap."""

    state: BootstrapState
    stages: list[StageResult] = field(default_factory=list)
    started_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    completed_at: Optional[str] = None
    total_elapsed_ms: float = 0.0
    errors: list[str] = field(default_factory=list)
    environment_info: Optional[dict] = None
    degraded: bool = False

    @property
    def is_ready(self) -> bool:
        return self.state in (BootstrapState.READY, BootstrapState.DEGRADED)

    def to_dict(self) -> dict:
        return {
            "state": self.state.value,
            "is_ready": self.is_ready,
            "degraded": self.degraded,
            "stages": [
                {
                    "stage": s.label,
                    "success": s.success,
                    "elapsed_ms": round(s.elapsed_ms, 1),
                    "error": s.error,
                }
                for s in self.stages
            ],
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "total_elapsed_ms": round(self.total_elapsed_ms, 1),
            "errors": self.errors,
            "environment_info": self.environment_info,
        }


class BootstrapManager:
    """
    Orquestrador do startup.
    Uso::

        await BootstrapManager.boot()  # No lifespan do FastAPI
        state = BootstrapManager.get_state()  # Endpoint healthcheck
    """

    _state: BootstrapState = BootstrapState.PENDING
    _stages: list[StageResult] = []
    _errors: list[str] = []
    _started_at: float = 0.0
    _completed_at: Optional[float] = None
    _env_info: Optional[dict] = None
    _degraded: bool = False
    _boot_complete: bool = False

    # Timeout padrao por etapa (segundos)
    STAGE_TIMEOUTS: dict[BootstrapStage, int] = {
        BootstrapStage.ENVIRONMENT: 10,
        BootstrapStage.DOCKER: 30,
        BootstrapStage.DATABASE: 30,
        BootstrapStage.WORKSPACE: 60,
        BootstrapStage.VAULT: 120,
        BootstrapStage.KNOWLEDGE_GRAPH: 60,
        BootstrapStage.ARCHITECTURE_GRAPH: 60,
        BootstrapStage.AUDIT: 60,
    }

    @classmethod
    async def boot(cls) -> BootstrapResult:
        """
        Pipeline completo de inicializacao.
        Cada etapa tem timeout e tratamento de erro independente.
        """
        cls._state = BootstrapState.PENDING
        cls._stages = []
        cls._errors = []
        cls._started_at = time.monotonic()
        cls._completed_at = None
        cls._degraded = False
        cls._boot_complete = False

        logger.info("=" * 60)
        logger.info("[boot] Iniciando bootstrap do K.A.O.S...")
        logger.info("=" * 60)

        # ── 1. ENVIRONMENT ────────────────────────────────────────────
        cls._state = BootstrapState.ENVIRONMENT_DETECTING
        stage_result = await cls._run_stage(
            BootstrapStage.ENVIRONMENT, cls._detect_environment
        )
        cls._stages.append(stage_result)
        if not stage_result.success:
            cls._errors.append(stage_result.error or "Environment detection failed")
            cls._finalize(BootstrapState.FAILED)
            return cls._build_result()

        # ── 2. DOCKER (opcional — apenas em container) ────────────────
        if cls._env_info and cls._env_info.get("is_container"):
            cls._state = BootstrapState.DOCKER_CHECKING
            stage_result = await cls._run_stage(
                BootstrapStage.DOCKER, cls._check_docker_services
            )
            cls._stages.append(stage_result)
            if not stage_result.success:
                cls._errors.append(stage_result.error or "Docker check failed")
                # Nao critico — continuar
                cls._degraded = True

        # ── 3. DATABASE ───────────────────────────────────────────────
        cls._state = BootstrapState.DATABASE_INITIALIZING
        stage_result = await cls._run_stage(BootstrapStage.DATABASE, cls._init_database)
        cls._stages.append(stage_result)
        if not stage_result.success:
            cls._errors.append(stage_result.error or "Database init failed")
            cls._degraded = True

        # ── 4. WORKSPACE SCAN ─────────────────────────────────────────
        cls._state = BootstrapState.WORKSPACE_SCANNING
        stage_result = await cls._run_stage(
            BootstrapStage.WORKSPACE, cls._scan_workspace
        )
        cls._stages.append(stage_result)
        if not stage_result.success:
            cls._errors.append(stage_result.error or "Workspace scan failed")
            cls._degraded = True

        # ── 5. VAULT INDEX ────────────────────────────────────────────
        cls._state = BootstrapState.VAULT_INDEXING
        stage_result = await cls._run_stage(BootstrapStage.VAULT, cls._index_vault)
        cls._stages.append(stage_result)
        if not stage_result.success:
            cls._errors.append(stage_result.error or "Vault index failed")
            cls._degraded = True

        # ── 6. KNOWLEDGE GRAPH ────────────────────────────────────────
        cls._state = BootstrapState.KNOWLEDGE_GRAPH_BUILDING
        stage_result = await cls._run_stage(
            BootstrapStage.KNOWLEDGE_GRAPH, cls._build_knowledge_graph
        )
        cls._stages.append(stage_result)
        if not stage_result.success:
            cls._errors.append(stage_result.error or "Knowledge Graph build failed")
            cls._degraded = True

        # ── 7. ARCHITECTURE GRAPH ─────────────────────────────────────
        cls._state = BootstrapState.ARCHITECTURE_GRAPH_BUILDING
        stage_result = await cls._run_stage(
            BootstrapStage.ARCHITECTURE_GRAPH, cls._build_arch_graph
        )
        cls._stages.append(stage_result)
        if not stage_result.success:
            cls._errors.append(stage_result.error or "Architecture Graph build failed")
            cls._degraded = True

        # ── 8. AUDIT SCAN ─────────────────────────────────────────────
        cls._state = BootstrapState.AUDIT_SCANNING
        stage_result = await cls._run_stage(BootstrapStage.AUDIT, cls._run_audit)
        cls._stages.append(stage_result)
        if not stage_result.success:
            cls._errors.append(stage_result.error or "Audit scan failed")
            cls._degraded = True

        # ── FINALIZAR ─────────────────────────────────────────────────
        if cls._degraded:
            cls._finalize(BootstrapState.DEGRADED)
        else:
            cls._finalize(BootstrapState.READY)

        return cls._build_result()

    @classmethod
    def get_state(cls) -> dict:
        """Retorna estado atual do bootstrap (para endpoint healthcheck)."""
        elapsed = 0.0
        if cls._completed_at:
            elapsed = (cls._completed_at - cls._started_at) * 1000
        elif cls._started_at > 0:
            elapsed = (time.monotonic() - cls._started_at) * 1000

        return {
            "state": cls._state.value,
            "is_ready": cls._state in (BootstrapState.READY, BootstrapState.DEGRADED),
            "degraded": cls._degraded,
            "boot_complete": cls._boot_complete,
            "stages": [
                {
                    "stage": s.label,
                    "success": s.success,
                    "elapsed_ms": round(s.elapsed_ms, 1),
                    "error": s.error,
                }
                for s in cls._stages
            ],
            "errors": cls._errors,
            "total_elapsed_ms": round(elapsed, 1),
            "environment": cls._env_info,
        }

    @classmethod
    def reset(cls) -> None:
        """Reseta o bootstrap (util em testes)."""
        cls._state = BootstrapState.PENDING
        cls._stages = []
        cls._errors = []
        cls._started_at = 0.0
        cls._completed_at = None
        cls._env_info = None
        cls._degraded = False
        cls._boot_complete = False

    # ── Executor de etapa com timeout ─────────────────────────────────

    @classmethod
    async def _run_stage(cls, stage: BootstrapStage, coro) -> StageResult:
        """
        Executa uma etapa do bootstrap com timeout.
        Falha em uma etapa NAO propaga excecao — retorna StageResult com erro.
        """
        timeout = cls.STAGE_TIMEOUTS.get(stage, 30)
        start = time.monotonic()
        logger.info("[boot] Stage {} iniciando (timeout={}s)...", stage.value, timeout)

        try:
            result = await asyncio.wait_for(coro(), timeout=timeout)
            elapsed = (time.monotonic() - start) * 1000
            logger.info(
                "[boot] Stage {} concluido com sucesso ({:.0f}ms)",
                stage.value,
                elapsed,
            )
            return StageResult(
                stage=stage, success=True, elapsed_ms=elapsed, details=result or {}
            )
        except asyncio.TimeoutError:
            elapsed = (time.monotonic() - start) * 1000
            logger.warning(
                "[boot] Stage {} TIMEOUT apos {:.0f}ms", stage.value, elapsed
            )
            return StageResult(
                stage=stage,
                success=False,
                elapsed_ms=elapsed,
                error=f"Timeout apos {timeout}s",
            )
        except Exception as e:
            elapsed = (time.monotonic() - start) * 1000
            logger.warning(
                "[boot] Stage {} FALHOU ({:.0f}ms): {}", stage.value, elapsed, e
            )
            return StageResult(
                stage=stage,
                success=False,
                elapsed_ms=elapsed,
                error=str(e),
            )

    # ── Implementacao de cada etapa ───────────────────────────────────

    @classmethod
    async def _detect_environment(cls) -> dict:
        """Etapa 1: Detectar ambiente."""
        from app.core.environment_service import EnvironmentService

        env = EnvironmentService.detect()
        cls._env_info = env.to_dict()
        return cls._env_info

    @classmethod
    async def _check_docker_services(cls) -> dict:
        """Etapa 2: Verificar servicos Docker (apenas em container)."""
        # Healthcheck dos servicos essenciais
        import httpx

        checks = {
            "postgres": "http://postgres:5432",
            "qdrant": "http://qdrant:6333",
        }
        results = {}
        for name, url in checks.items():
            try:
                async with httpx.AsyncClient(timeout=3) as c:
                    r = await c.get(url)
                    results[name] = r.is_success
            except Exception:
                results[name] = False

        failed = [name for name, ok in results.items() if not ok]
        if failed:
            logger.warning("[boot] Servicos Docker offline: {}", failed)
        return results

    @classmethod
    async def _init_database(cls) -> dict:
        """Etapa 3: Inicializar database."""
        from app.database import create_tables

        await create_tables()
        return {"tables_created": True}

    @classmethod
    async def _scan_workspace(cls) -> dict:
        """Etapa 4: Escanear workspace."""
        from app.audit.code_scanner import CodeScanner

        snapshot = CodeScanner.scan_all()
        return {
            "stores": len(snapshot.stores),
            "routes": len(snapshot.routes),
            "tools": len(snapshot.tools),
            "events": len(snapshot.events),
            "agents": len(snapshot.agents),
            "workflows": len(snapshot.workflows),
            "providers": len(snapshot.providers),
            "components": len(snapshot.components),
            "hooks": len(snapshot.hooks),
        }

    @classmethod
    async def _index_vault(cls) -> dict:
        """Etapa 5: Indexar vault."""
        from app.obsidian.vault_init import create_vault_structure

        created = create_vault_structure()
        return {"folders_created": len(created)}

    @classmethod
    async def _build_knowledge_graph(cls) -> dict:
        """Etapa 6: Construir grafo de conhecimento."""
        from app.ai.vault_analyzer.knowledge_graph import KnowledgeGraphBuilder

        kg = KnowledgeGraphBuilder.build()
        return {
            "nodes": len(kg.nodes),
            "edges": len(kg.edges),
            "features": len(kg.features),
            "sdds": len(kg.sdds),
        }

    @classmethod
    async def _build_arch_graph(cls) -> dict:
        """Etapa 7: Construir grafo de arquitetura."""
        from app.ai.vault_analyzer.graph_builder import GraphBuilder

        graph = GraphBuilder.build()
        return {"nodes": len(graph.nodes), "edges": len(graph.edges)}

    @classmethod
    async def _run_audit(cls) -> dict:
        """Etapa 8: Executar auditoria inicial."""
        from app.audit.audit_engine import AuditEngine

        report = AuditEngine.run_audit()
        return {
            "coverage": round(report.coverage, 1),
            "drift_level": report.drift_level,
            "missing_features": len(report.missing_features),
            "outdated_docs": len(report.outdated_docs),
        }

    # ── Finalizacao ───────────────────────────────────────────────────

    @classmethod
    def _finalize(cls, state: BootstrapState) -> None:
        """Finaliza o bootstrap com o estado dado."""
        cls._state = state
        cls._completed_at = time.monotonic()
        cls._boot_complete = True

        total_elapsed = (cls._completed_at - cls._started_at) * 1000
        success_count = sum(1 for s in cls._stages if s.success)
        total_count = len(cls._stages)

        logger.info("=" * 60)
        logger.info(
            "[boot] Bootstrap concluido: state={} stages={}/{} errors={} total={:.0f}ms",
            state.value,
            success_count,
            total_count,
            len(cls._errors),
            total_elapsed,
        )
        if cls._errors:
            for err in cls._errors:
                logger.info("[boot]   Error: {}", err)
        logger.info("=" * 60)

    @classmethod
    def _build_result(cls) -> BootstrapResult:
        """Constrói o resultado final."""
        total_elapsed = 0.0
        if cls._completed_at:
            total_elapsed = (cls._completed_at - cls._started_at) * 1000

        return BootstrapResult(
            state=cls._state,
            stages=list(cls._stages),
            errors=list(cls._errors),
            total_elapsed_ms=total_elapsed,
            environment_info=cls._env_info,
            degraded=cls._degraded,
            completed_at=datetime.now(timezone.utc).isoformat(),
        )
