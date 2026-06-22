import asyncio
from pathlib import Path
from datetime import datetime, timezone
from loguru import logger

from app.audit.vault_sync import VaultSync
from app.audit.drl_snapshot import DRLSnapshotManager


class SDDWatcher:
    _watched_dirs = [Path("docs/sdd"), Path("docs/runtime")]
    _interval_seconds = 10
    _running = False

    @classmethod
    def set_interval(cls, seconds: int) -> None:
        cls._interval_seconds = seconds

    @classmethod
    async def start(cls) -> None:
        if cls._running:
            return
        cls._running = True
        logger.info("[sdd_watcher] started monitoring SDD directories")

        last_states: dict[str, float] = {}
        for d in cls._watched_dirs:
            d.mkdir(parents=True, exist_ok=True)
            for f in d.rglob("*.md"):
                last_states[str(f)] = f.stat().st_mtime

        while cls._running:
            await asyncio.sleep(cls._interval_seconds)
            changes = cls._detect_changes(last_states)
            if changes:
                logger.info(f"[sdd_watcher] detected {len(changes)} changes")
                VaultSync.sync_to_vault(changes)
                DRLSnapshotManager.build_snapshot()

    @classmethod
    def stop(cls) -> None:
        cls._running = False
        logger.info("[sdd_watcher] stopped")

    @classmethod
    def _detect_changes(cls, last_states: dict[str, float]) -> list[Path]:
        changes = []
        for d in cls._watched_dirs:
            if not d.exists():
                continue
            for f in d.rglob("*.md"):
                current_mtime = f.stat().st_mtime
                key = str(f)
                if key not in last_states or last_states[key] != current_mtime:
                    changes.append(f)
                last_states[key] = current_mtime
        return changes