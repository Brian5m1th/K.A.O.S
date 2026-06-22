from pathlib import Path
from loguru import logger
import yaml
import re


class FrontmatterParser:
    @staticmethod
    def parse(file_path: Path) -> dict | None:
        try:
            content = file_path.read_text(encoding="utf-8")
        except Exception:
            return None

        match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if not match:
            return None

        try:
            return yaml.safe_load(match.group(1))
        except Exception as e:
            logger.warning(f"[frontmatter_parser] failed to parse {file_path}: {e}")
            return None

    @staticmethod
    def serialize(meta: dict) -> str:
        return f"---\n{yaml.dump(meta, allow_unicode=True, sort_keys=False).strip()}\n---\n\n"

    @staticmethod
    def extract_links(content: str) -> list[str]:
        links = re.findall(r"\[\[([^\]]+)\]\]", content)
        return list(set(links))

    @staticmethod
    def extract_tags(content: str) -> list[str]:
        tags = re.findall(r"#([a-zA-Z0-9_-]+)", content)
        system_tags = [t for t in tags if t not in ("kaos", "index", "home")]
        return list(set(system_tags))

    @staticmethod
    def has_frontmatter(file_path: Path) -> bool:
        return FrontmatterParser.parse(file_path) is not None
