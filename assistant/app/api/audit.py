from fastapi import APIRouter, BackgroundTasks
from loguru import logger

from app.audit.audit_engine import AuditEngine
from app.audit.drl_snapshot import DRLSnapshotManager
from app.audit.feature_registry import FeatureRegistry
from app.audit.commit_mapper import CommitMapper
from app.audit.code_scanner import CodeScanner
from app.audit.sdd_resolver import SDDResolver
from app.audit.sdd_generator import SDDGenerator, SDDTemplate

router = APIRouter(prefix="/api/audit", tags=["audit"])


@router.post("/run")
async def run_audit(background_tasks: BackgroundTasks):
    """Run full documentation audit and return drift report."""
    logger.info("[api/audit] manual audit requested")
    report = AuditEngine.run_audit()
    DRLSnapshotManager.build_snapshot(report)

    return {
        "coverage": round(report.coverage, 1),
        "driftLevel": report.drift_level,
        "missingFeatures": report.missing_features,
        "outdatedDocs": report.outdated_docs,
        "inconsistentPhases": report.inconsistent_phases,
        "orphanedSDDs": report.orphaned_sdds,
        "undocumentedCode": report.undocumented_code,
        "timestamp": report.generated_at,
    }


@router.get("/snapshot")
async def get_snapshot():
    """Get latest DRL snapshot for frontend consumption."""
    snapshot = DRLSnapshotManager.load()
    if not snapshot:
        return {"error": "No snapshot available. Run audit first."}

    return {
        "features": [f.to_dict() for f in snapshot.features],
        "coverage": snapshot.coverage,
        "driftLevel": snapshot.drift_level,
        "lastCommit": snapshot.last_commit,
        "missingCount": snapshot.missing_count,
        "outdatedCount": snapshot.outdated_count,
        "graphSummary": {
            "totalNodes": snapshot.graph_summary.total_nodes,
            "totalEdges": snapshot.graph_summary.total_edges,
            "nodeTypes": snapshot.graph_summary.node_types,
            "generatedAt": snapshot.graph_summary.generated_at,
        },
        "timestamp": snapshot.generated_at,
    }


@router.get("/coverage")
async def get_coverage():
    """Get quick coverage percentage."""
    coverage = DRLSnapshotManager.get_coverage()
    drift = DRLSnapshotManager.get_drift_level()
    return {"coverage": coverage, "driftLevel": drift}


@router.post("/scan-commits")
async def scan_commits(limit: int = 200):
    """Generate commit map from git log."""
    entries = CommitMapper.generate_map(limit)
    return {
        "total": len(entries),
        "commits": [
            {
                "hash": e.hash,
                "message": e.message,
                "type": e.type,
                "impact": e.impact,
                "scope": e.scope,
                "features": e.features,
            }
            for e in entries
        ],
    }


@router.get("/commit-map")
async def get_commit_map():
    """Get existing commit map."""
    entries = CommitMapper.load()
    return {
        "total": len(entries),
        "commits": [
            {
                "hash": e.hash,
                "message": e.message,
                "type": e.type,
                "impact": e.impact,
                "scope": e.scope,
                "features": e.features,
            }
            for e in entries
        ],
    }


@router.post("/scan-code")
async def scan_code():
    """Scan codebase for features."""
    snapshot = CodeScanner.scan_all()
    return {
        "stores": snapshot.stores,
        "routes": snapshot.routes,
        "tools": snapshot.tools,
        "events": snapshot.events,
        "agents": snapshot.agents,
        "workflows": snapshot.workflows,
        "providers": snapshot.providers,
        "components": snapshot.components,
        "hooks": snapshot.hooks,
    }


@router.post("/register-feature")
async def register_feature(feature_data: dict):
    """Register a new feature in the registry."""
    from app.audit.feature_registry import FeatureEntry

    feature = FeatureEntry(
        id=feature_data.get("id", ""),
        name=feature_data.get("name", ""),
        phase=feature_data.get("phase", ""),
        status=feature_data.get("status", "planned"),
        docs=feature_data.get("docs", []),
        code_refs=feature_data.get("codeRefs", []),
        last_commit=feature_data.get("lastCommit", ""),
    )
    FeatureRegistry.register(feature)
    return feature.to_dict()


@router.get("/features")
async def list_features():
    """List all registered features."""
    FeatureRegistry.load_from_json()
    features = FeatureRegistry.list()
    return {"total": len(features), "features": [f.to_dict() for f in features]}


@router.get("/features/{feature_id}")
async def get_feature(feature_id: str):
    """Get a specific feature."""
    FeatureRegistry.load_from_json()
    feature = FeatureRegistry.get(feature_id)
    if not feature:
        return {"error": "Feature not found"}
    return feature.to_dict()


@router.post("/generate-sdd")
async def generate_sdd(template: dict):
    """Generate an SDD from template."""
    t = SDDTemplate(
        feature_id=template.get("featureId", ""),
        feature_name=template.get("featureName", ""),
        commit_hash=template.get("commitHash", ""),
        commit_message=template.get("commitMessage", ""),
        phase=template.get("phase", ""),
        detected_code_refs=template.get("detectedCodeRefs", []),
        impact_type=template.get("impactType", ""),
    )
    path = SDDGenerator.generate_sdd(t)
    return {"path": str(path), "generated": True}


@router.post("/generate-feature-node")
async def generate_feature_node(data: dict):
    """Generate a feature node SDD (Obsidian-ready)."""
    path = SDDGenerator.generate_feature_node(
        feature_id=data.get("featureId", ""),
        feature_name=data.get("featureName", ""),
        feature_type=data.get("featureType", "feature"),
        phase=data.get("phase", ""),
        tags=data.get("tags", []),
        links=data.get("links", []),
        description=data.get("description", ""),
        responsibilities=data.get("responsibilities", []),
        emits=data.get("emits", []),
        used_by=data.get("usedBy", []),
    )
    return {"path": str(path), "generated": True}