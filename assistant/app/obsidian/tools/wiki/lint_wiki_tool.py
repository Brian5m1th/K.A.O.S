from collections import defaultdict
from pathlib import Path
from loguru import logger
from langchain_core.tools import tool

from app.obsidian.tools.wiki.wiki_utils import resolve_wiki_path


def _find_orphans(vault: Path) -> list[str]:
    all_wiki = list(vault.rglob("*.md"))
    all_pages = set()
    links_to = defaultdict(list)
    for f in all_wiki:
        rel = str(f.relative_to(vault))
        if ".draft" in rel:
            continue
        all_pages.add(rel)
        content = f.read_text(encoding="utf-8")
        for match in __import__("re").finditer(r"\[\[([^\]]+)\]\]", content):
            links_to[match.group(1)].append(rel)
    orphans = []
    for page in sorted(all_pages):
        if page == "wiki/index.md" or page == "wiki/log.md":
            continue
        page_ref = page.replace(".md", "").replace("\\", "/")
        page_name = Path(page).stem
        has_inbound = False
        for refs in links_to.values():
            for r in refs:
                if page_ref in r or page_name in r:
                    has_inbound = True
                    break
            if has_inbound:
                break
        if not has_inbound:
            orphans.append(page)
    return orphans


def _find_broken_links(vault: Path) -> list[str]:
    broken = []
    for f in vault.rglob("*.md"):
        if ".draft" in str(f):
            continue
        content = f.read_text(encoding="utf-8")
        rel = str(f.relative_to(vault))
        for match in __import__("re").finditer(r"\[\[([^\]]+)\]\]", content):
            target = match.group(1)
            if "|" in target:
                target = target.split("|")[0]
            target_path = target + ".md"
            if not (vault / target_path).exists():
                broken.append(f"{rel} -> [[{target}]]")
    return broken


@tool
def lint_wiki() -> str:
    """Verifica a saúde da wiki: orphans, broken links."""
    logger.info("[info] lint_wiki")
    vault = resolve_wiki_path("wiki").parent
    orphans = _find_orphans(vault)
    broken = _find_broken_links(vault)
    lines = ["## Resultado do Lint\n"]
    if orphans:
        lines.append(f"\n### Orphans ({len(orphans)})\n")
        for o in orphans:
            lines.append(f"- {o}\n")
    else:
        lines.append("\n### Orphans\nNenhuma pagina orphan encontrada.\n")
    if broken:
        lines.append(f"\n### Broken Links ({len(broken)})\n")
        for b in broken:
            lines.append(f"- {b}\n")
    else:
        lines.append("\n### Broken Links\nNenhum link quebrado encontrado.\n")
    return "".join(lines)
