from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal
import json
from pathlib import Path

from loguru import logger


@dataclass
class FeatureEntry:
    id: str
    name: str
    phase: str
    status: Literal["planned", "in-progress", "done"]
    docs: list[str] = field(default_factory=list)
    code_refs: list[str] = field(default_factory=list)
    last_commit: str = ""
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    updated_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "phase": self.phase,
            "status": self.status,
            "docs": self.docs,
            "codeRefs": self.code_refs,
            "lastCommit": self.last_commit,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "FeatureEntry":
        return cls(
            id=data["id"],
            name=data["name"],
            phase=data["phase"],
            status=data["status"],
            docs=data.get("docs", []),
            code_refs=data.get("codeRefs", []),
            last_commit=data.get("lastCommit", ""),
            created_at=data.get("createdAt", datetime.now(timezone.utc).isoformat()),
            updated_at=data.get("updatedAt", datetime.now(timezone.utc).isoformat()),
        )


class FeatureRegistry:
    _features: dict[str, FeatureEntry] = {}
    _registry_path: Path = Path("docs/runtime/registry/features-index.json")

    @classmethod
    def register(cls, feature: FeatureEntry) -> None:
        feature.updated_at = datetime.now(timezone.utc).isoformat()
        cls._features[feature.id] = feature
        logger.info(
            f"[feature_registry] registered: {feature.id} ({feature.name}) v{feature.status}"
        )
        cls._persist()

    @classmethod
    def register_many(cls, features: list[FeatureEntry]) -> None:
        for feature in features:
            cls.register(feature)

    @classmethod
    def get(cls, feature_id: str) -> FeatureEntry | None:
        return cls._features.get(feature_id)

    @classmethod
    def get_by_name(cls, name: str) -> FeatureEntry | None:
        for feature in cls._features.values():
            if feature.name == name:
                return feature
        return None

    @classmethod
    def list(cls) -> list[FeatureEntry]:
        return list(cls._features.values())

    @classmethod
    def list_by_phase(cls, phase: str) -> list[FeatureEntry]:
        return [f for f in cls._features.values() if f.phase == phase]

    @classmethod
    def list_by_status(cls, status: str) -> list[FeatureEntry]:
        return [f for f in cls._features.values() if f.status == status]

    @classmethod
    def unregister(cls, feature_id: str) -> None:
        if feature_id in cls._features:
            del cls._features[feature_id]
            logger.info(f"[feature_registry] unregistered: {feature_id}")
            cls._persist()

    @classmethod
    def update_status(
        cls, feature_id: str, status: Literal["planned", "in-progress", "done"]
    ) -> None:
        if feature_id in cls._features:
            cls._features[feature_id].status = status
            cls._features[feature_id].updated_at = datetime.now(
                timezone.utc
            ).isoformat()
            cls._persist()

    @classmethod
    def update_last_commit(cls, feature_id: str, commit_hash: str) -> None:
        if feature_id in cls._features:
            cls._features[feature_id].last_commit = commit_hash
            cls._features[feature_id].updated_at = datetime.now(
                timezone.utc
            ).isoformat()
            cls._persist()

    @classmethod
    def add_doc_ref(cls, feature_id: str, doc_path: str) -> None:
        if (
            feature_id in cls._features
            and doc_path not in cls._features[feature_id].docs
        ):
            cls._features[feature_id].docs.append(doc_path)
            cls._features[feature_id].updated_at = datetime.now(
                timezone.utc
            ).isoformat()
            cls._persist()

    @classmethod
    def add_code_ref(cls, feature_id: str, code_path: str) -> None:
        if (
            feature_id in cls._features
            and code_path not in cls._features[feature_id].code_refs
        ):
            cls._features[feature_id].code_refs.append(code_path)
            cls._features[feature_id].updated_at = datetime.now(
                timezone.utc
            ).isoformat()
            cls._persist()

    @classmethod
    def search(cls, query: str) -> list[FeatureEntry]:
        q = query.lower()
        return [
            f
            for f in cls._features.values()
            if q in f.id.lower() or q in f.name.lower() or q in f.phase.lower()
        ]

    @classmethod
    def export_json(cls) -> dict:
        return {
            "version": "1.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_features": len(cls._features),
            "features": [f.to_dict() for f in cls._features.values()],
        }

    @classmethod
    def _persist(cls) -> None:
        cls._registry_path.parent.mkdir(parents=True, exist_ok=True)
        data = cls.export_json()
        with open(cls._registry_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.debug(f"[feature_registry] persisted to {cls._registry_path}")

    @classmethod
    def load_from_json(cls) -> None:
        if cls._registry_path.exists():
            with open(cls._registry_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            cls._features = {
                feat["id"]: FeatureEntry.from_dict(feat)
                for feat in data.get("features", [])
            }
            logger.info(
                f"[feature_registry] loaded {len(cls._features)} features from {cls._registry_path}"
            )
        else:
            logger.info("[feature_registry] no existing registry found, starting fresh")

    @classmethod
    def clear(cls) -> None:
        cls._features.clear()
        cls._persist()
