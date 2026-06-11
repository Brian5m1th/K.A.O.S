import os
import re
from pathlib import Path
from datetime import datetime
from loguru import logger
from app.config.settings import settings
from app.domain.document import NoteReadResult, SearchResult


class ObsidianService:

    def __init__(self) -> None:
        logger.info("[start] ObsidianService - __init__")
        self._vault_path = Path(settings.OBSIDIAN_VAULT_PATH)
        if not self._vault_path.exists():
            logger.error(f"[error] ObsidianService - vault nao encontrado: {self._vault_path}")
            raise ValueError(f"Vault não encontrado em: {self._vault_path}")
        logger.info(f"[info] ObsidianService - vault: {self._vault_path}")
        logger.debug("[finish] ObsidianService - __init__")

    def _resolve_path(self, relative_path: str) -> Path:
        resolved = (self._vault_path / relative_path).resolve()
        if not str(resolved).startswith(str(self._vault_path.resolve())):
            raise PermissionError(f"Acesso negado fora do Vault: {relative_path}")
        return resolved

    def create_note(self, title: str, folder: str, content: str) -> str:
        logger.info("[start] ObsidianService - create_note")
        folder_path = self._vault_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        safe_title = re.sub(r'[<>:"/\\|?*]', "_", title)
        file_path = folder_path / f"{safe_title}.md"

        if file_path.exists():
            logger.error(f"[error] ObsidianService - nota ja existe: {folder}/{safe_title}.md")
            raise FileExistsError(f"Nota já existe: {folder}/{safe_title}.md")

        file_path.write_text(content, encoding="utf-8")
        relative = str(file_path.relative_to(self._vault_path))
        logger.info(f"[info] ObsidianService - nota criada: {relative}")
        logger.debug("[finish] ObsidianService - create_note")
        return relative

    def read_note(self, relative_path: str) -> NoteReadResult:
        logger.info("[start] ObsidianService - read_note")
        file_path = self._resolve_path(relative_path)
        if not file_path.exists():
            logger.error(f"[error] ObsidianService - nota nao encontrada: {relative_path}")
            raise FileNotFoundError(f"Nota não encontrada: {relative_path}")

        content = file_path.read_text(encoding="utf-8")
        last_modified = datetime.fromtimestamp(file_path.stat().st_mtime)
        logger.debug("[finish] ObsidianService - read_note")
        return NoteReadResult(path=relative_path, content=content, last_modified=last_modified)

    def update_note(self, relative_path: str, content: str, mode: str = "overwrite") -> None:
        logger.info("[start] ObsidianService - update_note")
        file_path = self._resolve_path(relative_path)
        if not file_path.exists():
            logger.error(f"[error] ObsidianService - nota nao encontrada: {relative_path}")
            raise FileNotFoundError(f"Nota não encontrada: {relative_path}")

        if mode == "append":
            existing = file_path.read_text(encoding="utf-8")
            file_path.write_text(existing + "\n\n" + content, encoding="utf-8")
        else:
            file_path.write_text(content, encoding="utf-8")
        logger.info(f"[info] ObsidianService - nota atualizada ({mode}): {relative_path}")
        logger.debug("[finish] ObsidianService - update_note")

    def delete_note(self, relative_path: str) -> None:
        logger.info("[start] ObsidianService - delete_note")
        file_path = self._resolve_path(relative_path)
        if not file_path.exists():
            logger.error(f"[error] ObsidianService - nota nao encontrada: {relative_path}")
            raise FileNotFoundError(f"Nota não encontrada: {relative_path}")
        file_path.unlink()
        logger.info(f"[info] ObsidianService - nota removida: {relative_path}")
        logger.debug("[finish] ObsidianService - delete_note")

    def list_notes(self, folder: str = "") -> list[str]:
        logger.info("[start] ObsidianService - list_notes")
        search_path = self._vault_path / folder if folder else self._vault_path
        result = [
            str(p.relative_to(self._vault_path))
            for p in search_path.rglob("*.md")
            if not p.name.startswith(".")
        ]
        logger.debug("[finish] ObsidianService - list_notes")
        return result

    def search_text(self, query: str, max_results: int = 10) -> list[SearchResult]:
        logger.info("[start] ObsidianService - search_text")
        results: list[SearchResult] = []
        query_lower = query.lower()

        for path in self._vault_path.rglob("*.md"):
            if path.name.startswith("."):
                continue
            try:
                content = path.read_text(encoding="utf-8")
                if query_lower in content.lower():
                    idx = content.lower().index(query_lower)
                    start = max(0, idx - 100)
                    end = min(len(content), idx + 200)
                    excerpt = content[start:end].strip()
                    relative = str(path.relative_to(self._vault_path))
                    results.append(SearchResult(path=relative, excerpt=excerpt))
                    if len(results) >= max_results:
                        break
            except (UnicodeDecodeError, OSError):
                logger.debug(f"[skip] ObsidianService - search_text: erro ao ler {path}")
                continue

        logger.debug("[finish] ObsidianService - search_text")
        return results
