import os
import re
from pathlib import Path
from datetime import datetime
from loguru import logger
from app.config.settings import settings
from app.domain.document import NoteReadResult, SearchResult


class ObsidianService:

    def __init__(self) -> None:
        self._vault_path = Path(settings.OBSIDIAN_VAULT_PATH)
        if not self._vault_path.exists():
            raise ValueError(f"Vault não encontrado em: {self._vault_path}")
        logger.info(f"ObsidianService iniciado. Vault: {self._vault_path}")

    def _resolve_path(self, relative_path: str) -> Path:
        resolved = (self._vault_path / relative_path).resolve()
        if not str(resolved).startswith(str(self._vault_path.resolve())):
            raise PermissionError(f"Acesso negado fora do Vault: {relative_path}")
        return resolved

    def create_note(self, title: str, folder: str, content: str) -> str:
        folder_path = self._vault_path / folder
        folder_path.mkdir(parents=True, exist_ok=True)

        safe_title = re.sub(r'[<>:"/\\|?*]', "_", title)
        file_path = folder_path / f"{safe_title}.md"

        if file_path.exists():
            raise FileExistsError(f"Nota já existe: {folder}/{safe_title}.md")

        file_path.write_text(content, encoding="utf-8")
        relative = str(file_path.relative_to(self._vault_path))
        logger.info(f"Nota criada: {relative}")
        return relative

    def read_note(self, relative_path: str) -> NoteReadResult:
        file_path = self._resolve_path(relative_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Nota não encontrada: {relative_path}")

        content = file_path.read_text(encoding="utf-8")
        last_modified = datetime.fromtimestamp(file_path.stat().st_mtime)
        return NoteReadResult(path=relative_path, content=content, last_modified=last_modified)

    def update_note(self, relative_path: str, content: str, mode: str = "overwrite") -> None:
        file_path = self._resolve_path(relative_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Nota não encontrada: {relative_path}")

        if mode == "append":
            existing = file_path.read_text(encoding="utf-8")
            file_path.write_text(existing + "\n\n" + content, encoding="utf-8")
        else:
            file_path.write_text(content, encoding="utf-8")
        logger.info(f"Nota atualizada ({mode}): {relative_path}")

    def delete_note(self, relative_path: str) -> None:
        file_path = self._resolve_path(relative_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Nota não encontrada: {relative_path}")
        file_path.unlink()
        logger.info(f"Nota removida: {relative_path}")

    def list_notes(self, folder: str = "") -> list[str]:
        search_path = self._vault_path / folder if folder else self._vault_path
        return [
            str(p.relative_to(self._vault_path))
            for p in search_path.rglob("*.md")
            if not p.name.startswith(".")
        ]

    def search_text(self, query: str, max_results: int = 10) -> list[SearchResult]:
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
                continue

        return results
