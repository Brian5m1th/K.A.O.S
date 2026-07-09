import { useEffect, useState, useCallback } from "react";
import { useNavigate } from "react-router-dom";
import { AnimatePresence, motion } from "framer-motion";
import { useUIStore, useSystemStore, useThemeStore } from "@/application";
import { commandRegistry, type CommandContext } from "@/infrastructure";
import { spring } from "@/shared/lib/motion";
import { Input } from "@/shared/ui/input";
import { Search } from "lucide-react";

export function CommandPalette() {
  const [query, setQuery] = useState("");
  const [selectedIndex, setSelectedIndex] = useState(0);
  const open = useUIStore((s) => s.commandPaletteOpen);
  const setOpen = useUIStore((s) => s.setCommandPaletteOpen);
  const navigate = useNavigate();
  const systemState = useSystemStore.getState();

  const buildContext = useCallback((): CommandContext => ({
    navigate,
    toggleTheme: () => {
      const currentTheme = useThemeStore.getState().mode;
      const nextTheme = currentTheme === "light" ? "dark" : "light";
      useThemeStore.getState().setMode(nextTheme);
    },
    system: systemState,
  }), [navigate, systemState]);

  const filtered = query
    ? commandRegistry.search(query)
    : commandRegistry.getAll();

  const handleKeyDown = useCallback(
    (e: KeyboardEvent) => {
      if (!open) return;

      if (e.key === "Escape") {
        setOpen(false);
        return;
      }

      if (e.key === "ArrowDown") {
        e.preventDefault();
        setSelectedIndex((i) => Math.min(i + 1, filtered.length - 1));
      }

      if (e.key === "ArrowUp") {
        e.preventDefault();
        setSelectedIndex((i) => Math.max(i - 1, 0));
      }

      if (e.key === "Enter" && filtered[selectedIndex]) {
        commandRegistry.execute(filtered[selectedIndex].id, buildContext());
        setOpen(false);
      }
    },
    [open, filtered, selectedIndex, setOpen, buildContext],
  );

  useEffect(() => {
    const listen = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault();
        setOpen(!useUIStore.getState().commandPaletteOpen);
      }
    };
    window.addEventListener("keydown", listen);
    return () => window.removeEventListener("keydown", listen);
  }, [setOpen]);

  useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [handleKeyDown]);

  useEffect(() => {
    if (open) setQuery("");
  }, [open]);

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.15 }}
          className="fixed inset-0 z-50 flex items-start justify-center pt-[15vh]"
        >
          <div
            className="fixed inset-0 bg-overlay backdrop-blur-sm"
            onClick={() => setOpen(false)}
          />
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: -10 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: -10 }}
            transition={spring.palette}
            className="relative w-full max-w-lg rounded-xl border border-border-subtle bg-surface shadow-2xl"
          >
            <div className="flex items-center gap-2 border-b border-border-subtle px-3 py-2">
              <Search className="h-4 w-4 text-text-dim" />
              <Input
                value={query}
                onChange={(e) => {
                  setQuery(e.target.value);
                  setSelectedIndex(0);
                }}
                placeholder="Search commands..."
                className="border-none bg-transparent shadow-none focus-visible:ring-0 h-8"
                autoFocus
              />
            </div>
            <div className="max-h-64 overflow-y-auto p-2">
              {filtered.map((cmd, i) => {
                const Icon = cmd.icon;
                return (
                  <button
                    key={cmd.id}
                    onClick={() => {
                      cmd.action(buildContext());
                      setOpen(false);
                    }}
                    className={`flex w-full items-center gap-2 rounded-md px-3 py-2 text-left text-sm transition-colors ${
                      i === selectedIndex
                        ? "bg-bg-active text-text-primary"
                        : "text-text-muted hover:bg-bg-active/50 hover:text-text-primary"
                    }`}
                  >
                    <Icon className="h-4 w-4" />
                    <span>{cmd.label}</span>
                    <span className="ml-auto text-[10px] uppercase text-text-dim">
                      {cmd.category}
                    </span>
                  </button>
                );
              })}
              {filtered.length === 0 && (
                <p className="py-4 text-center text-sm text-text-dim">
                  No commands found
                </p>
              )}
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
