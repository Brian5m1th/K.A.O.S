from typing import AsyncIterator
from loguru import logger
from app.service.agent_service import AgentService


class SmartRouter:
    def __init__(self):
        logger.info("[start] SmartRouter - __init__")
        self._agent = AgentService()
        logger.debug("[finish] SmartRouter - __init__")

    async def process(self, session_id: str, user_message: str) -> str:
        logger.info("[start] SmartRouter - process")
        result = await self._agent.process_message(session_id, user_message)
        logger.debug("[finish] SmartRouter - process")
        return result

    async def stream(
        self, session_id: str, user_message: str
    ) -> AsyncIterator[str]:
        logger.info("[start] SmartRouter - stream")
        async for token in self._agent.stream_message(session_id, user_message):
            yield token
        logger.debug("[finish] SmartRouter - stream")