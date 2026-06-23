from pathlib import Path
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/opencode", tags=["OpenCode"])

OPCODE_DIR = Path(__file__).resolve().parent.parent.parent.parent / ".opencode"


@router.get("/status")
async def opencode_status():
    if not OPCODE_DIR.exists():
        return {"configured": False, "path": str(OPCODE_DIR)}
    agents = (
        sorted(p.stem for p in (OPCODE_DIR / "agents").glob("*.md"))
        if (OPCODE_DIR / "agents").exists()
        else []
    )
    refs = (
        sorted(p.stem for p in (OPCODE_DIR / "references").glob("*.md"))
        if (OPCODE_DIR / "references").exists()
        else []
    )
    rules = (
        sorted(p.stem for p in (OPCODE_DIR / "rules").glob("*.md"))
        if (OPCODE_DIR / "rules").exists()
        else []
    )
    skills = (
        sorted(p.stem for p in (OPCODE_DIR / "skills").glob("*.md"))
        if (OPCODE_DIR / "skills").exists()
        else []
    )
    tools = (
        sorted(p.stem for p in (OPCODE_DIR / "tools").glob("*.md"))
        if (OPCODE_DIR / "tools").exists()
        else []
    )
    return {
        "configured": True,
        "path": str(OPCODE_DIR),
        "agents": agents,
        "references": refs,
        "rules": rules,
        "skills": skills,
        "tools": tools,
        "total": len(agents) + len(refs) + len(rules) + len(skills) + len(tools),
    }


@router.get("/agents")
async def list_agents():
    d = OPCODE_DIR / "agents"
    if not d.exists():
        return {"agents": []}
    agents = []
    for f in sorted(d.glob("*.md")):
        c = f.read_text(encoding="utf-8")
        agents.append(
            {
                "id": f.stem,
                "name": c.split("\n")[0].lstrip("# ") if c else f.stem,
                "file": f.name,
            }
        )
    return {"agents": agents}


@router.get("/agent/{agent_id}")
async def get_agent(agent_id: str):
    f = OPCODE_DIR / "agents" / f"{agent_id}.md"
    if not f.exists():
        raise HTTPException(404, detail="Agent not found")
    return {"id": agent_id, "content": f.read_text(encoding="utf-8")}
