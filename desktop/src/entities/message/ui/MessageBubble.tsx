import { cn } from "@/shared/lib/utils";
import type { Message } from "../types";

interface Props {
  message: Message;
  isLast?: boolean;
}

export function MessageBubble({ message, isLast }: Props) {
  const isUser = message.role === "user";

  return (
    <div
      className={cn(
        "flex",
        isUser ? "justify-end" : "justify-start",
        isLast ? "mb-0" : "mb-3",
      )}
    >
      <div
        className={cn(
          "max-w-[70%] rounded-xl px-4 py-2.5 text-sm leading-relaxed whitespace-pre-wrap",
          isUser
            ? "bg-accent text-white rounded-br-sm"
            : "bg-zinc-800/80 text-zinc-200 rounded-bl-sm border border-zinc-700/50",
        )}
      >
        {message.text}
      </div>
    </div>
  );
}
