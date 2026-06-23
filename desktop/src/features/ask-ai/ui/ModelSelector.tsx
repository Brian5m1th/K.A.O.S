import { useState } from "react";
import { Input } from "@/shared/ui/input";
import { Button } from "@/shared/ui/button";

interface ProviderOption {
  id: string;
  name: string;
  models: string[];
}

interface Props {
  currentModel: string;
  defaultModel: string;
  fastModel: string;
  fastMode: boolean;
  providers: ProviderOption[];
  selectedProvider: string;
  onProviderChange: (provider: string) => void;
  onModelChange: (model: string) => void;
  onFastModeToggle: (active: boolean) => void;
}

export function ModelSelector({
  currentModel,
  defaultModel,
  fastModel,
  fastMode,
  providers,
  selectedProvider,
  onProviderChange,
  onModelChange,
  onFastModeToggle,
}: Props) {
  const [custom, setCustom] = useState(false);
  const [customValue, setCustomValue] = useState("");
  const [providerOpen, setProviderOpen] = useState(false);
  const [modelOpen, setModelOpen] = useState(false);

  const currentProvider = providers.find((p) => p.id === selectedProvider);
  const models = currentProvider?.models || [];
  const providerName = currentProvider?.name || selectedProvider;

  const display =
    fastMode && fastModel
      ? `⚡ ${fastModel}`
      : currentModel || defaultModel;

  const handleSelectModel = (model: string) => {
    onModelChange(model);
    setModelOpen(false);
  };

  const handleSelectProvider = (id: string) => {
    onProviderChange(id);
    setProviderOpen(false);
    // Auto-select first model of new provider
    const provider = providers.find((p) => p.id === id);
    if (provider?.models?.length) {
      onModelChange(provider.models[0]);
    }
  };

  const handleCustomConfirm = () => {
    if (customValue.trim()) {
      onModelChange(customValue.trim());
      setCustom(false);
      setCustomValue("");
    }
  };

  // Close dropdowns on blur
  const handleBlur = (type: "provider" | "model") => {
    setTimeout(() => {
      if (type === "provider") setProviderOpen(false);
      else setModelOpen(false);
    }, 200);
  };

  return (
    <div className="flex items-center gap-1.5">
      {/* Provider dropdown */}
      <div className="relative">
        <button
          type="button"
          onClick={() => setProviderOpen(!providerOpen)}
          onBlur={() => handleBlur("provider")}
          className="flex items-center gap-1 rounded-lg border border-zinc-700 bg-zinc-800/50 px-2 py-1.5 text-[11px] text-zinc-300 hover:bg-zinc-700/50 transition-colors"
        >
          {providerName}
          <svg className="h-3 w-3 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>
        {providerOpen && (
          <div className="absolute left-0 top-full z-20 mt-1 w-40 rounded-lg border border-zinc-700 bg-zinc-900 py-1 shadow-xl">
            {providers.map((p) => (
              <button
                key={p.id}
                type="button"
                className={`w-full px-3 py-1.5 text-left text-[11px] transition-colors ${
                  p.id === selectedProvider
                    ? "bg-accent-primary/20 text-accent-primary"
                    : "text-zinc-300 hover:bg-zinc-800"
                }`}
                onMouseDown={() => handleSelectProvider(p.id)}
              >
                {p.name}
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Model dropdown */}
      <div className="relative">
        <button
          type="button"
          onClick={() => setModelOpen(!modelOpen)}
          onBlur={() => handleBlur("model")}
          className="flex items-center gap-1 rounded-lg border border-zinc-700 bg-zinc-800/50 px-2 py-1.5 text-[11px] text-zinc-300 hover:bg-zinc-700/50 transition-colors"
        >
          {display}
          <svg className="h-3 w-3 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
          </svg>
        </button>
        {modelOpen && (
          <div className="absolute left-0 top-full z-20 mt-1 w-52 max-h-60 overflow-y-auto rounded-lg border border-zinc-700 bg-zinc-900 py-1 shadow-xl">
            {models.map((model) => (
              <button
                key={model}
                type="button"
                className={`w-full px-3 py-1.5 text-left text-[11px] transition-colors ${
                  model === (fastMode ? fastModel : currentModel)
                    ? "bg-accent-primary/20 text-accent-primary"
                    : "text-zinc-300 hover:bg-zinc-800"
                }`}
                onMouseDown={() => handleSelectModel(model)}
              >
                {model}
              </button>
            ))}
            {models.length > 0 && <div className="border-t border-zinc-700 my-1" />}
            <button
              type="button"
              className="w-full px-3 py-1.5 text-left text-[11px] text-zinc-500 hover:bg-zinc-800 transition-colors italic"
              onMouseDown={() => {
                setModelOpen(false);
                setCustom(true);
              }}
            >
              Type custom model...
            </button>
          </div>
        )}
      </div>

      {/* D / ⚡ / ✏ shortcuts */}
      <div className="flex gap-0.5">
        <button
          type="button"
          onClick={() => onModelChange(defaultModel)}
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
              onModelChange(fastModel);
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

      {/* Fast Mode toggle */}
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

      {/* Custom model input */}
      {custom && (
        <div className="flex gap-1">
          <Input
            value={customValue}
            onChange={(e) => setCustomValue(e.target.value)}
            placeholder="Type any model name..."
            className="h-7 text-[11px] w-44"
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
            className="h-7 px-2 text-[10px]"
            onClick={handleCustomConfirm}
          >
            OK
          </Button>
        </div>
      )}
    </div>
  );
}
