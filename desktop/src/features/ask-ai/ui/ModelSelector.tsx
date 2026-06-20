import { useState } from "react";
import { Input } from "@/shared/ui/input";
import { Button } from "@/shared/ui/button";
import { Badge } from "@/shared/ui/badge";

interface Props {
  currentModel: string;
  defaultModel: string;
  fastModel: string;
  fastMode: boolean;
  onModelChange: (model: string) => void;
  onFastModeToggle: (active: boolean) => void;
}

export function ModelSelector({
  currentModel,
  defaultModel,
  fastModel,
  fastMode,
  onModelChange,
  onFastModeToggle,
}: Props) {
  const [custom, setCustom] = useState(false);
  const [customValue, setCustomValue] = useState("");

  const display =
    fastMode && fastModel
      ? `⚡ ${fastModel}`
      : currentModel || defaultModel;

  const handleSelect = (model: string, isCustom?: boolean) => {
    setCustom(!!isCustom);
    if (!isCustom) {
      setCustomValue("");
      onModelChange(model);
    }
  };

  const handleCustomConfirm = () => {
    if (customValue.trim()) {
      onModelChange(customValue.trim());
      setCustom(false);
    }
  };

  return (
    <div className="flex items-center gap-2">
      <div className="relative">
        <div className="flex items-center gap-1.5 rounded-lg border border-zinc-700 bg-zinc-800/50 px-2.5 py-1.5">
          <span className="text-xs text-zinc-300">{display}</span>
          <div className="flex gap-0.5">
            <button
              type="button"
              onClick={() => handleSelect(defaultModel)}
              className={`rounded px-1.5 py-0.5 text-[10px] transition-colors ${
                !custom && currentModel === defaultModel && !fastMode
                  ? "bg-zinc-600 text-zinc-100"
                  : "text-zinc-500 hover:text-zinc-300"
              }`}
              title="Default model"
            >
              D
            </button>
            {fastModel && (
              <button
                type="button"
                onClick={() => {
                  onFastModeToggle(true);
                  handleSelect(fastModel);
                }}
                className={`rounded px-1.5 py-0.5 text-[10px] transition-colors ${
                  fastMode
                    ? "bg-amber-600/30 text-amber-400"
                    : "text-zinc-500 hover:text-zinc-300"
                }`}
                title="Fast model"
              >
                ⚡
              </button>
            )}
            <button
              type="button"
              onClick={() => setCustom(true)}
              className={`rounded px-1.5 py-0.5 text-[10px] transition-colors ${
                custom
                  ? "bg-zinc-600 text-zinc-100"
                  : "text-zinc-500 hover:text-zinc-300"
              }`}
              title="Custom model"
            >
              ✏
            </button>
          </div>
        </div>
        {custom && (
          <div className="absolute left-0 top-full z-10 mt-1 flex w-64 gap-1">
            <Input
              value={customValue}
              onChange={(e) => setCustomValue(e.target.value)}
              placeholder="Type any model name..."
              className="h-8 text-xs"
              onKeyDown={(e) => {
                if (e.key === "Enter") handleCustomConfirm();
                if (e.key === "Escape") {
                  setCustom(false);
                  setCustomValue("");
                }
              }}
              autoFocus
            />
            <Button
              variant="secondary"
              size="sm"
              className="h-8 px-2 text-xs"
              onClick={handleCustomConfirm}
            >
              OK
            </Button>
          </div>
        )}
      </div>

      {fastModel && (
        <button
          type="button"
          onClick={() => {
            onFastModeToggle(!fastMode);
            if (!fastMode) {
              onModelChange(fastModel);
            } else {
              onModelChange(defaultModel);
            }
          }}
          className={`rounded px-2 py-1 text-[10px] font-medium transition-colors ${
            fastMode
              ? "bg-amber-600/20 text-amber-400"
              : "text-zinc-500 hover:text-zinc-300"
          }`}
        >
          Fast Mode {fastMode ? "ON" : "OFF"}
        </button>
      )}
    </div>
  );
}
