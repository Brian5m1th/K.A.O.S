from collections import defaultdict
from datetime import datetime, timezone
from typing import Any
from uuid import UUID

from prometheus_client import Counter, Gauge

from app.observability.event_bus import Event, EventSubscriber

_cost_total = Counter(
    "kaos_cost_total_usd",
    "Total accumulated cost in USD",
    ["provider", "workflow"],
)

_cost_current_execution = Gauge(
    "kaos_cost_current_execution_usd",
    "Cost of the current execution",
    ["execution_id"],
)


class CostTracker(EventSubscriber):
    def __init__(self) -> None:
        self._executions: dict[UUID, dict[str, Any]] = {}
        self._provider_costs: dict[str, float] = defaultdict(float)
        self._workflow_costs: dict[str, float] = defaultdict(float)
        self._total_cost: float = 0.0

    async def on_event(self, event: Event) -> None:
        if event.name == "llm_request":
            self._executions[event.execution_id] = {
                "provider": event.data.get("provider", "unknown"),
                "model": event.data.get("model", "unknown"),
                "workflow": "unknown",
                "tokens_in": 0,
                "tokens_out": 0,
                "cost": 0.0,
            }

        elif event.name == "workflow_started":
            if event.execution_id not in self._executions:
                self._executions[event.execution_id] = {
                    "provider": "unknown",
                    "model": "unknown",
                    "workflow": event.data.get("workflow", "unknown"),
                    "tokens_in": 0,
                    "tokens_out": 0,
                    "cost": 0.0,
                }
            else:
                self._executions[event.execution_id]["workflow"] = event.data.get(
                    "workflow", "unknown"
                )

        elif event.name in ("llm_response", "workflow_completed"):
            tokens_in = event.data.get("tokens_in", 0)
            tokens_out = event.data.get("tokens_out", 0)
            provider = event.data.get("provider", "unknown")
            cost = self._estimate_cost(provider, tokens_in, tokens_out)

            execution = self._executions.get(event.execution_id)
            workflow = execution["workflow"] if execution else "unknown"

            self._provider_costs[provider] += cost
            self._workflow_costs[workflow] += cost
            self._total_cost += cost

            _cost_total.labels(provider=provider, workflow=workflow).inc(cost)
            _cost_current_execution.labels(execution_id=str(event.execution_id)).set(
                self._total_cost
            )

    def _estimate_cost(self, provider: str, tokens_in: int, tokens_out: int) -> float:
        rates = {
            "ollama": 0.0,
            "openai": (0.000003, 0.000012),
            "claude": (0.000008, 0.000024),
            "gemini": (0.000002, 0.000005),
        }
        rate = rates.get(provider, (0.0, 0.0))
        if isinstance(rate, (int, float)):
            return tokens_in * rate + tokens_out * rate
        return tokens_in * rate[0] + tokens_out * rate[1]

    def summary(self) -> dict[str, Any]:
        return {
            "total_cost": round(self._total_cost, 6),
            "by_provider": {
                k: round(v, 6) for k, v in sorted(self._provider_costs.items())
            },
            "by_workflow": {
                k: round(v, 6) for k, v in sorted(self._workflow_costs.items())
            },
            "executions_count": len(self._executions),
            "tracked_since": datetime.now(timezone.utc).isoformat(),
        }

    def reset(self) -> None:
        self._executions.clear()
        self._provider_costs.clear()
        self._workflow_costs.clear()
        self._total_cost = 0.0
