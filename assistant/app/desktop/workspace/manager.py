from datetime import datetime
from pathlib import Path
from loguru import logger
from app.config.settings import settings


class WorkspaceManager:
    def __init__(self) -> None:
        self._root = Path(settings.WORKSPACE_ROOT)
        logger.debug(f"[start] WorkspaceManager - root={self._root}")

    @property
    def root(self) -> Path:
        return self._root

    def workspace_path(self, slug: str, *parts: str) -> Path:
        return self._root.joinpath(slug, *parts)

    def vault_path(self, slug: str, *parts: str) -> Path:
        return self.workspace_path(slug, "vault", *parts)

    def data_path(self, slug: str, *parts: str) -> Path:
        return self.workspace_path(slug, "data", *parts)

    def conversations_path(
        self, slug: str, year: str | None = None, month: str | None = None
    ) -> Path:
        base = self.data_path(slug, "conversations")
        if year:
            base = base / year
        if month:
            base = base / month
        return base

    def logs_path(self, slug: str, *parts: str) -> Path:
        return self.workspace_path(slug, "logs", *parts)

    def apps_path(self, slug: str, *parts: str) -> Path:
        return self.workspace_path(slug, "apps", *parts)

    def settings_path(self, slug: str, *parts: str) -> Path:
        return self.workspace_path(slug, "settings", *parts)

    def exports_path(self, slug: str, *parts: str) -> Path:
        return self.workspace_path(slug, "exports", *parts)

    def dot_kaos_path(self, slug: str, *parts: str) -> Path:
        return self.workspace_path(slug, ".kaos", *parts)

    def ensure_structure(self, slug: str) -> None:
        dirs = [
            self.workspace_path(slug),
            self.vault_path(slug),
            self.data_path(slug),
            self.data_path(slug, "conversations"),
            self.data_path(slug, "memories"),
            self.data_path(slug, "projects"),
            self.data_path(slug, "cache"),
            self.logs_path(slug),
            self.apps_path(slug),
            self.settings_path(slug),
            self.exports_path(slug),
            self.dot_kaos_path(slug),
        ]
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
        logger.info(
            f"[info] WorkspaceManager - estrutura criada para workspace '{slug}'"
        )

    def ensure_conversation_month(self, slug: str, year: str, month: str) -> Path:
        path = self.conversations_path(slug, year, month)
        path.mkdir(parents=True, exist_ok=True)
        return path

    def conversation_filepath(self, slug: str, title: str) -> Path:
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        self.ensure_conversation_month(slug, year, month)
        safe_title = title.replace(" ", "-").replace("/", "-").lower()[:80]
        filename = f"{now.strftime('%Y-%m-%d')}-{safe_title}.md"
        return self.conversations_path(slug, year, month) / filename
