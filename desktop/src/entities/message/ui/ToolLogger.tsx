import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronDown, ChevronRight, Terminal, Loader2, CheckCircle2, XCircle } from "lucide-react";
import type { ToolCall } from "../types";

interface ToolLoggerProps {
  toolCall: ToolCall;
}

type ToolDisplayStatus = "running" | "success" | "error";

export function ToolLogger({ toolCall }: ToolLoggerProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [displayStatus] = useState<ToolDisplayStatus>(
    toolCall.output ? "success" : "running",
  );

  const statusConfig = {
    running: { icon: Loader2, color: "text-accent-neon", bg: "bg-accent-neon/5" },
    success: { icon: CheckCircle2, color: "text-success", bg: "bg-success/5" },
    error: { icon: XCircle, color: "text-error", bg: "bg-error/5" },
  };

  const config = statusConfig[displayStatus];
  const StatusIcon = config.icon;

  return (
    <motion.div
      initial={{ opacity: 0, y: 4 }}
      animate={{ opacity: 1, y: 0 }}
      className="my-2 border border-border-subtle bg-canvas/50 rounded-lg overflow-hidden"
    >
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className={`w-full flex items-center justify-between p-2.5 text-xs transition-colors ${config.bg} hover:bg-surface`}
      >
        <div className="flex items-center gap-2 font-mono">
          <Terminal className="h-3.5 w-3.5 text-accent-neon" />
          <span className="text-text-muted">tool:</span>
          <span className="text-accent-neon font-semibold">{toolCall.name}</span>
        </div>
        <div className="flex items-center gap-2">
          <StatusIcon className={`h-3.5 w-3.5 ${config.color} ${displayStatus === "running" ? "animate-spin" : ""}`} />
          {isOpen ? <ChevronDown className="h-3.5 w-3.5 text-text-dim" /> : <ChevronRight className="h-3.5 w-3.5 text-text-dim" />}
        </div>
      </button>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ type: "spring", stiffness: 380, damping: 35 }}
            className="border-t border-border-subtle overflow-hidden"
          >
            <div className="p-3 font-mono text-[11px] bg-canvas text-text-muted flex flex-col gap-2">
              <div>
                <span className="text-text-dim block select-none mb-1">// arguments</span>
                <pre className="overflow-x-auto p-2 bg-surface/30 rounded text-warning leading-5">
                  {toolCall.arguments}
                </pre>
              </div>
              {toolCall.output && (
                <div>
                  <span className="text-text-dim block select-none mb-1">// output</span>
                  <pre className="overflow-x-auto p-2 bg-surface/30 rounded text-success leading-5">
                    {toolCall.output}
                  </pre>
                </div>
              )}
              {displayStatus === "running" && (
                <div className="flex items-center gap-2 text-accent-neon">
                  <Loader2 className="h-3 w-3 animate-spin" />
                  <span>Executing...</span>
                </div>
              )}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  );
}
