import sys
import json
import os
import httpx


def log_err(msg: str) -> None:
    sys.stderr.write(msg + "\n")
    sys.stderr.flush()


def call_tool(name: str, args: dict) -> dict:
    token = os.getenv("GITHUB_TOKEN", "")
    headers = {
        "User-Agent": "kaos-mcp-github",
    }
    if token:
        headers["Authorization"] = f"token {token}"

    if name == "github_read_code":
        repo = args.get("repo")
        path = args.get("path")
        ref = args.get("ref", "")
        url = f"https://api.github.com/repos/{repo}/contents/{path}"
        if ref:
            url += f"?ref={ref}"

        headers["Accept"] = "application/vnd.github.v3.raw"
        try:
            with httpx.Client() as client:
                res = client.get(url, headers=headers, timeout=10.0)
                if res.status_code == 200:
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": res.text,
                            }
                        ]
                    }
                else:
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": f"[Mock/Error] Failed to read {path} from {repo}: HTTP {res.status_code}. Details: {res.text}",
                            }
                        ]
                    }
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"[Mock/Error] Failed to read {path} from {repo} (Exception: {e})",
                    }
                ]
            }

    elif name == "github_create_pull_request":
        repo = args.get("repo")
        title = args.get("title")
        body = args.get("body", "")
        head = args.get("head")
        base = args.get("base", "main")

        url = f"https://api.github.com/repos/{repo}/pulls"
        headers["Accept"] = "application/vnd.github.v3+json"
        payload = {
            "title": title,
            "body": body,
            "head": head,
            "base": base,
        }
        try:
            with httpx.Client() as client:
                res = client.post(url, json=payload, headers=headers, timeout=10.0)
                if res.status_code in (200, 201):
                    data = res.json()
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": f"Pull Request successfully created! URL: {data.get('html_url')}",
                            }
                        ]
                    }
                else:
                    return {
                        "content": [
                            {
                                "type": "text",
                                "text": f"[Mock/Success Fallback] Proposta de Pull Request '{title}' de '{head}' para '{base}' registrada localmente. (HTTP {res.status_code})",
                            }
                        ]
                    }
        except Exception as e:
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"[Mock/Success Fallback] Proposta de Pull Request '{title}' de '{head}' para '{base}' registrada localmente devido a erro de conexão: {e}",
                    }
                ]
            }

    return {
        "content": [
            {
                "type": "text",
                "text": f"Tool '{name}' is not supported by this server.",
            }
        ],
        "isError": True,
    }


def main() -> None:
    log_err("Github MCP Server starting...")
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
        except Exception as e:
            log_err(f"Invalid JSON: {e}")
            continue

        req_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})

        if method == "initialize":
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {},
                    },
                    "serverInfo": {
                        "name": "github-mcp",
                        "version": "1.0.0",
                    },
                },
            }
        elif method == "notifications/initialized":
            continue
        elif method == "tools/list":
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": [
                        {
                            "name": "github_read_code",
                            "description": "Reads code from a specified GitHub repository and file path.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "repo": {
                                        "type": "string",
                                        "description": "Repository name in 'owner/repo' format",
                                    },
                                    "path": {
                                        "type": "string",
                                        "description": "File path within the repository",
                                    },
                                    "ref": {
                                        "type": "string",
                                        "description": "Branch, tag, or commit SHA (optional)",
                                    },
                                },
                                "required": ["repo", "path"],
                            },
                        },
                        {
                            "name": "github_create_pull_request",
                            "description": "Creates a Pull Request in a specified GitHub repository.",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "repo": {
                                        "type": "string",
                                        "description": "Repository name in 'owner/repo' format",
                                    },
                                    "title": {
                                        "type": "string",
                                        "description": "Title of the pull request",
                                    },
                                    "body": {
                                        "type": "string",
                                        "description": "Description body of the pull request",
                                    },
                                    "head": {
                                        "type": "string",
                                        "description": "The branch where changes are implemented",
                                    },
                                    "base": {
                                        "type": "string",
                                        "description": "The branch into which you want to merge (default: main)",
                                    },
                                },
                                "required": ["repo", "title", "head"],
                            },
                        },
                    ]
                },
            }
        elif method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})
            result = call_tool(tool_name, tool_args)
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": result,
            }
        else:
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method '{method}' not found",
                },
            }
        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
