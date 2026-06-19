import os

import httpx
from langchain_core.tools import tool
from loguru import logger


def _github_api(
    method: str, endpoint: str, token: str | None = None, data: dict | None = None
) -> dict | list:
    token = token or os.getenv("GITHUB_TOKEN", "")
    url = f"https://api.github.com{endpoint}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "K.A.O.S",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        with httpx.Client(timeout=15) as client:
            if data is not None:
                resp = client.request(method, url, headers=headers, json=data)
            else:
                resp = client.request(method, url, headers=headers)
            resp.raise_for_status()
            return resp.json()
    except httpx.HTTPStatusError as e:
        logger.error(
            f"[error] github - {method} {endpoint}: {e.response.status_code} {e.response.text[:200]}"
        )
        return {"error": str(e), "status": e.response.status_code}
    except Exception as e:
        logger.error(f"[error] github - {method} {endpoint}: {e}")
        return {"error": str(e)}


@tool
def github_list_repos(owner: str = "") -> list | dict:
    """Lista repositorios do GitHub do usuario ou de um owner especifico."""
    endpoint = f"/users/{owner}/repos" if owner else "/user/repos"
    logger.info(f"[tool] github - list_repos: {endpoint}")
    result = _github_api("GET", endpoint)
    if isinstance(result, list):
        return [
            {"name": r["name"], "url": r["html_url"], "private": r["private"]}
            for r in result[:20]
        ]
    return result


@tool
def github_get_repo(repo: str, owner: str = "") -> dict:
    """Obtem detalhes de um repositorio do GitHub."""
    full_name = f"{owner}/{repo}" if owner else repo
    logger.info(f"[tool] github - get_repo: {full_name}")
    return _github_api("GET", f"/repos/{full_name}")


@tool
def github_list_issues(repo: str, owner: str = "", state: str = "open") -> list | dict:
    """Lista issues de um repositorio do GitHub."""
    full_name = f"{owner}/{repo}" if owner else repo
    logger.info(f"[tool] github - list_issues: {full_name} state={state}")
    result = _github_api("GET", f"/repos/{full_name}/issues?state={state}")
    if isinstance(result, list):
        return [
            {
                "number": i["number"],
                "title": i["title"],
                "state": i["state"],
                "url": i["html_url"],
            }
            for i in result[:20]
        ]
    return result


def register_github_tools():
    from app.agent.nodes.executor import TOOL_REGISTRY

    TOOL_REGISTRY["github_list_repos"] = github_list_repos
    TOOL_REGISTRY["github_get_repo"] = github_get_repo
    TOOL_REGISTRY["github_list_issues"] = github_list_issues
    logger.info("[info] github - 3 tools registradas no TOOL_REGISTRY")


register_github_tools()
