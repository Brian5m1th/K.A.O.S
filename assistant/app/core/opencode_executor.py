import subprocess
import os
import shutil
from pathlib import Path
from loguru import logger
from app.core.environment_service import EnvironmentService


class OpenCodeExecutor:
    # Rigid command whitelist (allowed command prefixes/programs)
    WHITELIST = {
        "git",
        "python",
        "pip",
        "npm",
        "echo",
        "ls",
        "dir",
        "cat",
        "grep",
        "mkdir",
        "pytest",
        "uv",
        "tsc",
        "vite",
    }

    # Strict blacklist of dangerous commands/patterns
    BLACKLIST = {
        "rm -rf /",
        "rm -rf *",
        "rmdir /s /q",
        "format-volume",
        "format-disk",
        "mkfs",
        "dd if=",
        "shred",
        "shutdown",
        "reboot",
    }

    @classmethod
    def validate_command(cls, command: str) -> bool:
        cmd_strip = command.strip()
        cmd_lower = cmd_strip.lower()

        # Check blacklist
        for blacklisted in cls.BLACKLIST:
            if blacklisted in cmd_lower:
                logger.error(
                    f"[opencode_executor] Comando contém termo proibido: '{blacklisted}'"
                )
                return False

        # Extract first token (the program/command)
        parts = cmd_strip.split()
        if not parts:
            return False

        program = parts[0].lower()
        # Strip potential path/exec prefixes (like ./ or python.exe)
        program = Path(program).name.replace(".exe", "")

        if program not in cls.WHITELIST:
            logger.error(
                f"[opencode_executor] Programa '{program}' não está na whitelist."
            )
            return False

        return True

    @classmethod
    def execute(cls, command: str, user_approved: bool = False) -> dict:
        logger.info(
            f"[start] OpenCodeExecutor - execute [command='{command}', approved={user_approved}]"
        )

        if not user_approved:
            logger.error("[opencode_executor] Execução negada: consentimento do usuário ausente.")
            return {
                "status": "error",
                "message": "Consentimento manual do usuário obrigatório para executar comandos CLI.",
            }

        if not cls.validate_command(command):
            return {
                "status": "error",
                "message": "Comando rejeitado pelas regras de segurança (whitelist/blacklist).",
            }

        # Check if Docker is available
        docker_available = shutil.which("docker") is not None
        project_root = EnvironmentService.detect().project_root.resolve().as_posix()

        if docker_available:
            logger.info("[opencode_executor] Docker detectado. Executando em sandbox...")
            # We map the project root to a workspace directory in docker
            # Running alpine or python container for single-use sandbox
            docker_cmd = [
                "docker",
                "run",
                "--rm",
                "-v",
                f"{project_root}:/workspace",
                "-w",
                "/workspace",
                "python:3.13-slim",
                "sh",
                "-c",
                command,
            ]
            try:
                res = subprocess.run(
                    docker_cmd,
                    capture_output=True,
                    text=True,
                    timeout=60,
                )
                logger.info(
                    f"[info] OpenCodeExecutor - sandbox return_code={res.returncode}"
                )
                return {
                    "status": "success" if res.returncode == 0 else "error",
                    "exit_code": res.returncode,
                    "stdout": res.stdout,
                    "stderr": res.stderr,
                    "sandbox": "docker",
                }
            except subprocess.TimeoutExpired:
                logger.warning("[opencode_executor] Execução docker expirou por timeout.")
                return {
                    "status": "error",
                    "message": "Execução do container docker expirou (timeout).",
                }
            except Exception as e:
                logger.warning(
                    f"[opencode_executor] Falha ao rodar Docker container, fallback local: {e}"
                )

        # Fallback to local subprocess execution with restricted path scoping
        logger.info(
            "[opencode_executor] Docker indisponível. Executando localmente..."
        )
        try:
            res = subprocess.run(
                command,
                shell=True,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60,
            )
            return {
                "status": "success" if res.returncode == 0 else "error",
                "exit_code": res.returncode,
                "stdout": res.stdout,
                "stderr": res.stderr,
                "sandbox": "local-fallback",
            }
        except subprocess.TimeoutExpired:
            return {
                "status": "error",
                "message": "Execução local expirou (timeout).",
            }
        except Exception as e:
            return {"status": "error", "message": f"Falha na execução local: {e}"}
