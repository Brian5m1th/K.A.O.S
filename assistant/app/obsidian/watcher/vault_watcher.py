from pathlib import Path

from loguru import logger
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

from app.config.settings import settings
from app.rag.indexer.vault_indexer import VaultIndexer


class _VaultEventHandler(FileSystemEventHandler):
    def __init__(self, indexer: VaultIndexer) -> None:
        self._indexer = indexer

    def _is_markdown(self, path: str) -> bool:
        return path.endswith(".md") and not Path(path).name.startswith(".")

    def on_created(self, event: FileSystemEvent) -> None:
        if not event.is_directory and self._is_markdown(event.src_path):
            logger.info(f"[info] VaultWatcher - CREATE: {event.src_path}")
            self._indexer.index_file(event.src_path)

    def on_modified(self, event: FileSystemEvent) -> None:
        if not event.is_directory and self._is_markdown(event.src_path):
            logger.info(f"[info] VaultWatcher - MODIFY: {event.src_path}")
            self._indexer.index_file(event.src_path)

    def on_deleted(self, event: FileSystemEvent) -> None:
        if not event.is_directory and self._is_markdown(event.src_path):
            vault = Path(settings.OBSIDIAN_VAULT_PATH)
            relative = str(Path(event.src_path).relative_to(vault))
            logger.info(f"[info] VaultWatcher - DELETE: {relative}")
            self._indexer.remove_file(relative)

    def on_moved(self, event: FileSystemEvent) -> None:
        if not event.is_directory:
            vault = Path(settings.OBSIDIAN_VAULT_PATH)
            if self._is_markdown(str(event.src_path)):
                old_relative = str(Path(event.src_path).relative_to(vault))
                logger.info(f"[info] VaultWatcher - MOVE (remove): {old_relative}")
                self._indexer.remove_file(old_relative)
            if self._is_markdown(str(event.dest_path)):
                logger.info(f"[info] VaultWatcher - MOVE (index): {event.dest_path}")
                self._indexer.index_file(str(event.dest_path))


class VaultWatcher:
    def __init__(self) -> None:
        self._indexer = VaultIndexer()
        self._available = self._indexer._available
        if not self._available:
            logger.warning("[warn] VaultWatcher - Qdrant indisponivel, watcher iniciara sem indexacao")
        self._observer = Observer()

    def start(self) -> None:
        logger.info("[start] VaultWatcher - start")
        handler = _VaultEventHandler(self._indexer)
        self._observer.schedule(
            handler, path=settings.OBSIDIAN_VAULT_PATH, recursive=True
        )
        self._observer.start()
        logger.info(
            f"[info] VaultWatcher - iniciado em: {settings.OBSIDIAN_VAULT_PATH}"
        )
        logger.debug("[finish] VaultWatcher - start")

    def stop(self) -> None:
        logger.info("[start] VaultWatcher - stop")
        self._observer.stop()
        self._observer.join()
        logger.info("[info] VaultWatcher - encerrado")
        logger.debug("[finish] VaultWatcher - stop")
