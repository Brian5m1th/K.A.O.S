"""API Router — Gerenciamento de Plugins Wasm.

Permite instalar, listar, executar e remover plugins
em ambiente sandbox via WebAssembly.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from loguru import logger

from app.core.plugin_sandbox import (
    PluginManifest,
    PluginSandbox,
    validate_wasm_bytes,
)
from app.core.plugin_registry import PluginRegistry

router = APIRouter(prefix="/api/plugins", tags=["Plugins"])

# Singletons
_sandbox: PluginSandbox | None = None
_registry: PluginRegistry | None = None


def _get_sandbox() -> PluginSandbox:
    global _sandbox
    if _sandbox is None:
        _sandbox = PluginSandbox()
    return _sandbox


def _get_registry() -> PluginRegistry:
    global _registry
    if _registry is None:
        _registry = PluginRegistry()
    return _registry


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------


@router.get("/")
async def list_plugins() -> dict[str, Any]:
    """Lista todos os plugins instalados (do registro + sandbox)."""
    registry = _get_registry()
    sandbox = _get_sandbox()
    records = registry.list_plugins()
    loaded_ids = {p.plugin_id for p in sandbox.loaded_plugins}

    plugins_list = []
    for rec in records:
        d = rec.to_dict()
        d["loaded"] = rec.plugin_id in loaded_ids
        plugins_list.append(d)

    return {"total": len(plugins_list), "plugins": plugins_list}


@router.post("/install")
async def install_plugin(
    wasm: UploadFile = File(...),
    manifest: str = Form(...),
) -> dict[str, Any]:
    """Instala um plugin a partir de arquivo .wasm + manifesto JSON.

    O manifesto deve ser um JSON string com os campos:
    - id (obrigatorio)
    - name (obrigatorio)
    - version (obrigatorio)
    - description, author, entrypoint, permissions, allowed_functions
    """
    # Ler manifesto
    try:
        manifest_data = json.loads(manifest)
        plugin_manifest = PluginManifest.from_dict(manifest_data)
    except (json.JSONDecodeError, KeyError) as e:
        raise HTTPException(status_code=400, detail=f"Manifesto invalido: {e}")

    # Validar manifesto
    errors = plugin_manifest.validate()
    if errors:
        raise HTTPException(
            status_code=400, detail=f"Manifesto invalido: {'; '.join(errors)}"
        )

    # Ler bytes do Wasm
    wasm_bytes = await wasm.read()
    if not validate_wasm_bytes(wasm_bytes):
        raise HTTPException(
            status_code=400, detail="Arquivo nao parece ser um modulo Wasm valido"
        )

    # Salvar em disco para persistencia
    plugins_dir = Path("data/plugins")
    plugins_dir.mkdir(parents=True, exist_ok=True)
    wasm_path = plugins_dir / f"{plugin_manifest.id}.wasm"
    wasm_path.write_bytes(wasm_bytes)

    # Carregar no sandbox
    sandbox = _get_sandbox()
    try:
        sandbox.load_plugin_from_bytes(wasm_bytes, plugin_manifest)
    except (ValueError, RuntimeError) as e:
        raise HTTPException(status_code=400, detail=str(e))

    # Registrar no banco
    registry = _get_registry()
    record = registry.install(
        plugin_id=plugin_manifest.id,
        name=plugin_manifest.name,
        version=plugin_manifest.version,
        description=plugin_manifest.description,
        author=plugin_manifest.author,
        wasm_path=str(wasm_path),
        manifest=manifest_data,
    )

    logger.info(
        "[plugins] installed: {} v{}", plugin_manifest.id, plugin_manifest.version
    )
    return {"status": "installed", "plugin": record.to_dict()}


@router.post("/{plugin_id}/execute")
async def execute_plugin(
    plugin_id: str,
    function: str = "main",
    args: list[Any] | None = None,
) -> dict[str, Any]:
    """Executa uma funcao em um plugin carregado."""
    sandbox = _get_sandbox()
    result = sandbox.execute(plugin_id, function, args or [])

    if not result.success:
        raise HTTPException(status_code=400, detail=result.error or "execucao falhou")

    return {
        "status": "ok",
        "output": result.output,
        "fuel_consumed": result.fuel_consumed,
    }


@router.delete("/{plugin_id}")
async def uninstall_plugin(plugin_id: str) -> dict[str, str]:
    """Remove um plugin do sandbox e do registro."""
    sandbox = _get_sandbox()
    registry = _get_registry()

    sandbox.unload_plugin(plugin_id)
    removed = registry.uninstall(plugin_id)

    # Remover arquivo .wasm do disco
    wasm_path = Path(f"data/plugins/{plugin_id}.wasm")
    if wasm_path.exists():
        wasm_path.unlink()

    if not removed:
        raise HTTPException(
            status_code=404, detail=f"Plugin nao encontrado: {plugin_id}"
        )

    return {"status": "removed", "plugin_id": plugin_id}


@router.get("/{plugin_id}")
async def get_plugin(plugin_id: str) -> dict[str, Any]:
    """Obtem detalhes de um plugin."""
    registry = _get_registry()
    record = registry.get_plugin(plugin_id)
    if not record:
        raise HTTPException(
            status_code=404, detail=f"Plugin nao encontrado: {plugin_id}"
        )

    sandbox = _get_sandbox()
    d = record.to_dict()
    d["loaded"] = any(p.plugin_id == plugin_id for p in sandbox.loaded_plugins)
    return d
