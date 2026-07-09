"""
K.A.O.S Environment Service
=============================
Servico central e unico de resolucao de ambiente e paths.
NENHUM outro modulo deve usar Path(...) diretamente para resolver caminhos
do projeto. Todos devem depender de EnvironmentService.

Filosofia:
  1. Detectar ambiente (container, local, CI)
  2. Resolver cada path independentemente (workspace, docs, vault, etc.)
  3. Validar existencia apos resolucao
  4. Logar diagnostico completo
  5. Cachear resultado (o ambiente nao muda durante o runtime)
"""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Optional

from loguru import logger


# ── Tipos de Ambiente ──────────────────────────────────────────────────────


class EnvironmentType(Enum):
    DOCKER = "docker"
    LOCAL = "local"
    CI = "ci"
    UNKNOWN = "unknown"


# ── Informacao de Ambiente (imutavel apos criacao) ─────────────────────────


@dataclass(frozen=True)
class EnvironmentInfo:
    """Snapshot completo do ambiente. Congelado apos criacao."""

    env_type: EnvironmentType
    workspace: Path
    docs: Path
    vault: Path
    config_dir: Path
    backend_src: Path
    desktop_src: Optional[Path]  # None se frontend nao estiver disponivel
    git_root: Optional[Path]  # None se .git nao for encontrado
    runtime_dir: Path  # Onde KIRL artifacts sao armazenados
    is_container: bool
    is_valid: bool
    generated_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    @property
    def project_root(self) -> Path:
        """Raiz do projeto = pai do workspace."""
        return self.workspace.parent

    @property
    def desktop_src_exists(self) -> bool:
        return self.desktop_src is not None and self.desktop_src.exists()

    @property
    def backend_src_exists(self) -> bool:
        return self.backend_src.exists()

    # ── KIRL paths (delegados ao runtime_dir) ──────────────────────────

    @property
    def kirl_dir(self) -> Path:
        return self.runtime_dir

    @property
    def registry_dir(self) -> Path:
        return self.runtime_dir / "registry"

    @property
    def audit_dir(self) -> Path:
        return self.runtime_dir / "audit"

    @property
    def snapshot_path(self) -> Path:
        return self.runtime_dir / "snapshot.json"

    @property
    def auto_dir(self) -> Path:
        return self.runtime_dir / "auto-generated"

    @property
    def architecture_dir(self) -> Path:
        return self.runtime_dir / "architecture"

    @property
    def architecture_history_dir(self) -> Path:
        return self.architecture_dir / "history"

    @property
    def issues_path(self) -> Path:
        return self.architecture_dir / "issues.json"

    @property
    def suggestions_path(self) -> Path:
        return self.architecture_dir / "suggestions.json"

    @property
    def analysis_path(self) -> Path:
        return self.architecture_dir / "analysis.json"

    @property
    def knowledge_graph_path(self) -> Path:
        return self.architecture_dir / "knowledge-graph.json"

    @property
    def graph_path(self) -> Path:
        return self.architecture_dir / "graph.json"

    @property
    def features_index_path(self) -> Path:
        return self.registry_dir / "features-index.json"

    @property
    def commit_map_path(self) -> Path:
        return self.registry_dir / "commit-map.json"

    # ── Serializacao ───────────────────────────────────────────────────

    def to_dict(self) -> dict:
        return {
            "env_type": self.env_type.value,
            "workspace": str(self.workspace),
            "docs": str(self.docs),
            "vault": str(self.vault),
            "config_dir": str(self.config_dir),
            "backend_src": str(self.backend_src),
            "desktop_src": str(self.desktop_src) if self.desktop_src else None,
            "git_root": str(self.git_root) if self.git_root else None,
            "runtime_dir": str(self.runtime_dir),
            "is_container": self.is_container,
            "is_valid": self.is_valid,
            "project_root": str(self.project_root),
            "generated_at": self.generated_at,
        }


# ── Environment Service ────────────────────────────────────────────────────


class EnvironmentService:
    """
    Servico unico de resolucao de ambiente.
    Use ``EnvironmentService.detect()`` para obter o snapshot do ambiente.
    O resultado eh cacheado em memoria — o ambiente nao muda durante o runtime.
    """

    _cached: Optional[EnvironmentInfo] = None
    _detect_attempted: bool = False

    @classmethod
    def detect(cls) -> EnvironmentInfo:
        """
        Detecta e retorna o ambiente atual.
        Cacheado apos a primeira chamada.
        """
        if cls._cached is not None:
            return cls._cached

        cls._detect_attempted = True
        logger.info("[env] Iniciando deteccao de ambiente...")

        # 1. Tipo de ambiente
        env_type = cls._detect_environment_type()
        is_container = env_type == EnvironmentType.DOCKER

        # 2. Resolver cada path independentemente
        workspace = cls._resolve_workspace(env_type)
        docs = cls._resolve_docs(env_type, workspace)
        vault = cls._resolve_vault(env_type, workspace, docs)
        config_dir = cls._resolve_config(env_type, workspace)
        backend_src = cls._resolve_backend_src(env_type, workspace)
        desktop_src = cls._resolve_desktop_src(env_type, workspace)
        git_root = cls._detect_git_root(workspace)
        runtime_dir = cls._resolve_runtime_dir(workspace, docs)

        # 3. Validar paths criticos
        errors: list[str] = []
        if not workspace.exists():
            errors.append(f"workspace {workspace} nao existe")
        if not docs.exists():
            errors.append(f"docs {docs} nao existe")
        if not backend_src.exists():
            errors.append(
                f"backend_src {backend_src} nao existe (pode ser normal em container sem volume app)"
            )

        is_valid = len(errors) == 0

        info = EnvironmentInfo(
            env_type=env_type,
            workspace=workspace.resolve(),
            docs=docs.resolve(),
            vault=vault.resolve(),
            config_dir=config_dir.resolve(),
            backend_src=backend_src.resolve(),
            desktop_src=desktop_src.resolve() if desktop_src else None,
            git_root=git_root.resolve() if git_root else None,
            runtime_dir=runtime_dir.resolve(),
            is_container=is_container,
            is_valid=is_valid,
        )

        # 4. Log obrigatorio de diagnostico
        cls._log_diagnostic(info, errors)
        cls._cached = info
        logger.info(
            "[env] Deteccao concluida: type={} valid={}", env_type.value, is_valid
        )
        return info

    @classmethod
    def invalidate_cache(cls) -> None:
        """Invalida o cache (util em testes)."""
        cls._cached = None
        cls._detect_attempted = False

    # ── Deteccao de tipo de ambiente ───────────────────────────────────

    @classmethod
    def _detect_environment_type(cls) -> EnvironmentType:
        """Detecta onde estamos rodando."""
        # Docker: /.dockerenv existe
        if Path("/.dockerenv").exists():
            logger.info("[env] Detectado: DOCKER (/.dockerenv presente)")
            return EnvironmentType.DOCKER

        # CI: variaveis comuns
        ci_vars = ["CI", "GITHUB_ACTIONS", "GITLAB_CI", "JENKINS_URL", "TF_BUILD"]
        for var in ci_vars:
            if os.environ.get(var):
                logger.info("[env] Detectado: CI ({}={})", var, os.environ.get(var))
                return EnvironmentType.CI

        logger.info("[env] Detectado: LOCAL (fallback)")
        return EnvironmentType.LOCAL

    # ── Resolucao individual de cada path ───────────────────────────────

    @classmethod
    def _resolve_workspace(cls, env_type: EnvironmentType) -> Path:
        """
        Resolve o diretorio workspace.
        Estrategias em ordem de precedencia:
          1. Variavel de ambiente WORKSPACE_ROOT
          2. settings.WORKSPACE_ROOT (se existir)
          3. Docker: /workspace (volume mount padrao)
          4. Git root + /workspace
          5. CWD + /workspace
        """
        strategies = []

        # 1. Env var
        env_val = os.environ.get("WORKSPACE_ROOT")
        if env_val:
            strategies.append(("env WORKSPACE_ROOT", Path(env_val)))

        # 2. Settings
        try:
            from app.config.settings import settings

            if settings.WORKSPACE_ROOT:
                p = Path(settings.WORKSPACE_ROOT)
                strategies.append(("settings.WORKSPACE_ROOT", p))
        except Exception:
            pass

        # 3. Docker mount padrao
        if env_type == EnvironmentType.DOCKER:
            strategies.append(("docker /workspace", Path("/workspace")))

        # 4. Git root
        git_root = cls._detect_git_root_from_cwd()
        if git_root:
            strategies.append(("git root + workspace", git_root / "workspace"))

        # 5. CWD
        strategies.append(("CWD + workspace", Path.cwd() / "workspace"))

        # Tentar cada estrategia
        tried = []
        for label, path in strategies:
            tried.append(f"{label}={path}")
            if path.exists():
                logger.info("[env] workspace resolvido por: {} -> {}", label, path)
                return path.resolve()

        # Se nada funcionou, usar a primeira estrategia (env ou default)
        logger.warning(
            "[env] workspace NAO ENCONTRADO. Estrategias tentadas: {}", tried
        )
        fallback = strategies[0][1] if strategies else Path.cwd() / "workspace"
        logger.warning("[env] Usando fallback: {}", fallback)
        return fallback.resolve()

    @classmethod
    def _resolve_docs(cls, env_type: EnvironmentType, workspace: Path) -> Path:
        """
        Resolve o diretorio de documentacao (docs).
        Estrategias:
          1. Variavel de ambiente OBSIDIAN_VAULT_PATH (pai)
          2. Docker: /vault (volume mount padrao)
          3. workspace.parent / "docs"
        """
        # 1. Env var
        env_val = os.environ.get("OBSIDIAN_VAULT_PATH")
        if env_val:
            p = Path(env_val)
            if p.exists():
                logger.info("[env] docs resolvido por env OBSIDIAN_VAULT_PATH: {}", p)
                return p.resolve()

        # 2. Docker: /vault
        if env_type == EnvironmentType.DOCKER:
            vault_path = Path("/vault")
            if vault_path.exists():
                logger.info("[env] docs resolvido por docker /vault: {}", vault_path)
                return vault_path.resolve()

        # 3. Settings
        try:
            from app.config.settings import settings

            if settings.OBSIDIAN_VAULT_PATH:
                p = Path(settings.OBSIDIAN_VAULT_PATH)
                if p.exists():
                    logger.info("[env] docs resolvido por settings: {}", p)
                    return p.resolve()
        except Exception:
            pass

        # 4. workspace.parent / "docs"
        docs_path = workspace.parent / "docs"
        if docs_path.exists():
            logger.info("[env] docs resolvido por workspace.parent/docs: {}", docs_path)
            return docs_path.resolve()

        # Fallback
        logger.warning(
            "[env] docs NAO ENCONTRADO, usando fallback: {}", workspace.parent / "docs"
        )
        return (workspace.parent / "docs").resolve()

    @classmethod
    def _resolve_vault(
        cls, env_type: EnvironmentType, workspace: Path, docs: Path
    ) -> Path:
        """
        Resolve o diretorio do vault (observian).
        Estrategias:
          1. Variavel de ambiente OBSIDIAN_VAULT_PATH
          2. Docker: /vault (volume mount)
          3. docs / "vault"
          4. workspace / "kaos" / "vault"
        """
        # 1. Env var
        env_val = os.environ.get("OBSIDIAN_VAULT_PATH")
        if env_val:
            p = Path(env_val)
            if p.exists():
                logger.info("[env] vault resolvido por env OBSIDIAN_VAULT_PATH: {}", p)
                return p.resolve()

        # 2. Docker: /vault
        if env_type == EnvironmentType.DOCKER:
            vault_path = Path("/vault")
            if vault_path.exists():
                logger.info("[env] vault resolvido por docker /vault: {}", vault_path)
                return vault_path.resolve()

        # 3. docs / "vault"
        vault_path = docs / "vault"
        if vault_path.exists():
            logger.info("[env] vault resolvido por docs/vault: {}", vault_path)
            return vault_path.resolve()

        # 4. workspace/kaos/vault
        vault_path = workspace / "kaos" / "vault"
        if vault_path.exists():
            logger.info(
                "[env] vault resolvido por workspace/kaos/vault: {}", vault_path
            )
            return vault_path.resolve()

        # Fallback
        logger.warning(
            "[env] vault NAO ENCONTRADO, usando fallback: {}",
            workspace / "kaos" / "vault",
        )
        return (workspace / "kaos" / "vault").resolve()

    @classmethod
    def _resolve_config(cls, env_type: EnvironmentType, workspace: Path) -> Path:
        """Resolve o diretorio de configuracao."""
        # Docker: /app/config (volume mount)
        if env_type == EnvironmentType.DOCKER:
            config_path = Path("/app/config")
            if config_path.exists():
                return config_path.resolve()

        # workspace.parent / "config"
        config_path = workspace.parent / "config"
        if config_path.exists():
            return config_path.resolve()

        return config_path.resolve()

    @classmethod
    def _resolve_backend_src(cls, env_type: EnvironmentType, workspace: Path) -> Path:
        """
        Resolve o diretorio do codigo fonte do backend (assistant/app).
        Dentro do Docker: /app/app (copiado no build) ou /app/app (volume mount read-only)
        """
        # Docker: /app/app
        if env_type == EnvironmentType.DOCKER:
            app_path = Path("/app/app")
            if app_path.exists():
                return app_path.resolve()

        # workspace.parent / "assistant" / "app"
        app_path = workspace.parent / "assistant" / "app"
        if app_path.exists():
            return app_path.resolve()

        # Fallback: self (estamos rodando de dentro do app)
        return Path(__file__).resolve().parent.parent

    @classmethod
    def _resolve_desktop_src(
        cls, env_type: EnvironmentType, workspace: Path
    ) -> Optional[Path]:
        """
        Resolve o diretorio do codigo fonte do frontend (desktop/src).
        Pode nao existir em ambientes de producao.
        """
        # Docker: /app/desktop/src (se montado como volume)
        if env_type == EnvironmentType.DOCKER:
            desktop_path = Path("/app/desktop/src")
            if desktop_path.exists():
                return desktop_path.resolve()

        # workspace.parent / "desktop" / "src"
        desktop_path = workspace.parent / "desktop" / "src"
        if desktop_path.exists():
            return desktop_path.resolve()

        # Frontend nao disponivel
        logger.info("[env] desktop/src nao encontrado. Scanner ignorara TypeScript.")
        return None

    @classmethod
    def _resolve_runtime_dir(cls, workspace: Path, docs: Path) -> Path:
        """
        Resolve o diretorio runtime do KIRL.
        Prioriza docs/runtime/ (canonico), fallback workspace.parent/docs/runtime.
        """
        canonical = docs / "runtime"
        if canonical.exists():
            return canonical.resolve()

        alt = workspace.parent / "docs" / "runtime"
        if alt.exists():
            return alt.resolve()

        # Criar o diretorio canonical
        canonical.mkdir(parents=True, exist_ok=True)
        return canonical.resolve()

    # ── Git root detection ─────────────────────────────────────────────

    @classmethod
    def _detect_git_root(cls, workspace: Path) -> Optional[Path]:
        """
        Detecta a raiz do repositorio git.
        """
        # Tentar pelo git CLI
        git_root = cls._detect_git_root_from_cli()
        if git_root:
            return git_root

        # Tentar pelo workspace
        git_root = cls._detect_git_root_from_workspace(workspace)
        if git_root:
            return git_root

        return None

    @classmethod
    def _detect_git_root_from_cli(cls) -> Optional[Path]:
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--show-toplevel"],
                capture_output=True,
                text=True,
                timeout=3,
            )
            if result.returncode == 0:
                path = Path(result.stdout.strip())
                if path.exists():
                    return path.resolve()
        except Exception:
            pass
        return None

    @classmethod
    def _detect_git_root_from_cwd(cls) -> Optional[Path]:
        return cls._detect_git_root_from_cli()

    @classmethod
    def _detect_git_root_from_workspace(cls, workspace: Path) -> Optional[Path]:
        """Sobe de workspace/ ate encontrar .git."""
        current = workspace.parent
        for _ in range(5):  # Max 5 niveis
            if (current / ".git").exists():
                return current.resolve()
            current = current.parent
        return None

    # ── Diagnostico ────────────────────────────────────────────────────

    @classmethod
    def _log_diagnostic(cls, info: EnvironmentInfo, errors: list[str]) -> None:
        """Log completo de diagnostico — sempre chamado apos detect()."""
        logger.info("=" * 60)
        logger.info("[env] DIAGNOSTICO DE AMBIENTE")
        logger.info("[env]   env_type:              {}", info.env_type.value)
        logger.info("[env]   is_container:          {}", info.is_container)
        logger.info("[env]   is_valid:              {}", info.is_valid)
        logger.info("[env]   project_root:          {}", info.project_root)
        logger.info("[env]   workspace:             {}", info.workspace)
        logger.info("[env]   docs:                  {}", info.docs)
        logger.info("[env]   vault:                 {}", info.vault)
        logger.info("[env]   config_dir:            {}", info.config_dir)
        logger.info("[env]   backend_src:           {}", info.backend_src)
        logger.info("[env]   desktop_src:           {}", info.desktop_src)
        logger.info("[env]   git_root:              {}", info.git_root)
        logger.info("[env]   runtime_dir:           {}", info.runtime_dir)
        logger.info("[env]   workspace exists:      {}", info.workspace.exists())
        logger.info("[env]   docs exists:           {}", info.docs.exists())
        logger.info("[env]   vault exists:          {}", info.vault.exists())
        logger.info("[env]   backend_src exists:    {}", info.backend_src_exists)
        logger.info("[env]   desktop_src exists:    {}", info.desktop_src_exists)
        if errors:
            logger.info("[env]   ERRORS:                {}", errors)
        logger.info("=" * 60)
