import { cn } from "@/shared/lib/utils";
import type { Message } from "../types";
import { ToolLogger } from "./ToolLogger";
import { motion } from "framer-motion";

interface Props {
  message: Message;
  isLast?: boolean;
}

export function MessageBubble({ message, isLast }: Props) {
  const isUser = message.role === "user";

  return (
    <motion.div
      initial={{ opacity: 0, y: 8 }}
      animate={{ opacity: 1, y: 0 }}
      className={cn(
        "flex flex-col",
        isUser ? "items-end" : "items-start",
        isLast ? "mb-0" : "mb-3",
      )}
    >
      <div
        className={cn(
          "max-w-[70%] rounded-xl px-4 py-2.5 text-sm leading-relaxed whitespace-pre-wrap",
          isUser
            ? "bg-accent-primary text-white rounded-br-sm"
            : "bg-surface text-text-primary rounded-bl-sm border border-border-subtle",
        )}
      >
        {message.text}
      </div>

      {message.toolCall && <ToolLogger toolCall={message.toolCall} />}

      {message.thinking && (
        <div className="mt-1 flex items-center gap-1.5 text-[11px] text-accent-neon font-mono">
          <span className="h-1.5 w-1.5 rounded-full bg-accent-neon animate-pulse" />
          Thinking...
        </div>
      )}
    </motion.div>
  );
}
