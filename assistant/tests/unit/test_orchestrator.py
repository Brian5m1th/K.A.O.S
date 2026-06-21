from uuid import UUID

import pytest

from app.domain.chat import ChatRequest
from app.domain.execution_plan import ExecutionPlan
from app.orchestrator.dead_letter_queue import DeadLetterQueue, FailedExecution
from app.orchestrator.plan_executor import PlanExecutor
from app.orchestrator.universal_orchestrator import UniversalOrchestrator
from app.providers.register_all import register_all_providers
from app.workflows.impl.registry import register_workflows


class TestDeadLetterQueue:
    def setup_method(self):
        DeadLetterQueue.clear()

    def test_add_and_list(self):
        fe = FailedExecution(
            execution_id=UUID(int=1),
            trace_id=UUID(int=2),
            workflow="chat",
            user_id=UUID(int=3),
            session_id=UUID(int=4),
            error="test error",
        )
        DeadLetterQueue.add(fe)
        assert DeadLetterQueue.count() == 1
        assert DeadLetterQueue.list_all()[0].error == "test error"

    def test_clear(self):
        DeadLetterQueue.add(
            FailedExecution(
                execution_id=UUID(int=1),
                trace_id=UUID(int=2),
                workflow="chat",
                user_id=UUID(int=3),
                session_id=UUID(int=4),
                error="err",
            )
        )
        DeadLetterQueue.clear()
        assert DeadLetterQueue.count() == 0

    def test_count(self):
        DeadLetterQueue.add(
            FailedExecution(
                execution_id=UUID(int=1),
                trace_id=UUID(int=2),
                workflow="chat",
                user_id=UUID(int=3),
                session_id=UUID(int=4),
                error="err",
            )
        )
        DeadLetterQueue.add(
            FailedExecution(
                execution_id=UUID(int=2),
                trace_id=UUID(int=2),
                workflow="rag",
                user_id=UUID(int=3),
                session_id=UUID(int=4),
                error="err2",
            )
        )
        assert DeadLetterQueue.count() == 2


class TestPlanExecutor:
    @pytest.mark.asyncio
    async def test_execute_unregistered_workflow_returns_error(self):
        register_all_providers()
        register_workflows()

        plan = ExecutionPlan.create(
            workflow="nonexistent",
            selected_model="qwen3:4b",
            user_id=UUID(int=0),
            session_id=UUID(int=1),
        )
        request = ChatRequest(session_id="test", message="hello")

        executor = PlanExecutor()
        result = ""
        async for chunk in executor.execute(plan, request):
            result += chunk

        assert "Erro na execucao" in result or "not registered" in result


class TestUniversalOrchestrator:
    @pytest.mark.asyncio
    async def test_execute_chat_workflow(self):
        register_all_providers()
        register_workflows()

        request = ChatRequest(session_id="test", message="hello")
        orchestrator = UniversalOrchestrator()

        result = ""
        async for chunk in orchestrator.execute(request, workflow="chat"):
            result += chunk

        assert isinstance(result, str)

    @pytest.mark.asyncio
    async def test_execute_memory_workflow(self):
        register_all_providers()
        register_workflows()

        request = ChatRequest(session_id="test", message="/save test")
        orchestrator = UniversalOrchestrator()

        result = ""
        async for chunk in orchestrator.execute(request, workflow="memory"):
            result += chunk

        assert isinstance(result, str)
