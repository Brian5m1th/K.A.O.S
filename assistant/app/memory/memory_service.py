from datetime import datetime
from pathlib import Path
from loguru import logger
from app.config.settings import settings


class MemoryService:
    def __init__(self) -> None:
        self._vault = Path(settings.OBSIDIAN_VAULT_PATH)
        self._base_dir = self._vault / "users"
        self._base_dir.mkdir(parents=True, exist_ok=True)

    def _user_dir(self, user_id: str) -> Path:
        user_path = self._base_dir / user_id
        user_path.mkdir(parents=True, exist_ok=True)
        return user_path

    def _default_user(self) -> str:
        return "default"

    def save_conversation(
        self, user_id: str, session_id: str, summary: str, user_message: str, assistant_response: str
    ) -> str:
        uid = user_id or self._default_user()
        logger.info(f"[start] MemoryService - save_conversation [user={uid}]")
        user_path = self._user_dir(uid)
        date_str = datetime.now().strftime("%Y-%m-%d")
        time_str = datetime.now().strftime("%H%M%S")
        filename = f"conversa_{date_str}_{time_str}_{session_id[:8]}.md"
        filepath = user_path / filename

        content = f"""# Conversa - {date_str}

**Sessao:** {session_id}
**Usuario:** {uid}
**Horario:** {datetime.now().strftime("%H:%M:%S")}

## Resumo

{summary}

## Usuario

{user_message}

## Assistente

{assistant_response}
"""
        filepath.write_text(content, encoding="utf-8")
        logger.info(f"[info] MemoryService - conversa salva: {filename} [user={uid}]")
        logger.debug("[finish] MemoryService - save_conversation")
        return str(filepath.relative_to(self._vault))

    def save_preference(self, user_id: str, key: str, value: str) -> None:
        uid = user_id or self._default_user()
        logger.info(f"[start] MemoryService - save_preference [user={uid}]")
        user_path = self._user_dir(uid)
        prefs_file = user_path / "preferencias.md"

        if prefs_file.exists():
            content = prefs_file.read_text(encoding="utf-8")
        else:
            content = f"# Preferencias do Usuario - {uid}\n\n"

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
        logger.info(f"[info] MemoryService - preferencia salva: {key} [user={uid}]")
        logger.debug("[finish] MemoryService - save_preference")

    def get_preferences(self, user_id: str = "") -> str:
        uid = user_id or self._default_user()
        user_path = self._user_dir(uid)
        prefs_file = user_path / "preferencias.md"
        if prefs_file.exists():
            return prefs_file.read_text(encoding="utf-8")
        return ""

    def list_recent_conversations(self, user_id: str = "", limit: int = 5) -> list[str]:
        uid = user_id or self._default_user()
        logger.info(f"[start] MemoryService - list_recent_conversations [user={uid}]")
        user_path = self._user_dir(uid)
        files = sorted(
            user_path.glob("conversa_*.md"),
            key=lambda f: f.stat().st_mtime,
            reverse=True,
        )
        result = [str(f.relative_to(self._vault)) for f in files[:limit]]
        logger.debug("[finish] MemoryService - list_recent_conversations")
        return result
