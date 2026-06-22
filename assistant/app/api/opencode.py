from pathlib import Path

from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/opencode", tags=["OpenCode"])

OPCODE_DIR = Path(__file__).resolve().parent.parent.parent.parent / ".opencode"


@router.get("/status")
async def opencode_status():
    """Return the status of the OpenCode configuration layer.

    OpenCode agents, references, rules, skills, and tools
    are defined in the `.opencode/` directory at the project root.
    """
    if not OPCODE_DIR.exists():
        return {"configured": False, "path": str(OPCODE_DIR)}

    agents = (
        sorted(p.stem for p in (OPCODE_DIR / "agents").glob("*.md"))
        if (OPCODE_DIR / "agents").exists()
        else []
    )
    references = (
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
        "references": references,
        "rules": rules,
        "skills": skills,
        "tools": tools,
        "total": len(agents) + len(references) + len(rules) + len(skills) + len(tools),
    }


@router.get("/agents")
async def list_opencode_agents():
    """List all OpenCode agents available."""
    agents_dir = OPCODE_DIR / "agents"
    if not agents_dir.exists():
        return {"agents": []}

    agents = []
    for f in sorted(agents_dir.glob("*.md")):
        content = f.read_text(encoding="utf-8")
        first_line = content.split("\n")[0].lstrip("# ") if content else f.stem
        agents.append({"id": f.stem, "name": first_line, "file": f.name})

    return {"agents": agents}


@router.get("/agent/{agent_id}")
async def get_opencode_agent(agent_id: str):
    """Get the content of a specific OpenCode agent definition."""
    agent_file = OPCODE_DIR / "agents" / f"{agent_id}.md"
    if not agent_file.exists():
        raise HTTPException(status_code=404, detail="Agent not found")
    content = agent_file.read_text(encoding="utf-8")
    return {"id": agent_id, "content": content}
