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
    "/auth/reset-password",
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
        path = request.url.path
        logger.info("[auth-middleware] Request path: {} | Method: {}", path, request.method)

        if request.method == "OPTIONS":
            logger.info("[auth-middleware] OPTIONS request allowed for {}", path)
            return await call_next(request)

        for public in PUBLIC_PATHS:
            if path == public or path.startswith(public + "/"):
                logger.info("[auth-middleware] Path {} matches public pattern {}", path, public)
                return await call_next(request)

        # Initialize state
        request.state.user_id = ""
        request.state.username = ""
        request.state.role = ""
        request.state.auth_method = ""

        auth_header = request.headers.get("Authorization", "")

        # 1. Try JWT Bearer token
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
                    "[auth] JWT authenticated: {} {} {}",
                    request.method,
                    path,
                    email,
                )
                return await call_next(request)

        # 2. Fall back to API Key
        api_key = request.headers.get("x-api-key", "")
        if not api_key and auth_header.startswith("Bearer "):
            api_key = auth_header[7:]

        app_key = getattr(request.app.state, "api_key", None)
        if app_key is None:
            return Response(
                status_code=503,
                content='{"detail":"Service not ready"}',
                media_type="application/json",
            )

        if api_key and api_key == app_key:
            user_id = _derive_user_id(api_key)
            request.state.user_id = str(user_id)
            request.state.username = request.headers.get("x-username", "kaos-user")
            request.state.role = "admin"
            request.state.auth_method = "api_key"

            logger.bind(event="auth.authenticated", user_id=str(user_id)).info(
                "[auth] API key authenticated: {} {}",
                request.method,
                path,
            )
            return await call_next(request)

        # 3. No valid auth found
        logger.warning("[auth] rejected: {} {} - no valid auth", request.method, path)
        return Response(
            status_code=401,
            content='{"detail":"Invalid authentication"}',
            media_type="application/json",
        )
