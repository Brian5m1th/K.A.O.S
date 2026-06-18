from loguru import logger
from langchain_core.tools import tool

from app.obsidian.tools.read_note_tool import read_note


@tool
def read_wiki_page(path: str) -> dict:
    """Lê uma página da wiki pelo caminho relativo (ex: wiki/entities/brian.md)."""
    logger.info(f"[info] read_wiki_page - {path}")
    return read_note.invoke({"path": path})
