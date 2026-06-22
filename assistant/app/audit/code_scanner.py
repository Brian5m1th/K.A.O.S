import re
from dataclasses import dataclass, field
from pathlib import Path
from loguru import logger


@dataclass
class CodeSnapshot:
    stores: list[str] = field(default_factory=list)
    routes: list[str] = field(default_factory=list)
    tools: list[str] = field(default_factory=list)
    events: list[str] = field(default_factory=list)
    agents: list[str] = field(default_factory=list)
    workflows: list[str] = field(default_factory=list)
    providers: list[str] = field(default_factory=list)
    components: list[str] = field(default_factory=list)
    hooks: list[str] = field(default_factory=list)


class CodeScanner:
    _root: Path = Path(".")
    _exclude_dirs = {".git", "__pycache__", "node_modules", ".venv", "dist", "build", ".idea", ".opencode"}

    @classmethod
    def set_root(cls, root: Path) -> None:
        cls._root = root

    @classmethod
    def scan_all(cls) -> CodeSnapshot:
        snapshot = CodeSnapshot()
        snapshot.stores = cls._scan_stores()
        snapshot.routes = cls._scan_routes()
        snapshot.tools = cls._scan_tools()
        snapshot.events = cls._scan_events()
        snapshot.agents = cls._scan_agents()
        snapshot.workflows = cls._scan_workflows()
        snapshot.providers = cls._scan_providers()
        snapshot.components = cls._scan_components()
        snapshot.hooks = cls._scan_hooks()
        logger.info(f"[code_scanner] scan complete: {len(snapshot.stores)} stores, {len(snapshot.routes)} routes, {len(snapshot.tools)} tools, {len(snapshot.events)} events, {len(snapshot.agents)} agents, {len(snapshot.workflows)} workflows, {len(snapshot.providers)} providers")
        return snapshot

    @classmethod
    def _walk_python(cls, base: Path, pattern: str) -> list[str]:
        results = []
        for file_path in base.rglob("*.py"):
            if any(excl in file_path.parts for excl in cls._exclude_dirs):
                continue
            try:
                content = file_path.read_text(encoding="utf-8")
                if re.search(pattern, content):
                    rel = file_path.relative_to(cls._root).as_posix()
                    results.append(rel)
            except Exception:
                pass
        return results

    @classmethod
    def _walk_ts(cls, base: Path, pattern: str) -> list[str]:
        results = []
        for file_path in base.rglob("*.ts"):
            if any(excl in file_path.parts for excl in cls._exclude_dirs):
                continue
            try:
                content = file_path.read_text(encoding="utf-8")
                if re.search(pattern, content):
                    rel = file_path.relative_to(cls._root).as_posix()
                    results.append(rel)
            except Exception:
                pass
        return results

    @classmethod
    def _walk_tsx(cls, base: Path, pattern: str) -> list[str]:
        results = []
        for file_path in base.rglob("*.tsx"):
            if any(excl in file_path.parts for excl in cls._exclude_dirs):
                continue
            try:
                content = file_path.read_text(encoding="utf-8")
                if re.search(pattern, content):
                    rel = file_path.relative_to(cls._root).as_posix()
                    results.append(rel)
            except Exception:
                pass
        return results

    @classmethod
    def _scan_stores(cls) -> list[str]:
        results = []
        results.extend(cls._walk_ts(cls._root / "desktop" / "src" / "shared" / "lib" / "stores", r"create\("))
        results.extend(cls._walk_ts(cls._root / "desktop" / "src" / "features", r"use[A-Z].*Store"))
        return list(set(results))

    @classmethod
    def _scan_routes(cls) -> list[str]:
        results = []
        results.extend(cls._walk_tsx(cls._root / "desktop" / "src" / "pages", r"export.*default"))
        results.extend(cls._walk_tsx(cls._root / "desktop" / "src" / "app" / "routes", r".*"))
        return list(set(results))

    @classmethod
    def _scan_tools(cls) -> list[str]:
        results = []
        results.extend(cls._walk_ts(cls._root / "desktop" / "src" / "shared" / "lib", r"ToolEvent|tool.?schema"))
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "tools", r"class.*Tool|BaseTool"))
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "workflows" / "impl", r"tools"))
        return list(set(results))

    @classmethod
    def _scan_events(cls) -> list[str]:
        results = []
        results.extend(cls._walk_ts(cls._root / "desktop" / "src" / "shared" / "lib", r"EventBus|eventBus|emit\(|on\("))
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "observability", r"EventBus|EventSubscriber|EVENT_"))
        return list(set(results))

    @classmethod
    def _scan_agents(cls) -> list[str]:
        results = []
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "agent", r"class.*Agent|AgentState"))
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "workflows" / "impl", r"agent"))
        results.extend(cls._walk_ts(cls._root / "desktop" / "src" / "entities" / "agent", r".*"))
        return list(set(results))

    @classmethod
    def _scan_workflows(cls) -> list[str]:
        results = []
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "workflows" / "impl", r"class.*Workflow|BaseWorkflow"))
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "workflows", r"registry"))
        return list(set(results))

    @classmethod
    def _scan_providers(cls) -> list[str]:
        results = []
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "providers" / "chat", r"class.*Provider|BaseChatProvider"))
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "providers" / "embedding", r"class.*Provider|BaseEmbeddingProvider"))
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "providers" / "vector", r"class.*Provider|BaseVectorStore"))
        results.extend(cls._walk_python(cls._root / "assistant" / "app" / "providers" / "memory", r"class.*Provider|BaseMemoryProvider"))
        return list(set(results))

    @classmethod
    def _scan_components(cls) -> list[str]:
        results = []
        results.extend(cls._walk_tsx(cls._root / "desktop" / "src" / "widgets", r"export.*function|export.*const"))
        results.extend(cls._walk_tsx(cls._root / "desktop" / "src" / "shared" / "ui", r"export.*function|export.*const"))
        return list(set(results))

    @classmethod
    def _scan_hooks(cls) -> list[str]:
        results = []
        results.extend(cls._walk_ts(cls._root / "desktop" / "src" / "features", r"use[A-Z].*"))
        results.extend(cls._walk_ts(cls._root / "desktop" / "src" / "shared" / "lib", r"use[A-Z].*"))
        return list(set(results))