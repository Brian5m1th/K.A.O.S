import { forwardRef } from "react";
import { cn } from "@/shared/lib/utils";

export const ScrollArea = forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, children, ...props }, ref) => {
  return (
    <div
      ref={ref}
      className={cn(
        "h-full w-full overflow-y-auto overflow-x-hidden",
        "scrollbar-thin scrollbar-thumb-zinc-800 scrollbar-track-transparent",
        "hover:scrollbar-thumb-zinc-700 transition-colors",
        "pr-1",
        className,
      )}
      {...props}
    >
      {children}
    </div>
  );
});

ScrollArea.displayName = "ScrollArea";
