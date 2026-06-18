import re
from pathlib import Path
from datetime import date

from app.config.settings import settings


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def frontmatter(title: str, type_: str, tags: list[str] | None = None, sources: list[str] | None = None) -> str:
    today = date.today().isoformat()
    lines = ["---", f"title: {title}", f"type: {type_}"]
    if tags:
        lines.append("tags:")
        for t in tags:
            lines.append(f"  - {t}")
    if sources:
        lines.append("sources:")
        for s in sources:
            lines.append(f"  - {s}")
    lines.extend([f"created: {today}", f"updated: {today}", "---"])
    return "\n".join(lines) + "\n\n"


def draft_path(path: str) -> str:
    p = Path(path)
    return str(p.with_name(p.stem + ".draft" + p.suffix))


def resolve_wiki_path(relative_path: str) -> Path:
    vault = Path(settings.OBSIDIAN_VAULT_PATH)
    resolved = (vault / relative_path).resolve()
    if not str(resolved).startswith(str(vault.resolve())):
        raise PermissionError(f"Acesso negado fora do Vault: {relative_path}")
    return resolved


def wiki_path(subdir: str, name: str) -> str:
    return f"wiki/{subdir}/{slugify(name)}.md"


def source_path(name: str) -> str:
    from datetime import date
    return f"wiki/sources/{date.today().isoformat()}_{slugify(name)}.md"
