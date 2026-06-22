from datetime import datetime
from loguru import logger
from app.desktop.workspace.manager import WorkspaceManager


class WorkspaceStorage:
    def __init__(self) -> None:
        self._manager = WorkspaceManager()

    def save(self, snapshot, slug: str, user_slug: str) -> str:
        now = datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        base = self._manager.conversations_path(slug, year, month)
        base.mkdir(parents=True, exist_ok=True)
        safe_title = (snapshot.title or "conversa").replace(" ", "-").replace("/", "-").lower()[:80]
        filename = f"{now.strftime('%Y-%m-%d')}-{safe_title}.md"
        filepath = base / filename

        lines = [f"# {snapshot.title or 'Conversa'}", ""]
        if snapshot.summary:
            lines.append(f"**Resumo:** {snapshot.summary}")
            lines.append("")
        if snapshot.tags:
            lines.append(f"**Tags:** {', '.join(snapshot.tags)}")
            lines.append("")
        lines.append(f"**Salvo em:** {now.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        if snapshot.metadata:
            lines.append(f"**Sessao:** {snapshot.metadata.get('session_id', '')}")
            lines.append("")
        if snapshot.history:
            for msg in snapshot.history:
                lines.append(f"## {msg.role.title()}")
                lines.append("")
                lines.append(msg.content)
                lines.append("")
        content = "\n".join(lines)
        filepath.write_text(content, encoding="utf-8")
        logger.info(f"[info] WorkspaceStorage - salvo: {filename}")
        return str(filepath)
