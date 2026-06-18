from datetime import date
from loguru import logger
from langchain_core.tools import tool

from app.obsidian.tools.wiki.wiki_utils import resolve_wiki_path


@tool
def append_log(entry: str) -> str:
    """Adiciona uma entrada no log.md da wiki (append-only)."""
    logger.info(f"[info] append_log - {entry[:60]}")
    log_path = resolve_wiki_path("wiki/log.md")
    today = date.today().isoformat()
    line = f"\n## {today}\n\n- {entry}\n"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(line)
    return f"Log atualizado: {entry}"
