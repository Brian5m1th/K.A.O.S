import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from loguru import logger


@dataclass
class SDDEntry:
    id: str
    path: str
    title: str
    version: str = "1.0"
    linked_features: list[str] = None
    status: str = "valid"  # valid, stale, missing
    last_updated: str = ""

    def __post_init__(self):
        if self.linked_features is None:
            self.linked_features = []


class SDDResolver:
    _sdd_dirs = [
        Path("docs/sdd"),
        Path("docs/architecture"),
        Path("docs/Arquitetura"),
        Path(".opencode/plans"),
    ]
    _sdd_cache: dict[str, SDDEntry] = {}
    _feature_to_sdd: dict[str, list[str]] = {}

    @classmethod
    def scan_all_sdds(cls) -> dict[str, SDDEntry]:
        cls._sdd_cache.clear()
        cls._feature_to_sdd.clear()

        for sdd_dir in cls._sdd_dirs:
            if not sdd_dir.exists():
                continue
            for md_file in sdd_dir.rglob("*.md"):
                entry = cls._parse_sdd(md_file)
                if entry:
                    cls._sdd_cache[entry.id] = entry
                    for feat in entry.linked_features:
                        if feat not in cls._feature_to_sdd:
                            cls._feature_to_sdd[feat] = []
                        cls._feature_to_sdd[feat].append(entry.id)

        logger.info(f"[sdd_resolver] scanned {len(cls._sdd_cache)} SDDs")
        return cls._sdd_cache

    @classmethod
    def _parse_sdd(cls, path: Path) -> Optional[SDDEntry]:
        try:
            content = path.read_text(encoding="utf-8")
        except Exception:
            return None

        title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem

        id_match = re.search(r"(?:SDD[-:]?\s*)?(\w+(?:[-_]\w+)*)", title, re.IGNORECASE)
        sdd_id = id_match.group(1).lower() if id_match else path.stem.lower()

        features = cls._extract_linked_features(content)

        entry = SDDEntry(
            id=sdd_id,
            path=path.relative_to(Path.cwd()).as_posix(),
            title=title,
            linked_features=features,
        )
        return entry

    @classmethod
    def _extract_linked_features(cls, content: str) -> list[str]:
        features = []

        feature_patterns = [
            r"feature[:\s]+([\w\-]+)",
            r"features?[:\s]+([\w\s,\-]+)",
            r"#\s*features?\s*\n([\s\S]*?)(?:\n#|\Z)",
            r"linked.?features?[:\s]+([\w\s,\-]+)",
        ]

        for pattern in feature_patterns:
            matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
            for match in matches:
                feat_text = match.group(1)
                for feat in re.split(r"[\s,]+", feat_text):
                    feat = feat.strip().lower()
                    if feat and len(feat) > 2:
                        features.append(feat)

        content_lower = content.lower()
        known_features = [
            "observability",
            "event-bus",
            "workflow-engine",
            "provider-adapters",
            "model-router",
            "circuit-breaker",
            "dead-letter-queue",
            "n8n-integration",
            "memory-system",
            "sse-layer",
            "tool-layer",
            "agent-runtime",
            "launcher",
            "auto-update",
            "database-schema",
            "service-registry",
            "core-contracts",
            "desktop-apis",
            "observability-production",
            "workflow-registry",
            "orchestrator",
            "plan-executor",
            "provider-selector",
            "health-cache",
            "base-workflow",
            "base-chat-provider",
            "base-embedding-provider",
        ]

        for feat in known_features:
            if feat in content_lower and feat not in features:
                features.append(feat)

        return list(set(features))

    @classmethod
    def find_sdd_for_feature(cls, feature: str) -> list[SDDEntry]:
        if not cls._sdd_cache:
            cls.scan_all_sdds()

        sdd_ids = cls._feature_to_sdd.get(feature.lower(), [])
        return [cls._sdd_cache[sid] for sid in sdd_ids if sid in cls._sdd_cache]

    @classmethod
    def get_sdd_status(cls, feature: str) -> str:
        sd_ds = cls.find_sdd_for_feature(feature)
        if not sd_ds:
            return "missing"
        for sdd in sd_ds:
            if sdd.status == "stale":
                return "stale"
        return "valid"

    @classmethod
    def get_all_sdds(cls) -> list[SDDEntry]:
        if not cls._sdd_cache:
            cls.scan_all_sdds()
        return list(cls._sdd_cache.values())

    @classmethod
    def get_missing_features(cls, known_features: list[str]) -> list[str]:
        if not cls._sdd_cache:
            cls.scan_all_sdds()

        documented = set()
        for sdd in cls._sdd_cache.values():
            documented.update(sdd.linked_features)

        return [f for f in known_features if f.lower() not in documented]

    @classmethod
    def get_orphaned_sdds(cls, known_features: list[str]) -> list[SDDEntry]:
        if not cls._sdd_cache:
            cls.scan_all_sdds()

        known = set(f.lower() for f in known_features)
        orphans = []
        for sdd in cls._sdd_cache.values():
            has_known = any(f.lower() in known for f in sdd.linked_features)
            if not has_known and sdd.linked_features:
                orphans.append(sdd)
        return orphans

    @classmethod
    def clear_cache(cls) -> None:
        cls._sdd_cache.clear()
        cls._feature_to_sdd.clear()
