import json
import os
import subprocess
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

from loguru import logger

from app.audit.runtime_resolver import RuntimePathResolver

from app.audit.commit_classifier import classify_commits


@dataclass
class CommitMapEntry:
    hash: str
    message: str
    type: str
    impact: str
    scope: str | None
    breaking: bool
    features: list[str]
    timestamp: str
    author: str


class CommitMapper:
    _map_path: Path = RuntimePathResolver.commit_map_path()
    _max_commits: int = 200

    @classmethod
    def set_max_commits(cls, max_commits: int) -> None:
        cls._max_commits = max_commits

    @classmethod
    def _run_git_log(cls, limit: int | None = None) -> list[tuple[str, str, str, str]]:
        project_root = RuntimePathResolver.project_root()
        if not (project_root / ".git").exists():
            logger.warning(
                "[commit_mapper] git repository not found (no .git directory/file)."
            )
            # Fallback: check CI environment variables before giving up
            for env_var in ("GITHUB_SHA", "GIT_COMMIT", "CI_COMMIT_SHA"):
                sha = os.environ.get(env_var)
                if sha:
                    logger.info(
                        "[commit_mapper] using commit hash from env {}={}",
                        env_var,
                        sha[:12],
                    )
                    return [
                        (
                            sha[:40],
                            f"commit from {env_var}",
                            "ci",
                            datetime.now(timezone.utc).isoformat(),
                        )
                    ]
            logger.warning(
                "[commit_mapper] no CI env vars found either. Returning empty."
            )
            return []

        cmd = [
            "git",
            "log",
            f"--max-count={limit or cls._max_commits}",
            "--pretty=format:%H|%s|%an|%aI",
            "--no-merges",
        ]
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=project_root,
                timeout=30,
            )
            if result.returncode != 0:
                logger.error(f"[commit_mapper] git log failed: {result.stderr}")
                return []
            lines = result.stdout.strip().split("\n")
            commits = []
            for line in lines:
                if not line:
                    continue
                parts = line.split("|", 3)
                if len(parts) == 4:
                    commits.append((parts[0], parts[1], parts[2], parts[3]))
            return commits
        except subprocess.TimeoutExpired:
            logger.error("[commit_mapper] git log timeout")
            return []
        except Exception as e:
            logger.error(f"[commit_mapper] git log error: {e}")
            return []

    @classmethod
    def generate_map(cls, limit: int | None = None) -> list[CommitMapEntry]:
        raw_commits = cls._run_git_log(limit)
        if not raw_commits:
            logger.warning("[commit_mapper] no commits found")
            return []

        classified = classify_commits([(h, m) for h, m, _, _ in raw_commits])

        mapped = []
        for (hash_, msg, author, timestamp), classified in zip(raw_commits, classified):
            entry = CommitMapEntry(
                hash=classified.hash,
                message=classified.message,
                type=classified.type.value,
                impact=classified.impact.value,
                scope=classified.scope,
                breaking=classified.breaking,
                features=classified.features_mentioned,
                timestamp=timestamp,
                author=author,
            )
            mapped.append(entry)

        cls._persist(mapped)
        logger.info(f"[commit_mapper] generated map with {len(mapped)} commits")
        return mapped

    @classmethod
    def _persist(cls, entries: list[CommitMapEntry]) -> None:
        cls._map_path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "version": "1.0",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "total_commits": len(entries),
            "commits": [asdict(e) for e in entries],
        }
        with open(cls._map_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.debug(f"[commit_mapper] persisted to {cls._map_path}")

    @classmethod
    def load(cls) -> list[CommitMapEntry]:
        if cls._map_path.exists():
            with open(cls._map_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [CommitMapEntry(**e) for e in data.get("commits", [])]
        return []

    @classmethod
    def get_features_for_commit(cls, commit_hash: str) -> list[str]:
        entries = cls.load()
        for entry in entries:
            if entry.hash == commit_hash[:8]:
                return entry.features
        return []

    @classmethod
    def get_commits_for_feature(cls, feature: str) -> list[CommitMapEntry]:
        entries = cls.load()
        return [e for e in entries if feature in e.features]

    @classmethod
    def get_high_impact_commits(cls, since: str | None = None) -> list[CommitMapEntry]:
        entries = cls.load()
        filtered = [e for e in entries if e.impact == "high"]
        if since:
            filtered = [e for e in filtered if e.timestamp >= since]
        return filtered

    @classmethod
    def get_commits_by_type(cls, ctype: str) -> list[CommitMapEntry]:
        entries = cls.load()
        return [e for e in entries if e.type == ctype]

    @classmethod
    def get_latest_commit(cls) -> CommitMapEntry | None:
        entries = cls.load()
        return entries[0] if entries else None


if __name__ == "__main__":
    entries = CommitMapper.generate_map(50)
    for e in entries[:10]:
        print(
            f"{e.hash} | {e.type:6} | {e.impact:6} | {e.scope or '-':15} | {e.features}"
        )
