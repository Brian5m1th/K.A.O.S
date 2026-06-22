from app.audit.code_scanner import CodeScanner, CodeSnapshot


class TestCodeSnapshot:
    def test_create_empty(self):
        snap = CodeSnapshot()
        assert snap.stores == []
        assert snap.routes == []
        assert snap.tools == []
        assert snap.events == []
        assert snap.agents == []
        assert snap.workflows == []
        assert snap.providers == []
        assert snap.components == []
        assert snap.hooks == []

    def test_create_with_data(self):
        snap = CodeSnapshot(
            stores=["chat-store.ts"],
            routes=["dashboard.tsx"],
            tools=["tool-schema.ts"],
        )
        assert snap.stores == ["chat-store.ts"]
        assert snap.routes == ["dashboard.tsx"]
        assert snap.tools == ["tool-schema.ts"]


class TestCodeScanner:
    def test_scan_returns_snapshot(self):
        result = CodeScanner.scan_all()
        assert isinstance(result, CodeSnapshot)
        assert hasattr(result, "stores")
        assert hasattr(result, "routes")
        assert hasattr(result, "tools")

    def test_exclude_dirs_present(self):
        assert ".git" in CodeScanner._exclude_dirs
        assert "node_modules" in CodeScanner._exclude_dirs
        assert "__pycache__" in CodeScanner._exclude_dirs
        assert ".venv" in CodeScanner._exclude_dirs
