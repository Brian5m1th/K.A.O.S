from typing import Any
from loguru import logger
from app.runtime.runtime_layer import AIRuntime, ProviderRuntimeAdapter
from app.llm.factory import LLMFactory
from app.config.settings import settings


class RuntimeSelector:
    def __init__(self):
        self.factory = LLMFactory()
        self._runtimes: list[AIRuntime] = []
        self._init_runtimes()

    def _init_runtimes(self):
        # 1. Local Ollama runtime config
        try:
            ollama_model = settings.OLLAMA_MODEL or "qwen3:4b"
            ollama_prov = self.factory.build(ollama_model)
            ollama_run = ProviderRuntimeAdapter(
                provider=ollama_prov,
                runtime_type="local",
                capabilities={
                    "vision": True,
                    "function_calling": True,
                    "structured_output": False,
                    "streaming": True,
                    "context_window": 8192,
                    "latency": 3.0,  # seconds TTFT
                    "offline": True,
                    "cost": 0.0,
                    "reasoning": False,
                },
                supported_models=[ollama_model],
            )
            self._runtimes.append(ollama_run)
        except Exception as e:
            logger.warning(f"Ollama runtime failed to init: {e}")

        # 2. Cloud OpenAI runtime config
        try:
            openai_prov = self.factory.build("gpt-4o")
            openai_run = ProviderRuntimeAdapter(
                provider=openai_prov,
                runtime_type="cloud",
                capabilities={
                    "vision": True,
                    "function_calling": True,
                    "structured_output": True,
                    "streaming": True,
                    "context_window": 128000,
                    "latency": 1.5,
                    "offline": False,
                    "cost": 0.005,  # USD/1k
                    "reasoning": True,
                },
                supported_models=["gpt-4o", "gpt-4o-mini"],
            )
            self._runtimes.append(openai_run)
        except Exception as e:
            logger.warning(f"OpenAI runtime failed to init: {e}")

        # 3. Cloud Gemini runtime config
        try:
            gemini_prov = self.factory.build("gemini-pro")
            gemini_run = ProviderRuntimeAdapter(
                provider=gemini_prov,
                runtime_type="cloud",
                capabilities={
                    "vision": True,
                    "function_calling": True,
                    "structured_output": True,
                    "streaming": True,
                    "context_window": 1000000,
                    "latency": 2.0,
                    "offline": False,
                    "cost": 0.001,
                    "reasoning": True,
                },
                supported_models=["gemini-1.5-pro", "gemini-1.5-flash"],
            )
            self._runtimes.append(gemini_run)
        except Exception as e:
            logger.warning(f"Gemini runtime failed to init: {e}")

    def select(self, objective: str) -> AIRuntime:
        """Seleciona o melhor runtime com base em objetivos do usuário."""
        logger.info(f"[start] RuntimeSelector - select [objective={objective}]")
        if not self._runtimes:
            raise RuntimeError("Nenhum AI Runtime disponível e inicializado.")

        ranked = []
        for run in self._runtimes:
            score = 0
            caps = run.capabilities

            if objective == "economia":
                # Custo: menor é melhor.
                cost_score = max(0, 10 - (caps.get("cost", 0) * 1000))
                score = cost_score
            elif objective in ("offline", "privacidade"):
                if caps.get("offline", False):
                    score = 100
                else:
                    score = -100
            elif objective in ("raciocinio", "qualidade"):
                if caps.get("reasoning", False):
                    score += 50
                if caps.get("structured_output", False):
                    score += 30
                if caps.get("function_calling", False):
                    score += 20
            elif objective == "latencia":
                score = max(0, 10 - caps.get("latency", 3.0))
            elif objective == "contexto":
                score = caps.get("context_window", 2048) / 1000.0
            else:
                score = 5 if caps.get("offline", False) else 2

            ranked.append((score, run))

        ranked.sort(key=lambda x: x[0], reverse=True)
        best_run = ranked[0][1]
        logger.info(
            f"[info] RuntimeSelector - selected: {best_run.name} ({best_run.type}) for objective={objective}"
        )
        logger.debug("[finish] RuntimeSelector - select")
        return best_run
