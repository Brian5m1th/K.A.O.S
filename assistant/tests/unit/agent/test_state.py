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
        assert state["tool_result"] is None
        assert state["messages"] == []
        assert state["retrieved_context"] == []
        assert state["tool_args"] == {}

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
        assert state["tool_args"]["content"] == "teste"

    def test_state_with_tool_result(self) -> None:
        state: AgentState = {
            "messages": [],
            "retrieved_context": [],
            "tool_to_call": None,
            "tool_args": {},
            "tool_result": "nota criada com sucesso",
            "session_id": "test",
        }
        assert state["tool_result"] == "nota criada com sucesso"
        assert state["tool_to_call"] is None

    def test_state_with_messages(self) -> None:
        state: AgentState = {
            "messages": [{"role": "user", "content": "ola"}],
            "retrieved_context": [],
            "tool_to_call": None,
            "tool_args": {},
            "tool_result": None,
            "session_id": "test",
        }
        assert len(state["messages"]) == 1
        assert state["messages"][0]["role"] == "user"
        assert state["messages"][0]["content"] == "ola"

    def test_state_with_context(self) -> None:
        state: AgentState = {
            "messages": [],
            "retrieved_context": [{"doc": "sobre KAOS", "score": 0.95}],
            "tool_to_call": None,
            "tool_args": {},
            "tool_result": None,
            "session_id": "test",
        }
        assert len(state["retrieved_context"]) == 1
        assert state["retrieved_context"][0]["score"] == 0.95
