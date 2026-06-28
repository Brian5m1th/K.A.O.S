import datetime
from fastapi import APIRouter
from pydantic import BaseModel
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from app.llm.factory import LLMFactory

router = APIRouter(prefix="/api/agents", tags=["Agents"])

# In-memory registry of running agent instances
AGENT_INSTANCES = {}


class AgentConfigPayload(BaseModel):
    name: str
    model: str
    systemPrompt: str
    temperature: float
    topP: float


@router.get("/status")
async def list_agent_statuses():
    return {
        "instances": {
            agent_id: {
                "status": inst["status"],
                "started_at": inst["started_at"],
                "model": inst["model"],
                "name": inst["name"],
            }
            for agent_id, inst in AGENT_INSTANCES.items()
        }
    }


@router.post("/{agent_id}/start")
async def start_agent(agent_id: str, payload: AgentConfigPayload):
    AGENT_INSTANCES[agent_id] = {
        "name": payload.name,
        "model": payload.model,
        "systemPrompt": payload.systemPrompt,
        "temperature": payload.temperature,
        "topP": payload.topP,
        "status": "running",
        "started_at": datetime.datetime.now().isoformat(),
    }
    return {"status": "running", "agent_id": agent_id}


@router.post("/{agent_id}/stop")
async def stop_agent(agent_id: str):
    if agent_id in AGENT_INSTANCES:
        AGENT_INSTANCES[agent_id]["status"] = "stopped"
        return {"status": "stopped", "agent_id": agent_id}
    return {"status": "stopped", "agent_id": agent_id}


@router.post("/{agent_id}/pause")
async def pause_agent(agent_id: str):
    if agent_id in AGENT_INSTANCES:
        AGENT_INSTANCES[agent_id]["status"] = "paused"
        return {"status": "paused", "agent_id": agent_id}
    return {"status": "paused", "agent_id": agent_id}


@router.post("/{agent_id}/resume")
async def resume_agent(agent_id: str):
    if agent_id in AGENT_INSTANCES:
        AGENT_INSTANCES[agent_id]["status"] = "running"
        return {"status": "running", "agent_id": agent_id}
    return {"status": "running", "agent_id": agent_id}


class ChatPayload(BaseModel):
    message: str
    history: list[dict] = []


@router.post("/{agent_id}/chat")
async def chat_with_agent(agent_id: str, payload: ChatPayload):
    inst = AGENT_INSTANCES.get(agent_id)
    system_prompt = inst["systemPrompt"] if inst else "You are a helpful AI assistant."
    model = inst["model"] if inst else "kaos"
    temperature = inst["temperature"] if inst else 0.7

    messages_list = []
    messages_list.append(SystemMessage(content=system_prompt))
    for m in payload.history:
        if m.get("role") == "user":
            messages_list.append(HumanMessage(content=m.get("content", "")))
        elif m.get("role") == "assistant":
            messages_list.append(AIMessage(content=m.get("content", "")))
    messages_list.append(HumanMessage(content=payload.message))

    try:
        factory = LLMFactory()
        provider = factory.build(model, temperature=temperature)
        resp = await provider.ainvoke(messages_list)
        return {"response": resp.content}
    except Exception:
        return {
            "response": f"[Agent Response] Ollama model '{model}' offline or not ready. Echo: '{payload.message}'"
        }
