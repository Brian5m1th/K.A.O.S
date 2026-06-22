import { useState } from "react";
import { ChevronDown, ChevronRight, Terminal, CheckCircle2 } from "lucide-react";
import type { ToolCall } from "../types";

interface ToolLoggerProps {
  toolCall: ToolCall;
}

export function ToolLogger({ toolCall }: ToolLoggerProps) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="my-2 border border-border-subtle bg-canvas/50 rounded-lg overflow-hidden">
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="w-full flex items-center justify-between p-2.5 text-xs text-text-muted hover:bg-surface transition-colors"
      >
        <div className="flex items-center gap-2 font-mono">
          <Terminal className="h-3.5 w-3.5 text-accent-neon" />
          <span>Executing tool:</span>
          <span className="text-accent-neon font-semibold">{toolCall.name}</span>
        </div>
        <div className="flex items-center gap-2">
          <CheckCircle2 className="h-3.5 w-3.5 text-success" />
          {isOpen ? <ChevronDown className="h-3.5 w-3.5" /> : <ChevronRight className="h-3.5 w-3.5" />}
        </div>
      </button>

      {isOpen && (
        <div className="p-3 border-t border-border-subtle font-mono text-[11px] bg-canvas text-text-muted flex flex-col gap-2">
          <div>
            <span className="text-text-dim block select-none">// Arguments passed:</span>
            <pre className="overflow-x-auto p-1.5 bg-surface/30 rounded text-warning">{toolCall.arguments}</pre>
          </div>
          <div>
            <span className="text-text-dim block select-none">// Execution Output:</span>
            <pre className="overflow-x-auto p-1.5 bg-surface/30 rounded text-success">{toolCall.output}</pre>
          </div>
        </div>
      )}
    </div>
  );
}
