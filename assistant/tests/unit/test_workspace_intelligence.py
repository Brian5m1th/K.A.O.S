import tempfile
from pathlib import Path
from unittest.mock import AsyncMock
import pytest
from fastapi.testclient import TestClient

from app.core.automation_bus import AutomationBus
from app.main import app


@pytest.fixture
def temp_vault(monkeypatch):
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        monkeypatch.setenv("OBSIDIAN_VAULT_PATH", str(tmp_path))
        # Mock AutomationBus methods to avoid event loop pollution issues
        monkeypatch.setattr(AutomationBus, "start_worker", AsyncMock())
        monkeypatch.setattr(AutomationBus, "stop_worker", AsyncMock())
        monkeypatch.setattr(AutomationBus, "auto_import_workflows", AsyncMock())
        yield tmp_path


def test_workspace_intelligence_routes(temp_vault):
    # Use 'with TestClient' to trigger startup/lifespan events
    with TestClient(app) as client:
        # Get active app key to bypass headers
        app_key = app.state.api_key
        headers = {"x-api-key": app_key}

        # 1. Create a test markdown file
        note_file = temp_vault / "test_note.md"
        note_file.write_text("---\ntitle: Test Note\ntags: [initial]\n---\nHello this is a test note content.", encoding="utf-8")

        # 2. Test Health Endpoint
        resp = client.get("/api/workspace-intelligence/health", headers=headers)
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "success"
        assert data["metrics"]["total_notes"] == 1
        assert data["metrics"]["missing_frontmatter"] == 0

        # 3. Test Auto Tag Endpoint
        resp = client.post(
            "/api/workspace-intelligence/auto-tag",
            json={"path": "test_note.md"},
            headers=headers
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "success"
        assert "tags" in data
        assert "initial" in data["tags"]

        # 4. Test Suggest Connections Endpoint
        resp = client.post(
            "/api/workspace-intelligence/suggest-connections",
            json={"path": "test_note.md"},
            headers=headers
        )
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "success"
        assert isinstance(data["recommendations"], list)
