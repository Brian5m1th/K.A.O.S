import time
from collections import OrderedDict
from loguru import logger


class ResponseCache:
    def __init__(self, ttl: int = 300, maxsize: int = 128):
        self._ttl = ttl
        self._maxsize = maxsize
        self._store: OrderedDict[str, tuple[float, str]] = OrderedDict()

    def _is_expired(self, timestamp: float) -> bool:
        return time.monotonic() - timestamp > self._ttl

    def get(self, key: str) -> str | None:
        entry = self._store.get(key)
        if entry is None:
            return None
        timestamp, value = entry
        if self._is_expired(timestamp):
            del self._store[key]
            logger.debug(f"[info] cache - expirado: {key}")
            return None
        self._store.move_to_end(key)
        logger.debug(f"[info] cache - hit: {key}")
        return value

    def set(self, key: str, value: str) -> None:
        if key in self._store:
            self._store.move_to_end(key)
        else:
            if len(self._store) >= self._maxsize:
                evicted = self._store.popitem(last=False)
                logger.debug(f"[info] cache - evict: {evicted[0]}")
        self._store[key] = (time.monotonic(), value)
        logger.debug(f"[info] cache - set: {key}")

    def clear(self) -> None:
        self._store.clear()
        logger.debug("[info] cache - limpo")

    @property
    def size(self) -> int:
        return len(self._store)
