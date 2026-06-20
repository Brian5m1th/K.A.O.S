import { forwardRef } from "react";
import { cn } from "@/shared/lib/utils";

export interface TextareaProps
  extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {}

export const Textarea = forwardRef<HTMLTextAreaElement, TextareaProps>(
  ({ className, ...props }, ref) => {
    return (
      <textarea
        ref={ref}
        className={cn(
          "flex min-h-[80px] w-full rounded-md border border-zinc-800 bg-zinc-950 px-3 py-2 text-sm text-zinc-100 shadow-inner transition-colors",
          "placeholder:text-zinc-500",
          "focus-visible:outline-none focus-visible:border-zinc-700 focus-visible:ring-1 focus-visible:ring-zinc-800",
          "disabled:cursor-not-allowed disabled:opacity-50",
          "resize-none",
          className,
        )}
        {...props}
      />
    );
  },
);

Textarea.displayName = "Textarea";
