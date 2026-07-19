import re
from dataclasses import dataclass
from enum import Enum
from loguru import logger


class CommitType(Enum):
    FEAT = "feat"
    FIX = "fix"
    TEST = "test"
    STYLE = "style"
    REFACTOR = "refactor"
    DOCS = "docs"
    MERGE = "merge"
    CHORE = "chore"
    BUILD = "build"
    CI = "ci"
    UNKNOWN = "unknown"


class ImpactLevel(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    NONE = "none"


@dataclass
class ClassifiedCommit:
    hash: str
    message: str
    type: CommitType
    impact: ImpactLevel
    scope: str | None
    breaking: bool
    features_mentioned: list[str]


HIGH_IMPACT_PATTERNS = [
    r"event.?bus",
    r"workflow",
    r"provider",
    r"model.?router",
    r"observability",
    r"memory",
    r"circuit.?breaker",
    r"dead.?letter",
    r"orchestrator",
    r"n8n",
    r"sse",
    r"tool.?layer",
    r"agent",
    r"launcher",
]

MEDIUM_IMPACT_PATTERNS = [
    r"api",
    r"endpoint",
    r"store",
    r"hook",
    r"component",
    r"schema",
    r"config",
    r"migration",
    r"database",
    r"registry",
]

FEATURE_KEYWORDS = {
    "observability": [
        "observability",
        "metrics",
        "prometheus",
        "grafana",
        "tracing",
        "otel",
        "cost",
    ],
    "event-bus": ["event.?bus", "subscriber", "publish", "emit"],
    "workflow-engine": ["workflow", "orchestrator", "plan.?executor"],
    "provider-adapters": [
        "provider",
        "adapter",
        "chat",
        "embedding",
        "vector",
        "memory",
    ],
    "model-router": ["model.?router", "capability", "selector"],
    "circuit-breaker": ["circuit.?breaker", "fallback", "health.?cache"],
    "dead-letter-queue": ["dead.?letter", "dlq"],
    "n8n-integration": ["n8n", "webhook"],
    "memory-system": ["memory", "conversation", "session"],
    "sse-layer": ["sse", "streaming", "server.?sent"],
    "tool-layer": ["tool", "tool.?schema", "tool.?event"],
    "agent-runtime": ["agent", "lifecycle"],
    "launcher": ["launcher"],
    "auto-update": ["auto.?update", "tauri.?updater"],
    "database-schema": ["schema", "migration", "table"],
    "service-registry": ["service.?registry", "registry"],
    "core-contracts": ["execution.?plan", "capability.?profile", "base.?workflow"],
    "desktop-apis": ["desktop", "profile", "policy"],
    "observability-production": ["production", "observability"],
}


def classify_type(message: str) -> CommitType:
    msg = message.strip().lower()
    if msg.startswith("merge") or "merge branch" in msg:
        return CommitType.MERGE
    for ct in CommitType:
        if (
            ct != CommitType.UNKNOWN
            and ct != CommitType.MERGE
            and msg.startswith(ct.value + ":")
        ):
            return ct
        if (
            ct != CommitType.UNKNOWN
            and ct != CommitType.MERGE
            and msg.startswith(ct.value + "(")
        ):
            return ct
    return CommitType.UNKNOWN


def extract_scope(message: str) -> str | None:
    match = re.match(r"^\w+\(([^)]+)\):", message.strip())
    if match:
        return match.group(1).strip()
    return None


def is_breaking(message: str) -> bool:
    return "BREAKING CHANGE" in message.upper() or "!" in message.split(":")[0]


def assess_impact(message: str) -> ImpactLevel:
    msg = message.lower()
    for pattern in HIGH_IMPACT_PATTERNS:
        if re.search(pattern, msg):
            return ImpactLevel.HIGH
    for pattern in MEDIUM_IMPACT_PATTERNS:
        if re.search(pattern, msg):
            return ImpactLevel.MEDIUM
    return ImpactLevel.LOW


def extract_features(message: str) -> list[str]:
    msg = message.lower()
    found = []
    for feature, keywords in FEATURE_KEYWORDS.items():
        for kw in keywords:
            if re.search(kw, msg):
                found.append(feature)
                break
    return list(set(found))


def classify_commit(commit_hash: str, message: str) -> ClassifiedCommit:
    ctype = classify_type(message)
    return ClassifiedCommit(
        hash=commit_hash[:8],
        message=message.strip(),
        type=ctype,
        impact=assess_impact(message),
        scope=extract_scope(message),
        breaking=is_breaking(message),
        features_mentioned=extract_features(message),
    )


def classify_commits(commits: list[tuple[str, str]]) -> list[ClassifiedCommit]:
    return [classify_commit(h, m) for h, m in commits]


if __name__ == "__main__":
    test_commits = [
        ("abc123", "feat: N8N integration, custom webhooks API"),
        (
            "def456",
            "fix: 3 production errors - model validation, Ollama streaming retry",
        ),
        (
            "ghi789",
            "feat: Memory Workflow - save conversation via WorkflowRouter (#70)",
        ),
        ("jkl012", "merge branch 'dev'"),
        ("mno345", "feat: Fase 8.5 - Production Observability (#69)"),
        ("pqr678", "fix: normalize docs as single K.A.O.S-storage submodule"),
        ("stu901", "feat: SDD040-03 model router and circuit breaker (#60)"),
    ]
    for c in classify_commits(test_commits):
        logger.info(
            "{} | {} | {} | {} | {}",
            c.hash,
            c.type.value,
            c.impact.value,
            c.scope or "-",
            c.features_mentioned,
        )
