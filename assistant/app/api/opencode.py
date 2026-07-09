"""
OpenCode Configuration Layer API.

Provides endpoints to discover agents, commands, models, providers,
rules, references, skills, and tools defined in the ``.opencode/`` directory.
Supports dynamic cache invalidation via ``OpenCodeWatcher``.
"""

from pathlib import Path

from fastapi import APIRouter, HTTPException
from loguru import logger
from pydantic import BaseModel

from app.core.opencode_executor import OpenCodeExecutor
from app.core.opencode_watcher import OpenCodeWatcher
from app.core.runtime_path_resolver import RuntimePathResolver

router = APIRouter(prefix="/api/opencode", tags=["OpenCode"])

# Module-level watcher instance (started/stopped by the app lifespan)
_watcher: OpenCodeWatcher | None = None
_scan_cache: dict | None = None

# Directories to scan (maps category → subdirectory name)
SCAN_DIRS: dict[str, str] = {
    "agents": "agents",
    "commands": "commands",
    "models": "models",
    "providers": "providers",
    "references": "references",
    "rules": "rules",
    "skills": "skills",
    "tools": "tools",
}

SUPPORTED_EXTENSIONS = (".md", ".yaml", ".yml", ".json")


def get_watcher() -> OpenCodeWatcher | None:
    return _watcher


def set_watcher(watcher: OpenCodeWatcher) -> None:
    global _watcher
    _watcher = watcher


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _opencode_root() -> Path:
    return RuntimePathResolver.get_opencode_path()


def _scan_subdir(subdir: str) -> list[dict]:
    """Scan a subdirectory of .opencode/ and return file entries."""
    d = _opencode_root() / subdir
    if not d.exists():
        return []
    entries = []
    for f in sorted(d.iterdir()):
        if f.is_file() and f.suffix in SUPPORTED_EXTENSIONS:
            try:
                content = f.read_text(encoding="utf-8")
            except Exception:
                content = ""
            entries.append(
                {
                    "id": f.stem,
                    "name": content.split("\n")[0].lstrip("# ") if content else f.stem,
                    "file": f.name,
                    "ext": f.suffix,
                }
            )
    return entries


def _full_scan(force: bool = False) -> dict:
    """Perform a full scan of the .opencode/ directory.

    Results are cached. If ``OpenCodeWatcher`` reports dirty cache,
    the scan is re-executed.
    """
    global _scan_cache

    # Check watcher cache state
    if _watcher and not force:
        if not _watcher.is_dirty() and _scan_cache is not None:
            return _scan_cache

    root = _opencode_root()
    if not root.exists():
        _scan_cache = {"configured": False, "path": str(root)}
        return _scan_cache

    result: dict = {"configured": True, "path": str(root)}
    total = 0
    for category, subdir in SCAN_DIRS.items():
        entries = _scan_subdir(subdir)
        result[category] = [e["id"] for e in entries]
        total += len(entries)

    result["total"] = total

    _scan_cache = result
    if _watcher:
        _watcher.mark_clean()

    return result


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@router.get("/status")
async def opencode_status():
    return _full_scan()


@router.post("/refresh")
async def refresh_cache():
    """Force a cache refresh."""
    result = _full_scan(force=True)
    logger.info("[opencode] cache manually refreshed")
    return {"status": "refreshed", "total": result.get("total", 0)}


@router.get("/agents")
async def list_agents():
    entries = _scan_subdir("agents")
    return {"agents": entries}


@router.get("/commands")
async def list_commands():
    entries = _scan_subdir("commands")
    return {"commands": entries}


@router.get("/models")
async def list_models():
    entries = _scan_subdir("models")
    return {"models": entries}


@router.get("/providers")
async def list_providers():
    entries = _scan_subdir("providers")
    return {"providers": entries}


@router.get("/{category}")
async def list_category(category: str):
    if category not in SCAN_DIRS:
        raise HTTPException(404, detail=f"Unknown category '{category}'")
    entries = _scan_subdir(SCAN_DIRS[category])
    return {category: entries}


@router.get("/agent/{agent_id}")
async def get_agent(agent_id: str):
    f = _opencode_root() / "agents" / f"{agent_id}.md"
    if not f.exists():
        raise HTTPException(404, detail="Agent not found")
    return {"id": agent_id, "content": f.read_text(encoding="utf-8")}


@router.get("/{category}/{item_id}")
async def get_category_item(category: str, item_id: str):
    if category not in SCAN_DIRS:
        raise HTTPException(404, detail=f"Unknown category '{category}'")
    subdir = SCAN_DIRS[category]
    for ext in SUPPORTED_EXTENSIONS:
        f = _opencode_root() / subdir / f"{item_id}{ext}"
        if f.exists():
            try:
                return {
                    "id": item_id,
                    "category": category,
                    "file": f.name,
                    "content": f.read_text(encoding="utf-8"),
                }
            except Exception as exc:
                raise HTTPException(500, detail=f"Failed to read file: {exc}")
    raise HTTPException(
        404, detail=f"Item '{item_id}' not found in category '{category}'"
    )


# Executar comandos CLI propostos na sandbox (Docker ou local)


class ExecuteCommandRequest(BaseModel):
    command: str
    user_approved: bool = False


@router.post("/execute")
async def execute_opencode_command(payload: ExecuteCommandRequest):
    return OpenCodeExecutor.execute(payload.command, payload.user_approved)
