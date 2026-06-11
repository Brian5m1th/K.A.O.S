from typing import AsyncIterator
from loguru import logger
from app.service.agent_service import AgentService


class SmartRouter:
    def __init__(self):
        logger.info("[start] SmartRouter - __init__")
        self._agent = AgentService()
        logger.debug("[finish] SmartRouter - __init__")

    async def process(
        self, session_id: str, user_message: str, user_id: str = "", username: str = "", role: str = "user"
    ) -> str:
        logger.info(f"[start] SmartRouter - process [user={user_id}]")
        result = await self._agent.process_message(session_id, user_message, user_id, username, role)
        logger.debug("[finish] SmartRouter - process")
        return result

    async def stream(
        self, session_id: str, user_message: str, user_id: str = "", username: str = "", role: str = "user"
    ) -> AsyncIterator[str]:
        logger.info(f"[start] SmartRouter - stream [user={user_id}]")
        async for token in self._agent.stream_message(session_id, user_message, user_id, username, role):
            yield token
        logger.debug("[finish] SmartRouter - stream")