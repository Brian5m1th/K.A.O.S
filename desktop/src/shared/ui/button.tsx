import { forwardRef } from "react";
import { cn } from "@/shared/lib/utils";
import { Loader2 } from "lucide-react";

export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "subtle" | "ghost" | "danger";
  size?: "sm" | "md" | "lg";
  isLoading?: boolean;
}

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      className,
      variant = "primary",
      size = "md",
      isLoading,
      disabled,
      children,
      ...props
    },
    ref,
  ) => {
    return (
      <button
        ref={ref}
        disabled={disabled || isLoading}
        className={cn(
          "inline-flex items-center justify-center rounded-lg font-medium transition-all duration-150",
          "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent-primary focus-visible:ring-offset-2 focus-visible:ring-offset-canvas",
          "disabled:pointer-events-none disabled:opacity-40 select-none",
          "active:scale-[0.98]",
          {
            "bg-accent-primary text-white hover:bg-blue-600 shadow-sm":
              variant === "primary",
            "bg-surface text-text-primary border border-border-subtle hover:bg-bg-active":
              variant === "secondary",
            "bg-transparent text-text-muted hover:bg-bg-active hover:text-text-primary":
              variant === "subtle",
            "bg-transparent text-text-muted hover:text-text-primary":
              variant === "ghost",
            "bg-error/10 text-error border border-error/30 hover:bg-error/20":
              variant === "danger",
          },
          {
            "h-7 px-2.5 text-xs": size === "sm",
            "h-9 px-4 text-sm": size === "md",
            "h-10 px-5 text-base": size === "lg",
          },
          className,
        )}
        {...props}
      >
        {isLoading && (
          <Loader2 className="mr-2 h-4 w-4 animate-spin" />
        )}
        {children}
      </button>
    );
  },
);

Button.displayName = "Button";
