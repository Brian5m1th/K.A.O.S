from unittest.mock import patch, MagicMock

from app.ai.vault_analyzer.knowledge_graph import KnowledgeGraphBuilder, KnowledgeGraph


class TestKnowledgeGraph:
    def test_infer_type(self):
        assert (
            KnowledgeGraphBuilder._infer_type(
                "desktop/src/shared/lib/stores/useThemeStore.ts"
            )
            == "store"
        )
        assert (
            KnowledgeGraphBuilder._infer_type("desktop/src/pages/welcome/index.tsx")
            == "page"
        )
        assert (
            KnowledgeGraphBuilder._infer_type("assistant/app/tools/calculator.py")
            == "tool"
        )
        assert (
            KnowledgeGraphBuilder._infer_type(
                "assistant/app/observability/event_bus.py"
            )
            == "event"
        )
        assert KnowledgeGraphBuilder._infer_type("unknown_ref") == "unknown"

    @patch(
        "app.ai.vault_analyzer.knowledge_graph.RuntimePathResolver.knowledge_graph_path"
    )
    def test_load_and_persist(self, mock_path, tmp_path):
        temp_file = tmp_path / "knowledge-graph.json"
        mock_path.return_value = temp_file

        kg = KnowledgeGraph(
            nodes=[
                {"id": "node-1", "title": "Node 1", "type": "sdd", "source": "vault"}
            ],
            edges=[{"source": "node-1", "target": "node-2", "relation": "depends_on"}],
        )

        KnowledgeGraphBuilder._persist(kg)
        assert temp_file.exists()

        loaded_kg = KnowledgeGraphBuilder.load()
        assert loaded_kg is not None
        assert len(loaded_kg.nodes) == 1
        assert loaded_kg.nodes[0]["id"] == "node-1"
        assert len(loaded_kg.edges) == 1

    @patch(
        "app.ai.vault_analyzer.knowledge_graph.RuntimePathResolver.knowledge_graph_path"
    )
    @patch("app.ai.vault_analyzer.knowledge_graph.RuntimePathResolver.project_root")
    @patch("app.ai.vault_analyzer.knowledge_graph.VaultReader.scan_single")
    def test_update_file_vault(
        self, mock_scan_single, mock_project_root, mock_path, tmp_path
    ):
        temp_file = tmp_path / "knowledge-graph.json"
        mock_path.return_value = temp_file
        mock_project_root.return_value = tmp_path

        # Configura grafo inicial
        kg = KnowledgeGraph(
            nodes=[
                {
                    "id": "old-node",
                    "title": "Old Node",
                    "type": "sdd",
                    "source": "vault",
                    "path": "docs/sdd/old.md",
                }
            ],
            edges=[],
        )
        KnowledgeGraphBuilder._persist(kg)

        # Mock de leitura do novo arquivo
        mock_node = MagicMock()
        mock_node.id = "new-node"
        mock_node.title = "New Node"
        mock_node.type = "sdd"
        mock_node.owner = "shared"
        mock_node.status = "valid"
        mock_node.tags = []
        mock_node.links = ["dependency-1"]
        mock_node.wikilinks = ["wiki-ref"]
        mock_node.path = "docs/sdd/new.md"
        mock_scan_single.return_value = mock_node

        file_to_update = tmp_path / "docs" / "sdd" / "new.md"
        file_to_update.parent.mkdir(parents=True, exist_ok=True)
        file_to_update.touch()

        # Executa o update incremental
        KnowledgeGraphBuilder.update_file(file_to_update)

        # Asserts
        updated_kg = KnowledgeGraphBuilder.load()
        assert updated_kg is not None

        node_ids = [n["id"] for n in updated_kg.nodes]
        assert "old-node" in node_ids
        assert "new-node" in node_ids

        assert len(updated_kg.edges) == 2
        edges_src = [e["source"] for e in updated_kg.edges]
        assert "new-node" in edges_src

    @patch(
        "app.ai.vault_analyzer.knowledge_graph.RuntimePathResolver.knowledge_graph_path"
    )
    @patch("app.ai.vault_analyzer.knowledge_graph.RuntimePathResolver.project_root")
    def test_delete_file(self, mock_project_root, mock_path, tmp_path):
        temp_file = tmp_path / "knowledge-graph.json"
        mock_path.return_value = temp_file
        mock_project_root.return_value = tmp_path

        # Configura grafo inicial
        kg = KnowledgeGraph(
            nodes=[
                {
                    "id": "node-to-delete",
                    "title": "Delete Me",
                    "type": "sdd",
                    "source": "vault",
                    "path": "docs/sdd/delete.md",
                }
            ],
            edges=[
                {
                    "source": "node-to-delete",
                    "target": "other-node",
                    "relation": "depends_on",
                }
            ],
        )
        KnowledgeGraphBuilder._persist(kg)

        file_to_delete = tmp_path / "docs" / "sdd" / "delete.md"

        # Remove o arquivo do grafo
        KnowledgeGraphBuilder.delete_file(file_to_delete)

        # Asserts
        updated_kg = KnowledgeGraphBuilder.load()
        assert updated_kg is not None
        assert len(updated_kg.nodes) == 0
        assert len(updated_kg.edges) == 0
