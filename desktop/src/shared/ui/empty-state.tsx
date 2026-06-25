import { ReactNode } from "react";
import { cn } from "@/shared/lib/utils";

interface EmptyStateProps {
  icon: ReactNode;
  title: string;
  description: string | ReactNode;
  action?: ReactNode;
  className?: string;
}

export function EmptyState({
  icon,
  title,
  description,
  action,
  className,
}: EmptyStateProps) {
  return (
    <div
      className={cn(
        "flex flex-col items-center justify-center text-center p-8 rounded-xl border border-border-subtle/50 bg-surface-raised/40 backdrop-blur-sm shadow-sm max-w-md mx-auto my-4",
        className
      )}
    >
      {/* Icon Container */}
      <div className="flex h-12 w-12 items-center justify-center rounded-xl border border-border-subtle bg-surface-elevated text-accent-primary shadow-sm mb-4 ring-8 ring-accent-primary/5">
        <div className="h-6 w-6">{icon}</div>
      </div>

      {/* Typography */}
      <h3 className="text-sm font-semibold text-text-primary tracking-tight mb-1">
        {title}
      </h3>
      <p className="text-xs text-text-muted leading-relaxed mb-5 max-w-xs">
        {description}
      </p>

      {/* Action CTA */}
      {action && <div className="flex items-center justify-center">{action}</div>}
    </div>
  );
}
