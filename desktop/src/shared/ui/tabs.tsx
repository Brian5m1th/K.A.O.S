import { cn } from "@/shared/lib/utils";
import { motion } from "framer-motion";

interface Tab {
  id: string;
  label: string;
}

interface TabsProps {
  tabs: Tab[];
  activeTab: string;
  onTabChange: (id: string) => void;
  className?: string;
}

export function Tabs({ tabs, activeTab, onTabChange, className }: TabsProps) {
  return (
    <div className={cn("flex gap-1 border-b border-border-subtle", className)}>
      {tabs.map((tab) => (
        <button
          key={tab.id}
          onClick={() => onTabChange(tab.id)}
          className={cn(
            "relative px-4 py-2 text-sm transition-colors",
            activeTab === tab.id
              ? "text-text-primary"
              : "text-text-muted hover:text-text-primary",
          )}
        >
          {tab.label}
          {activeTab === tab.id && (
            <motion.div
              layoutId="tab-indicator"
              className="absolute bottom-0 left-0 right-0 h-0.5 bg-accent-primary rounded-full"
              transition={{ type: "spring", stiffness: 380, damping: 35 }}
            />
          )}
        </button>
      ))}
    </div>
  );
}
