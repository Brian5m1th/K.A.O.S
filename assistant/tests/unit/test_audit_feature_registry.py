import pytest
from app.audit.feature_registry import FeatureEntry, FeatureRegistry


class TestFeatureEntry:
    def test_create_minimal(self):
        entry = FeatureEntry(id="test-feature", name="Test Feature", phase="fase-1", status="planned")
        assert entry.id == "test-feature"
        assert entry.name == "Test Feature"
        assert entry.status == "planned"
        assert entry.docs == []
        assert entry.code_refs == []

    def test_create_full(self):
        entry = FeatureEntry(id="test-feature", name="Test Feature", phase="fase-1", status="done",
                             docs=["SDD-TEST.md"], code_refs=["src/app/main.py"])
        assert entry.docs == ["SDD-TEST.md"]
        assert entry.code_refs == ["src/app/main.py"]

    def test_to_dict(self):
        entry = FeatureEntry(id="test", name="Test", phase="p1", status="in-progress")
        data = entry.to_dict()
        assert data["id"] == "test"
        assert data["name"] == "Test"
        assert data["phase"] == "p1"
        assert data["status"] == "in-progress"
        assert "createdAt" in data
        assert "updatedAt" in data

    def test_from_dict(self):
        data = {"id": "test", "name": "Test", "phase": "p1", "status": "done",
                "docs": ["doc.md"], "codeRefs": ["code.py"], "lastCommit": "abc123"}
        entry = FeatureEntry.from_dict(data)
        assert entry.id == "test"
        assert entry.docs == ["doc.md"]
        assert entry.code_refs == ["code.py"]
        assert entry.last_commit == "abc123"


class TestFeatureRegistry:
    def setup_method(self):
        FeatureRegistry.clear()

    def test_register_and_get(self):
        entry = FeatureEntry(id="test", name="Test", phase="p1", status="planned")
        FeatureRegistry.register(entry)
        assert FeatureRegistry.get("test") is entry

    def test_register_many(self):
        entries = [
            FeatureEntry(id="a", name="A", phase="p1", status="planned"),
            FeatureEntry(id="b", name="B", phase="p2", status="done"),
        ]
        FeatureRegistry.register_many(entries)
        assert FeatureRegistry.get("a") is not None
        assert FeatureRegistry.get("b") is not None

    def test_list(self):
        FeatureRegistry.register(FeatureEntry(id="a", name="A", phase="p1", status="planned"))
        FeatureRegistry.register(FeatureEntry(id="b", name="B", phase="p1", status="done"))
        assert len(FeatureRegistry.list()) == 2

    def test_list_by_phase(self):
        FeatureRegistry.register(FeatureEntry(id="a", name="A", phase="p1", status="planned"))
        FeatureRegistry.register(FeatureEntry(id="b", name="B", phase="p2", status="done"))
        assert len(FeatureRegistry.list_by_phase("p1")) == 1
        assert len(FeatureRegistry.list_by_phase("p2")) == 1

    def test_list_by_status(self):
        FeatureRegistry.register(FeatureEntry(id="a", name="A", phase="p1", status="planned"))
        FeatureRegistry.register(FeatureEntry(id="b", name="B", phase="p1", status="done"))
        assert len(FeatureRegistry.list_by_status("done")) == 1
        assert len(FeatureRegistry.list_by_status("planned")) == 1

    def test_unregister(self):
        FeatureRegistry.register(FeatureEntry(id="a", name="A", phase="p1", status="planned"))
        FeatureRegistry.unregister("a")
        assert FeatureRegistry.get("a") is None

    def test_update_status(self):
        FeatureRegistry.register(FeatureEntry(id="a", name="A", phase="p1", status="planned"))
        FeatureRegistry.update_status("a", "done")
        assert FeatureRegistry.get("a").status == "done"

    def test_update_last_commit(self):
        FeatureRegistry.register(FeatureEntry(id="a", name="A", phase="p1", status="planned"))
        FeatureRegistry.update_last_commit("a", "abc123")
        assert FeatureRegistry.get("a").last_commit == "abc123"

    def test_add_doc_ref(self):
        FeatureRegistry.register(FeatureEntry(id="a", name="A", phase="p1", status="planned"))
        FeatureRegistry.add_doc_ref("a", "SDD-TEST.md")
        assert "SDD-TEST.md" in FeatureRegistry.get("a").docs

    def test_add_code_ref(self):
        FeatureRegistry.register(FeatureEntry(id="a", name="A", phase="p1", status="planned"))
        FeatureRegistry.add_code_ref("a", "src/main.py")
        assert "src/main.py" in FeatureRegistry.get("a").code_refs

    def test_search(self):
        FeatureRegistry.register(FeatureEntry(id="my-feature", name="My Feature", phase="p1", status="planned"))
        results = FeatureRegistry.search("my-feature")
        assert len(results) >= 1

    def test_get_by_name(self):
        FeatureRegistry.register(FeatureEntry(id="test", name="Test Feature", phase="p1", status="planned"))
        entry = FeatureRegistry.get_by_name("Test Feature")
        assert entry is not None
        assert entry.id == "test"

    def test_export_json(self):
        FeatureRegistry.register(FeatureEntry(id="test", name="Test", phase="p1", status="done"))
        data = FeatureRegistry.export_json()
        assert data["version"] == "1.0"
        assert data["total_features"] >= 1
        assert len(data["features"]) >= 1