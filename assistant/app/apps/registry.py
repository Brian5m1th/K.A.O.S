from loguru import logger
from app.apps.base import BaseApp


class AppRegistry:
    _apps: dict[str, BaseApp] = {}

    @classmethod
    def register(cls, app: BaseApp) -> None:
        cls._apps[app.name] = app
        logger.info(f"[app_registry] registered: {app.name} v{app.version}")

    @classmethod
    def unregister(cls, name: str) -> None:
        cls._apps.pop(name, None)
        logger.info(f"[app_registry] unregistered: {name}")

    @classmethod
    def get(cls, name: str) -> BaseApp | None:
        return cls._apps.get(name)

    @classmethod
    def list(cls) -> list[dict]:
        return [
            {
                "name": app.name,
                "version": app.version,
                "enabled": app.enabled,
            }
            for app in cls._apps.values()
        ]

    @classmethod
    def clear(cls) -> None:
        cls._apps.clear()
