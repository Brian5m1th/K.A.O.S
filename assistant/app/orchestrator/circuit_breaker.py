import time
from enum import Enum
from typing import Optional, Callable, Awaitable

from loguru import logger


class CircuitState(Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"


class CircuitBreaker:
    def __init__(
        self,
        name: str,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
        half_open_max_requests: int = 1,
    ):
        self._name = name
        self._failure_threshold = failure_threshold
        self._recovery_timeout = recovery_timeout
        self._half_open_max_requests = half_open_max_requests

        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._last_failure_time: float = 0.0
        self._half_open_requests = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> CircuitState:
        return self._state

    @property
    def failure_count(self) -> int:
        return self._failure_count

    async def call(self, fn: Callable[..., Awaitable]) -> tuple[bool, Optional[str]]:
        if self._state == CircuitState.OPEN:
            if time.monotonic() - self._last_failure_time >= self._recovery_timeout:
                self._state = CircuitState.HALF_OPEN
                self._half_open_requests = 0
                logger.info(f"[circuit_breaker] {self._name} OPEN -> HALF_OPEN")
            else:
                return False, "circuit_open"

        if self._state == CircuitState.HALF_OPEN:
            if self._half_open_requests >= self._half_open_max_requests:
                return False, "half_open_limit"

            self._half_open_requests += 1

        try:
            await fn()
            self._on_success()
            return True, None
        except Exception as e:
            error_msg = str(e)
            self._on_failure(error_msg)
            return False, error_msg

    def _on_success(self) -> None:
        if self._state == CircuitState.HALF_OPEN:
            logger.info(
                f"[circuit_breaker] {self._name} HALF_OPEN -> CLOSED (recovered)"
            )
        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._half_open_requests = 0

    def _on_failure(self, error: str) -> None:
        self._failure_count += 1
        self._last_failure_time = time.monotonic()

        if self._state == CircuitState.HALF_OPEN:
            self._state = CircuitState.OPEN
            logger.warning(
                f"[circuit_breaker] {self._name} HALF_OPEN -> OPEN (test failed)"
            )
        elif self._failure_count >= self._failure_threshold:
            self._state = CircuitState.OPEN
            logger.warning(
                f"[circuit_breaker] {self._name} CLOSED -> OPEN "
                f"({self._failure_count} failures)"
            )
        else:
            logger.debug(
                f"[circuit_breaker] {self._name} failure {self._failure_count}/"
                f"{self._failure_threshold}"
            )

    def reset(self) -> None:
        self._state = CircuitState.CLOSED
        self._failure_count = 0
        self._half_open_requests = 0
        logger.info(f"[circuit_breaker] {self._name} reset -> CLOSED")

    def to_dict(self) -> dict:
        return {
            "name": self._name,
            "state": self._state.value,
            "failure_count": self._failure_count,
            "failure_threshold": self._failure_threshold,
            "recovery_timeout": self._recovery_timeout,
        }
