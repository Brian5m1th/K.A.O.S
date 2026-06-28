"""
Runtime Path Resolver for K.A.O.S.
Responsible for resolving absolute paths for workspace, config, logs, vault, and updates.
"""

from pathlib import Path
from loguru import logger


class RuntimePathResolver:
    @classmethod
    def project_root(cls) -> Path:
        """Return the absolute path to the project root directory."""
        return Path(__file__).resolve().parent.parent.parent.parent

    @classmethod
    def backend_root(cls) -> Path:
        """Return the absolute path to the backend directory."""
        return cls.project_root() / "assistant"

    @classmethod
    def frontend_root(cls) -> Path:
        """Return the absolute path to the desktop directory."""
        return cls.project_root() / "desktop"

    @classmethod
    def get_workspace_path(cls) -> Path:
        """Return the absolute path to the workspace directory."""
        return cls.project_root() / "workspace"

    @classmethod
    def get_vault_path(cls) -> Path:
        """Return the absolute path to the Obsidian vault directory."""
        try:
            from app.config.settings import settings

            if settings.OBSIDIAN_VAULT_PATH:
                return Path(settings.OBSIDIAN_VAULT_PATH).resolve()
        except Exception as exc:
            logger.warning(
                "[runtime_path_resolver] failed to resolve Obsidian vault path from settings, falling back: {}",
                exc,
            )
        return cls.project_root() / "docs" / "vault"

    @classmethod
    def get_opencode_path(cls) -> Path:
        """Return the absolute path to the .opencode configuration folder."""
        return cls.project_root() / ".opencode"

    @classmethod
    def get_logs_path(cls) -> Path:
        """Return the absolute path to the logs directory, creating it if it doesn't exist."""
        p = cls.project_root() / "logs"
        p.mkdir(parents=True, exist_ok=True)
        return p

    @classmethod
    def get_config_path(cls) -> Path:
        """Return the absolute path to the config directory, creating it if it doesn't exist."""
        p = cls.project_root() / "config"
        p.mkdir(parents=True, exist_ok=True)
        return p

    @classmethod
    def get_data_path(cls) -> Path:
        """Return the absolute path to the data directory (for configs, db, etc.)."""
        p = cls.project_root() / "data"
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
        return cls.project_root() / "docs"

    @classmethod
    def resolve(cls) -> Path:
        """Compatibilidade KIRL — delegado para resolve_kirl_dir()."""
        return cls.resolve_kirl_dir()

    @classmethod
    def resolve_kirl_dir(cls) -> Path:
        """Return the active runtime directory for KIRL (canonical or legacy)."""
        canonical_path = cls.docs_root() / "runtime"
        if canonical_path.exists():
            return canonical_path
        return cls.backend_root() / "docs" / "runtime"

    @classmethod
    def registry_dir(cls) -> Path:
        return cls.resolve_kirl_dir() / "registry"

    @classmethod
    def audit_dir(cls) -> Path:
        return cls.resolve_kirl_dir() / "audit"

    @classmethod
    def snapshot_path(cls) -> Path:
        return cls.resolve_kirl_dir() / "snapshot.json"

    @classmethod
    def auto_dir(cls) -> Path:
        return cls.resolve_kirl_dir() / "auto-generated"

    @classmethod
    def architecture_dir(cls) -> Path:
        return cls.resolve_kirl_dir() / "architecture"

    @classmethod
    def architecture_history_dir(cls) -> Path:
        return cls.architecture_dir() / "history"

    @classmethod
    def issues_path(cls) -> Path:
        return cls.architecture_dir() / "issues.json"

    @classmethod
    def suggestions_path(cls) -> Path:
        return cls.architecture_dir() / "suggestions.json"

    @classmethod
    def analysis_path(cls) -> Path:
        return cls.architecture_dir() / "analysis.json"

    @classmethod
    def knowledge_graph_path(cls) -> Path:
        return cls.architecture_dir() / "knowledge-graph.json"

    @classmethod
    def graph_path(cls) -> Path:
        return cls.architecture_dir() / "graph.json"

    @classmethod
    def features_index_path(cls) -> Path:
        return cls.registry_dir() / "features-index.json"

    @classmethod
    def commit_map_path(cls) -> Path:
        return cls.registry_dir() / "commit-map.json"
