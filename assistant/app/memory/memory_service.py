from datetime import datetime
from pathlib import Path
from loguru import logger
from app.config.settings import settings


class MemoryService:
    def __init__(self) -> None:
        self._vault = Path(settings.OBSIDIAN_VAULT_PATH)
        self._memories_dir = self._vault / "IA"
        self._memories_dir.mkdir(parents=True, exist_ok=True)

    def save_conversation(
        self, session_id: str, summary: str, user_message: str, assistant_response: str
    ) -> str:
        logger.info("[start] MemoryService - save_conversation")
        date_str = datetime.now().strftime("%Y-%m-%d")
        time_str = datetime.now().strftime("%H%M%S")
        filename = f"conversa_{date_str}_{time_str}_{session_id[:8]}.md"
        filepath = self._memories_dir / filename

        content = f"""# Conversa - {date_str}

**Sessao:** {session_id}
**Horario:** {datetime.now().strftime("%H:%M:%S")}

## Resumo

{summary}

## Usuario

{user_message}

## Assistente

{assistant_response}
"""
        filepath.write_text(content, encoding="utf-8")
        logger.info(f"[info] MemoryService - conversa salva: {filename}")
        logger.debug("[finish] MemoryService - save_conversation")
        return str(filepath.relative_to(self._vault))

    def save_preference(self, key: str, value: str) -> None:
        logger.info("[start] MemoryService - save_preference")
        prefs_file = self._memories_dir / "preferencias.md"

        if prefs_file.exists():
            content = prefs_file.read_text(encoding="utf-8")
        else:
            content = "# Preferencias do Usuario\n\n"

        if f"- **{key}**:" in content:
            lines = content.split("\n")
            for i, line in enumerate(lines):
                if line.startswith(f"- **{key}**:"):
                    lines[i] = f"- **{key}**: {value}"
                    break
            content = "\n".join(lines)
        else:
            content += f"- **{key}**: {value}\n"

        prefs_file.write_text(content, encoding="utf-8")
        logger.info(f"[info] MemoryService - preferencia salva: {key}")
        logger.debug("[finish] MemoryService - save_preference")

    def get_preferences(self) -> str:
        prefs_file = self._memories_dir / "preferencias.md"
        if prefs_file.exists():
            return prefs_file.read_text(encoding="utf-8")
        return ""

    def list_recent_conversations(self, limit: int = 5) -> list[str]:
        logger.info("[start] MemoryService - list_recent_conversations")
        files = sorted(
            self._memories_dir.glob("conversa_*.md"),
            key=lambda f: f.stat().st_mtime,
            reverse=True,
        )
        result = [str(f.relative_to(self._vault)) for f in files[:limit]]
        logger.debug("[finish] MemoryService - list_recent_conversations")
        return result
