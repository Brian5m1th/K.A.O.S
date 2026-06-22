import hashlib
from uuid import UUID, uuid5, NAMESPACE_DNS
from fastapi import Request, Response
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware

from app.auth.jwt import decode_token

PUBLIC_PATHS = {
    "/health",
    "/docs",
    "/openapi.json",
    "/auth/setup-status",
    "/auth/register",
    "/auth/login",
    "/auth/refresh",
    "/api/setup",
    "/",
    "/metrics",
}

_USER_SALT = "kaos-user-v1"


def _derive_user_id(api_key: str) -> UUID:
    digest = hashlib.sha256(f"{_USER_SALT}:{api_key}".encode()).hexdigest()
    return uuid5(NAMESPACE_DNS, digest)


class ApiKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        if request.method == "OPTIONS":
            return await call_next(request)

        path = request.url.path
        for public in PUBLIC_PATHS:
            if path == public or path.startswith(public + "/"):
                return await call_next(request)

        # Initialize state defaults
        request.state.user_id = ""
        request.state.username = ""
        request.state.role = ""
        request.state.auth_method = ""

        auth_header = request.headers.get("Authorization", "")

        # Try JWT Bearer token first
        if auth_header.startswith("Bearer "):
            token = auth_header[7:]
            payload = decode_token(token)
            if payload:
                user_id = payload.get("sub", "")
                email = payload.get("email", "")
                role = payload.get("role", "user")
                request.state.user_id = user_id
                request.state.username = email
                request.state.role = role
                request.state.auth_method = "jwt"

                logger.bind(event="auth.authenticated", user_id=user_id).info(
                    "[auth] JWT authenticated request from {} - {} {}",
                    request.client.host if request.client else "unknown",
                    request.method,
                    path,
                )
                return await call_next(request)

        # Fall back to API Key
        key = request.headers.get("x-api-key", "")
        if not key:
            if auth_header.startswith("Bearer "):
                key = auth_header[7:]

        app_key = getattr(request.app.state, "api_key", None)
        if app_key is None:
            logger.warning("[auth] API key not configured on app.state")
            return Response(
                status_code=503,
                content='{"detail":"Service not ready"}',
                media_type="application/json",
            )

        if key and key == app_key:
            user_id = _derive_user_id(key)
            request.state.user_id = str(user_id)
            request.state.username = request.headers.get("x-username", "kaos-user")
            request.state.role = "admin"
            request.state.auth_method = "api_key"

            logger.bind(event="auth.authenticated", user_id=str(user_id)).info(
                "[auth] API key authenticated request from {} - {} {}",
                request.client.host if request.client else "unknown",
                request.method,
                path,
            )
            return await call_next(request)

        # No valid auth found
        logger.warning(
            "[auth] rejected request from {} - no valid auth",
            request.client.host if request.client else "unknown",
        )
        return Response(
            status_code=401,
            content='{"detail":"Invalid authentication"}',
            media_type="application/json",
        )
