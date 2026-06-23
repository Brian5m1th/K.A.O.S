#!/usr/bin/env python3
"""
Sincroniza features-index.json com o repositório remoto do GitHub.

Garante fluxo seguro:
1. Baixa a versão remota
2. Compara os hashes/metadados
3. Valida contra o schema básico
4. Realiza o merge inteligente
5. Registra metadados no arquivo
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# Add app to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from app.audit.runtime_resolver import RuntimePathResolver

try:
    import httpx
except ImportError:
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "httpx"], capture_output=True)
    import httpx

OWNER = "Brian5m1th"
REPO = "K.A.O.S"
PATH_IN_REPO = "docs/runtime/registry/features-index.json"


def fetch_remote_registry() -> tuple[dict | None, str]:
    """Busca o registry remoto e retorna o JSON e o commit SHA correspondente."""
    headers = {"User-Agent": "KAOS-Registry-Sync"}
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    # 1. Obter o último commit SHA que modificou o arquivo
    commit_sha = "unknown"
    api_url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits"
    params = {"path": PATH_IN_REPO, "per_page": 1}
    try:
        r = httpx.get(api_url, params=params, headers=headers, timeout=10)
        if r.status_code == 200 and r.json():
            commit_sha = r.json()[0]["sha"]
    except Exception as e:
        print(f"[sync] Aviso: não foi possível obter commit SHA do GitHub API: {e}")

    # 2. Obter o conteúdo do arquivo
    raw_urls = [
        f"https://raw.githubusercontent.com/{OWNER}/{REPO}/dev/{PATH_IN_REPO}",
        f"https://raw.githubusercontent.com/{OWNER}/{REPO}/main/{PATH_IN_REPO}",
    ]
    for url in raw_urls:
        try:
            r = httpx.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                print(f"[sync] Sucesso ao baixar de: {url}")
                return r.json(), commit_sha
        except Exception:
            continue

    print("[sync] ERRO: Não foi possível obter o arquivo remoto do GitHub.")
    return None, commit_sha


def validate_schema(data: dict) -> bool:
    """Valida o schema do registry json."""
    if not isinstance(data, dict):
        return False
    if "features" not in data or not isinstance(data["features"], list):
        return False
    for feat in data["features"]:
        if not isinstance(feat, dict) or "id" not in feat or "name" not in feat:
            return False
    return True


def merge_registries(local: dict, remote: dict) -> dict:
    """Realiza o merge inteligente entre local e remote."""
    local_feats = {f["id"]: f for f in local.get("features", [])}
    remote_feats = {f["id"]: f for f in remote.get("features", [])}

    merged_feats = {}
    
    # Processar todas as chaves
    all_keys = set(local_feats.keys()) | set(remote_feats.keys())
    
    for fid in all_keys:
        loc = local_feats.get(fid)
        rem = remote_feats.get(fid)
        
        if loc and not rem:
            # Apenas no local
            merged_feats[fid] = loc
        elif rem and not loc:
            # Apenas no remoto (adicionar)
            merged_feats[fid] = rem
        else:
            # Merge das duas
            # Union de listas docs e codeRefs
            docs_union = list(set(loc.get("docs", []) or []) | set(rem.get("docs", []) or []))
            code_union = list(set(loc.get("codeRefs", []) or []) | set(rem.get("codeRefs", []) or []))
            
            # Preferir updatedAt mais recente se existirem e forem válidos
            local_updated = loc.get("updatedAt", loc.get("updated_at", ""))
            remote_updated = rem.get("updatedAt", rem.get("updated_at", ""))
            
            if remote_updated > local_updated:
                merged = rem.copy()
            else:
                merged = loc.copy()
                
            merged["docs"] = sorted(docs_union)
            merged["codeRefs"] = sorted(code_union)
            merged_feats[fid] = merged

    # Retorna o dict mesclado ordenado por ID
    return {
        "version": local.get("version", remote.get("version", "1.0")),
        "features": [merged_feats[k] for k in sorted(merged_feats.keys())]
    }


def main():
    local_path = RuntimePathResolver.features_index_path()
    print(f"[sync] Caminho local do registry: {local_path}")
    
    # 1. Carregar local
    if local_path.exists():
        try:
            with open(local_path, "r", encoding="utf-8") as f:
                local_data = json.load(f)
        except Exception as e:
            print(f"[sync] Erro ao ler local: {e}")
            local_data = {"version": "1.0", "features": []}
    else:
        local_data = {"version": "1.0", "features": []}

    # 2. Buscar remoto
    remote_data, commit_sha = fetch_remote_registry()
    if not remote_data:
        print("[sync] Abortando sincronização por falha ao obter dados remotos.")
        sys.exit(1)

    # 3. Validar remoto
    if not validate_schema(remote_data):
        print("[sync] ERRO: O arquivo remoto não passou na validação do schema.")
        sys.exit(1)

    # 4. Calcular hashes/diferença simples
    local_ids = {f["id"] for f in local_data.get("features", [])}
    remote_ids = {f["id"] for f in remote_data.get("features", [])}
    
    added = remote_ids - local_ids
    removed = local_ids - remote_ids
    common = local_ids & remote_ids
    
    print("[sync] Analisando Registry Diff:")
    print(f"  - No local: {len(local_ids)} features")
    print(f"  - No remoto: {len(remote_ids)} features")
    print(f"  - Apenas no remoto (serão adicionadas): {list(added) or 'Nenhuma'}")
    print(f"  - Apenas no local (serão mantidas): {list(removed) or 'Nenhuma'}")
    print(f"  - Em comum: {len(common)}")

    # 5. Merge
    merged_data = merge_registries(local_data, remote_data)

    # 6. Atualizar metadados
    merged_data["sync_source"] = f"github"
    merged_data["sync_commit"] = commit_sha
    merged_data["sync_branch"] = "dev"
    merged_data["sync_timestamp"] = datetime.now(timezone.utc).isoformat()
    merged_data["schema_version"] = merged_data.get("version", "1.0")

    # 7. Salvar
    local_path.parent.mkdir(parents=True, exist_ok=True)
    with open(local_path, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, indent=2, ensure_ascii=False)

    print(f"[sync] Sincronização concluída com sucesso! Atualizado em {local_path}")


if __name__ == "__main__":
    main()
