"""Plugin Registry — Gerenciamento persistente de plugins.

Mantem registro dos plugins instalados em SQLite, permitindo
listar, instalar e remover plugins.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from loguru import logger

from app.core.plugin_sandbox import PluginManifest
from app.core.runtime_path_resolver import RuntimePathResolver


# ---------------------------------------------------------------------------
# Plugin Registry — Persistencia em SQLite
# ---------------------------------------------------------------------------


class PluginRecord:
    """Representacao de um plugin registrado no banco."""

    def __init__(
        self,
        plugin_id: str,
        name: str,
        version: str,
        description: str = "",
        author: str = "",
        wasm_path: str = "",
        manifest_json: str = "{}",
        installed_at: str | None = None,
        enabled: bool = True,
    ) -> None:
        self.plugin_id = plugin_id
        self.name = name
        self.version = version
        self.description = description
        self.author = author
        self.wasm_path = wasm_path
        self.manifest_json = manifest_json
        self.installed_at = installed_at or datetime.now(timezone.utc).isoformat()
        self.enabled = enabled

    @classmethod
    def from_manifest(cls, manifest: PluginManifest, wasm_path: str) -> "PluginRecord":
        return cls(
            plugin_id=manifest.id,
            name=manifest.name,
            version=manifest.version,
            description=manifest.description,
            author=manifest.author,
            wasm_path=wasm_path,
            manifest_json=json.dumps(
                {
                    "id": manifest.id,
                    "name": manifest.name,
                    "version": manifest.version,
                    "description": manifest.description,
                    "author": manifest.author,
                    "entrypoint": manifest.entrypoint,
                    "permissions": manifest.permissions,
                    "allowed_functions": manifest.allowed_functions,
                }
            ),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "plugin_id": self.plugin_id,
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "author": self.author,
            "wasm_path": self.wasm_path,
            "manifest": json.loads(self.manifest_json),
            "installed_at": self.installed_at,
            "enabled": self.enabled,
        }


class PluginRegistry:
    """Gerencia o registro persistente de plugins no SQLite.

    Mantem uma tabela 'plugins' com metadados de cada plugin instalado,
    permitindo consulta, instalacao e remocao.
    """

    def __init__(self, db_path: str | Path | None = None) -> None:
        if db_path is None:
            db_path = RuntimePathResolver.get_data_path() / "plugins_registry.db"
        self._db_path = Path(db_path)
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(str(self._db_path)) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS plugins (
                    plugin_id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    version TEXT NOT NULL,
                    description TEXT DEFAULT '',
                    author TEXT DEFAULT '',
                    wasm_path TEXT DEFAULT '',
                    manifest_json TEXT DEFAULT '{}',
                    installed_at TEXT NOT NULL,
                    enabled INTEGER DEFAULT 1
                )
            """)
            conn.commit()

    def install(
        self,
        plugin_id: str,
        name: str,
        version: str,
        description: str = "",
        author: str = "",
        wasm_path: str = "",
        manifest: dict | None = None,
    ) -> PluginRecord:
        """Registra um plugin no banco de dados."""
        record = PluginRecord(
            plugin_id=plugin_id,
            name=name,
            version=version,
            description=description,
            author=author,
            wasm_path=wasm_path,
            manifest_json=json.dumps(manifest or {}),
        )
        with sqlite3.connect(str(self._db_path)) as conn:
            conn.execute(
                """INSERT OR REPLACE INTO plugins
                   (plugin_id, name, version, description, author,
                    wasm_path, manifest_json, installed_at, enabled)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    record.plugin_id,
                    record.name,
                    record.version,
                    record.description,
                    record.author,
                    record.wasm_path,
                    record.manifest_json,
                    record.installed_at,
                    1 if record.enabled else 0,
                ),
            )
            conn.commit()
        logger.info("[registry] plugin installed: {} v{}", plugin_id, version)
        return record

    def uninstall(self, plugin_id: str) -> bool:
        """Remove o registro de um plugin."""
        with sqlite3.connect(str(self._db_path)) as conn:
            cursor = conn.execute(
                "DELETE FROM plugins WHERE plugin_id = ?", (plugin_id,)
            )
            conn.commit()
            removed = cursor.rowcount > 0
        if removed:
            logger.info("[registry] plugin uninstalled: {}", plugin_id)
        return removed

    def list_plugins(self) -> list[PluginRecord]:
        """Lista todos os plugins registrados."""
        with sqlite3.connect(str(self._db_path)) as conn:
            rows = conn.execute(
                "SELECT plugin_id, name, version, description, author, "
                "wasm_path, manifest_json, installed_at, enabled "
                "FROM plugins ORDER BY installed_at DESC"
            ).fetchall()
        return [PluginRecord(*row) for row in rows]

    def get_plugin(self, plugin_id: str) -> PluginRecord | None:
        """Busca um plugin pelo ID."""
        with sqlite3.connect(str(self._db_path)) as conn:
            row = conn.execute(
                "SELECT plugin_id, name, version, description, author, "
                "wasm_path, manifest_json, installed_at, enabled "
                "FROM plugins WHERE plugin_id = ?",
                (plugin_id,),
            ).fetchone()
        return PluginRecord(*row) if row else None

    def set_enabled(self, plugin_id: str, enabled: bool) -> bool:
        """Ativa/desativa um plugin."""
        with sqlite3.connect(str(self._db_path)) as conn:
            cursor = conn.execute(
                "UPDATE plugins SET enabled = ? WHERE plugin_id = ?",
                (1 if enabled else 0, plugin_id),
            )
            conn.commit()
            return cursor.rowcount > 0
