from loguru import logger
from langchain_core.tools import tool
from app.config.settings import settings
from pathlib import Path


def _get_vault_path() -> Path:
    return Path(settings.OBSIDIAN_VAULT_PATH)


@tool
def list_projects() -> dict:
    """Lista projetos no Vault Obsidian (pastas de primeiro nivel com notas .md)."""
    logger.info("[info] list_projects - listando projetos")
    vault = _get_vault_path()
    projects = []
    for entry in sorted(vault.iterdir()):
        if entry.is_dir() and not entry.name.startswith("."):
            md_files = list(entry.rglob("*.md"))
            if md_files:
                projects.append({
                    "name": entry.name,
                    "notes": len(md_files),
                })
    return {"total": len(projects), "projects": projects}