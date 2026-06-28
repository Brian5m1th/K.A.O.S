from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from loguru import logger


class UserContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        # Prevent header injection of user context: do not read x-user- headers directly from untrusted client requests.
        # Authenticators (like ApiKeyMiddleware) will set request.state variables.
        if not hasattr(request.state, "user_id"):
            request.state.user_id = ""
        if not hasattr(request.state, "username"):
            request.state.username = ""
        if not hasattr(request.state, "role"):
            request.state.role = "user"

        if request.state.user_id:
            logger.debug(
                f"[middleware] user_context - id={request.state.user_id} username={request.state.username} role={request.state.role}"
            )

        return await call_next(request)

