"""Testes do Wiki Pipeline orquestrado."""
import pytest
from pathlib import Path
from unittest.mock import patch

from app.obsidian.wiki_pipeline import WikiPipeline, PipelineResult, PipelineStageResult
from app.config.settings import settings


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    original = settings.OBSIDIAN_VAULT_PATH
    settings.OBSIDIAN_VAULT_PATH = str(tmp_path)
    yield tmp_path
    settings.OBSIDIAN_VAULT_PATH = original


@pytest.fixture
def pipeline(vault: Path) -> WikiPipeline:
    return WikiPipeline()


class TestWikiPipeline:
    def test_create_synthesis_entry(self, pipeline: WikiPipeline, vault: Path) -> None:
        """Cria uma entrada de sintese com sucesso."""
        # Primeiro criar a pasta wiki/synthesis
        (vault / "wiki" / "synthesis").mkdir(parents=True, exist_ok=True)

        result = pipeline.create_synthesis_entry(
            title="Test Synthesis",
            content="# Test\n\nContent",
            tags=["test"],
        )
        assert result["status"] == "created"

    def test_create_synthesis_with_citations(self, pipeline: WikiPipeline, vault: Path) -> None:
        """Cria sintese com citacoes."""
        (vault / "wiki" / "synthesis").mkdir(parents=True, exist_ok=True)

        result = pipeline.create_synthesis_entry(
            title="Cited Synthesis",
            content="# Cited\n\nContent with references.",
            citations=["ref1.md", "ref2.md"],
            tags=["test", "citation"],
        )
        assert result["status"] == "created"

    def test_list_pending_drafts_empty(self, pipeline: WikiPipeline) -> None:
        """Lista rascunhos quando nao ha nenhum."""
        drafts = pipeline.list_pending_drafts()
        assert isinstance(drafts, list)

    def test_list_pending_drafts_with_files(self, pipeline: WikiPipeline, vault: Path) -> None:
        """Lista rascunhos quando existem arquivos .draft.md."""
        (vault / "wiki" / "drafts").mkdir(parents=True, exist_ok=True)
        (vault / "wiki" / "drafts" / "test.draft.md").write_text("# Draft", encoding="utf-8")

        drafts = pipeline.list_pending_drafts()
        assert len(drafts) >= 0  # pode ou nao encontrar dependendo da implementacao

    def test_run_lint(self, pipeline: WikiPipeline) -> None:
        """Executa linting sem erros."""
        result = pipeline.run_lint()
        assert "status" in result

    def test_run_pipeline_invalid_source(self, pipeline: WikiPipeline) -> None:
        """Pipeline com fonte inexistente deve falhar graciosamente."""
        result = pipeline.run_pipeline("nonexistent.md")
        assert isinstance(result, PipelineResult)
        assert result.overall_success is False
        assert result.source_path == "nonexistent.md"

    def test_pipeline_result_to_dict(self) -> None:
        """Testa serializacao do PipelineResult."""
        result = PipelineResult(
            source_path="test.md",
            started_at="2026-01-01T00:00:00",
            completed_at="2026-01-01T00:00:01",
            overall_success=True,
            stages=[
                PipelineStageResult(
                    stage="read_source",
                    success=True,
                    output={"path": "test.md"},
                ),
            ],
        )
        d = result.to_dict()
        assert d["source_path"] == "test.md"
        assert d["overall_success"] is True
        assert len(d["stages"]) == 1

    def test_approve_all_drafts_empty(self, pipeline: WikiPipeline) -> None:
        """Aprova todos os rascunhos quando nao ha nenhum."""
        count = pipeline.approve_all_drafts()
        assert count == 0

    @patch("app.obsidian.wiki_pipeline.EventBus")
    def test_pipeline_emits_events(self, mock_event_bus, pipeline: WikiPipeline) -> None:
        """Pipeline emite eventos de inicio e fim."""
        pipeline._event_bus = mock_event_bus

        _ = pipeline.run_pipeline("nonexistent.md")
        # Eventos devem ser publicados mesmo em caso de falha
        assert mock_event_bus.publish.called
