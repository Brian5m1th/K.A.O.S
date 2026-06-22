from loguru import logger

from app.domain.intent import IntentResult
from app.domain.context import RequestContext
from app.domain.workflow import WorkflowType


class WorkflowRouter:
    def resolve(self, intent: IntentResult, context: RequestContext) -> WorkflowType:
        logger.bind(
            event="workflow.resolved",
            workflow=intent.workflow.value,
            command=intent.command.value if intent.command else None,
            confidence=intent.confidence,
            trace_id=str(context.trace_id),
            execution_id=str(context.execution_id),
        ).info(f"workflow resolved: {intent.workflow.value}")
        return intent.workflow
