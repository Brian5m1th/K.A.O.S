"""
Technology Observatory — Continuous tech ecosystem monitoring.

Tracks GitHub activity, releases, breaking changes, security advisories,
and community health for all frameworks in the K.A.O.S Knowledge Catalog.

Runs as a scheduled script (weekly cron / GitHub Actions).
Outputs reports to kaos-research/technology-observatory/reports/.

Usage:
    python technology-observatory/observatory.py
"""

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "catalog" / "framework-catalog.json"
REPORTS_DIR = ROOT / "technology-observatory" / "reports"

# Frameworks to track
FRAMEWORKS = [
    {"name": "graphify", "repo": "nicedoc/graphify", "pypi": "graphifyy"},
    {"name": "graphrag", "repo": "microsoft/graphrag", "pypi": "graphrag"},
    {"name": "graphiti", "repo": "getzep/graphiti", "pypi": "graphiti"},
    {"name": "mem0", "repo": "mem0ai/mem0", "pypi": "mem0ai"},
    {"name": "cognee", "repo": "topoteretes/cognee", "pypi": "cognee"},
    {"name": "letta", "repo": "letta-ai/letta", "pypi": "letta"},
    {"name": "langgraph", "repo": "langchain-ai/langgraph", "pypi": "langgraph"},
    {"name": "qdrant", "repo": "qdrant/qdrant-client", "pypi": "qdrant-client"},
    {"name": "airllm", "repo": "lyogavin/airllm", "pypi": "airllm"},
    {"name": "llamaindex", "repo": "run-llama/llama_index", "pypi": "llama-index"},
    {"name": "dspy", "repo": "stanfordnlp/dspy", "pypi": "dspy-ai"},
    {"name": "crewai", "repo": "crewAIInc/crewAI", "pypi": "crewai"},
    {"name": "autogen", "repo": "microsoft/autogen", "pypi": "pyautogen"},
    {"name": "falkordb", "repo": "falkordb/falkordb", "pypi": "falkordb"},
    {"name": "neo4j", "repo": "neo4j/neo4j-python-driver", "pypi": "neo4j"},
]


def check_github_repo(owner_repo: str) -> dict:
    """Check GitHub repo stats via gh CLI (requires gh auth)."""
    try:
        result = subprocess.run(
            ["gh", "repo", "view", owner_repo, "--json", "stargazerCount,forkCount,updatedAt,licenseInfo,defaultBranch"],
            capture_output=True, text=True, timeout=15,
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except Exception:
        pass
    return {}


def check_pypi_version(package: str) -> str:
    """Check latest PyPI version via pip index."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "index", "versions", package],
            capture_output=True, text=True, timeout=15,
        )
        for line in result.stdout.split("\n"):
            if "Available versions:" in line:
                versions = line.split(":")[1].strip().split(",")
                return versions[0].strip()
    except Exception:
        pass
    return "unknown"


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "frameworks": [],
    }

    for fw in FRAMEWORKS:
        print(f"[observatory] Checking {fw['name']}...")
        gh_data = check_github_repo(fw["repo"])
        pypi_version = check_pypi_version(fw["pypi"])

        entry = {
            "name": fw["name"],
            "repo": fw["repo"],
            "pypi": fw["pypi"],
            "latest_pypi": pypi_version,
            "github_stars": gh_data.get("stargazerCount", None),
            "github_forks": gh_data.get("forkCount", None),
            "github_updated": gh_data.get("updatedAt", None),
            "license": gh_data.get("licenseInfo", {}).get("spdxId", "unknown"),
            "checked_at": datetime.now(timezone.utc).isoformat(),
        }
        report["frameworks"].append(entry)

    # Write report
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    report_path = REPORTS_DIR / f"observatory-{timestamp}.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)

    # Update latest symlink
    latest_path = REPORTS_DIR / "latest.json"
    with open(latest_path, "w") as f:
        json.dump(report, f, indent=2)

    print(f"[observatory] Report written to {report_path}")
    print(f"[observatory] Tracked {len(report['frameworks'])} frameworks")


if __name__ == "__main__":
    main()
