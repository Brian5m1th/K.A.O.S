import tempfile
from pathlib import Path
from app.audit.sdd_generator import SDDGenerator, SDDTemplate


class TestSDDGenerator:
    def test_generate_sdd_creates_file(self):
        template = SDDTemplate(
            feature_id="test-feature",
            feature_name="Test Feature",
            commit_hash="abc123",
            commit_message="feat: test feature",
            phase="p1",
            detected_code_refs=["src/test.py"],
            impact_type="high",
        )
        with tempfile.TemporaryDirectory() as tmp:
            SDDGenerator._auto_dir = Path(tmp)
            SDDGenerator._sdd_dir = Path(tmp)
            result = SDDGenerator.generate_sdd(template)
            assert result.exists()
            content = result.read_text(encoding="utf-8")
            assert "test-feature" in content
            assert "Test Feature" in content
            assert "AUTO-GENERATED" in content

    def test_generate_sdd_frontmatter(self):
        template = SDDTemplate(
            feature_id="test-feature",
            feature_name="Test Feature",
            commit_hash="abc123",
            commit_message="feat: test",
            phase="p1",
            detected_code_refs=["src/test.py"],
            impact_type="medium",
        )
        with tempfile.TemporaryDirectory() as tmp:
            SDDGenerator._auto_dir = Path(tmp)
            SDDGenerator._sdd_dir = Path(tmp)
            result = SDDGenerator.generate_sdd(template)
            content = result.read_text(encoding="utf-8")
            assert "---" in content
            assert "id: test-feature" in content
            assert "type: generated" in content
            assert "requires_review: true" in content

    def test_generate_feature_node(self):
        with tempfile.TemporaryDirectory() as tmp:
            SDDGenerator._sdd_dir = Path(tmp)
            path = SDDGenerator.generate_feature_node(
                feature_id="chat-streaming",
                feature_name="Chat Streaming",
                feature_type="feature",
                phase="p3",
                tags=["chat", "streaming"],
                links=["event-bus"],
                description="Handles SSE streaming",
                responsibilities=["Token streaming", "Tool call parsing"],
                emits=["tool:start", "tool:complete"],
                used_by=["Chat UI", "Chat Store"],
            )
            assert path.exists()
            content = path.read_text(encoding="utf-8")
            assert "chat-streaming" in content
            assert "Chat Streaming" in content
            assert "Token streaming" in content