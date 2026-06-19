from unittest.mock import MagicMock, patch

from app.obsidian.watcher.vault_watcher import _VaultEventHandler, VaultWatcher


class TestVaultEventHandler:
    @patch("app.obsidian.watcher.vault_watcher.settings")
    def test_is_markdown_positive(self, MockSettings) -> None:
        handler = _VaultEventHandler(MagicMock())
        assert handler._is_markdown("nota.md") is True

    @patch("app.obsidian.watcher.vault_watcher.settings")
    def test_is_markdown_negative_extension(self, MockSettings) -> None:
        handler = _VaultEventHandler(MagicMock())
        assert handler._is_markdown("nota.txt") is False

    @patch("app.obsidian.watcher.vault_watcher.settings")
    def test_is_markdown_hidden_file(self, MockSettings) -> None:
        handler = _VaultEventHandler(MagicMock())
        assert handler._is_markdown(".hidden.md") is False

    @patch("app.obsidian.watcher.vault_watcher.settings")
    def test_on_created_triggers_index(self, MockSettings) -> None:
        mock_indexer = MagicMock()
        handler = _VaultEventHandler(mock_indexer)
        event = MagicMock()
        event.is_directory = False
        event.src_path = "nota.md"

        handler.on_created(event)
        mock_indexer.index_file.assert_called_once_with("nota.md")

    @patch("app.obsidian.watcher.vault_watcher.settings")
    def test_on_created_skips_directory(self, MockSettings) -> None:
        mock_indexer = MagicMock()
        handler = _VaultEventHandler(mock_indexer)
        event = MagicMock()
        event.is_directory = True

        handler.on_created(event)
        mock_indexer.index_file.assert_not_called()

    @patch("app.obsidian.watcher.vault_watcher.settings")
    def test_on_modified_triggers_index(self, MockSettings) -> None:
        mock_indexer = MagicMock()
        handler = _VaultEventHandler(mock_indexer)
        event = MagicMock()
        event.is_directory = False
        event.src_path = "nota.md"

        handler.on_modified(event)
        mock_indexer.index_file.assert_called_once_with("nota.md")

    @patch("app.obsidian.watcher.vault_watcher.settings")
    def test_on_deleted_triggers_remove(self, MockSettings) -> None:
        MockSettings.OBSIDIAN_VAULT_PATH = "/vault"
        mock_indexer = MagicMock()
        handler = _VaultEventHandler(mock_indexer)
        event = MagicMock()
        event.is_directory = False
        event.src_path = "/vault/pasta/nota.md"

        handler.on_deleted(event)
        mock_indexer.remove_file.assert_called_once()
        args = mock_indexer.remove_file.call_args[0][0]
        assert args.replace("\\", "/") == "pasta/nota.md"


class TestVaultWatcher:
    @patch("app.obsidian.watcher.vault_watcher.Observer")
    @patch("app.obsidian.watcher.vault_watcher.VaultIndexer")
    def test_start_schedules_observer(self, MockIndexer, MockObserver) -> None:
        mock_observer = MagicMock()
        MockObserver.return_value = mock_observer

        watcher = VaultWatcher()
        watcher.start()

        mock_observer.schedule.assert_called_once()
        mock_observer.start.assert_called_once()

    @patch("app.obsidian.watcher.vault_watcher.Observer")
    @patch("app.obsidian.watcher.vault_watcher.VaultIndexer")
    def test_stop_observer(self, MockIndexer, MockObserver) -> None:
        mock_observer = MagicMock()
        MockObserver.return_value = mock_observer

        watcher = VaultWatcher()
        watcher.stop()

        mock_observer.stop.assert_called_once()
        mock_observer.join.assert_called_once()
