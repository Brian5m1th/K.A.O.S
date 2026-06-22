import { cn } from "@/shared/lib/utils";

interface BadgeProps {
  variant?: "success" | "warning" | "error" | "info" | "neutral";
  children: React.ReactNode;
  className?: string;
}

export function Badge({ variant = "neutral", children, className }: BadgeProps) {
  return (
    <span
      className={cn(
        "inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium",
        {
          "bg-success/10 text-success border border-success/30":
            variant === "success",
          "bg-warning/10 text-warning border border-warning/30":
            variant === "warning",
          "bg-error/10 text-error border border-error/30":
            variant === "error",
          "bg-accent-primary/10 text-accent-primary border border-accent-primary/30":
            variant === "info",
          "bg-surface text-text-muted border border-border-subtle":
            variant === "neutral",
        },
        className,
      )}
    >
      <span
        className={cn("mr-1.5 h-1.5 w-1.5 rounded-full", {
          "bg-success": variant === "success",
          "bg-warning": variant === "warning",
          "bg-error": variant === "error",
          "bg-accent-primary": variant === "info",
          "bg-text-dim": variant === "neutral",
        })}
      />
      {children}
    </span>
  );
}
