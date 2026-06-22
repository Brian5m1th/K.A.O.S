from pathlib import Path
from loguru import logger
import shutil

from app.audit.frontmatter_parser import FrontmatterParser


class VaultSync:
    _source_dirs = [Path("docs/sdd"), Path("docs/runtime")]
    _vault_base = Path("docs/vault")

    @classmethod
    def set_vault_base(cls, path: Path) -> None:
        cls._vault_base = path

    @classmethod
    def sync_to_vault(cls, paths: list[Path] | None = None) -> int:
        synced = 0
        sources = paths or cls._source_dirs

        for source_dir in sources:
            if not source_dir.exists():
                continue

            target_dir = cls._vault_base / "sdd"
            target_dir.mkdir(parents=True, exist_ok=True)

            for md_file in source_dir.rglob("*.md"):
                try:
                    target_path = target_dir / md_file.name
                    shutil.copy2(md_file, target_path)
                    synced += 1
                    logger.debug(f"[vault_sync] synced {md_file.name} -> {target_path}")
                except Exception as e:
                    logger.error(f"[vault_sync] failed to sync {md_file.name}: {e}")

        logger.info(f"[vault_sync] synced {synced} files to vault")
        return synced

    @classmethod
    def sync_from_vault(cls, paths: list[Path] | None = None) -> int:
        synced = 0
        vault_source = cls._vault_base / "sdd"

        if not vault_source.exists():
            logger.warning("[vault_sync] vault sdd directory not found")
            return 0

        for md_file in vault_source.rglob("*.md"):
            if not cls._validate_frontmatter(md_file):
                logger.warning(
                    f"[vault_sync] skipping invalid frontmatter: {md_file.name}"
                )
                continue

            try:
                target_path = Path("docs/sdd") / md_file.name
                shutil.copy2(md_file, target_path)
                synced += 1
            except Exception as e:
                logger.error(
                    f"[vault_sync] failed to sync from vault {md_file.name}: {e}"
                )

        logger.info(f"[vault_sync] synced {synced} files from vault")
        return synced

    @classmethod
    def _validate_frontmatter(cls, file_path: Path) -> bool:
        meta = FrontmatterParser.parse(file_path)
        if not meta:
            return False
        required = ["id", "type"]
        return all(key in meta for key in required)

    @classmethod
    def ensure_vault_structure(cls) -> None:
        folders = [
            cls._vault_base / "sdd",
            cls._vault_base / "features",
            cls._vault_base / "systems",
            cls._vault_base / "runtime",
            cls._vault_base / "auto-generated",
        ]
        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)
            logger.debug(f"[vault_sync] ensured vault folder: {folder}")

    @classmethod
    def is_vault_mounted(cls) -> bool:
        return cls._vault_base.exists() and (cls._vault_base / ".git").exists()
