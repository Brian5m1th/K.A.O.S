import { useEffect, useState } from "react";
import { BookOpen, FileText, Search, Loader2, RefreshCw } from "lucide-react";
import { kaosFetch } from "@/infrastructure";
import { Card, CardContent } from "@/shared/ui/card";

interface VaultFile {
  name: string;
  path: string;
  size: number;
}

export default function VaultPage() {
  const [files, setFiles] = useState<VaultFile[]>([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedPath, setSelectedPath] = useState<string | null>(null);
  const [selectedContent, setSelectedContent] = useState<string>("");
  const [loadingList, setLoadingList] = useState(false);
  const [loadingContent, setLoadingContent] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [viewMode, setViewMode] = useState<"preview" | "raw">("preview");

  const fetchFiles = async () => {
    setLoadingList(true);
    setError(null);
    try {
      const response = await kaosFetch("/rag/vault/files", "");
      if (!response.ok) {
        throw new Error("Failed to load vault files");
      }
      const data = await response.json();
      setFiles(data.files || []);
    } catch (err: any) {
      setError(err.message || "Error accessing backend server");
    } finally {
      setLoadingList(false);
    }
  };

  const fetchFileContent = async (path: string) => {
    setLoadingContent(true);
    try {
      const response = await kaosFetch(`/rag/vault/file?path=${encodeURIComponent(path)}`, "");
      if (!response.ok) {
        throw new Error("Failed to load file content");
      }
      const text = await response.text();
      setSelectedContent(text);
      setSelectedPath(path);
    } catch (err: any) {
      setSelectedContent(`Erro ao carregar o arquivo: ${err.message}`);
    } finally {
      setLoadingContent(false);
    }
  };

  useEffect(() => {
    fetchFiles();
  }, []);

  const filteredFiles = files.filter(
    (f) =>
      f.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      f.path.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const formatSize = (bytes: number) => {
    if (bytes < 1024) return `${bytes} B`;
    const kb = bytes / 1024;
    if (kb < 1024) return `${kb.toFixed(1)} KB`;
    return `${(kb / 1024).toFixed(1)} MB`;
  };

  // Helper component to render simple Markdown layout nicely
  const MarkdownPreview = ({ content }: { content: string }) => {
    if (!content) return <p className="text-xs text-text-dim">Sem conteúdo</p>;

    const lines = content.split("\n");
    let inCodeBlock = false;
    let codeLines: string[] = [];
    const elements: React.ReactNode[] = [];

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];

      // Code blocks
      if (line.trim().startsWith("```")) {
        if (inCodeBlock) {
          elements.push(
            <pre key={`code-${i}`} className="bg-canvas/80 p-3.5 rounded-lg border border-border-subtle font-mono text-[11px] text-accent-neon my-3 overflow-x-auto select-text">
              <code>{codeLines.join("\n")}</code>
            </pre>
          );
          codeLines = [];
          inCodeBlock = false;
        } else {
          inCodeBlock = true;
        }
        continue;
      }

      if (inCodeBlock) {
        codeLines.push(line);
        continue;
      }

      // Headers
      if (line.startsWith("# ")) {
        elements.push(<h1 key={i} className="text-lg font-bold text-text-primary mt-6 mb-3 border-b border-border-subtle pb-1">{line.slice(2)}</h1>);
        continue;
      }
      if (line.startsWith("## ")) {
        elements.push(<h2 key={i} className="text-base font-semibold text-text-primary mt-5 mb-2.5">{line.slice(3)}</h2>);
        continue;
      }
      if (line.startsWith("### ")) {
        elements.push(<h3 key={i} className="text-xs font-semibold text-text-primary mt-4 mb-2">{line.slice(4)}</h3>);
        continue;
      }

      // Blockquotes / GitHub-style alerts
      if (line.startsWith("> ")) {
        const text = line.slice(2);
        if (text.startsWith("[!NOTE]") || text.startsWith("[!IMPORTANT]") || text.startsWith("[!WARNING]") || text.startsWith("[!TIP]")) {
          const type = text.includes("WARNING") ? "warning" : text.includes("IMPORTANT") ? "error" : text.includes("TIP") ? "success" : "info";
          elements.push(
            <div key={i} className={`p-3 rounded-lg border my-3 text-xs leading-relaxed ${
              type === "warning" ? "bg-warning/5 border-warning/30 text-warning" :
              type === "error" ? "bg-error/5 border-error/30 text-error font-semibold" :
              type === "success" ? "bg-success/5 border-success/30 text-success" :
              "bg-accent-primary/5 border-accent-primary/30 text-accent-primary"
            }`}>
              {text.replace(/\[!(NOTE|IMPORTANT|WARNING|TIP)\]/, "").trim()}
            </div>
          );
        } else {
          elements.push(
            <blockquote key={i} className="border-l-4 border-accent-primary/45 pl-3 italic text-text-muted my-3 text-xs leading-relaxed">
              {text}
            </blockquote>
          );
        }
        continue;
      }

      // Lists
      if (line.trim().startsWith("- ") || line.trim().startsWith("* ")) {
        elements.push(
          <div key={i} className="flex items-start gap-2 pl-3 my-1.5 text-xs text-text-muted leading-relaxed">
            <span className="h-1.5 w-1.5 rounded-full bg-accent-primary mt-1.5 shrink-0" />
            <span>{line.trim().slice(2)}</span>
          </div>
        );
        continue;
      }

      // Divider
      if (line.trim() === "---" || line.trim() === "***") {
        elements.push(<hr key={i} className="border-border-subtle my-5" />);
        continue;
      }

      // Standard text parsing
      if (line.trim() === "") {
        elements.push(<div key={i} className="h-2" />);
      } else {
        let renderedText: React.ReactNode = line;
        if (line.includes("**")) {
          const parts = line.split("**");
          renderedText = parts.map((part, index) => index % 2 === 1 ? <strong key={index} className="font-semibold text-text-primary">{part}</strong> : part);
        }
        elements.push(<p key={i} className="text-xs text-text-muted leading-relaxed my-2 select-text">{renderedText}</p>);
      }
    }

    if (inCodeBlock && codeLines.length > 0) {
      elements.push(
        <pre key="code-unclosed" className="bg-canvas/80 p-3.5 rounded-lg border border-border-subtle font-mono text-[11px] text-accent-neon my-3 overflow-x-auto select-text">
          <code>{codeLines.join("\n")}</code>
        </pre>
      );
    }

    return <div className="space-y-1">{elements}</div>;
  };

  return (
    <div className="flex h-full bg-canvas text-text-primary">
      {/* Sidebar: File List */}
      <div className="w-80 border-r border-border flex flex-col h-full bg-canvas-sidebar">
        <div className="p-4 border-b border-border space-y-3">
          <div className="flex items-center justify-between">
            <h2 className="text-sm font-semibold text-text-primary flex items-center gap-2">
              <BookOpen className="w-4 h-4 text-accent-primary" />
              Knowledge Vault
            </h2>
            <button
              onClick={fetchFiles}
              disabled={loadingList}
              className="p-1 rounded hover:bg-canvas-subtle transition-colors text-text-muted hover:text-text-primary"
              title="Recarregar arquivos"
            >
              <RefreshCw className={`w-3.5 h-3.5 ${loadingList ? "animate-spin" : ""}`} />
            </button>
          </div>
          
          <div className="relative">
            <Search className="w-3.5 h-3.5 text-text-dim absolute left-3 top-2.5" />
            <input
              type="text"
              placeholder="Buscar documentos..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-8 pr-3 py-1.5 bg-canvas-subtle border border-border rounded-md text-xs text-text-primary placeholder-text-dim focus:outline-none focus:border-accent-primary transition-colors"
            />
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-2 space-y-1">
          {loadingList ? (
            <div className="flex flex-col items-center justify-center p-8 gap-2">
              <Loader2 className="w-5 h-5 animate-spin text-text-dim" />
              <span className="text-[10px] text-text-muted">Carregando índice...</span>
            </div>
          ) : error ? (
            <div className="p-4 text-center">
              <p className="text-xs text-error mb-2">{error}</p>
              <button
                onClick={fetchFiles}
                className="px-3 py-1 text-xs bg-canvas-subtle hover:bg-border rounded border border-border transition-colors text-text-primary"
              >
                Tentar Novamente
              </button>
            </div>
          ) : filteredFiles.length === 0 ? (
            <div className="p-6 text-center text-text-dim text-xs">
              Nenhum documento encontrado.
            </div>
          ) : (
            filteredFiles.map((file) => {
              const isSelected = selectedPath === file.path;
              return (
                <button
                  key={file.path}
                  onClick={() => fetchFileContent(file.path)}
                  className={`w-full text-left p-2.5 rounded-md flex items-start gap-2.5 transition-all text-xs ${
                    isSelected
                      ? "bg-accent-primary/10 text-accent-primary border-l-2 border-accent-primary"
                      : "hover:bg-canvas-subtle text-text-muted hover:text-text-primary"
                  }`}
                >
                  <FileText className={`w-4 h-4 mt-0.5 shrink-0 ${isSelected ? "text-accent-primary" : "text-text-dim"}`} />
                  <div className="overflow-hidden">
                    <div className="font-medium truncate text-text-primary">{file.name}</div>
                    <div className="text-[10px] text-text-dim truncate mt-0.5 font-mono">{file.path}</div>
                  </div>
                </button>
              );
            })
          )}
        </div>
      </div>

      {/* Main Panel: File Viewer */}
      <div className="flex-1 flex flex-col h-full overflow-hidden">
        {selectedPath ? (
          <div className="flex-1 flex flex-col h-full overflow-hidden">
            {/* Header */}
            <div className="p-4 border-b border-border flex items-center justify-between shrink-0 bg-canvas-header">
              <div>
                <h1 className="text-sm font-semibold text-text-primary truncate">{selectedPath.split("/").pop()}</h1>
                <p className="text-[10px] text-text-dim mt-0.5 font-mono truncate">{selectedPath}</p>
              </div>
              <div className="flex items-center gap-3">
                {/* View toggle */}
                <div className="flex items-center gap-1 bg-canvas-subtle p-0.5 rounded border border-border">
                  <button
                    onClick={() => setViewMode("preview")}
                    className={`px-2.5 py-1 text-[10px] rounded transition-all font-medium ${
                      viewMode === "preview"
                        ? "bg-accent-primary text-white shadow-sm font-bold"
                        : "text-text-muted hover:text-text-primary"
                    }`}
                  >
                    Preview
                  </button>
                  <button
                    onClick={() => setViewMode("raw")}
                    className={`px-2.5 py-1 text-[10px] rounded transition-all font-medium ${
                      viewMode === "raw"
                        ? "bg-accent-primary text-white shadow-sm font-bold"
                        : "text-text-muted hover:text-text-primary"
                    }`}
                  >
                    Raw Source
                  </button>
                </div>
                <div className="text-[10px] text-text-muted px-2 py-1 bg-canvas-subtle rounded border border-border font-mono shrink-0">
                  {formatSize(files.find(f => f.path === selectedPath)?.size || 0)}
                </div>
              </div>
            </div>

            {/* Content Area */}
            <div className="flex-1 overflow-y-auto p-6 bg-canvas-editor relative">
              {loadingContent ? (
                <div className="absolute inset-0 bg-canvas/50 flex items-center justify-center">
                  <Loader2 className="w-8 h-8 animate-spin text-accent-primary" />
                </div>
              ) : (
                <Card className="max-w-4xl mx-auto shadow-sm border border-border">
                  <CardContent className="p-8">
                    {viewMode === "preview" ? (
                      <MarkdownPreview content={selectedContent} />
                    ) : (
                      <pre className="whitespace-pre-wrap font-mono text-xs text-text-primary leading-relaxed select-text">
                        {selectedContent}
                      </pre>
                    )}
                  </CardContent>
                </Card>
              )}
            </div>
          </div>
        ) : (
          <div className="flex-1 flex items-center justify-center">
            <div className="text-center p-8 max-w-sm">
              <BookOpen className="h-16 w-16 text-text-dim mx-auto mb-4 stroke-1 animate-pulse" />
              <h2 className="text-base font-semibold text-text-primary mb-1">Knowledge Explorer</h2>
              <p className="text-xs text-text-muted">
                Selecione um arquivo de documentação técnica (SDD) ou nota do Obsidian no menu lateral para visualizar seu conteúdo.
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
