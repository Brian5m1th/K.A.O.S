"""
Runtime Path Resolver for KIRL/DRL artifacts.

Responsible for locating the canonical `docs/runtime/` directory.

Migration strategy (KIRL-F2):
  Phase 1: CANONICAL = docs/runtime/ (project root)
  Phase 2: Fallback to LEGACY = assistant/docs/runtime/ (old location)
  Phase 3: Remove LEGACY after full validation

TODO(KIRL-F2): Remover fallback LEGACY após validação completa.
"""

from pathlib import Path


class RuntimePathResolver:
    """Resolves paths for KIRL runtime artifacts.

    Canonical location: <project_root>/docs/runtime/
    Legacy location:    <project_root>/assistant/docs/runtime/

    During migration period, the resolver checks canonical first,
    then falls back to legacy. After KIRL-F2, only canonical is used.
    """

    # Canonical: docs/runtime/ at the project root (submodule docs)
    CANONICAL: Path = (
        Path(__file__).resolve().parent.parent.parent.parent / "docs" / "runtime"
    )

    # Legacy: assistant/docs/runtime/ (old location, to be removed)
    LEGACY: Path = Path(__file__).resolve().parent.parent.parent / "docs" / "runtime"

    @classmethod
    def project_root(cls) -> Path:
        """Return the absolute path to the project root directory."""
        return Path(__file__).resolve().parent.parent.parent.parent

    @classmethod
    def docs_root(cls) -> Path:
        """Return the absolute path to the docs directory."""
        return cls.project_root() / "docs"

    @classmethod
    def vault_root(cls) -> Path:
        """Return the absolute path to the Obsidian vault directory."""
        # Check if settings overrides OBSIDIAN_VAULT_PATH
        try:
            from app.config.settings import settings
            if settings.OBSIDIAN_VAULT_PATH:
                return Path(settings.OBSIDIAN_VAULT_PATH).resolve()
        except Exception:
            pass
        return cls.docs_root() / "vault"

    @classmethod
    def workspace_root(cls) -> Path:
        """Return the absolute path to the workspace directory."""
        return cls.project_root() / "workspace"

    @classmethod
    def backend_root(cls) -> Path:
        """Return the absolute path to the backend directory."""
        return cls.project_root() / "assistant"

    @classmethod
    def frontend_root(cls) -> Path:
        """Return the absolute path to the desktop directory."""
        return cls.project_root() / "desktop"

    @classmethod
    def resolve(cls) -> Path:
        """Return the active runtime directory.

        Uses canonical if it exists, falls back to legacy.
        """
        canonical_path = cls.docs_root() / "runtime"
        if canonical_path.exists():
            return canonical_path
        return cls.backend_root() / "docs" / "runtime"

    @classmethod
    def registry_dir(cls) -> Path:
        return cls.resolve() / "registry"

    @classmethod
    def audit_dir(cls) -> Path:
        return cls.resolve() / "audit"

    @classmethod
    def snapshot_path(cls) -> Path:
        return cls.resolve() / "snapshot.json"

    @classmethod
    def auto_dir(cls) -> Path:
        return cls.resolve() / "auto-generated"

    @classmethod
    def architecture_dir(cls) -> Path:
        return cls.resolve() / "architecture"

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
