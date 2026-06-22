from datetime import datetime
from loguru import logger
from app.domain.chat import Message


class ConversationSummarizer:
    @staticmethod
    def generate(history: list[Message]) -> str:
        if not history:
            logger.debug("[skip] ConversationSummarizer - empty history")
            return ""
        first_user = ""
        last_user = ""
        for msg in history:
            if msg.role == "user":
                if not first_user:
                    first_user = msg.content[:120]
                last_user = msg.content[:120]
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        if first_user and first_user != last_user:
            summary = f"{first_user} / {last_user} ({now})"
        elif last_user:
            summary = f"{last_user} ({now})"
        else:
            summary = f"Conversa em {now}"
        logger.debug(f"[finish] ConversationSummarizer - summary={summary[:60]}...")
        return summary

    @staticmethod
    def generate_title(history: list[Message]) -> str:
        if not history:
            return "conversa"
        first_user = ""
        for msg in history:
            if msg.role == "user":
                first_user = msg.content[:80]
                break
        if first_user:
            safe = first_user.strip().replace(" ", "-").lower()[:60]
            return safe
        return "conversa"
