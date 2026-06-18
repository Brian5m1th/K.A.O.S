from app.agent.state import AgentState


class TestAgentState:
    def test_state_keys(self) -> None:
        state: AgentState = {
            "messages": [],
            "retrieved_context": [],
            "tool_to_call": None,
            "tool_args": {},
            "tool_result": None,
            "session_id": "test",
        }
        assert state["session_id"] == "test"
        assert state["tool_to_call"] is None

    def test_state_with_tool(self) -> None:
        state: AgentState = {
            "messages": [],
            "retrieved_context": [],
            "tool_to_call": "create_note",
            "tool_args": {"title": "Teste", "content": "teste"},
            "tool_result": None,
            "session_id": "test",
        }
        assert state["tool_to_call"] == "create_note"
        assert state["tool_args"]["title"] == "Teste"
