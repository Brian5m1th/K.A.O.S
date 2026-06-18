from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage
import operator


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], operator.add]
    retrieved_context: list[dict]
    tool_to_call: str | None
    tool_args: dict
    tool_result: dict | None
    session_id: str
    user_id: str
    username: str
    role: str
    model: str | None
    ingest_source_path: str | None
