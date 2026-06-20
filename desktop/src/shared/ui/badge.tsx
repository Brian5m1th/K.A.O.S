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
          "bg-emerald-950/50 text-emerald-400 border border-emerald-900/50":
            variant === "success",
          "bg-amber-950/50 text-amber-400 border border-amber-900/50":
            variant === "warning",
          "bg-red-950/50 text-red-400 border border-red-900/50":
            variant === "error",
          "bg-blue-950/50 text-blue-400 border border-blue-900/50":
            variant === "info",
          "bg-zinc-800 text-zinc-400 border border-zinc-700/50":
            variant === "neutral",
        },
        className,
      )}
    >
      <span
        className={cn("mr-1.5 h-1.5 w-1.5 rounded-full", {
          "bg-emerald-400": variant === "success",
          "bg-amber-400": variant === "warning",
          "bg-red-400": variant === "error",
          "bg-blue-400": variant === "info",
          "bg-zinc-400": variant === "neutral",
        })}
      />
      {children}
    </span>
  );
}
