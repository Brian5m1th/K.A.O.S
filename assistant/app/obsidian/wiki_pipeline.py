"""Wiki Pipeline — Pipeline orquestrado Source -> Entities -> Concepts -> Synthesis.

Consolida as ferramentas wiki existentes em um fluxo unificado
que pode ser executado de forma atomica ou em etapas.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from loguru import logger

from app.obsidian.services.obsidian_service import ObsidianService
from app.obsidian.tools.wiki.create_synthesis_tool import create_synthesis
from app.obsidian.tools.wiki.lint_wiki_tool import lint_wiki
from app.obsidian.tools.wiki.draft_tools import approve_draft, list_drafts
from app.observability.event_bus import EventBus


# ---------------------------------------------------------------------------
# DTOs
# ---------------------------------------------------------------------------


@dataclass
class PipelineStageResult:
    """Resultado de uma etapa do pipeline."""

    stage: str
    success: bool
    output: Any = None
    error: str | None = None
    duration_ms: float = 0.0


@dataclass
class PipelineResult:
    """Resultado completo da execucao do pipeline."""

    source_path: str
    stages: list[PipelineStageResult] = field(default_factory=list)
    started_at: str = ""
    completed_at: str = ""
    overall_success: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "source_path": self.source_path,
            "stages": [asdict(s) for s in self.stages],
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "overall_success": self.overall_success,
        }


# ---------------------------------------------------------------------------
# Wiki Pipeline
# ---------------------------------------------------------------------------


class WikiPipeline:
    """Pipeline orquestrado do fluxo Wiki-First.

    Fluxo completo:
    1. Source -> Leitura do arquivo fonte
    2. Entities -> Extração de entidades
    3. Concepts -> Criação de conceitos
    4. Synthesis -> Geração de síntese
    5. Draft -> Criação de rascunho
    6. Approve -> Aprovação do rascunho (opcional)
    """

    def __init__(
        self,
        obsidian_service: ObsidianService | None = None,
        event_bus: EventBus | None = None,
    ) -> None:
        self._obsidian = obsidian_service or ObsidianService()
        self._event_bus = event_bus

    def create_synthesis_entry(
        self,
        title: str,
        content: str,
        citations: list[str] | None = None,
        tags: list[str] | None = None,
        folder: str = "wiki/synthesis",
    ) -> dict[str, Any]:
        """Cria uma entrada de sintese no wiki.

        Args:
            title: Titulo da sintese.
            content: Conteudo markdown da sintese.
            citations: Lista de citacoes/referencias.
            tags: Tags para categorizacao.
            folder: Pasta de destino no vault.

        Returns:
            Dicionario com resultado da operacao.
        """
        try:
            # Usa a tool existente de criacao de sintese
            result = create_synthesis.invoke(
                {
                    "title": title,
                    "content": content,
                    "citations": citations or [],
                    "tags": tags or [],
                }
            )
            logger.info("[wiki] synthesis created: {}", title)
            return {"status": "created", "title": title, "result": result}
        except Exception as e:
            logger.error("[wiki] synthesis failed: {} - {}", title, e)
            return {"status": "error", "title": title, "error": str(e)}

    def run_lint(self) -> dict[str, Any]:
        """Executa linting completo no wiki.

        Returns:
            Relatorio com orfaos e links quebrados.
        """
        try:
            result = lint_wiki.invoke({})
            logger.info("[wiki] lint complete")
            return {
                "status": "ok",
                "orphans": result.get("orphans", []),
                "broken_links": result.get("broken_links", []),
            }
        except Exception as e:
            logger.error("[wiki] lint failed: {}", e)
            return {"status": "error", "error": str(e)}

    def list_pending_drafts(self) -> list[dict[str, Any]]:
        """Lista todos os rascunhos pendentes no wiki.

        Returns:
            Lista de rascunhos com metadados.
        """
        try:
            result = list_drafts.invoke({})
            drafts = result.get("drafts", [])
            logger.info("[wiki] {} pending drafts", len(drafts))
            return drafts
        except Exception as e:
            logger.error("[wiki] list drafts failed: {}", e)
            return []

    def approve_all_drafts(self) -> int:
        """Aprova todos os rascunhos pendentes.

        Returns:
            Numero de rascunhos aprovados.
        """
        drafts = self.list_pending_drafts()
        approved = 0
        for draft in drafts:
            try:
                path = draft.get("path", "")
                if path:
                    approve_draft.invoke({"path": path})
                    approved += 1
            except Exception as e:
                logger.warning(
                    "[wiki] failed to approve draft {}: {}", draft.get("path"), e
                )

        logger.info("[wiki] approved {} / {} drafts", approved, len(drafts))
        return approved

    def run_pipeline(
        self,
        source_path: str,
        auto_approve: bool = False,
    ) -> PipelineResult:
        """Executa o pipeline completo para uma fonte.

        Fluxo:
        source -> entities -> concepts -> synthesis -> draft -> (opcional) approve

        Args:
            source_path: Caminho do arquivo fonte no vault.
            auto_approve: Se True, aprova o rascunho automaticamente.

        Returns:
            PipelineResult com resultados de cada etapa.
        """
        result = PipelineResult(
            source_path=source_path,
            started_at=datetime.now(timezone.utc).isoformat(),
        )

        # Emitir evento de inicio
        if self._event_bus:
            self._event_bus.publish(
                "WIKI_PIPELINE_STARTED",
                {
                    "source_path": source_path,
                    "auto_approve": auto_approve,
                },
            )

        try:
            # Etapa 1: Ler o arquivo fonte
            logger.info("[pipeline] stage 1/5: reading source {}", source_path)
            note = self._obsidian.read_note(source_path)
            result.stages.append(
                PipelineStageResult(
                    stage="read_source",
                    success=True,
                    output={"path": source_path, "size": len(note.content)},
                )
            )

            # Extrair titulo do conteudo
            title = (
                note.content.split("\n")[0].replace("# ", "").strip()
                or Path(source_path).stem
            )

            # Etapa 2-5: Criar sintese (unifica entities -> concepts -> synthesis)
            logger.info("[pipeline] stage 2/5: creating synthesis for '{}'", title)
            synthesis_result = self.create_synthesis_entry(
                title=f"{title} - Synthesis",
                content=note.content,
                tags=["auto-generated", "pipeline"],
                folder="wiki/synthesis",
            )
            result.stages.append(
                PipelineStageResult(
                    stage="create_synthesis",
                    success=synthesis_result["status"] == "created",
                    output=synthesis_result,
                    error=synthesis_result.get("error"),
                )
            )

            # Etapa 6: Lint (opcional, sempre executa)
            logger.info("[pipeline] stage 3/5: running lint")
            lint_result = self.run_lint()
            result.stages.append(
                PipelineStageResult(
                    stage="lint",
                    success=lint_result["status"] == "ok",
                    output=lint_result,
                    error=lint_result.get("error"),
                )
            )

            # Auto-approve se solicitado
            if auto_approve:
                logger.info("[pipeline] stage 4/5: approving drafts")
                approved = self.approve_all_drafts()
                result.stages.append(
                    PipelineStageResult(
                        stage="approve_drafts",
                        success=True,
                        output={"approved": approved},
                    )
                )

            result.overall_success = all(s.success for s in result.stages)

        except Exception as e:
            logger.error("[pipeline] failed: {}", e)
            result.stages.append(
                PipelineStageResult(
                    stage="pipeline",
                    success=False,
                    error=str(e),
                )
            )
            result.overall_success = False

        finally:
            result.completed_at = datetime.now(timezone.utc).isoformat()

        # Emitir evento de conclusao
        if self._event_bus:
            self._event_bus.publish("WIKI_PIPELINE_COMPLETED", result.to_dict())

        return result

    def run_full_pipeline(
        self,
        source_paths: list[str] | None = None,
        auto_approve: bool = False,
    ) -> list[PipelineResult]:
        """Executa o pipeline para multiplas fontes.

        Se source_paths for None, busca automaticamente na pasta raw/.
        """
        if source_paths is None:
            source_paths = self._discover_raw_sources()

        results = []
        for path in source_paths:
            try:
                pr = self.run_pipeline(path, auto_approve=auto_approve)
                results.append(pr)
            except Exception as e:
                logger.error("[pipeline] error processing {}: {}", path, e)
                results.append(
                    PipelineResult(
                        source_path=path,
                        overall_success=False,
                        stages=[
                            PipelineStageResult(
                                stage="pipeline",
                                success=False,
                                error=str(e),
                            )
                        ],
                    )
                )

        return results

    def _discover_raw_sources(self) -> list[str]:
        """Descobre arquivos fonte na pasta raw/ do vault."""
        try:
            notes = self._obsidian.list_notes("raw")
            return [n for n in notes if n.endswith(".md")]
        except Exception:
            return []
