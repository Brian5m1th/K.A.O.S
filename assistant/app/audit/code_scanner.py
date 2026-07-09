import re
from dataclasses import dataclass, field
from pathlib import Path
from loguru import logger
from app.core.environment_service import EnvironmentService


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
    """
    Scanner de codigo fonte do K.A.O.S.
    Usa EnvironmentService para resolver paths corretamente
    em qualquer ambiente (Docker, Local, CI).

    Regras:
      - Arquivos TypeScript/TSX sao escaneados em ``env.desktop_src``
      - Arquivos Python sao escaneados em ``env.backend_src``
      - Paths relativos sao calculados contra ``env.project_root``
    """

    _exclude_dirs = {
        ".git",
        "__pycache__",
        "node_modules",
        ".venv",
        "dist",
        "build",
        ".idea",
        ".opencode",
    }

    @classmethod
    def scan_all(cls) -> CodeSnapshot:
        """Escaneia todo o codebase e retorna um snapshot."""
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
        logger.info(
            f"[code_scanner] scan complete: {len(snapshot.stores)} stores, "
            f"{len(snapshot.routes)} routes, {len(snapshot.tools)} tools, "
            f"{len(snapshot.events)} events, {len(snapshot.agents)} agents, "
            f"{len(snapshot.workflows)} workflows, {len(snapshot.providers)} providers"
        )
        return snapshot

    # ── Helpers ───────────────────────────────────────────────────────

    @classmethod
    def _env(cls):
        """Retorna EnvironmentInfo cacheado."""
        return EnvironmentService.detect()

    @classmethod
    def _rel(cls, path: Path) -> str:
        """Path relativo ao project_root."""
        try:
            return path.relative_to(cls._env().project_root).as_posix()
        except ValueError:
            return path.as_posix()

    @classmethod
    def _walk(cls, base: Path, pattern: str, ext: str = ".py") -> list[str]:
        """Walk em um diretorio buscando arquivos que contem pattern."""
        results = []
        if not base.exists():
            return results
        for file_path in base.rglob(f"*{ext}"):
            if any(excl in file_path.parts for excl in cls._exclude_dirs):
                continue
            try:
                content = file_path.read_text(encoding="utf-8")
                if re.search(pattern, content):
                    results.append(cls._rel(file_path))
            except Exception:
                pass
        return results

    @classmethod
    def _walk_python(cls, base: Path, pattern: str) -> list[str]:
        return cls._walk(base, pattern, ".py")

    @classmethod
    def _walk_ts(cls, base: Path, pattern: str) -> list[str]:
        return cls._walk(base, pattern, ".ts")

    @classmethod
    def _walk_tsx(cls, base: Path, pattern: str) -> list[str]:
        return cls._walk(base, pattern, ".tsx")

    # ── Desktop paths ─────────────────────────────────────────────────

    @classmethod
    def _desktop_src(cls) -> Path | None:
        """Path para desktop/src, ou None se nao existir."""
        return cls._env().desktop_src

    @classmethod
    def _desktop_path(cls, *parts: str) -> Path | None:
        src = cls._desktop_src()
        if src is None:
            return None
        return src.joinpath(*parts)

    # ── Backend paths ─────────────────────────────────────────────────

    @classmethod
    def _backend_src(cls) -> Path:
        """Path para assistant/app (backendo Python)."""
        return cls._env().backend_src

    @classmethod
    def _backend_path(cls, *parts: str) -> Path:
        return cls._backend_src().joinpath(*parts)

    # ── Scans individuais ─────────────────────────────────────────────

    @classmethod
    def _scan_stores(cls) -> list[str]:
        results: list[str] = []
        stores_dir = cls._desktop_path("shared", "lib", "stores")
        if stores_dir:
            results.extend(cls._walk_ts(stores_dir, r"create\("))
        features_dir = cls._desktop_path("features")
        if features_dir:
            results.extend(cls._walk_ts(features_dir, r"use[A-Z].*Store"))
        return list(set(results))

    @classmethod
    def _scan_routes(cls) -> list[str]:
        results: list[str] = []
        pages_dir = cls._desktop_path("pages")
        if pages_dir:
            results.extend(cls._walk_tsx(pages_dir, r"export.*default"))
        routes_dir = cls._desktop_path("app", "routes")
        if routes_dir:
            results.extend(cls._walk_tsx(routes_dir, r".*"))
        return list(set(results))

    @classmethod
    def _scan_tools(cls) -> list[str]:
        results: list[str] = []
        lib_dir = cls._desktop_path("shared", "lib")
        if lib_dir:
            results.extend(cls._walk_ts(lib_dir, r"ToolEvent|tool.?schema"))
        tools_dir = cls._backend_path("tools")
        results.extend(cls._walk_python(tools_dir, r"class.*Tool|BaseTool"))
        workflows_dir = cls._backend_path("workflows", "impl")
        results.extend(cls._walk_python(workflows_dir, r"tools"))
        return list(set(results))

    @classmethod
    def _scan_events(cls) -> list[str]:
        results: list[str] = []
        lib_dir = cls._desktop_path("shared", "lib")
        if lib_dir:
            results.extend(cls._walk_ts(lib_dir, r"EventBus|eventBus|emit\(|on\("))
        obs_dir = cls._backend_path("observability")
        results.extend(cls._walk_python(obs_dir, r"EventBus|EventSubscriber|EVENT_"))
        return list(set(results))

    @classmethod
    def _scan_agents(cls) -> list[str]:
        results: list[str] = []
        agent_dir = cls._backend_path("agent")
        results.extend(cls._walk_python(agent_dir, r"class.*Agent|AgentState"))
        wf_dir = cls._backend_path("workflows", "impl")
        results.extend(cls._walk_python(wf_dir, r"agent"))
        agent_ts_dir = cls._desktop_path("entities", "agent")
        if agent_ts_dir:
            results.extend(cls._walk_ts(agent_ts_dir, r".*"))
        return list(set(results))

    @classmethod
    def _scan_workflows(cls) -> list[str]:
        results: list[str] = []
        wf_dir = cls._backend_path("workflows", "impl")
        results.extend(cls._walk_python(wf_dir, r"class.*Workflow|BaseWorkflow"))
        registry_dir = cls._backend_path("workflows")
        results.extend(cls._walk_python(registry_dir, r"registry"))
        return list(set(results))

    @classmethod
    def _scan_providers(cls) -> list[str]:
        results: list[str] = []
        for sub in ("chat", "embedding", "vector", "memory"):
            d = cls._backend_path("providers", sub)
            results.extend(cls._walk_python(d, r"class.*Provider|Base"))
        return list(set(results))

    @classmethod
    def _scan_components(cls) -> list[str]:
        results: list[str] = []
        widgets_dir = cls._desktop_path("widgets")
        if widgets_dir:
            results.extend(
                cls._walk_tsx(widgets_dir, r"export.*function|export.*const")
            )
        ui_dir = cls._desktop_path("shared", "ui")
        if ui_dir:
            results.extend(cls._walk_tsx(ui_dir, r"export.*function|export.*const"))
        return list(set(results))

    @classmethod
    def _scan_hooks(cls) -> list[str]:
        results: list[str] = []
        features_dir = cls._desktop_path("features")
        if features_dir:
            results.extend(cls._walk_ts(features_dir, r"use[A-Z].*"))
        lib_dir = cls._desktop_path("shared", "lib")
        if lib_dir:
            results.extend(cls._walk_ts(lib_dir, r"use[A-Z].*"))
        return list(set(results))
