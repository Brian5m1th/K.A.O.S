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


class ApiKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
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

        return await call_next(request)
