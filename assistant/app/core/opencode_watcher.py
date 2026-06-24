"""
OpenCode Watcher — monitors the ``.opencode/`` directory for file changes
and invalidates the API cache so changes are reflected without restart.

Features:
- Watchdog observer with 250ms debounce
- Graceful fallback to on-demand scanning on UNC / network paths
- Thread-safe cache invalidation
"""

import threading
from pathlib import Path

from loguru import logger

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    HAS_WATCHDOG = True
except ImportError:
    HAS_WATCHDOG = False
    logger.warning("[opencode_watcher] watchdog not available; falling back to on-demand scan mode")


DEBOUNCE_INTERVAL = 0.25  # 250ms


class _OpenCodeHandler(FileSystemEventHandler):
    """Watchdog event handler with debounce."""

    def __init__(self, callback) -> None:
        super().__init__()
        self._callback = callback
        self._timer: threading.Timer | None = None
        self._lock = threading.Lock()

    def _debounce_invalidate(self) -> None:
        with self._lock:
            if self._timer:
                self._timer.cancel()
            self._timer = threading.Timer(DEBOUNCE_INTERVAL, self._callback)
            self._timer.daemon = True
            self._timer.start()

    def on_modified(self, event) -> None:
        if not event.is_directory and event.src_path.endswith((".md", ".yaml", ".yml", ".json")):
            self._debounce_invalidate()

    def on_created(self, event) -> None:
        if not event.is_directory and event.src_path.endswith((".md", ".yaml", ".yml", ".json")):
            self._debounce_invalidate()

    def on_deleted(self, event) -> None:
        if not event.is_directory:
            self._debounce_invalidate()


class OpenCodeWatcher:
    """Background watcher for the ``.opencode/`` directory.

    Usage::

        watcher = OpenCodeWatcher()
        watcher.start()
        ...
        watcher.stop()
    """

    def __init__(self, opencode_path: Path | None = None) -> None:
        from app.core.runtime_path_resolver import RuntimePathResolver

        self._path = opencode_path or RuntimePathResolver.get_opencode_path()
        self._observer: Observer | None = None
        self._handler: _OpenCodeHandler | None = None
        self._fallback_mode: bool = False
        self._cache_dirty: bool = True

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def start(self) -> None:
        """Start the filesystem watcher.

        Falls back gracefully to on-demand scanning if the path is on
        a network filesystem (UNC) where watchdog cannot register.
        """
        if not HAS_WATCHDOG:
            logger.warning("[opencode_watcher] watchdog library not installed, using on-demand scan mode")
            self._fallback_mode = True
            return

        if not self._path.exists():
            logger.warning("[opencode_watcher] path '{}' does not exist yet, skipping", self._path)
            self._fallback_mode = True
            return

        self._handler = _OpenCodeHandler(self._invalidate_cache)
        self._observer = Observer()

        try:
            self._observer.schedule(self._handler, str(self._path), recursive=True)
            self._observer.start()
            logger.info("[opencode_watcher] watching {} (recursive)", self._path)
        except OSError as exc:
            logger.warning(
                "[opencode_watcher] cannot watch '{}' ({}), switching to on-demand scan mode",
                self._path,
                exc,
            )
            self._fallback_mode = True
            self._observer = None

    def stop(self) -> None:
        """Stop the filesystem watcher."""
        if self._observer and self._observer.is_alive():
            self._observer.stop()
            self._observer.join(timeout=3)
            logger.info("[opencode_watcher] stopped")
        self._observer = None

    def is_dirty(self) -> bool:
        """Return True if the cache needs refresh."""
        return self._cache_dirty

    def mark_clean(self) -> None:
        """Mark the cache as clean after a refresh."""
        self._cache_dirty = False

    def is_fallback_mode(self) -> bool:
        """Return True if running in on-demand (no watchdog) mode."""
        return self._fallback_mode

    # ------------------------------------------------------------------
    # Internal
    # ------------------------------------------------------------------

    def _invalidate_cache(self) -> None:
        logger.debug("[opencode_watcher] cache invalidated")
        self._cache_dirty = True
