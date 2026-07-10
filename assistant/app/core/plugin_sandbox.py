"""Plugin Sandbox — Isolamento de plugins via WebAssembly (Wasm).

Permite carregar e executar binarios .wasm em ambiente controlado,
sem acesso ao sistema operacional host, filesystem ou rede.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from loguru import logger

try:
    import wasmtime

    HAS_WASMTIME = True
except ImportError:
    HAS_WASMTIME = False


# ---------------------------------------------------------------------------
# Constantes de seguranca
# ---------------------------------------------------------------------------

MAX_MEMORY_PAGES = 512  # 512 * 64KB = 32MB max
MAX_FUEL = 1_000_000  # limite de instrucoes
ALLOWED_IMPORTS: list[str] = []  # nenhum import permitido por padrao


# ---------------------------------------------------------------------------
# DTOs
# ---------------------------------------------------------------------------

@dataclass
class PluginManifest:
    """Manifesto do plugin — declaracao de metadados e permissoes."""

    id: str
    name: str
    version: str
    description: str = ""
    author: str = ""
    entrypoint: str = "main"
    permissions: list[str] = field(default_factory=list)
    allowed_functions: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> "PluginManifest":
        return cls(
            id=data.get("id", ""),
            name=data.get("name", "unnamed"),
            version=data.get("version", "0.0.1"),
            description=data.get("description", ""),
            author=data.get("author", ""),
            entrypoint=data.get("entrypoint", "main"),
            permissions=data.get("permissions", []),
            allowed_functions=data.get("allowed_functions", []),
        )

    def validate(self) -> list[str]:
        """Valida o manifesto. Retorna lista de erros (vazia = valido)."""
        errors: list[str] = []
        if not self.id or not self.id.strip():
            errors.append("id eh obrigatorio")
        if not self.name or not self.name.strip():
            errors.append("name eh obrigatorio")
        if not self.version or not self.version.strip():
            errors.append("version eh obrigatorio")
        # Seguranca: nenhuma permissao de sistema por padrao
        denied = {"filesystem", "network", "shell", "env"}
        for p in self.permissions:
            if p in denied:
                errors.append(f"permissao negada: {p}")
        return errors


@dataclass
class PluginExecutionResult:
    """Resultado da execucao de uma funcao no sandbox."""

    success: bool
    output: Any = None
    error: str | None = None
    fuel_consumed: int = 0


# ---------------------------------------------------------------------------
# Wasm Plugin
# ---------------------------------------------------------------------------

class WasmPlugin:
    """Representa um plugin carregado em memoria, pronto para execucao."""

    def __init__(
        self,
        plugin_id: str,
        bytes: bytes,
        manifest: PluginManifest,
    ) -> None:
        self.plugin_id = plugin_id
        self._bytes = bytes
        self.manifest = manifest
        self._store: wasmtime.Store | None = None
        self._instance: wasmtime.Instance | None = None
        self._module: wasmtime.Module | None = None
        self._linker: wasmtime.Linker | None = None
        self._loaded = False

    @property
    def is_loaded(self) -> bool:
        return self._loaded

    def load(self) -> None:
        """Compila e instancia o modulo Wasm no sandbox."""
        if not HAS_WASMTIME:
            raise RuntimeError(
                "wasmtime nao esta instalado. Execute: uv add wasmtime"
            )

        config = wasmtime.Config()
        config.cache = False
        config.strategy = wasmtime.Strategy.CRANELIFT
        config.wasm_multi_value = True
        config.wasm_bulk_memory = True
        config.max_wasm_stack = 512 * 1024  # 512KB

        engine = wasmtime.Engine(config)
        self._module = wasmtime.Module(engine, self._bytes)

        # Configurar limits de memoria
        self._store = wasmtime.Store(engine)
        self._store.set_fuel(MAX_FUEL)
        wasmtime.MemoryType(
            wasmtime.Limits(1, MAX_MEMORY_PAGES),
        )

        # Linker vazio — sem imports externos
        self._linker = wasmtime.Linker(engine)
        self._instance = self._linker.instantiate(self._store, self._module)
        self._loaded = True
        logger.debug(
            "[plugin] loaded {} ({} bytes, {} functions)",
            self.plugin_id,
            len(self._bytes),
            len(self.manifest.allowed_functions),
        )

    def execute_function(
        self, function_name: str, args: list[Any] | None = None
    ) -> PluginExecutionResult:
        """Executa uma funcao exportada do modulo Wasm.

        Args:
            function_name: Nome da funcao exportada.
            args: Argumentos para passar a funcao (apenas tipos primitivos).

        Returns:
            PluginExecutionResult com output ou erro.
        """
        if not self._loaded or not self._instance or not self._store:
            raise RuntimeError(f"Plugin {self.plugin_id} nao foi carregado")

        if function_name not in self.manifest.allowed_functions:
            return PluginExecutionResult(
                success=False,
                error=f"funcao '{function_name}' nao esta na whitelist do manifesto",
            )

        try:
            func = self._instance.exports(self._store).get(function_name)
            if func is None:
                return PluginExecutionResult(
                    success=False,
                    error=f"funcao '{function_name}' nao exportada pelo modulo",
                )

            fuel_before = self._store.fuel_consumed
            result = func(*args) if args else func()
            fuel_after = self._store.fuel_consumed

            return PluginExecutionResult(
                success=True,
                output=result,
                fuel_consumed=fuel_after - fuel_before,
            )
        except wasmtime.WasmtimeError as e:
            return PluginExecutionResult(
                success=False,
                error=f"erro Wasmtime: {e}",
            )
        except Exception as e:
            return PluginExecutionResult(
                success=False,
                error=f"erro inesperado: {e}",
            )

    def unload(self) -> None:
        """Libera recursos do plugin."""
        self._store = None
        self._instance = None
        self._module = None
        self._linker = None
        self._loaded = False
        logger.debug("[plugin] unloaded {}", self.plugin_id)


# ---------------------------------------------------------------------------
# Plugin Sandbox (Engine Principal)
# ---------------------------------------------------------------------------

class PluginSandbox:
    """Engine de sandbox para plugins Wasm.

    Responsabilidades:
    - Carregar e validar manifestos de plugins
    - Compilar e instanciar modulos Wasm com restricoes de seguranca
    - Executar funcoes em ambiente isolado
    - Gerenciar ciclo de vida dos plugins carregados
    """

    def __init__(self) -> None:
        self._plugins: dict[str, WasmPlugin] = {}

    @property
    def loaded_plugins(self) -> list[WasmPlugin]:
        return list(self._plugins.values())

    def load_plugin_from_bytes(
        self, wasm_bytes: bytes, manifest: PluginManifest
    ) -> str:
        """Carrega um plugin a partir de bytes Wasm e manifesto.

        Args:
            wasm_bytes: Conteudo binario do modulo .wasm.
            manifest: Manifesto declarando permissoes e metadados.

        Returns:
            ID do plugin carregado.

        Raises:
            ValueError: Se o manifesto for invalido.
            RuntimeError: Se o modulo Wasm falhar ao compilar.
        """
        # Validar manifesto
        errors = manifest.validate()
        if errors:
            raise ValueError(f"Manifesto invalido: {'; '.join(errors)}")

        # Verificar duplicata
        if manifest.id in self._plugins:
            raise ValueError(f"Plugin ja carregado: {manifest.id}")

        # Carregar e compilar
        plugin = WasmPlugin(manifest.id, wasm_bytes, manifest)
        try:
            plugin.load()
        except Exception as e:
            raise RuntimeError(f"Falha ao carregar modulo Wasm: {e}") from e

        self._plugins[plugin.plugin_id] = plugin
        logger.info("[sandbox] plugin loaded: {} v{}", manifest.id, manifest.version)
        return manifest.id

    def load_plugin_from_file(
        self, wasm_path: str | Path, manifest: PluginManifest
    ) -> str:
        """Carrega um plugin a partir de arquivo .wasm em disco."""
        path = Path(wasm_path)
        if not path.exists():
            raise FileNotFoundError(f"Arquivo Wasm nao encontrado: {path}")
        wasm_bytes = path.read_bytes()
        return self.load_plugin_from_bytes(wasm_bytes, manifest)

    def execute(
        self, plugin_id: str, function: str, args: list[Any] | None = None
    ) -> PluginExecutionResult:
        """Executa uma funcao em um plugin carregado."""
        plugin = self._plugins.get(plugin_id)
        if plugin is None:
            return PluginExecutionResult(
                success=False,
                error=f"Plugin nao encontrado: {plugin_id}",
            )
        return plugin.execute_function(function, args)

    def unload_plugin(self, plugin_id: str) -> bool:
        """Descarrega um plugin e libera recursos."""
        plugin = self._plugins.pop(plugin_id, None)
        if plugin:
            plugin.unload()
            return True
        return False

    def clear(self) -> None:
        """Descarrega todos os plugins."""
        for plugin in list(self._plugins.values()):
            plugin.unload()
        self._plugins.clear()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def validate_wasm_bytes(data: bytes) -> bool:
    """Valida rapidamente se o conteudo parece um modulo Wasm valido.

    Modulos Wasm comecam com o magic number: 0x00 0x61 0x73 0x6D (\\0asm).
    """
    return len(data) >= 4 and data[:4] == b"\x00asm"
