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
        "h-full w-full overflow-y-auto overflow-x-hidden pr-1",
        className,
      )}
      {...props}
    >
      {children}
    </div>
  );
});

ScrollArea.displayName = "ScrollArea";
