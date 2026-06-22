import { cn } from "@/shared/lib/utils";

interface StatusDotProps {
  variant: "success" | "warning" | "error" | "info" | "neutral";
  pulse?: boolean;
  className?: string;
}

export function StatusDot({ variant, pulse = false, className }: StatusDotProps) {
  return (
    <span
      className={cn(
        "inline-block h-2 w-2 rounded-full",
        {
          "bg-success": variant === "success",
          "bg-warning": variant === "warning",
          "bg-error": variant === "error",
          "bg-accent-primary": variant === "info",
          "bg-text-dim": variant === "neutral",
        },
        pulse && "animate-pulse",
        className,
      )}
    />
  );
}
