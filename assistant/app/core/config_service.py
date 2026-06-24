"""
Config Service for K.A.O.S.

Manages kaos.config.json (public settings) and kaos.secrets.json (isolated credentials)
with schema versioning, migration, and opportunistic legacy data import.
"""

import json
import shutil
import sys
import time
from pathlib import Path

from loguru import logger

from app.core.runtime_path_resolver import RuntimePathResolver

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
SCHEMA_VERSION = 1

CONFIG_FILE_NAME = "kaos.config.json"
SECRETS_FILE_NAME = "kaos.secrets.json"
BACKUP_EXT = ".bak"

# Legacy files (to be migrated and removed)
LEGACY_FILES = [
    ("data", "settings.json"),
    ("data", "provider_config.json"),
    ("data", "integrations.json"),
]

DEFAULT_CONFIG: dict = {
    "schemaVersion": SCHEMA_VERSION,
    "theme": "dark",
    "accent_color": "#3B82F6",
    "language": "pt-BR",
    "telemetry": True,
    "providers": {},
    "integrations": {},
    "_activeProvider": "ollama",
    "_fallbackChain": [],
    "_embeddingModel": "",
}

# ---------------------------------------------------------------------------
# Helpers — file permissions
# ---------------------------------------------------------------------------


def _set_restricted_permissions(path: Path, *, is_secrets: bool = True) -> None:
    """Restrict file access to the current user only.

    - Unix: chmod 0o600
    - Windows: use pywin32 to set ACL to current user only (when is_secrets)
    """
    if not path.exists():
        return
    if sys.platform != "win32":
        # Unix — simple chmod
        path.chmod(0o600 if is_secrets else 0o644)
        return

    # Windows — attempt ACL restriction for secrets via pywin32
    if not is_secrets:
        return  # only restrict secrets files
    try:
        import win32security
        import win32api
        import win32con

        # Get current user SID
        token = win32security.OpenProcessToken(
            win32api.GetCurrentProcess(), win32con.TOKEN_QUERY
        )
        user_sid = win32security.GetTokenInformation(
            token, win32security.TokenUser
        )[0]
        token.Close()

        # Build ACL with single entry for current user (full control)
        sd = win32security.SECURITY_DESCRIPTOR()
        acl = win32security.ACL()
        acl.AddAccessAllowedAce(
            win32security.ACL_REVISION,
            win32con.GENERIC_READ | win32con.GENERIC_WRITE,
            user_sid,
        )
        sd.SetSecurityDescriptorDacl(1, acl, 0)
        win32security.SetFileSecurity(
            str(path), win32security.DACL_SECURITY_INFORMATION, sd
        )
        logger.debug("[config] Windows ACL set on {}", path)
    except Exception as exc:
        logger.warning(
            "[config] could not set restricted ACL on {}: {}", path, exc
        )


# ---------------------------------------------------------------------------
# Retry helper for Windows file locks
# ---------------------------------------------------------------------------


def _write_with_retry(path: Path, content: str, *, max_retries: int = 3) -> None:
    """Write file with exponential backoff retry for Windows file-lock scenarios."""
    for attempt in range(max_retries):
        try:
            path.write_text(content, encoding="utf-8")
            return
        except PermissionError as exc:
            if attempt < max_retries - 1:
                wait = 0.1 * (2 ** attempt)
                logger.debug(
                    "[config] write lock on {} (attempt {}/{}), retrying in {:.1f}s",
                    path,
                    attempt + 1,
                    max_retries,
                    wait,
                )
                time.sleep(wait)
            else:
                logger.error(
                    "[config] failed to write {} after {} attempts: {}",
                    path,
                    max_retries,
                    exc,
                )
                raise


# ---------------------------------------------------------------------------
# Migration helpers
# ---------------------------------------------------------------------------

_SUPPORTED_SECRET_KEYS = {"apiKey", "token", "botToken", "webhookUrl"}


def _extract_secrets(data: dict, secrets: dict) -> dict:
    """Recursively extract known secret fields into secrets dict.

    Returns the cleaned data (with secret fields removed).
    """
    cleaned = {}
    for key, value in data.items():
        if key in _SUPPORTED_SECRET_KEYS and isinstance(value, str) and value:
            secrets[key] = value
            # Keep a placeholder reference in the public config
            cleaned[key] = ""
        elif isinstance(value, dict):
            cleaned[key] = _extract_secrets(value, secrets)
        else:
            cleaned[key] = value
    return cleaned


# ---------------------------------------------------------------------------
# ConfigService
# ---------------------------------------------------------------------------


class ConfigService:
    """Central configuration manager for K.A.O.S.

    Reads and writes ``kaos.config.json`` and ``kaos.secrets.json``
    inside the config directory resolved by ``RuntimePathResolver``.
    """

    _config_path: Path | None = None
    _secrets_path: Path | None = None

    # ------------------------------------------------------------------
    # Paths
    # ------------------------------------------------------------------

    @classmethod
    def _ensure_paths(cls) -> None:
        if cls._config_path is not None:
            return
        config_dir = RuntimePathResolver.get_config_path()
        cls._config_path = config_dir / CONFIG_FILE_NAME
        cls._secrets_path = config_dir / SECRETS_FILE_NAME

    @classmethod
    def config_path(cls) -> Path:
        cls._ensure_paths()
        return cls._config_path  # type: ignore[return-value]

    @classmethod
    def secrets_path(cls) -> Path:
        cls._ensure_paths()
        return cls._secrets_path  # type: ignore[return-value]

    # ------------------------------------------------------------------
    # Public config (kaos.config.json)
    # ------------------------------------------------------------------

    @classmethod
    def load_config(cls) -> dict:
        """Load configuration with automatic migration from legacy files."""
        cls._ensure_paths()
        config_file = cls.config_path()

        # --- Step 1: attempt legacy migration (first run only) ---
        if not config_file.exists():
            legacy_data = cls._try_migrate_legacy()
            if legacy_data is not None:
                return legacy_data

        # --- Step 2: read current file ---
        if config_file.exists():
            try:
                data = json.loads(config_file.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, PermissionError) as exc:
                logger.error("[config] failed to decode {}: {}", config_file, exc)
                # Backup corrupted file
                backup = config_file.with_suffix(config_file.suffix + BACKUP_EXT)
                shutil.copy2(str(config_file), str(backup))
                logger.warning("[config] backed up corrupted file to {}", backup)
                data = {}
        else:
            data = {}

        # --- Step 3: ensure schemaVersion ---
        current_version = data.get("schemaVersion", 0)
        if current_version < SCHEMA_VERSION:
            data = cls._migrate_schema(data, from_version=current_version)
            data["schemaVersion"] = SCHEMA_VERSION
            cls.save_config(data)

        # --- Step 4: merge with defaults (fill missing keys) ---
        merged = dict(DEFAULT_CONFIG)
        merged.update(data)
        merged["schemaVersion"] = SCHEMA_VERSION
        return merged

    @classmethod
    def save_config(cls, data: dict) -> None:
        """Validate, backup, and persist configuration."""
        cls._ensure_paths()
        config_file = cls.config_path()

        # Ensure schemaVersion
        data["schemaVersion"] = SCHEMA_VERSION

        # Backup current file if it exists
        cls._backup_config()

        # Serialise and write
        content = json.dumps(data, indent=2, ensure_ascii=False)
        _write_with_retry(config_file, content)
        logger.info("[config] saved config to {} (schemaVersion={})", config_file, SCHEMA_VERSION)

    # ------------------------------------------------------------------
    # Secrets (kaos.secrets.json)
    # ------------------------------------------------------------------

    @classmethod
    def load_secrets(cls) -> dict:
        """Load secrets from the isolated secrets file."""
        cls._ensure_paths()
        secrets_file = cls.secrets_path()
        if not secrets_file.exists():
            return {}
        try:
            data = json.loads(secrets_file.read_text(encoding="utf-8"))
            return data if isinstance(data, dict) else {}
        except (json.JSONDecodeError, PermissionError) as exc:
            logger.warning("[config] failed to decode secrets: {}", exc)
            return {}

    @classmethod
    def save_secrets(cls, data: dict) -> None:
        """Persist secrets with restricted file permissions."""
        cls._ensure_paths()
        secrets_file = cls.secrets_path()
        # Serialise
        content = json.dumps(data, indent=2, ensure_ascii=False)
        _write_with_retry(secrets_file, content)
        # Apply restricted permissions
        _set_restricted_permissions(secrets_file, is_secrets=True)
        logger.info("[config] saved secrets to {} (restricted permissions)", secrets_file)

    # ------------------------------------------------------------------
    # Backup
    # ------------------------------------------------------------------

    @classmethod
    def _backup_config(cls) -> None:
        """Create a .bak copy of the current config file before overwriting."""
        config_file = cls.config_path()
        if not config_file.exists():
            return
        backup = config_file.with_suffix(config_file.suffix + BACKUP_EXT)
        try:
            shutil.copy2(str(config_file), str(backup))
            logger.debug("[config] backed up {} -> {}", config_file, backup)
        except OSError as exc:
            logger.warning("[config] backup failed: {}", exc)

    # ------------------------------------------------------------------
    # Schema migration
    # ------------------------------------------------------------------

    @classmethod
    def _migrate_schema(cls, data: dict, from_version: int) -> dict:
        """Run incremental schema migrations.

        Currently supports: 0 → 1
        """
        if from_version >= SCHEMA_VERSION:
            return data

        logger.info("[config] migrating schema from v{} to v{}", from_version, SCHEMA_VERSION)

        # v0 → v1: ensure all top-level keys exist
        if from_version < 1:
            # Ensure providers dict exists
            if "providers" not in data:
                data["providers"] = {}
            # Ensure integrations dict exists
            if "integrations" not in data:
                data["integrations"] = {}
            # Extract any loose apiKey fields into secrets
            secrets = cls.load_secrets()
            data = _extract_secrets(data, secrets)
            if secrets:
                cls.save_secrets(secrets)

        return data

    # ------------------------------------------------------------------
    # Legacy migration (opportunistic, one-time)
    # ------------------------------------------------------------------

    @classmethod
    def _try_migrate_legacy(cls) -> dict | None:
        """Check for legacy data files and merge them into the new format.

        Returns the merged config dict if migration was performed, else None.
        """
        project_root = RuntimePathResolver.project_root()
        legacy_sources = {}

        for rel_dir, filename in LEGACY_FILES:
            path = project_root / rel_dir / filename
            if path.exists():
                try:
                    legacy_sources[filename] = json.loads(
                        path.read_text(encoding="utf-8")
                    )
                    logger.info("[config] found legacy file: {}", path)
                except (json.JSONDecodeError, PermissionError) as exc:
                    logger.warning("[config] could not read legacy {}: {}", path, exc)

        if not legacy_sources:
            return None  # no legacy data to migrate

        # --- Merge into new format ---
        merged = dict(DEFAULT_CONFIG)

        # settings.json
        if "settings.json" in legacy_sources:
            s = legacy_sources["settings.json"]
            for key in ("theme", "accent_color", "language", "telemetry"):
                if key in s:
                    merged[key] = s[key]

        # provider_config.json
        if "provider_config.json" in legacy_sources:
            pc = legacy_sources["provider_config.json"]
            providers = pc.get("providers", {})
            if not providers:
                # Some versions stored provider data at top level
                providers = {k: v for k, v in pc.items() if isinstance(v, dict)}
            merged["providers"] = providers
            if "_activeProvider" in pc:
                merged["_activeProvider"] = pc["_activeProvider"]
            if "_fallbackChain" in pc:
                merged["_fallbackChain"] = pc["_fallbackChain"]
            if "_embeddingModel" in pc:
                merged["_embeddingModel"] = pc["_embeddingModel"]

        # integrations.json
        if "integrations.json" in legacy_sources:
            integrations = legacy_sources["integrations.json"]
            if isinstance(integrations, dict):
                # It might be {"integrations": [...]} or direct dict
                merged["integrations"] = integrations.get("integrations", integrations)

        # --- Extract secrets ---
        secrets: dict = {}
        merged = _extract_secrets(merged, secrets)

        # --- Persist new files ---
        merged["schemaVersion"] = SCHEMA_VERSION
        cls.save_config(merged)
        if secrets:
            cls.save_secrets(secrets)

        # --- Remove legacy files ---
        for rel_dir, filename in LEGACY_FILES:
            path = project_root / rel_dir / filename
            if path.exists():
                try:
                    path.unlink()
                    logger.info("[config] removed legacy file: {}", path)
                except OSError as exc:
                    logger.warning("[config] could not remove legacy {}: {}", path, exc)

        logger.info("[config] legacy migration completed")
        return merged

    # ------------------------------------------------------------------
    # Convenience: get a specific provider config merged with secrets
    # ------------------------------------------------------------------

    @classmethod
    def get_provider(cls, provider_id: str) -> dict:
        """Return provider config with apiKey from secrets merged in."""
        config = cls.load_config()
        secrets = cls.load_secrets()
        provider = dict(config.get("providers", {}).get(provider_id, {}))
        # Merge apiKey from secrets if present
        provider_secrets = secrets.get("providers", {}).get(provider_id, {})
        for key in _SUPPORTED_SECRET_KEYS:
            if key in provider_secrets and provider_secrets[key]:
                provider[key] = provider_secrets[key]
        return provider
