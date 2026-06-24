from app.observability.event_bus import Event, EventSubscriber, EventBus
from datetime import datetime, timezone
from uuid import uuid4
import asyncio

from loguru import logger

from app.audit.audit_engine import AuditEngine
from app.audit.drl_snapshot import DRLSnapshotManager
from app.config.settings import settings

from app.ai.vault_analyzer.analyzer_engine import AnalyzerEngine


class DriftSubscriber(EventSubscriber):
    async def on_event(self, event: Event) -> None:
        if event.name == "audit.started":
            logger.info("[drift_subscriber] audit cycle started")
            return

        if event.name == "audit.completed":
            report = event.data.get("report")
            if report:
                logger.info(
                    f"[drift_subscriber] audit completed: coverage={report.get('coverage')}%"
                )
                DRLSnapshotManager.build_snapshot()

                drift_level = report.get("drift_level", "low")
                if drift_level == "high":
                    await self._emit_alert(report)

        if event.name == "drift.detected":
            severity = event.data.get("severity", "medium")
            missing = event.data.get("missing", [])
            logger.warning(
                f"[drift_subscriber] drift detected: {severity}, missing={missing}"
            )

            # Auto-trigger VaultAnalyzer quando drift é detectado (RF-B04)
            logger.info("[kirl] drift detectado — disparando VaultAnalyzer")
            asyncio.create_task(AnalyzerEngine.analyze_async())

    async def _emit_alert(self, report: dict) -> None:
        alert_event = Event(
            name="system:alert",
            execution_id=uuid4(),
            trace_id=uuid4(),
            data={
                "type": "documentation-drift",
                "severity": "high",
                "message": "Architecture documentation is behind implementation",
                "coverage": report.get("coverage"),
                "missing": report.get("missing_features", []),
                "outdated": report.get("outdated_docs", []),
            },
        )
        await EventBus.publish(alert_event)


class AuditScheduler:
    _interval_seconds = 30

    @classmethod
    async def run_periodic_audit(cls) -> None:
        # RF-H02: Só executa automaticamente em production
        if settings.APP_ENV != "production":
            logger.info(
                "[kirl] AuditScheduler desativado em modo {} "
                "(só executa automaticamente em production)",
                settings.APP_ENV,
            )
            return

        logger.info(
            "[kirl] AuditScheduler ativo: {} days entre auditorias",
            settings.AUDIT_INTERVAL_DAYS,
        )

        while True:
            start_event = Event(
                name="audit.started",
                execution_id=uuid4(),
                trace_id=uuid4(),
                data={"timestamp": datetime.now(timezone.utc).isoformat()},
            )
            await EventBus.publish(start_event)

            report = AuditEngine.run_audit()

            complete_event = Event(
                name="audit.completed",
                execution_id=uuid4(),
                trace_id=uuid4(),
                data={
                    "coverage": report.coverage,
                    "drift_level": report.drift_level,
                    "missing_features": report.missing_features,
                    "outdated_docs": report.outdated_docs,
                    "inconsistent_phases": report.inconsistent_phases,
                    "orphaned_sdds": report.orphaned_sdds,
                    "undocumented_code": report.undocumented_code,
                    "report": {
                        "coverage": report.coverage,
                        "drift_level": report.drift_level,
                        "missing_features": report.missing_features,
                        "outdated_docs": report.outdated_docs,
                    },
                },
            )
            await EventBus.publish(complete_event)

            if report.drift_level == "high":
                drift_event = Event(
                    name="drift.detected",
                    execution_id=uuid4(),
                    trace_id=uuid4(),
                    data={
                        "severity": "high",
                        "missing": report.missing_features,
                        "outdated": report.outdated_docs,
                    },
                )
                await EventBus.publish(drift_event)

            interval = settings.AUDIT_INTERVAL_DAYS * 86400
            logger.debug(
                "[kirl] next audit in {} days ({} seconds)",
                settings.AUDIT_INTERVAL_DAYS,
                interval,
            )
            await asyncio.sleep(interval)

    @classmethod
    def set_interval(cls, seconds: int) -> None:
        cls._interval_seconds = seconds
