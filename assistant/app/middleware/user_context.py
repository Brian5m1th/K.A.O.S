from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from loguru import logger


class UserContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        user_id = request.headers.get("x-user-id", "")
        username = request.headers.get("x-username", "")
        role = request.headers.get("x-user-role", "")

        # Only overwrite state if headers are explicitly provided
        # Otherwise preserve values set by ApiKeyMiddleware (JWT or API key)
        if user_id:
            request.state.user_id = user_id
        if username:
            request.state.username = username
        if role:
            request.state.role = role

        if user_id:
            logger.debug(
                f"[middleware] user_context - id={user_id} username={username} role={role}"
            )

        return await call_next(request)
