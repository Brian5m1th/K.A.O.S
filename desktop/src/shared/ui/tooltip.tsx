import { useState } from "react";
import { cn } from "@/shared/lib/utils";

interface TooltipProps {
  content: string;
  children: React.ReactNode;
  side?: "top" | "bottom" | "left" | "right";
  className?: string;
}

export function Tooltip({ content, children, side = "top", className }: TooltipProps) {
  const [visible, setVisible] = useState(false);
  let timeout: ReturnType<typeof setTimeout>;

  const show = () => {
    clearTimeout(timeout);
    timeout = setTimeout(() => setVisible(true), 300);
  };

  const hide = () => {
    clearTimeout(timeout);
    setVisible(false);
  };

  const sideClasses = {
    top: "bottom-full left-1/2 -translate-x-1/2 mb-1.5",
    bottom: "top-full left-1/2 -translate-x-1/2 mt-1.5",
    left: "right-full top-1/2 -translate-y-1/2 mr-1.5",
    right: "left-full top-1/2 -translate-y-1/2 ml-1.5",
  };

  return (
    <div className="relative inline-flex" onMouseEnter={show} onMouseLeave={hide}>
      {children}
      {visible && (
        <div
          className={cn(
            "absolute z-50 pointer-events-none",
            sideClasses[side],
            className,
          )}
        >
          <div className="whitespace-nowrap rounded-md bg-surface-elevated px-2 py-1 text-[11px] text-text-primary shadow-lg border border-border-subtle">
            {content}
          </div>
        </div>
      )}
    </div>
  );
}
