"""
Knowledge Graph Watcher — monitors workspace files (docs, backend app, desktop src)
and triggers incremental updates to the Knowledge Graph when changes occur.
"""

import threading
from pathlib import Path
from loguru import logger

from app.ai.vault_analyzer.knowledge_graph import KnowledgeGraphBuilder
from app.core.runtime_path_resolver import RuntimePathResolver

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    HAS_WATCHDOG = True
except ImportError:
    HAS_WATCHDOG = False

DEBOUNCE_INTERVAL = 1.0  # 1 segundo de debounce para multiplas alteracoes


class KnowledgeGraphEventHandler(FileSystemEventHandler):
    def __init__(self) -> None:
        super().__init__()
        self._dirty_files: set[tuple[Path, bool]] = set()
        self._timer: threading.Timer | None = None
        self._lock = threading.Lock()

    def _is_relevant(self, path_str: str) -> bool:
        path = Path(path_str)
        # Ignorar diretorios
        if path.is_dir():
            return False
        # Ignorar arquivos ocultos
        if any(part.startswith(".") for part in path.parts):
            return False
        # Ignorar diretorios comuns de build/cache
        exclude_dirs = {"__pycache__", "node_modules", "dist", "build", "history", "runtime", "logs", "data"}
        if any(part in exclude_dirs for part in path.parts):
            return False
        # Filtro de extensao
        return path.suffix.lower() in (".md", ".py", ".ts", ".tsx")

    def _trigger_debounce(self, path_str: str, deleted: bool = False) -> None:
        if not self._is_relevant(path_str):
            return

        path = Path(path_str)
        with self._lock:
            # Remover se ja existia para atualizar o status de deletado/alterado
            self._dirty_files = {item for item in self._dirty_files if item[0] != path}
            self._dirty_files.add((path, deleted))

            if self._timer:
                self._timer.cancel()
            self._timer = threading.Timer(DEBOUNCE_INTERVAL, self._process_dirty_files)
            self._timer.daemon = True
            self._timer.start()

    def _process_dirty_files(self) -> None:
        with self._lock:
            files_to_process = list(self._dirty_files)
            self._dirty_files.clear()

        for path, deleted in files_to_process:
            try:
                if deleted or not path.exists():
                    logger.info(f"[kg_watcher] file deleted: {path.name}")
                    KnowledgeGraphBuilder.delete_file(path)
                else:
                    logger.info(f"[kg_watcher] file changed: {path.name}")
                    KnowledgeGraphBuilder.update_file(path)
            except Exception as e:
                logger.warning(f"[kg_watcher] error processing file {path}: {e}")

    def on_modified(self, event) -> None:
        if not event.is_directory:
            self._trigger_debounce(event.src_path, deleted=False)

    def on_created(self, event) -> None:
        if not event.is_directory:
            self._trigger_debounce(event.src_path, deleted=False)

    def on_deleted(self, event) -> None:
        if not event.is_directory:
            self._trigger_debounce(event.src_path, deleted=True)

    def on_moved(self, event) -> None:
        if not event.is_directory:
            self._trigger_debounce(event.src_path, deleted=True)
            self._trigger_debounce(event.dest_path, deleted=False)


class KnowledgeGraphWatcher:
    def __init__(self) -> None:
        self._observer: Observer | None = None
        self._handler: KnowledgeGraphEventHandler | None = None
        self._running = False

    def start(self) -> None:
        if not HAS_WATCHDOG:
            logger.warning("[kg_watcher] watchdog nao esta instalado, watcher desativado")
            return

        if self._running:
            return

        self._handler = KnowledgeGraphEventHandler()
        self._observer = Observer()

        project_root = RuntimePathResolver.project_root()
        watch_dirs = [
            project_root / "docs",
            project_root / "assistant" / "app",
            project_root / "desktop" / "src"
        ]

        started_any = False
        for d in watch_dirs:
            if d.exists():
                try:
                    self._observer.schedule(self._handler, str(d), recursive=True)
                    logger.info(f"[kg_watcher] monitorando diretorio: {d}")
                    started_any = True
                except Exception as exc:
                    logger.warning(f"[kg_watcher] falha ao monitorar {d}: {exc}")

        if started_any:
            self._observer.start()
            self._running = True
            logger.info("[kg_watcher] iniciado com sucesso")

    def stop(self) -> None:
        if self._observer and self._observer.is_alive():
            self._observer.stop()
            self._observer.join(timeout=3)
            logger.info("[kg_watcher] parado")
        self._running = False
