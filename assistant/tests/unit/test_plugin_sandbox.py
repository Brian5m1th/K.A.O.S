"""Testes unitarios do Plugin Sandbox (WebAssembly).

Testa validacao de manifesto, carregamento e execucao de modulos Wasm,
e recursos de seguranca do sandbox.
"""
import pytest
from unittest.mock import patch, MagicMock

from app.core.plugin_sandbox import (
    PluginManifest,
    PluginSandbox,
    WasmPlugin,
    validate_wasm_bytes,
    PluginExecutionResult,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def valid_manifest_data() -> dict:
    return {
        "id": "hello-world",
        "name": "Hello World",
        "version": "1.0.0",
        "description": "A simple hello world plugin",
        "author": "K.A.O.S",
        "entrypoint": "main",
        "permissions": [],
        "allowed_functions": ["hello", "add"],
    }


@pytest.fixture
def valid_manifest(valid_manifest_data: dict) -> PluginManifest:
    return PluginManifest.from_dict(valid_manifest_data)


@pytest.fixture
def wasm_magic_bytes() -> bytes:
    """Retorna apenas o magic number do Wasm (\\0asm) para testes de validacao."""
    return b"\x00asm" + b"\x01\x00\x00\x00"


# ---------------------------------------------------------------------------
# Testes: PluginManifest
# ---------------------------------------------------------------------------


class TestPluginManifest:
    def test_create_from_dict_full(self, valid_manifest_data: dict) -> None:
        manifest = PluginManifest.from_dict(valid_manifest_data)
        assert manifest.id == "hello-world"
        assert manifest.name == "Hello World"
        assert manifest.version == "1.0.0"
        assert manifest.entrypoint == "main"

    def test_create_from_dict_minimal(self) -> None:
        manifest = PluginManifest.from_dict({"id": "x", "name": "x", "version": "1"})
        assert manifest.id == "x"
        assert manifest.permissions == []

    def test_validate_valid(self, valid_manifest: PluginManifest) -> None:
        errors = valid_manifest.validate()
        assert errors == []

    def test_validate_missing_id(self) -> None:
        m = PluginManifest.from_dict({"name": "x", "version": "1"})
        errors = m.validate()
        assert "id eh obrigatorio" in errors

    def test_validate_empty_name(self) -> None:
        m = PluginManifest(id="x", name="", version="1")
        errors = m.validate()
        assert "name eh obrigatorio" in errors

    def test_validate_empty_version(self) -> None:
        m = PluginManifest(id="x", name="x", version="")
        errors = m.validate()
        assert "version eh obrigatorio" in errors

    def test_validate_denied_permissions(self) -> None:
        m = PluginManifest.from_dict({
            "id": "x", "name": "x", "version": "1",
            "permissions": ["filesystem", "network"],
        })
        errors = m.validate()
        assert "permissao negada: filesystem" in errors
        assert "permissao negada: network" in errors

    def test_validate_allowed_permissions(self) -> None:
        """Permissoes nao proibidas devem passar."""
        m = PluginManifest.from_dict({
            "id": "x", "name": "x", "version": "1",
            "permissions": ["storage:local"],
        })
        errors = m.validate()
        assert errors == []

    def test_empty_id_rejected(self) -> None:
        m = PluginManifest.from_dict({"id": "", "name": "x", "version": "1"})
        errors = m.validate()
        assert "id eh obrigatorio" in errors


# ---------------------------------------------------------------------------
# Testes: validate_wasm_bytes
# ---------------------------------------------------------------------------


class TestValidateWasmBytes:
    def test_valid_magic_number(self) -> None:
        assert validate_wasm_bytes(b"\x00asm\x01\x00\x00\x00") is True

    def test_invalid_magic_number(self) -> None:
        assert validate_wasm_bytes(b"not wasm") is False

    def test_empty_bytes(self) -> None:
        assert validate_wasm_bytes(b"") is False

    def test_short_bytes(self) -> None:
        assert validate_wasm_bytes(b"\x00as") is False


# ---------------------------------------------------------------------------
# Testes: PluginSandbox (com mocks)
# ---------------------------------------------------------------------------


class TestPluginSandbox:
    def test_sandbox_init_empty(self) -> None:
        sandbox = PluginSandbox()
        assert sandbox.loaded_plugins == []

    def test_load_plugin_invalid_manifest(self) -> None:
        sandbox = PluginSandbox()
        with pytest.raises(ValueError, match="Manifesto invalido"):
            sandbox.load_plugin_from_bytes(
                b"\x00asm\x01\x00\x00\x00",
                PluginManifest.from_dict({"id": "", "name": "", "version": ""}),
            )

    @patch("app.core.plugin_sandbox.HAS_WASMTIME", False)
    def test_load_without_wasmtime_raises(self, valid_manifest: PluginManifest) -> None:
        """Sem wasmtime instalado, deve levantar erro."""
        sandbox = PluginSandbox()
        with pytest.raises(RuntimeError, match="wasmtime nao esta instalado"):
            sandbox.load_plugin_from_bytes(
                b"\x00asm\x01\x00\x00\x00",
                valid_manifest,
            )

    def test_execute_unloaded_plugin(self) -> None:
        sandbox = PluginSandbox()
        result = sandbox.execute("nonexistent", "main")
        assert result.success is False
        assert "nao encontrado" in (result.error or "")

    def test_execute_function_not_in_whitelist(self) -> None:
        """Funcao nao listada no allowed_functions deve ser rejeitada."""
        manifest = PluginManifest.from_dict({
            "id": "secure-plugin",
            "name": "Secure",
            "version": "1.0.0",
            "allowed_functions": ["safe_func"],
        })

        # Mock WasmPlugin para testar apenas a whitelist
        sandbox = PluginSandbox()
        mock_plugin = MagicMock(spec=WasmPlugin)
        mock_plugin.plugin_id = "secure-plugin"
        mock_plugin.manifest = manifest
        mock_plugin.is_loaded = True
        mock_plugin.execute_function.return_value = PluginExecutionResult(
            success=False,
            error="funcao 'unsafe' nao esta na whitelist do manifesto",
        )

        sandbox._plugins["secure-plugin"] = mock_plugin

        result = sandbox.execute("secure-plugin", "unsafe")
        assert result.success is False
        mock_plugin.execute_function.assert_called_with("unsafe", None)

    def test_unload_plugin(self) -> None:
        sandbox = PluginSandbox()
        mock_plugin = MagicMock(spec=WasmPlugin)
        mock_plugin.plugin_id = "test-plugin"
        mock_plugin.is_loaded = True
        sandbox._plugins["test-plugin"] = mock_plugin

        assert sandbox.unload_plugin("test-plugin") is True
        assert "test-plugin" not in sandbox._plugins
        mock_plugin.unload.assert_called_once()

    def test_unload_nonexistent(self) -> None:
        sandbox = PluginSandbox()
        assert sandbox.unload_plugin("ghost") is False

    def test_clear_all_plugins(self) -> None:
        sandbox = PluginSandbox()
        for i in range(3):
            mock_plugin = MagicMock(spec=WasmPlugin)
            mock_plugin.plugin_id = f"p{i}"
            mock_plugin.is_loaded = True
            sandbox._plugins[f"p{i}"] = mock_plugin

        sandbox.clear()
        assert sandbox.loaded_plugins == []

    def test_duplicate_plugin_rejected(self, valid_manifest: PluginManifest) -> None:
        sandbox = PluginSandbox()
        mock_plugin = MagicMock(spec=WasmPlugin)
        mock_plugin.plugin_id = "hello-world"
        mock_plugin.is_loaded = True
        sandbox._plugins["hello-world"] = mock_plugin

        with pytest.raises(ValueError, match="Plugin ja carregado"):
            sandbox.load_plugin_from_bytes(b"\x00asm\x01\x00\x00\x00", valid_manifest)
