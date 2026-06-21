from dataclasses import dataclass, field
from typing import Optional

from loguru import logger

from app.repositories.capability_policy_repository import (
    CapabilityPolicyRepository,
)
from app.repositories.model_repository import ModelRepository
from app.repositories.user_model_profile_repository import (
    UserModelProfileRepository,
)
from app.orchestrator.health_cache import ProviderHealthCache


@dataclass
class ModelSelection:
    model: str
    provider: str
    reason: str
    candidates: list[dict] = field(default_factory=list)
    capabilities: list[str] = field(default_factory=list)


class ModelRouter:
    def __init__(
        self,
        model_repo: ModelRepository,
        policy_repo: CapabilityPolicyRepository,
        profile_repo: UserModelProfileRepository,
        health_cache: ProviderHealthCache,
    ):
        self._model_repo = model_repo
        self._policy_repo = policy_repo
        self._profile_repo = profile_repo
        self._health_cache = health_cache

    async def select_model(
        self,
        capabilities: list[str],
        user_id: Optional[str] = None,
        workflow_type: Optional[str] = None,
    ) -> ModelSelection:
        logger.info(
            f"[start] ModelRouter - select_model caps={capabilities} user={user_id}"
        )

        candidates = []
        selected = None
        reason = "capability_policy"

        if user_id and workflow_type:
            profile = await self._profile_repo.get(user_id, workflow_type)
            if profile:
                model_record = await self._model_repo.get_by_name(profile.model_name)
                if model_record:
                    healthy = await self._health_cache.is_healthy(
                        model_record.provider_name
                    )
                    if healthy:
                        candidates.append(
                            {
                                "model": model_record.name,
                                "provider": model_record.provider_name,
                                "score": 1.0,
                                "source": "user_profile",
                            }
                        )
                        selected = model_record
                        reason = "user_profile_override"

        if not selected:
            for cap in capabilities:
                policies = await self._policy_repo.get_by_capability(cap)
                for policy in policies:
                    model_record = await self._model_repo.get_by_name(
                        policy.model_name
                    )
                    if not model_record:
                        continue
                    healthy = await self._health_cache.is_healthy(
                        model_record.provider_name
                    )
                    candidates.append(
                        {
                            "model": model_record.name,
                            "provider": model_record.provider_name,
                            "score": 1.0 / (policy.priority_order + 1),
                            "source": f"policy:{cap}",
                        }
                    )
                    if healthy and not selected:
                        selected = model_record
                        reason = f"capability_policy:{cap}"

        if not selected:
            for cap in capabilities:
                models_for_cap = await self._model_repo.list_by_capability(cap)
                for m in models_for_cap:
                    healthy = await self._health_cache.is_healthy(m.provider_name)
                    candidates.append(
                        {
                            "model": m.name,
                            "provider": m.provider_name,
                            "score": 0.5,
                            "source": f"fallback:{cap}",
                        }
                    )
                    if healthy and not selected:
                        selected = m
                        reason = f"provider_fallback:{cap}"

        if not selected:
            all_models = await self._model_repo.list_all()
            for m in all_models:
                healthy = await self._health_cache.is_healthy(m.provider_name)
                candidates.append(
                    {
                        "model": m.name,
                        "provider": m.provider_name,
                        "score": 0.1,
                        "source": "last_resort",
                    }
                )
                if healthy and not selected:
                    selected = m
                    reason = "last_resort"

        model_name = selected.name if selected else "unknown"
        provider_name = selected.provider_name if selected else "unknown"

        result = ModelSelection(
            model=model_name,
            provider=provider_name,
            reason=reason,
            candidates=candidates,
            capabilities=capabilities,
        )

        logger.info(
            f"[model_router] selected={model_name} provider={provider_name} reason={reason}"
        )
        logger.debug("[finish] ModelRouter - select_model")
        return result
