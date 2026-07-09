from contextvars import ContextVar
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from loguru import logger

# ContextVar definitions for thread-safe propagation of user context
user_id_context: ContextVar[str] = ContextVar("user_id", default="")
username_context: ContextVar[str] = ContextVar("username", default="")
role_context: ContextVar[str] = ContextVar("role", default="user")


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

        user_id = request.state.user_id
        username = request.state.username
        role = request.state.role

        # Fallback to headers for unauthenticated public requests or where state is empty
        if not user_id:
            user_id = request.headers.get("X-User-Id", "")
        if not username:
            username = request.headers.get("X-Username", "anonymous")
        if not role:
            role = request.headers.get("X-User-Role", "user")

        # Set context variables for downstream services and loguru
        token_user_id = user_id_context.set(user_id)
        token_username = username_context.set(username)
        token_role = role_context.set(role)

        try:
            if user_id:
                logger.debug(
                    f"[middleware] user_context - id={user_id} username={username} role={role}"
                )
            response = await call_next(request)
            return response
        finally:
            # Reset context variables
            user_id_context.reset(token_user_id)
            username_context.reset(token_username)
            role_context.reset(token_role)
