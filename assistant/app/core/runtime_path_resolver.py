"""
Runtime Path Resolver for K.A.O.S.
=====================================
Responsible for resolving absolute paths for workspace, config, logs, vault, and updates.

ATENCAO: Esta implementacao delega para EnvironmentService.
Nenhum modulo novo deve usar RuntimePathResolver diretamente.
Use ``EnvironmentService.detect()`` para acesso ao ambiente.

Compatibilidade retroativa mantida para todos os consumidores existentes.
"""

from pathlib import Path

from app.core.environment_service import EnvironmentService, EnvironmentInfo


class RuntimePathResolver:
    """Wrapper de compatibilidade — delega para EnvironmentService."""

    _env_cache: EnvironmentInfo | None = None

    @classmethod
    def _get_env(cls) -> EnvironmentInfo:
        """Retorna o EnvironmentInfo cacheado."""
        if cls._env_cache is None:
            cls._env_cache = EnvironmentService.detect()
        return cls._env_cache

    @classmethod
    def project_root(cls) -> Path:
        """Return the absolute path to the project root directory."""
        return cls._get_env().project_root

    @classmethod
    def backend_root(cls) -> Path:
        """Return the absolute path to the backend directory."""
        env = cls._get_env()
        return env.backend_src.parent

    @classmethod
    def frontend_root(cls) -> Path:
        """Return the absolute path to the desktop directory."""
        env = cls._get_env()
        if env.desktop_src:
            return env.desktop_src.parent.parent
        return env.project_root / "desktop"

    @classmethod
    def get_workspace_path(cls) -> Path:
        """Return the absolute path to the workspace directory."""
        return cls._get_env().workspace

    @classmethod
    def get_vault_path(cls) -> Path:
        """Return the absolute path to the Obsidian vault directory."""
        return cls._get_env().vault

    @classmethod
    def get_opencode_path(cls) -> Path:
        """Return the absolute path to the .opencode configuration folder."""
        return cls._get_env().project_root / ".opencode"

    @classmethod
    def get_logs_path(cls) -> Path:
        """Return the absolute path to the logs directory, creating it if it doesn't exist."""
        p = cls._get_env().project_root / "logs"
        p.mkdir(parents=True, exist_ok=True)
        return p

    @classmethod
    def get_config_path(cls) -> Path:
        """Return the absolute path to the config directory, creating it if it doesn't exist."""
        return cls._get_env().config_dir

    @classmethod
    def get_data_path(cls) -> Path:
        """Return the absolute path to the data directory (for configs, db, etc.)."""
        p = cls._get_env().project_root / "data"
        p.mkdir(parents=True, exist_ok=True)
        return p

    @classmethod
    def get_updates_temp_dir(cls) -> Path:
        """Return the absolute path to the temporary directory for auto-updates."""
        p = cls.get_config_path() / "updates_temp"
        p.mkdir(parents=True, exist_ok=True)
        return p

    @classmethod
    def get_updater_log_path(cls) -> Path:
        """Return the absolute path to the updater log file."""
        return cls.get_logs_path() / "updater.log"

    # KIRL compatibility paths
    @classmethod
    def docs_root(cls) -> Path:
        """Return the absolute path to the docs directory."""
        return cls._get_env().docs

    @classmethod
    def resolve(cls) -> Path:
        """Compatibilidade KIRL — delegado para resolve_kirl_dir()."""
        return cls.resolve_kirl_dir()

    @classmethod
    def resolve_kirl_dir(cls) -> Path:
        """Return the active runtime directory for KIRL."""
        return cls._get_env().kirl_dir

    @classmethod
    def registry_dir(cls) -> Path:
        return cls._get_env().registry_dir

    @classmethod
    def audit_dir(cls) -> Path:
        return cls._get_env().audit_dir

    @classmethod
    def snapshot_path(cls) -> Path:
        return cls._get_env().snapshot_path

    @classmethod
    def auto_dir(cls) -> Path:
        return cls._get_env().auto_dir

    @classmethod
    def architecture_dir(cls) -> Path:
        return cls._get_env().architecture_dir

    @classmethod
    def architecture_history_dir(cls) -> Path:
        return cls._get_env().architecture_history_dir

    @classmethod
    def issues_path(cls) -> Path:
        return cls._get_env().issues_path

    @classmethod
    def suggestions_path(cls) -> Path:
        return cls._get_env().suggestions_path

    @classmethod
    def analysis_path(cls) -> Path:
        return cls._get_env().analysis_path

    @classmethod
    def knowledge_graph_path(cls) -> Path:
        return cls._get_env().knowledge_graph_path

    @classmethod
    def graph_path(cls) -> Path:
        return cls._get_env().graph_path

    @classmethod
    def features_index_path(cls) -> Path:
        return cls._get_env().features_index_path

    @classmethod
    def commit_map_path(cls) -> Path:
        return cls._get_env().commit_map_path
