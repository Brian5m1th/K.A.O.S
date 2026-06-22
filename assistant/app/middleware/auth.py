import hashlib
from uuid import UUID, uuid5, NAMESPACE_DNS
from fastapi import Request, Response
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware

PUBLIC_PATHS = {
    "/health",
    "/docs",
    "/openapi.json",
    "/auth",
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

        app_key = getattr(request.app.state, "api_key", None)
        if app_key is None:
            logger.warning("[auth] API key not configured on app.state")
            return Response(
                status_code=503,
                content='{"detail":"Service not ready"}',
                media_type="application/json",
            )

        key = request.headers.get("x-api-key", "")
        if not key:
            auth_header = request.headers.get("Authorization", "")
            if auth_header.startswith("Bearer "):
                key = auth_header[7:]
        if key != app_key:
            logger.warning(
                "[auth] rejected request from {} - invalid key",
                request.client.host if request.client else "unknown",
            )
            return Response(
                status_code=401,
                content='{"detail":"Invalid API key"}',
                media_type="application/json",
            )

        user_id = _derive_user_id(key)
        request.state.user_id = str(user_id)
        request.state.username = request.headers.get("x-username", "kaos-user")

        logger.bind(event="auth.authenticated", user_id=str(user_id)).info(
            "[auth] authenticated request from {} - {} {}",
            request.client.host if request.client else "unknown",
            request.method,
            path,
        )

        return await call_next(request)
