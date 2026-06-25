import { useState } from "react";
import { FileText, BookOpen, StickyNote, X, Loader2, CheckCircle2, ExternalLink } from "lucide-react";
import { kaosFetch } from "@/shared/api/kaos-client";

interface DocGeneratorModalProps {
  sessionId: string;
  userId: string;
  serverUrl: string;
  onClose: () => void;
}

const DOC_TYPES = [
  {
    id: "sdd",
    label: "Especificação Técnica",
    sublabel: "SDD",
    icon: FileText,
    description: "Extrai decisões de arquitetura, diagramas e especificações funcionais da conversa.",
    color: "from-violet-500/20 to-purple-500/10 border-violet-500/30",
    iconColor: "text-violet-400",
  },
  {
    id: "guide",
    label: "Guia de Configuração",
    sublabel: "GUIDE",
    icon: BookOpen,
    description: "Gera um guia passo a passo de instalação e configuração baseado na conversa.",
    color: "from-sky-500/20 to-cyan-500/10 border-sky-500/30",
    iconColor: "text-sky-400",
  },
  {
    id: "general",
    label: "Nota Geral",
    sublabel: "NOTE",
    icon: StickyNote,
    description: "Cria um resumo com os principais pontos e decisões discutidas.",
    color: "from-emerald-500/20 to-teal-500/10 border-emerald-500/30",
    iconColor: "text-emerald-400",
  },
] as const;

type DocTypeId = "sdd" | "guide" | "general";
type Status = "idle" | "loading" | "success" | "error";

export function DocGeneratorModal({ sessionId, userId, serverUrl, onClose }: DocGeneratorModalProps) {
  const [selectedType, setSelectedType] = useState<DocTypeId>("sdd");
  const [title, setTitle] = useState("");
  const [status, setStatus] = useState<Status>("idle");
  const [result, setResult] = useState<{ path: string; title: string } | null>(null);
  const [errorMsg, setErrorMsg] = useState("");

  const handleGenerate = async () => {
    setStatus("loading");
    setErrorMsg("");
    try {
      const res = await kaosFetch(`${serverUrl}/api/docs/generate`, "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          session_id: sessionId,
          user_id: userId,
          document_type: selectedType,
          title: title.trim(),
        }),
      });

      if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: "Falha na requisição" }));
        throw new Error(err.detail || `HTTP ${res.status}`);
      }

      const data = await res.json();
      setResult({ path: data.doc_path, title: data.title });
      setStatus("success");
    } catch (e: any) {
      setErrorMsg(e?.message || "Erro desconhecido");
      setStatus("error");
    }
  };

  return (
    /* Backdrop */
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm"
      onClick={(e) => e.target === e.currentTarget && onClose()}
    >
      {/* Modal panel */}
      <div className="relative w-full max-w-lg mx-4 rounded-2xl border border-border-subtle bg-surface-raised shadow-2xl overflow-hidden animate-in fade-in slide-in-from-bottom-4 duration-200">
        {/* Gradient accent top bar */}
        <div className="h-1 w-full bg-gradient-to-r from-violet-500 via-sky-500 to-emerald-500" />

        {/* Header */}
        <div className="flex items-center justify-between px-6 pt-5 pb-4">
          <div>
            <h2 className="text-base font-semibold text-text-primary">Exportar para Docs</h2>
            <p className="mt-0.5 text-xs text-text-dim">
              Converta essa conversa em documentação técnica com IA.
            </p>
          </div>
          <button
            onClick={onClose}
            className="rounded-lg p-1.5 text-text-dim hover:bg-surface-hover hover:text-text-primary transition-colors"
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        {status === "success" && result ? (
          /* ── Success state ── */
          <div className="flex flex-col items-center gap-4 px-6 py-8 text-center">
            <div className="flex h-14 w-14 items-center justify-center rounded-full bg-emerald-500/10 ring-2 ring-emerald-500/30">
              <CheckCircle2 className="h-7 w-7 text-emerald-400" />
            </div>
            <div>
              <p className="text-sm font-medium text-text-primary">Documentação gerada!</p>
              <p className="mt-1 text-xs text-text-dim">A IA está sintetizando os dados em segundo plano.</p>
            </div>
            <div className="w-full rounded-lg border border-border-subtle bg-surface-elevated px-4 py-3 text-left">
              <p className="text-[11px] text-text-dim">Arquivo</p>
              <p className="mt-0.5 break-all font-mono text-xs text-text-secondary">{result.path}</p>
            </div>
            <div className="flex gap-2 mt-1">
              <button
                onClick={onClose}
                className="rounded-lg border border-border-subtle px-4 py-2 text-xs text-text-secondary hover:bg-surface-hover transition-colors"
              >
                Fechar
              </button>
              <button
                onClick={() => { setStatus("idle"); setResult(null); }}
                className="flex items-center gap-1.5 rounded-lg bg-primary px-4 py-2 text-xs font-medium text-white hover:bg-primary/90 transition-colors"
              >
                <ExternalLink className="h-3 w-3" />
                Gerar outro
              </button>
            </div>
          </div>
        ) : (
          /* ── Form state ── */
          <div className="px-6 pb-6 space-y-5">
            {/* Doc type selector */}
            <div className="space-y-2">
              <label className="text-xs font-medium text-text-secondary">Tipo de documento</label>
              <div className="grid grid-cols-3 gap-2">
                {DOC_TYPES.map((type) => {
                  const Icon = type.icon;
                  const isActive = selectedType === type.id;
                  return (
                    <button
                      key={type.id}
                      onClick={() => setSelectedType(type.id as DocTypeId)}
                      className={`
                        relative flex flex-col items-center gap-2 rounded-xl border p-3 text-center
                        transition-all duration-150
                        ${isActive
                          ? `bg-gradient-to-br ${type.color} shadow-sm scale-[1.02]`
                          : "border-border-subtle bg-surface-elevated hover:bg-surface-hover hover:border-border-default"
                        }
                      `}
                    >
                      <Icon className={`h-5 w-5 ${isActive ? type.iconColor : "text-text-dim"}`} />
                      <div>
                        <p className={`text-[11px] font-semibold leading-tight ${isActive ? "text-text-primary" : "text-text-secondary"}`}>
                          {type.label}
                        </p>
                        <p className={`text-[9px] font-mono ${isActive ? "text-text-dim" : "text-text-dim/60"}`}>
                          {type.sublabel}
                        </p>
                      </div>
                    </button>
                  );
                })}
              </div>
              <p className="text-[11px] text-text-dim px-0.5">
                {DOC_TYPES.find((t) => t.id === selectedType)?.description}
              </p>
            </div>

            {/* Title input */}
            <div className="space-y-1.5">
              <label htmlFor="doc-title" className="text-xs font-medium text-text-secondary">
                Título <span className="text-text-dim font-normal">(opcional)</span>
              </label>
              <input
                id="doc-title"
                type="text"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="Ex: Arquitetura do Sistema de Webhooks"
                className="w-full rounded-lg border border-border-subtle bg-surface-elevated px-3 py-2 text-sm text-text-primary placeholder:text-text-dim focus:border-primary focus:outline-none focus:ring-1 focus:ring-primary/30 transition-colors"
              />
            </div>

            {/* Error msg */}
            {status === "error" && (
              <p className="rounded-lg border border-error/20 bg-error/10 px-3 py-2 text-xs text-error">
                ⚠ {errorMsg}
              </p>
            )}

            {/* Actions */}
            <div className="flex items-center justify-end gap-2 pt-1">
              <button
                onClick={onClose}
                disabled={status === "loading"}
                className="rounded-lg border border-border-subtle px-4 py-2 text-xs text-text-secondary hover:bg-surface-hover transition-colors disabled:opacity-50"
              >
                Cancelar
              </button>
              <button
                id="generate-doc-btn"
                onClick={handleGenerate}
                disabled={status === "loading"}
                className="flex min-w-[120px] items-center justify-center gap-2 rounded-lg bg-gradient-to-r from-violet-600 to-sky-600 px-4 py-2 text-xs font-semibold text-white shadow-md hover:from-violet-500 hover:to-sky-500 transition-all disabled:opacity-60"
              >
                {status === "loading" ? (
                  <>
                    <Loader2 className="h-3.5 w-3.5 animate-spin" />
                    Gerando...
                  </>
                ) : (
                  <>
                    <FileText className="h-3.5 w-3.5" />
                    Gerar Documento
                  </>
                )}
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
