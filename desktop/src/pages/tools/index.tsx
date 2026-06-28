import { useState, useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Textarea } from "@/shared/ui/textarea";
import { Tabs } from "@/shared/ui/tabs";
import { Dialog } from "@/shared/ui/dialog";
import { motion, AnimatePresence } from "framer-motion";
import {
  Wrench,
  Server,
  Cpu,
  RefreshCw,
  Plus,
  Terminal,
  FileText,
  Search,
  CheckCircle,
  AlertTriangle,
  Play,
  Layers,
  ChevronRight,
  Trash2,
} from "lucide-react";
import { kaosFetch } from "@/shared/api/kaos-client";

interface MCPServer {
  name: string;
  health: {
    status: string;
    error?: string;
  };
  tools_count: number;
}

interface MCPTool {
  name: string;
  server: string;
  description: string;
  schema?: {
    type: string;
    properties: Record<string, any>;
    required?: string[];
  } | null;
  status: string;
}

interface OpenCodeItem {
  id: string;
  name: string;
  file: string;
  ext: string;
}

interface OpenCodeItemDetail {
  id: string;
  category: string;
  file: string;
  content: string;
}

const TOOLS_TABS = [
  { id: "mcp", label: "MCP Registry" },
  { id: "opencode", label: "OpenCode Catalog" },
];

const OPENCODE_CATEGORIES = [
  { id: "skills", label: "Skills", icon: Wrench },
  { id: "rules", label: "Rules", icon: Layers },
  { id: "tools", label: "Tools", icon: Cpu },
  { id: "commands", label: "Commands", icon: Terminal },
  { id: "references", label: "References", icon: FileText },
];

export default function ToolsPage() {
  const [activeTab, setActiveTab] = useState("mcp");

  // --- MCP State ---
  const [mcpServers, setMcpServers] = useState<MCPServer[]>([]);
  const [mcpTools, setMcpTools] = useState<MCPTool[]>([]);
  const [selectedTool, setSelectedTool] = useState<MCPTool | null>(null);
  const [mcpSearch, setMcpSearch] = useState("");
  const [mcpDialogOpen, setMcpDialogOpen] = useState(false);
  const [loadingMcp, setLoadingMcp] = useState(false);

  // New MCP Server Form
  const [newServerName, setNewServerName] = useState("");
  const [newServerCmd, setNewServerCmd] = useState("");
  const [newServerArgs, setNewServerArgs] = useState("");
  const [newServerEnv, setNewServerEnv] = useState("");
  const [registerLoading, setRegisterLoading] = useState(false);
  const [registerError, setRegisterError] = useState("");
  const [registerSuccess, setRegisterSuccess] = useState("");

  // --- OpenCode State ---
  const [activeCategory, setActiveCategory] = useState("skills");
  const [opencodeItems, setOpencodeItems] = useState<OpenCodeItem[]>([]);
  const [selectedOpencodeItem, setSelectedOpencodeItem] = useState<OpenCodeItemDetail | null>(null);
  const [loadingOpencode, setLoadingOpencode] = useState(false);
  const [loadingItemDetail, setLoadingItemDetail] = useState(false);
  const [refreshingCatalog, setRefreshingCatalog] = useState(false);

  // --- Fetch MCP ---
  const fetchMcpData = async () => {
    setLoadingMcp(true);
    try {
      const [serversRes, toolsRes] = await Promise.all([
        kaosFetch("/api/mcp/servers"),
        kaosFetch("/api/mcp/tools"),
      ]);

      if (serversRes.ok) {
        const serversData = await serversRes.json();
        setMcpServers(serversData.servers || []);
      }
      if (toolsRes.ok) {
        const toolsData = await toolsRes.json();
        setMcpTools(toolsData.tools || []);
      }
    } catch (err) {
      console.error("Failed to fetch MCP registry:", err);
    } finally {
      setLoadingMcp(false);
    }
  };

  // --- Fetch OpenCode Category Items ---
  const fetchOpenCodeCategory = async (category: string) => {
    setLoadingOpencode(true);
    try {
      const res = await kaosFetch(`/api/opencode/${category}`);
      if (res.ok) {
        const data = await res.json();
        setOpencodeItems(data[category] || []);
      }
    } catch (err) {
      console.error(`Failed to fetch opencode ${category}:`, err);
    } finally {
      setLoadingOpencode(false);
    }
  };

  // --- Fetch OpenCode Item Detail ---
  const fetchOpenCodeItemDetail = async (category: string, id: string) => {
    setLoadingItemDetail(true);
    setSelectedOpencodeItem(null);
    try {
      const res = await kaosFetch(`/api/opencode/${category}/${id}`);
      if (res.ok) {
        const data = await res.json();
        setSelectedOpencodeItem(data);
      }
    } catch (err) {
      console.error(`Failed to fetch opencode item details:`, err);
    } finally {
      setLoadingItemDetail(false);
    }
  };

  // --- Refresh OpenCode Catalog Cache ---
  const handleRefreshCatalog = async () => {
    setRefreshingCatalog(true);
    try {
      const res = await kaosFetch("/api/opencode/refresh", "", { method: "POST" });
      if (res.ok) {
        await fetchOpenCodeCategory(activeCategory);
      }
    } catch (err) {
      console.error("Failed to refresh opencode catalog:", err);
    } finally {
      setRefreshingCatalog(false);
    }
  };

  // --- Register MCP Server ---
  const handleRegisterMcp = async (e: React.FormEvent) => {
    e.preventDefault();
    setRegisterError("");
    setRegisterSuccess("");
    setRegisterLoading(true);

    // Parse env variables (KEY=VALUE lines)
    const env: Record<string, string> = {};
    if (newServerEnv.trim()) {
      newServerEnv.split("\n").forEach((line) => {
        const parts = line.split("=");
        if (parts.length >= 2) {
          env[parts[0].trim()] = parts.slice(1).join("=").trim();
        }
      });
    }

    // Parse args
    const args = newServerArgs
      .split(",")
      .map((arg) => arg.trim())
      .filter(Boolean);

    const payload = {
      name: newServerName.trim(),
      command: newServerCmd.trim(),
      args,
      env,
    };

    try {
      const res = await kaosFetch("/api/mcp/servers", "", {
        method: "POST",
        body: JSON.stringify(payload),
      });

      const data = await res.json();
      if (res.ok) {
        setRegisterSuccess(data.message || `Server '${payload.name}' registered successfully.`);
        setNewServerName("");
        setNewServerCmd("");
        setNewServerArgs("");
        setNewServerEnv("");
        fetchMcpData(); // Refresh list
        setTimeout(() => {
          setMcpDialogOpen(false);
          setRegisterSuccess("");
        }, 1500);
      } else {
        setRegisterError(data.detail || "Failed to register MCP server.");
      }
    } catch (err) {
      setRegisterError("Failed to connect to backend server.");
      console.error(err);
    } finally {
      setRegisterLoading(false);
    }
  };

  const handleDeleteServer = async (name: string) => {
    if (!confirm(`Are you sure you want to delete MCP server '${name}'?`)) return;
    try {
      const res = await kaosFetch(`/api/mcp/servers/${encodeURIComponent(name)}`, "", {
        method: "DELETE",
      });
      if (res.ok) {
        fetchMcpData();
      } else {
        const data = await res.json();
        alert(data.detail || "Failed to delete MCP server");
      }
    } catch (err) {
      console.error(err);
      alert("Network error. Please try again.");
    }
  };

  // Load appropriate data on mount or tab change
  useEffect(() => {
    if (activeTab === "mcp") {
      fetchMcpData();
    } else {
      fetchOpenCodeCategory(activeCategory);
    }
  }, [activeTab]);

  // Sync category items when category selection changes
  useEffect(() => {
    if (activeTab === "opencode") {
      fetchOpenCodeCategory(activeCategory);
      setSelectedOpencodeItem(null);
    }
  }, [activeCategory]);

  const filteredMcpTools = mcpTools.filter((tool) => {
    const term = mcpSearch.toLowerCase();
    return (
      tool.name.toLowerCase().includes(term) ||
      tool.server.toLowerCase().includes(term) ||
      tool.description.toLowerCase().includes(term)
    );
  });

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">Tools & Registry</h1>
          <p className="text-xs text-text-muted mt-0.5">
            Gerencie servidores Model Context Protocol (MCP) e explore extensões do catálogo OpenCode.
          </p>
        </div>
        {activeTab === "mcp" ? (
          <div className="flex gap-2">
            <Button variant="secondary" size="sm" onClick={fetchMcpData} disabled={loadingMcp}>
              <RefreshCw className={`h-3.5 w-3.5 mr-1.5 ${loadingMcp ? "animate-spin" : ""}`} />
              Reload
            </Button>
            <Button variant="primary" size="sm" onClick={() => setMcpDialogOpen(true)}>
              <Plus className="h-3.5 w-3.5 mr-1.5" />
              Register Server
            </Button>
          </div>
        ) : (
          <Button variant="secondary" size="sm" onClick={handleRefreshCatalog} disabled={refreshingCatalog}>
            <RefreshCw className={`h-3.5 w-3.5 mr-1.5 ${refreshingCatalog ? "animate-spin" : ""}`} />
            Refresh Catalog
          </Button>
        )}
      </div>

      {/* Tabs */}
      <Tabs tabs={TOOLS_TABS} activeTab={activeTab} onTabChange={setActiveTab} />

      {/* Content */}
      <div className="flex-1 min-h-0">
        <AnimatePresence mode="wait">
          {activeTab === "mcp" ? (
            <motion.div
              key="mcp"
              initial={{ opacity: 0, y: 5 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -5 }}
              className="flex flex-col gap-4 h-full"
            >
              {/* Servers section */}
              <div>
                <h3 className="text-xs font-semibold text-text-muted mb-2 font-mono uppercase tracking-wider">
                  Active MCP Servers ({mcpServers.length})
                </h3>
                {loadingMcp && mcpServers.length === 0 ? (
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                    {Array.from({ length: 3 }).map((_, i) => (
                      <Card key={i} className="border-border-subtle bg-surface animate-pulse h-[72px]" />
                    ))}
                  </div>
                ) : mcpServers.length === 0 ? (
                  <Card className="border-dashed border-border-subtle bg-surface/50 p-4 text-center">
                    <p className="text-xs text-text-muted">Nenhum servidor MCP registrado no momento.</p>
                  </Card>
                ) : (
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                    {mcpServers.map((server) => {
                      const isHealthy = server.health?.status === "healthy";
                      return (
                        <Card key={server.name} className="border-border-subtle bg-surface hover:border-border-hover transition-all">
                          <CardContent className="p-3.5 flex items-center justify-between">
                            <div className="flex items-center gap-3">
                              <div className={`p-2 rounded-lg ${isHealthy ? "bg-success/10 text-success" : "bg-error/10 text-error"}`}>
                                <Server className="h-4 w-4" />
                              </div>
                              <div>
                                <h4 className="text-sm font-semibold text-text-primary">{server.name}</h4>
                                <p className="text-[11px] text-text-dim mt-0.5">{server.tools_count} ferramentas registradas</p>
                              </div>
                            </div>
                            <div className="flex items-center gap-1.5">
                              <Badge variant={isHealthy ? "success" : "error"}>
                                {server.health?.status?.toUpperCase() || "UNKNOWN"}
                              </Badge>
                              <Button
                                variant="ghost"
                                size="sm"
                                onClick={(e) => {
                                  e.stopPropagation();
                                  handleDeleteServer(server.name);
                                }}
                                className="p-1 h-auto text-text-muted hover:text-error hover:bg-error/10 transition-all rounded"
                                title="Delete server"
                              >
                                <Trash2 className="h-3.5 w-3.5" />
                              </Button>
                            </div>
                          </CardContent>
                        </Card>
                      );
                    })}
                  </div>
                )}
              </div>

              {/* Tools section */}
              <div className="flex-1 flex gap-4 min-h-0 border-t border-border-subtle pt-4">
                {/* Tools List */}
                <div className="w-80 shrink-0 flex flex-col gap-2 min-h-0">
                  <div className="relative">
                    <Search className="absolute left-2.5 top-2.5 h-3.5 w-3.5 text-text-dim" />
                    <Input
                      placeholder="Buscar ferramenta..."
                      value={mcpSearch}
                      onChange={(e) => setMcpSearch(e.target.value)}
                      className="pl-8 text-xs h-9 bg-surface border-border-subtle focus:border-accent-primary"
                    />
                  </div>

                  <div className="flex-1 overflow-y-auto pr-1 space-y-1">
                    {loadingMcp && mcpTools.length === 0 ? (
                      Array.from({ length: 4 }).map((_, i) => (
                        <div key={i} className="h-14 rounded-lg bg-surface animate-pulse" />
                      ))
                    ) : filteredMcpTools.length === 0 ? (
                      <div className="p-4 text-center text-xs text-text-muted">Nenhuma ferramenta encontrada.</div>
                    ) : (
                      filteredMcpTools.map((tool) => (
                        <button
                          key={tool.name}
                          onClick={() => setSelectedTool(tool)}
                          className={`w-full text-left p-3 rounded-lg border text-xs transition-all flex items-center justify-between ${
                            selectedTool?.name === tool.name
                              ? "border-accent-primary bg-accent-primary/5 text-text-primary"
                              : "border-border-subtle bg-surface hover:border-border-hover text-text-muted hover:text-text-primary"
                          }`}
                        >
                          <div className="min-w-0 flex-1">
                            <span className="font-semibold truncate block font-mono text-text-primary">
                              {tool.name.replace(/^mcp_[^_]+_/, "")}
                            </span>
                            <span className="text-[10px] text-text-dim mt-0.5 block truncate">
                              Provider: <b className="font-medium text-text-muted">{tool.server}</b>
                            </span>
                          </div>
                          <ChevronRight className="h-3.5 w-3.5 text-text-dim ml-2" />
                        </button>
                      ))
                    )}
                  </div>
                </div>

                {/* Tool Detail Panel */}
                <div className="flex-1 min-w-0">
                  {selectedTool ? (
                    <Card className="h-full flex flex-col border-border-subtle bg-surface overflow-hidden">
                      <CardHeader className="pb-3 border-b border-border-subtle">
                        <div className="flex items-center justify-between">
                          <CardTitle className="text-sm font-mono text-accent-neon font-bold">
                            {selectedTool.name}
                          </CardTitle>
                          <Badge variant={selectedTool.status === "active" ? "success" : "neutral"}>
                            {selectedTool.status.toUpperCase()}
                          </Badge>
                        </div>
                        <p className="text-xs text-text-dim mt-1">
                          Server origin: <b className="font-mono text-text-muted">{selectedTool.server}</b>
                        </p>
                      </CardHeader>
                      <CardContent className="flex-1 overflow-y-auto p-4 space-y-4 font-mono text-xs">
                        <div>
                          <h4 className="text-[10px] font-semibold text-text-muted uppercase tracking-wider mb-1">
                            Descrição
                          </h4>
                          <p className="text-text-primary bg-bg-active/30 p-2.5 rounded border border-border-subtle leading-relaxed whitespace-pre-wrap">
                            {selectedTool.description || "Nenhuma descrição disponível para esta ferramenta."}
                          </p>
                        </div>

                        {selectedTool.schema && (
                          <div>
                            <h4 className="text-[10px] font-semibold text-text-muted uppercase tracking-wider mb-1.5">
                              Esquema de Entrada (Input Schema)
                            </h4>
                            <div className="border border-border-subtle rounded-md overflow-hidden bg-canvas/30">
                              <div className="bg-bg-active/50 px-3 py-1.5 border-b border-border-subtle flex justify-between items-center text-[10px] text-text-dim">
                                <span>TYPE: {selectedTool.schema.type.toUpperCase()}</span>
                                {selectedTool.schema.required && selectedTool.schema.required.length > 0 && (
                                  <span>{selectedTool.schema.required.length} required fields</span>
                                )}
                              </div>
                              <div className="p-3 overflow-x-auto max-h-72">
                                <pre className="text-[11px] leading-relaxed text-text-primary">
                                  {JSON.stringify(selectedTool.schema.properties, null, 2)}
                                </pre>
                              </div>
                            </div>
                          </div>
                        )}
                      </CardContent>
                    </Card>
                  ) : (
                    <Card className="h-full flex items-center justify-center border-border-subtle bg-surface/30">
                      <CardContent className="text-center text-text-muted">
                        <Cpu className="h-8 w-8 mx-auto mb-2 opacity-50 text-text-muted" />
                        <p className="text-xs">Selecione uma ferramenta da lista para visualizar suas configurações e parâmetros.</p>
                      </CardContent>
                    </Card>
                  )}
                </div>
              </div>
            </motion.div>
          ) : (
            <motion.div
              key="opencode"
              initial={{ opacity: 0, y: 5 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -5 }}
              className="flex gap-4 h-full"
            >
              {/* Category sidebar selector */}
              <div className="w-52 shrink-0 flex flex-col gap-1.5">
                <h3 className="text-xs font-semibold text-text-muted mb-1 font-mono uppercase tracking-wider px-2">
                  Categorias
                </h3>
                {OPENCODE_CATEGORIES.map((cat) => {
                  const Icon = cat.icon;
                  return (
                    <button
                      key={cat.id}
                      onClick={() => setActiveCategory(cat.id)}
                      className={`flex items-center gap-2.5 px-3 py-2 rounded-lg text-xs font-medium transition-all ${
                        activeCategory === cat.id
                          ? "bg-accent-primary/10 text-accent-neon font-bold border-l-2 border-accent-primary pl-2.5"
                          : "text-text-muted hover:bg-bg-active/50 hover:text-text-primary"
                      }`}
                    >
                      <Icon className="h-4 w-4" />
                      <span>{cat.label}</span>
                    </button>
                  );
                })}
              </div>

              {/* Items List */}
              <div className="w-64 shrink-0 flex flex-col gap-2 min-h-0 border-l border-border-subtle pl-4">
                <h3 className="text-xs font-semibold text-text-muted font-mono uppercase tracking-wider">
                  Módulos ({opencodeItems.length})
                </h3>
                <div className="flex-1 overflow-y-auto space-y-1 pr-1">
                  {loadingOpencode ? (
                    Array.from({ length: 4 }).map((_, i) => (
                      <div key={i} className="h-10 rounded-lg bg-surface animate-pulse" />
                    ))
                  ) : opencodeItems.length === 0 ? (
                    <div className="p-4 text-center text-xs text-text-muted">Nenhum item encontrado nesta categoria.</div>
                  ) : (
                    opencodeItems.map((item) => (
                      <button
                        key={item.id}
                        onClick={() => fetchOpenCodeItemDetail(activeCategory, item.id)}
                        className={`w-full text-left px-3 py-2.5 rounded-lg border text-xs transition-all flex items-center justify-between ${
                          selectedOpencodeItem?.id === item.id
                            ? "border-accent-primary bg-accent-primary/5 text-text-primary"
                            : "border-border-subtle bg-surface hover:border-border-hover text-text-muted hover:text-text-primary"
                        }`}
                      >
                        <div className="min-w-0 flex-1">
                          <span className="font-semibold block truncate">{item.name}</span>
                          <span className="text-[10px] text-text-dim mt-0.5 block truncate font-mono">
                            {item.file}
                          </span>
                        </div>
                        <ChevronRight className="h-3 w-3 text-text-dim ml-2" />
                      </button>
                    ))
                  )}
                </div>
              </div>

              {/* Item Content Previewer */}
              <div className="flex-1 min-w-0 border-l border-border-subtle pl-4">
                {loadingItemDetail ? (
                  <Card className="h-full flex items-center justify-center border-border-subtle bg-surface">
                    <CardContent className="text-center text-text-muted">
                      <RefreshCw className="h-6 w-6 animate-spin mx-auto mb-2 text-text-dim" />
                      <p className="text-xs">Carregando detalhes do item...</p>
                    </CardContent>
                  </Card>
                ) : selectedOpencodeItem ? (
                  <Card className="h-full flex flex-col border-border-subtle bg-surface overflow-hidden">
                    <CardHeader className="pb-3 border-b border-border-subtle">
                      <div className="flex items-center justify-between">
                        <CardTitle className="text-sm font-semibold text-text-primary">
                          {selectedOpencodeItem.id}
                        </CardTitle>
                        <Badge variant="info">{activeCategory.toUpperCase()}</Badge>
                      </div>
                      <p className="text-[10px] text-text-dim mt-1 font-mono">
                        Caminho do arquivo: .opencode/{activeCategory}/{selectedOpencodeItem.file}
                      </p>
                    </CardHeader>
                    <CardContent className="flex-1 overflow-y-auto p-0">
                      <div className="p-4">
                        <pre className="text-xs font-mono text-text-primary leading-relaxed whitespace-pre-wrap bg-canvas/30 p-4 border border-border-subtle rounded-lg max-w-full overflow-x-auto">
                          {selectedOpencodeItem.content || "# Sem conteúdo"}
                        </pre>
                      </div>
                    </CardContent>
                  </Card>
                ) : (
                  <Card className="h-full flex items-center justify-center border-border-subtle bg-surface/30">
                    <CardContent className="text-center text-text-muted">
                      <FileText className="h-8 w-8 mx-auto mb-2 opacity-50" />
                      <p className="text-xs">Selecione um módulo do OpenCode para ver suas diretivas e regras de execução.</p>
                    </CardContent>
                  </Card>
                )}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>

      {/* Register MCP Server Dialog */}
      <Dialog open={mcpDialogOpen} onClose={() => setMcpDialogOpen(false)} title="Register MCP Server">
        <form onSubmit={handleRegisterMcp} className="space-y-4">
          <div>
            <label className="block text-xs font-medium text-text-muted mb-1.5">Server Name</label>
            <Input
              required
              placeholder="Ex: filesystem"
              value={newServerName}
              onChange={(e) => setNewServerName(e.target.value)}
              className="text-xs"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-text-muted mb-1.5">Command</label>
            <Input
              required
              placeholder="Ex: npx, node, python, docker"
              value={newServerCmd}
              onChange={(e) => setNewServerCmd(e.target.value)}
              className="text-xs font-mono"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-text-muted mb-1.5">
              Arguments (Comma-separated)
            </label>
            <Input
              placeholder="Ex: -y, @modelcontextprotocol/server-filesystem, c:/workspace"
              value={newServerArgs}
              onChange={(e) => setNewServerArgs(e.target.value)}
              className="text-xs font-mono"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-text-muted mb-1.5">
              Environment Variables (KEY=VALUE lines)
            </label>
            <Textarea
              placeholder="Ex:&#10;PORT=8000&#10;API_KEY=mysecret"
              value={newServerEnv}
              onChange={(e) => setNewServerEnv(e.target.value)}
              className="text-xs font-mono min-h-[90px]"
            />
          </div>

          {registerError && (
            <div className="flex items-center gap-2 p-2.5 rounded bg-error/10 border border-error/30 text-error text-[11px] font-mono">
              <AlertTriangle className="h-4 w-4 shrink-0" />
              <span>{registerError}</span>
            </div>
          )}

          {registerSuccess && (
            <div className="flex items-center gap-2 p-2.5 rounded bg-success/10 border border-success/30 text-success text-[11px] font-mono">
              <CheckCircle className="h-4 w-4 shrink-0" />
              <span>{registerSuccess}</span>
            </div>
          )}

          <div className="flex justify-end gap-2 pt-2 border-t border-border-subtle">
            <Button
              type="button"
              variant="secondary"
              size="sm"
              onClick={() => setMcpDialogOpen(false)}
              disabled={registerLoading}
            >
              Cancel
            </Button>
            <Button type="submit" variant="primary" size="sm" disabled={registerLoading}>
              {registerLoading ? "Registering..." : "Register Server"}
            </Button>
          </div>
        </form>
      </Dialog>
    </div>
  );
}
