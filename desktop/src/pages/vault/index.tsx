import { useEffect, useState } from "react";
import { BookOpen, FileText, Search, Loader2, RefreshCw } from "lucide-react";
import { kaosFetch } from "@/shared/api/kaos-client";
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
              <div className="text-[10px] text-text-muted px-2 py-1 bg-canvas-subtle rounded border border-border font-mono shrink-0">
                {formatSize(files.find(f => f.path === selectedPath)?.size || 0)}
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
                    <pre className="whitespace-pre-wrap font-mono text-xs text-text-primary leading-relaxed select-text">
                      {selectedContent}
                    </pre>
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
