from pathlib import Path
from loguru import logger
from langchain_core.tools import tool

from app.obsidian.tools.wiki.wiki_utils import resolve_wiki_path


def _scan_pages(vault: Path, subdir: str) -> list[tuple[str, str]]:
    pages = []
    base = vault / "wiki" / subdir
    if base.exists():
        for f in sorted(base.glob("*.md")):
            if f.stem.endswith(".draft"):
                continue
            name = f.stem
            pages.append((name, f"wiki/{subdir}/{f.name}"))
    return pages


def _page_title(filepath: Path) -> str:
    content = filepath.read_text(encoding="utf-8")
    for line in content.splitlines():
        if line.startswith("title: "):
            return line.replace("title: ", "", 1).strip()
    return filepath.stem


@tool
def update_index() -> str:
    """Regenera o index.md da wiki varrendo todas as páginas."""
    logger.info("[info] update_index")
    vault = resolve_wiki_path("wiki").parent
    sections = {
        "Entities": "entities",
        "Concepts": "concepts",
        "Sources": "sources",
        "Synthesis": "synthesis",
    }
    lines = ["# Wiki — Índice\n", "Catálogo vivo de todas as páginas wiki.\n"]
    for section, subdir in sections.items():
        pages = _scan_pages(vault, subdir)
        lines.append(f"\n## {section}\n")
        if not pages:
            lines.append("_Empty_\n")
        else:
            for name, path in pages:
                filepath = vault / path
                title = _page_title(filepath) if filepath.exists() else name
                lines.append(f"- [[{path}|{title}]]\n")
    index_path = vault / "wiki" / "index.md"
    index_path.write_text("".join(lines), encoding="utf-8")
    logger.info(f"[info] update_index - {len(lines)} linhas escritas")
    return "index.md atualizado"
