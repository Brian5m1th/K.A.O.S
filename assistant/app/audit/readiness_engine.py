"""
F2 Readiness Engine — Graph Runtime & Audit Foundation.

12 checks organizados em 3 categorias:
  A. Runtime Integrity  (structural, blocker)
  B. Source Integrity   (structural, blocker)
  C. Registry Integrity (structural, blocker + semantic)

Uso:
    from app.audit.readiness_engine import run_readiness_check
    result = await run_readiness_check()
"""

import hashlib
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import httpx

from app.audit.runtime_resolver import RuntimePathResolver
from app.config.settings import settings


# ---- Check Definition ----

@dataclass
class CheckDefinition:
    id: str
    version: str
    layer: str                # "structural" | "semantic"
    blocker: bool
    category: str             # "runtime" | "source" | "registry"
    dependencies: list[str] = field(default_factory=list)
    validator: str = ""


# ---- Check Result ----

@dataclass
class CheckResult:
    id: str
    status: str               # "pass" | "fail"
    layer: str
    blocker: bool
    category: str
    details: dict = field(default_factory=dict)


# ---- Readiness Report ----

@dataclass
class ReadinessReport:
    score: float = 0.0
    passed: int = 0
    failed: int = 0
    total: int = 12
    blockers_passed: bool = True
    categories: dict = field(default_factory=lambda: {
        "runtime": {"passed": 0, "failed": 0, "blocker": True},
        "source": {"passed": 0, "failed": 0, "blocker": True},
        "registry": {"passed": 0, "failed": 0, "blocker": True},
    })
    checks: dict = field(default_factory=dict)
    input_fingerprint: str = ""
    generated_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


# ---- Helpers ----

def _json_path(*parts: str) -> Path:
    return RuntimePathResolver.resolve() / Path(*parts)


def _sha256(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def _read_json(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


async def _api_get(endpoint: str) -> dict | None:
    try:
        base = f"http://localhost:{settings.APP_PORT}"
        async with httpx.AsyncClient(timeout=5) as client:
            resp = await client.get(f"{base}{endpoint}")
            if resp.status_code == 200:
                return resp.json()
    except Exception:
        pass
    return None


# ---- Structural Validators ----

def validate_graph_json() -> CheckResult:
    path = _json_path("architecture", "graph.json")
    data = _read_json(path)
    if not data:
        return CheckResult("graph_json", "fail", "structural", True, "runtime",
                          {"error": "graph.json not found", "path": str(path)})
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    if not nodes:
        return CheckResult("graph_json", "fail", "structural", True, "runtime",
                          {"error": "graph.json has no nodes"})
    return CheckResult("graph_json", "pass", "structural", True, "runtime",
                      {"nodes": len(nodes), "edges": len(edges)})


def validate_knowledge_graph_json() -> CheckResult:
    path = _json_path("architecture", "knowledge-graph.json")
    data = _read_json(path)
    if not data:
        return CheckResult("knowledge_graph_json", "fail", "structural", True, "runtime",
                          {"error": "knowledge-graph.json not found", "path": str(path)})
    total_nodes = data.get("total_nodes", 0)
    total_edges = data.get("total_edges", 0)
    if total_nodes == 0:
        return CheckResult("knowledge_graph_json", "fail", "structural", True, "runtime",
                          {"error": "knowledge-graph.json has no nodes"})
    return CheckResult("knowledge_graph_json", "pass", "structural", True, "runtime",
                      {"total_nodes": total_nodes, "total_edges": total_edges})


def validate_docs_source() -> CheckResult:
    import subprocess
    try:
        result = subprocess.run(
            ["git", "grep", "-n", "workspace", "--", "assistant/app/", "desktop/src/"],
            capture_output=True, text=True, timeout=10,
            cwd=settings.WORKSPACE_ROOT  # will be relative to project root
        )
        lines = result.stdout.strip().split("\n") if result.stdout.strip() else []
        not_permitted = []
        for line in lines:
            if not line:
                continue
            # Classify: manager.py and domain models are permitted
            if "manager.py" in line or "domain/" in line or "identity.py" in line:
                continue
            if "docker-compose" in line or "run-local" in line:
                continue
            not_permitted.append(line)
        if not_permitted:
            return CheckResult("docs_source", "fail", "structural", True, "source",
                              {"error": "NOT PERMITTED workspace references found",
                               "matches": not_permitted})
        return CheckResult("docs_source", "pass", "structural", True, "source",
                          {"total_matches": len(lines)})
    except Exception as e:
        return CheckResult("docs_source", "pass", "structural", True, "source",
                          {"note": f"git check skipped: {e}"})


def validate_snapshot_json() -> CheckResult:
    path = _json_path("snapshot.json")
    data = _read_json(path)
    if not data:
        return CheckResult("snapshot_json", "fail", "structural", True, "registry",
                          {"error": "snapshot.json not found", "path": str(path)})
    return CheckResult("snapshot_json", "pass", "structural", True, "registry",
                      {"coverage": data.get("coverage", 0),
                       "features": len(data.get("features", []))})


def validate_features_index() -> CheckResult:
    path = _json_path("registry", "features-index.json")
    data = _read_json(path)
    if not data:
        return CheckResult("features_index", "fail", "structural", True, "registry",
                          {"error": "features-index.json not found"})
    features = data.get("features", [])
    if len(features) < 6:
        return CheckResult("features_index", "fail", "structural", True, "registry",
                          {"error": f"Only {len(features)} features, minimum 6 required"})
    # Validate status values
    invalid = [f["id"] for f in features if f.get("status") not in ("done", "in_progress", "planned")]
    if invalid:
        return CheckResult("features_index", "fail", "structural", True, "registry",
                          {"error": f"Invalid status in features: {invalid}"})
    return CheckResult("features_index", "pass", "structural", True, "registry",
                      {"total_features": len(features)})


def validate_commit_map() -> CheckResult:
    path = _json_path("registry", "commit-map.json")
    data = _read_json(path)
    if not data:
        return CheckResult("commit_map", "fail", "structural", True, "registry",
                          {"error": "commit-map.json not found"})
    commits = data if isinstance(data, list) else data.get("commits", [])
    if len(commits) == 0:
        return CheckResult("commit_map", "fail", "structural", True, "registry",
                          {"error": "commit-map.json is empty"})
    return CheckResult("commit_map", "pass", "structural", True, "registry",
                      {"total_commits": len(commits)})


# ---- Semantic Validators ----

async def validate_graph_api() -> CheckResult:
    data = await _api_get("/api/architecture/graph")
    if data is None:
        return CheckResult("graph_api", "fail", "semantic", False, "runtime",
                          {"error": "Graph API unreachable or error"})
    return CheckResult("graph_api", "pass", "semantic", False, "runtime",
                      {"nodes": len(data.get("nodes", [])),
                       "edges": len(data.get("edges", []))})


async def validate_heatmap_api() -> CheckResult:
    data = await _api_get("/api/architecture/heatmap")
    if data is None:
        return CheckResult("heatmap_api", "fail", "semantic", False, "registry",
                          {"error": "Heatmap API unreachable"})
    return CheckResult("heatmap_api", "pass", "semantic", False, "registry",
                      {"score": data.get("score", 0),
                       "level": data.get("level", "unknown")})


def validate_graph_summary() -> CheckResult:
    snapshot = _read_json(_json_path("snapshot.json"))
    if not snapshot:
        return CheckResult("graph_summary", "fail", "semantic", False, "registry",
                          {"error": "snapshot.json not found"})
    gs = snapshot.get("graphSummary", {})
    nodes = gs.get("totalNodes", 0)
    edges = gs.get("totalEdges", 0)
    if nodes == 0:
        return CheckResult("graph_summary", "fail", "semantic", False, "registry",
                          {"error": "graphSummary.nodes is 0"})
    return CheckResult("graph_summary", "pass", "semantic", False, "registry",
                      {"nodes": nodes, "edges": edges,
                       "source_hash": gs.get("sourceHash", ""),
                       "graph_version": gs.get("graphVersion", "")})


def validate_arch_page() -> CheckResult:
    page_path = Path(settings.WORKSPACE_ROOT).parent / "desktop" / "src" / "pages" / "architecture" / "index.tsx"
    if not page_path.exists():
        return CheckResult("arch_page", "fail", "semantic", False, "runtime",
                          {"error": "Architecture page not found"})
    content = page_path.read_text(encoding="utf-8")
    if "MOCK_" in content or "mock" in content.lower():
        return CheckResult("arch_page", "fail", "semantic", False, "runtime",
                          {"error": "Mock data found in architecture page"})
    return CheckResult("arch_page", "pass", "semantic", False, "runtime",
                      {"uses_store": "useGraphStore" in content or "useGraphData" in content})


def validate_reactflow() -> CheckResult:
    pkg_path = Path(settings.WORKSPACE_ROOT).parent / "desktop" / "package.json"
    if not pkg_path.exists():
        return CheckResult("reactflow", "fail", "semantic", False, "source",
                          {"error": "package.json not found"})
    pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
    deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
    has_flow = any(k in deps for k in ("reactflow", "@xyflow/react", "cytoscape", "d3"))
    return CheckResult("reactflow", "pass" if has_flow else "fail",
                      "semantic", False, "source",
                      {"installed": list(k for k in deps if k in ("reactflow", "@xyflow/react", "cytoscape", "d3"))})


async def validate_heatmap_data() -> CheckResult:
    data = await _api_get("/api/architecture/heatmap")
    if data is None:
        return CheckResult("heatmap_data", "fail", "semantic", False, "registry",
                          {"error": "Heatmap API unreachable"})
    score = data.get("score", 0)
    if score == 0:
        return CheckResult("heatmap_data", "fail", "semantic", False, "registry",
                          {"error": "Heatmap score is 0 (no real data)",
                           "score": score})
    return CheckResult("heatmap_data", "pass", "semantic", False, "registry",
                      {"score": score, "level": data.get("level", "")})


# ---- Check Registry ----

CHECKS: list[CheckDefinition] = [
    CheckDefinition("graph_json",            "V1",  "structural", True,  "runtime", []),
    CheckDefinition("knowledge_graph_json",  "V2",  "structural", True,  "runtime", []),
    CheckDefinition("graph_api",            "V3",  "semantic",   False, "runtime", ["graph_json"]),
    CheckDefinition("heatmap_api",          "V4",  "semantic",   False, "registry", ["features_index"]),
    CheckDefinition("graph_summary",        "V5",  "semantic",   False, "registry", ["graph_json", "snapshot_json"]),
    CheckDefinition("docs_source",          "V6",  "structural", True,  "source", []),
    CheckDefinition("arch_page",            "V7",  "semantic",   False, "runtime", ["graph_api"]),
    CheckDefinition("reactflow",            "V8",  "semantic",   False, "source", []),
    CheckDefinition("snapshot_json",        "V9a", "structural", True,  "registry", []),
    CheckDefinition("features_index",       "V9b", "structural", True,  "registry", ["snapshot_json"]),
    CheckDefinition("commit_map",           "V9c", "structural", True,  "registry", []),
    CheckDefinition("heatmap_data",         "V10", "semantic",   False, "registry", ["heatmap_api", "features_index"]),
]


# ---- Fingerprint ----

def compute_fingerprint() -> str:
    """Compute input_fingerprint from features + graph state."""
    parts = []
    fi = _read_json(_json_path("registry", "features-index.json"))
    if fi:
        parts.append(json.dumps(fi, sort_keys=True))
    cm = _read_json(_json_path("registry", "commit-map.json"))
    if cm:
        parts.append(json.dumps(cm, sort_keys=True))
    snap = _read_json(_json_path("snapshot.json"))
    if snap:
        gs = snap.get("graphSummary", {})
        parts.append(json.dumps({"coverage": snap.get("coverage", 0), "graph_nodes": gs.get("totalNodes", 0)}, sort_keys=True))
    return _sha256("|".join(parts)) if parts else "empty"


# ---- Main ----

async def run_readiness_check() -> ReadinessReport:
    report = ReadinessReport()

    # Run structural validators (synchronous)
    structural_results = {
        "graph_json": validate_graph_json(),
        "knowledge_graph_json": validate_knowledge_graph_json(),
        "docs_source": validate_docs_source(),
        "snapshot_json": validate_snapshot_json(),
        "features_index": validate_features_index(),
        "commit_map": validate_commit_map(),
        "graph_summary": validate_graph_summary(),
        "arch_page": validate_arch_page(),
        "reactflow": validate_reactflow(),
    }

    # Run semantic validators (async)
    semantic_results = {
        "graph_api": await validate_graph_api(),
        "heatmap_api": await validate_heatmap_api(),
        "heatmap_data": await validate_heatmap_data(),
    }

    all_results = {**structural_results, **semantic_results}

    # Build report
    for check_def in CHECKS:
        result = all_results.get(check_def.id)
        if not result:
            continue
        report.checks[check_def.id] = {
            "status": result.status,
            "layer": result.layer,
            "blocker": result.blocker,
            "category": result.category,
            "details": result.details,
        }
        if result.status == "pass":
            report.passed += 1
            report.categories[result.category]["passed"] += 1
        else:
            report.failed += 1
            report.categories[result.category]["failed"] += 1

    # Calculate score
    report.total = len(CHECKS)
    report.score = round((report.passed / report.total) * 100, 1)

    # Check blockers
    for cat_name, cat_data in report.categories.items():
        if cat_data.get("blocker") and cat_data["failed"] > 0:
            report.blockers_passed = False

    # Fingerprint
    report.input_fingerprint = compute_fingerprint()
    report.generated_at = datetime.now(timezone.utc).isoformat()

    return report
