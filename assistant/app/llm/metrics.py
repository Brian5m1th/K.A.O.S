import time
from dataclasses import dataclass
from loguru import logger


@dataclass
class MetricEntry:
    provider: str
    model: str
    latency_ms: float
    tokens_in: int
    tokens_out: int
    cost: float
    error: str | None = None


class ProviderMetrics:
    def __init__(self):
        self._entries: list[MetricEntry] = []

    def record(self, entry: MetricEntry) -> None:
        self._entries.append(entry)
        level = "error" if entry.error else "info"
        logger.log(
            level,
            f"[metrics] provider={entry.provider} model={entry.model} "
            f"latency={entry.latency_ms:.0f}ms tokens_in={entry.tokens_in} "
            f"tokens_out={entry.tokens_out} cost={entry.cost:.6f}"
            + (f" error={entry.error}" if entry.error else ""),
        )

    async def ainvoke_and_record(self, provider, messages: list) -> str:
        start = time.perf_counter()
        try:
            response = await provider.ainvoke(messages)
            elapsed = (time.perf_counter() - start) * 1000
            tokens_in = 0
            tokens_out = 0
            if hasattr(response, "usage_metadata") and response.usage_metadata:
                tokens_in = response.usage_metadata.get("input_tokens", 0) if isinstance(response.usage_metadata, dict) else getattr(response.usage_metadata, "input_tokens", 0)
                tokens_out = response.usage_metadata.get("output_tokens", 0) if isinstance(response.usage_metadata, dict) else getattr(response.usage_metadata, "output_tokens", 0)
            cost = self._estimate_cost(provider.provider_name, tokens_in, tokens_out)
            self.record(MetricEntry(
                provider=provider.provider_name,
                model=provider.model_name,
                latency_ms=elapsed,
                tokens_in=tokens_in,
                tokens_out=tokens_out,
                cost=cost,
            ))
            return response.content if hasattr(response, "content") else response
        except Exception as e:
            elapsed = (time.perf_counter() - start) * 1000
            self.record(MetricEntry(
                provider=provider.provider_name,
                model=provider.model_name,
                latency_ms=elapsed,
                tokens_in=0,
                tokens_out=0,
                cost=0.0,
                error=str(e),
            ))
            raise

    def _estimate_cost(self, provider: str, tokens_in: int, tokens_out: int) -> float:
        rates = {
            "ollama": 0.0,
            "openai":   (0.000003, 0.000012),
            "claude":   (0.000008, 0.000024),
            "gemini":   (0.000002, 0.000005),
        }
        rate = rates.get(provider, (0.0, 0.0))
        return tokens_in * rate[0] + tokens_out * rate[1]

    def summary(self) -> dict:
        if not self._entries:
            return {}
        total_cost = sum(e.cost for e in self._entries)
        total_latency = sum(e.latency_ms for e in self._entries)
        return {
            "total_calls": len(self._entries),
            "total_cost": round(total_cost, 6),
            "total_latency_ms": round(total_latency, 0),
            "avg_latency_ms": round(total_latency / len(self._entries), 0),
        }
