"""
Tests for the configuration management module.

Priority #2 — tests cover:
    - Path resolution (get_mcp_home, get_registry_path, etc.)
    - YAML I/O (load_yaml, save_yaml)
    - Missing / invalid file handling
    - PlatformConfig initialization and server resolution
"""

import os
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest
import yaml

from mcp_cli.core.config import (
    get_mcp_home,
    get_registry_path,
    get_config_path,
    get_server_config_path,
    get_active_profile_path,
    get_profile_path,
    get_secrets_path,
    ensure_dirs,
    load_yaml,
    save_yaml,
    PlatformConfig,
)


# ── Path resolution ──────────────────────────────────────────────────


class TestGetMcpHome:
    """get_mcp_home() resolves the platform root directory."""

    def test_uses_mcp_home_env_var(self, temp_dir):
        """When MCP_HOME is set, it takes priority."""
        home = get_mcp_home()
        assert home == temp_dir

    def test_expands_user_in_env_var(self):
        """MCP_HOME with ~ is expanded."""
        old = os.environ.pop("MCP_HOME", None)
        try:
            os.environ["MCP_HOME"] = "~/mcp-test-home"
            home = get_mcp_home()
            assert home == Path.home() / "mcp-test-home"
        finally:
            if old is not None:
                os.environ["MCP_HOME"] = old
            else:
                os.environ.pop("MCP_HOME", None)

    def test_unset_returns_platform_default(self):
        """Without MCP_HOME, a platform-specific default is returned."""
        old = os.environ.pop("MCP_HOME", None)
        try:
            home = get_mcp_home()
            if sys.platform == "win32":
                expected = (
                    Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
                    / "mcp"
                )
            elif sys.platform == "darwin":
                expected = Path.home() / "Library" / "Application Support" / "mcp"
            else:
                expected = Path.home() / ".config" / "mcp"
            assert home == expected
        finally:
            if old is not None:
                os.environ["MCP_HOME"] = old


class TestPathHelpers:
    """Convenience path helpers derive paths from get_mcp_home()."""

    def test_get_registry_path(self, temp_dir):
        assert get_registry_path() == temp_dir / "registry.yaml"

    def test_get_config_path(self, temp_dir):
        assert get_config_path() == temp_dir / "config.yaml"

    def test_get_active_profile_path(self, temp_dir):
        assert get_active_profile_path() == temp_dir / "active_profile.yaml"

    def test_get_server_config_path(self, temp_dir):
        assert get_server_config_path("my-server") == temp_dir / "servers" / "my-server.yaml"

    def test_get_profile_path(self, temp_dir):
        assert get_profile_path("dev") == temp_dir / "profiles" / "dev.yaml"

    def test_get_secrets_path(self, temp_dir):
        assert get_secrets_path("github") == temp_dir / "secrets" / "github.yaml"


# ── Directory initialisation ─────────────────────────────────────────


class TestEnsureDirs:
    """ensure_dirs() creates all required platform directories."""

    def test_creates_expected_directories(self, temp_dir):
        """All required subdirectories exist after ensure_dirs()."""
        ensure_dirs()
        subdirs = [
            temp_dir,
            temp_dir / "profiles",
            temp_dir / "servers",
            temp_dir / "secrets",
            temp_dir / "cache" / "tools",
            temp_dir / "cache" / "schemas",
            temp_dir / "cache" / "health",
            temp_dir / "logs" / "servers",
            temp_dir / "downloads",
            temp_dir / "templates",
            temp_dir / "backups",
        ]
        for d in subdirs:
            assert d.is_dir(), f"Directory missing: {d}"

    def test_idempotent(self, temp_dir):
        """Calling ensure_dirs() twice does not raise."""
        ensure_dirs()
        ensure_dirs()  # Should be a no-op
        assert temp_dir.is_dir()


# ── YAML I/O ─────────────────────────────────────────────────────────


class TestLoadYaml:
    """load_yaml() reads YAML files or returns empty dict."""

    def test_missing_file_returns_empty_dict(self, temp_dir):
        """A non-existent file returns {} without error."""
        missing = temp_dir / "does_not_exist.yaml"
        data = load_yaml(missing)
        assert data == {}

    def test_valid_file_returns_parsed_dict(self, temp_dir):
        """A valid YAML file is parsed into a Python dict."""
        path = temp_dir / "config.yaml"
        path.write_text("server: test\nenabled: true\n")
        data = load_yaml(path)
        assert data == {"server": "test", "enabled": True}

    def test_empty_file_returns_empty_dict(self, temp_dir):
        """An empty file returns {}."""
        path = temp_dir / "empty.yaml"
        path.write_text("")
        data = load_yaml(path)
        assert data == {}

    def test_invalid_yaml_returns_empty_dict(self, temp_dir):
        """Malformed YAML is handled gracefully and returns {}."""
        path = temp_dir / "bad.yaml"
        path.write_text(": : invalid yaml !!")
        data = load_yaml(path)
        # load_yaml catches bare Exception → returns {}
        assert data == {}

    def test_yaml_with_list(self, temp_dir):
        """YAML sequences are loaded as lists."""
        path = temp_dir / "list.yaml"
        path.write_text("- one\n- two\n- three\n")
        data = load_yaml(path)
        assert data == ["one", "two", "three"]


class TestSaveYaml:
    """save_yaml() writes dicts as well-formed YAML files."""

    def test_save_simple_dict(self, temp_dir):
        """A dict is written as YAML and can be read back."""
        path = temp_dir / "out.yaml"
        save_yaml(path, {"key": "value", "count": 42})
        assert path.exists()
        with open(path, "r", encoding="utf-8") as f:
            raw = f.read()
        assert "key:" in raw
        assert "value" in raw

    def test_save_then_load_roundtrip(self, temp_dir):
        """A save followed by load returns an equivalent dict."""
        path = temp_dir / "roundtrip.yaml"
        original = {"name": "test", "enabled": True, "nested": {"a": 1}}
        save_yaml(path, original)
        loaded = load_yaml(path)
        assert loaded == original

    def test_save_creates_parent_dirs(self, temp_dir):
        """Parent directories are created automatically."""
        path = temp_dir / "a" / "b" / "deep.yaml"
        save_yaml(path, {"hello": "world"})
        assert path.exists()

    def test_save_overwrites_existing(self, temp_dir):
        """save_yaml replaces an existing file."""
        path = temp_dir / "overwrite.yaml"
        save_yaml(path, {"v1": "data"})
        save_yaml(path, {"v2": "new"})
        loaded = load_yaml(path)
        assert loaded == {"v2": "new"}

    def test_save_empty_dict(self, temp_dir):
        """An empty dict produces a valid (empty) YAML file."""
        path = temp_dir / "empty.yaml"
        save_yaml(path, {})
        assert path.exists()
        loaded = load_yaml(path)
        assert loaded == {} or loaded is None  # yaml.dump({}) → ''


# ── PlatformConfig ───────────────────────────────────────────────────


class TestPlatformConfig:
    """PlatformConfig loads registry, config, and profile data from disk."""

    def test_init_loads_empty_when_no_files(self, temp_dir):
        """Without any config files, PlatformConfig has empty data."""
        ensure_dirs()
        cfg = PlatformConfig()
        assert cfg.registry == {}
        assert cfg.config == {}
        assert cfg.active_profile == {}

    def test_init_loads_registry(self, temp_dir):
        """A registry.yaml file is loaded on construction."""
        ensure_dirs()
        reg_path = get_registry_path()
        save_yaml(reg_path, {"servers": [{"id": "s1"}]})

        cfg = PlatformConfig()
        assert cfg.registry == {"servers": [{"id": "s1"}]}

    def test_get_server_found(self, temp_dir):
        """get_server returns the matching server entry by ID."""
        ensure_dirs()
        save_yaml(get_registry_path(), {
            "servers": [
                {"id": "alpha", "name": "Alpha"},
                {"id": "beta", "name": "Beta"},
            ],
        })
        cfg = PlatformConfig()
        server = cfg.get_server("alpha")
        assert server is not None
        assert server["name"] == "Alpha"

    def test_get_server_not_found(self, temp_dir):
        """get_server returns None when no entry matches."""
        ensure_dirs()
        save_yaml(get_registry_path(), {"servers": [{"id": "alpha"}]})
        cfg = PlatformConfig()
        assert cfg.get_server("nonexistent") is None

    def test_get_enabled_servers_with_active_profile(self, temp_dir):
        """get_enabled_servers filters by the active profile's enabled list."""
        ensure_dirs()
        save_yaml(get_registry_path(), {
            "servers": [
                {"id": "s1", "name": "Server 1"},
                {"id": "s2", "name": "Server 2"},
                {"id": "s3", "name": "Server 3"},
            ],
        })
        save_yaml(get_active_profile_path(), {"active_profiles": ["full-stack"]})
        save_yaml(get_profile_path("full-stack"), {
            "enabled_servers": ["s1", "s3"],
        })

        cfg = PlatformConfig()
        enabled = cfg.get_enabled_servers()
        assert len(enabled) == 2
        ids = [s["id"] for s in enabled]
        assert "s1" in ids
        assert "s3" in ids
        assert "s2" not in ids

    def test_get_enabled_servers_fallback_all(self, temp_dir):
        """When profile has no enabled_servers, all registry servers are returned."""
        ensure_dirs()
        save_yaml(get_registry_path(), {
            "servers": [
                {"id": "s1"},
                {"id": "s2"},
            ],
        })
        save_yaml(get_active_profile_path(), {"active_profiles": ["custom"]})
        save_yaml(get_profile_path("custom"), {"name": "Custom"})  # no enabled_servers

        cfg = PlatformConfig()
        enabled = cfg.get_enabled_servers()
        assert len(enabled) == 2  # fallback to all

    def test_get_installed_servers(self, temp_dir):
        """get_installed_servers lists .yaml files in the servers directory."""
        ensure_dirs()
        svc_dir = temp_dir / "servers"
        save_yaml(svc_dir / "github.yaml", {"id": "github"})
        save_yaml(svc_dir / "postgres.yaml", {"id": "postgres"})

        cfg = PlatformConfig()
        installed = cfg.get_installed_servers()
        assert sorted(installed) == ["github", "postgres"]

    def test_get_installed_servers_no_dir(self, temp_dir):
        """When servers dir doesn't exist, return empty list."""
        cfg = PlatformConfig()
        # ensure_dirs hasn't been called for this test → servers dir may not exist
        installed = cfg.get_installed_servers()
        assert installed == []
