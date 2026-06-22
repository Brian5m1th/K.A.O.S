from fastapi import APIRouter
from app.apps.registry import AppRegistry

router = APIRouter(prefix="/api/apps", tags=["Apps"])


@router.get("/")
async def list_apps() -> dict:
    apps = AppRegistry.list()
    return {"apps": apps}


@router.get("/{name}")
async def get_app(name: str) -> dict:
    app = AppRegistry.get(name)
    if app is None:
        return {"error": "app not found"}
    return {
        "name": app.name,
        "version": app.version,
        "enabled": app.enabled,
    }
