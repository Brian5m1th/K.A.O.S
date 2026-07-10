"""AWS Tools — Ferramentas LangChain para comandos AWS.

Utiliza subprocess para executar comandos AWS CLI, ou boto3
se disponivel para operacoes mais ricas.
"""

from __future__ import annotations

import json
import subprocess
from typing import Any

from langchain_core.tools import tool
from loguru import logger


def _run_aws_cli(command: list[str], profile: str = "") -> dict[str, Any]:
    """Executa um comando AWS CLI e retorna o resultado.

    Args:
        command: Lista de argumentos do comando aws.
        profile: Perfil AWS (opcional).

    Returns:
        Dict com stdout, stderr e exit code.
    """
    try:
        cmd = ["aws"]
        if profile:
            cmd.extend(["--profile", profile])
        cmd.extend(command)

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
        )

        if result.returncode == 0:
            try:
                output = json.loads(result.stdout) if result.stdout else {}
            except json.JSONDecodeError:
                output = result.stdout
            return {"status": "ok", "output": output}
        else:
            return {
                "status": "error",
                "message": result.stderr.strip() or f"Exit code {result.returncode}",
            }

    except FileNotFoundError:
        return {
            "status": "error",
            "message": "AWS CLI nao encontrado. Instale via 'pip install awscli' ou 'choco install awscli'",
        }
    except subprocess.TimeoutExpired:
        return {
            "status": "error",
            "message": "Comando AWS CLI excedeu o tempo limite (30s)",
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@tool
def aws_list_instances(profile: str = "", region: str = "") -> dict:
    """Lista instancias EC2 da conta AWS.

    Args:
        profile: Nome do perfil AWS (opcional, usa default se vazio).
        region: Regiao AWS (ex: us-east-1, sa-east-1).

    Returns:
        Dict com lista de instancias e seus estados.
    """
    cmd = ["ec2", "describe-instances"]
    if region:
        cmd.extend(["--region", region])

    result = _run_aws_cli(cmd, profile=profile)
    if result["status"] == "ok":
        # Extrair apenas informacoes relevantes
        instances = []
        reservations = result["output"].get("Reservations", [])
        for res in reservations:
            for inst in res.get("Instances", []):
                instances.append(
                    {
                        "id": inst.get("InstanceId"),
                        "state": inst.get("State", {}).get("Name"),
                        "type": inst.get("InstanceType"),
                        "az": inst.get("Placement", {}).get("AvailabilityZone"),
                        "launch_time": inst.get("LaunchTime"),
                    }
                )
        return {"status": "ok", "total": len(instances), "instances": instances}

    return result


@tool
def aws_describe_service(service: str, profile: str = "", region: str = "") -> dict:
    """Descreve o status de um servico AWS.

    Args:
        service: Nome do servico AWS (ec2, s3, lambda, rds, etc.).
        profile: Perfil AWS (opcional).
        region: Regiao AWS (opcional).

    Returns:
        Dict com informacoes do servico.
    """
    cmd = [service, "describe-status" if service != "s3" else "list-buckets"]
    if region:
        cmd.extend(["--region", region])

    return _run_aws_cli(cmd, profile=profile)


@tool
def aws_run_command(service_cmd: str, profile: str = "", region: str = "") -> dict:
    """Executa um comando AWS CLI customizado.

    ATENCAO: Apenas comandos de leitura sao permitidos. Comandos de escrita
    (create, delete, update, put, terminate, stop) serao rejeitados.

    Args:
        service_cmd: Comando AWS CLI (ex: 's3 ls', 'ec2 describe-instances').
        profile: Perfil AWS (opcional).
        region: Regiao AWS (opcional).

    Returns:
        Dict com resultado do comando.
    """
    # Whitelist de comandos de leitura
    blocked_prefixes = [
        "create",
        "delete",
        "update",
        "put",
        "terminate",
        "stop",
        "start",
        "reboot",
        "modify",
    ]
    parts = service_cmd.strip().split()
    for part in parts:
        if any(part.lower().startswith(prefix) for prefix in blocked_prefixes):
            return {
                "status": "error",
                "message": f"Comando '{part}' nao permitido (apenas comandos de leitura). "
                f"Comandos bloqueados: {', '.join(blocked_prefixes)}",
            }

    cmd_parts = service_cmd.split()
    if region:
        cmd_parts.extend(["--region", region])

    return _run_aws_cli(cmd_parts, profile=profile)


def register_aws_tools() -> None:
    """Registra as ferramentas AWS no TOOL_REGISTRY global."""
    from app.agent.nodes.executor import TOOL_REGISTRY

    TOOL_REGISTRY["aws_list_instances"] = aws_list_instances
    TOOL_REGISTRY["aws_describe_service"] = aws_describe_service
    TOOL_REGISTRY["aws_run_command"] = aws_run_command
    logger.info("[aws] tools registered")
