import { useState } from "react";
import { ProviderDropdown } from "./ProviderDropdown";
import { ModelDropdown } from "./ModelDropdown";
import { ModelShortcuts } from "./ModelShortcuts";
import { CustomModelInput } from "./CustomModelInput";

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

  const currentProvider = providers.find((p) => p.id === selectedProvider);
  const models = currentProvider?.models || [];

  const display = fastMode && fastModel ? `⚡ ${fastModel}` : currentModel || defaultModel;

  const handleSelectProvider = (id: string) => {
    onProviderChange(id);
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

  const handleCustomCancel = () => {
    setCustom(false);
    setCustomValue("");
  };

  const handleDefaultModel = () => onModelChange(defaultModel);

  const handleFastMode = () => {
    onFastModeToggle(true);
    onModelChange(fastModel);
  };

  return (
    <div className="flex items-center gap-1.5">
      <ProviderDropdown
        providers={providers}
        selectedProvider={selectedProvider}
        onSelect={handleSelectProvider}
      />

      <ModelDropdown
        models={models}
        selectedModel={fastMode ? fastModel : currentModel}
        display={display}
        onSelect={onModelChange}
        onCustomRequest={() => setCustom(true)}
      />

      <ModelShortcuts
        defaultModel={defaultModel}
        fastModel={fastModel}
        fastMode={fastMode}
        custom={custom}
        currentModel={currentModel}
        onDefaultModel={handleDefaultModel}
        onFastMode={handleFastMode}
        onCustomRequest={() => setCustom(true)}
      />

      {fastModel && (
        <button
          type="button"
          onClick={() => {
            onFastModeToggle(!fastMode);
            onModelChange(fastMode ? defaultModel : fastModel);
          }}
          className={`rounded px-2 py-1 text-[10px] font-medium transition-colors ${
            fastMode ? "bg-amber-600/20 text-amber-400" : "text-zinc-500 hover:text-zinc-300"
          }`}
        >
          Fast Mode {fastMode ? "ON" : "OFF"}
        </button>
      )}

      {custom && (
        <CustomModelInput
          value={customValue}
          onChange={setCustomValue}
          onConfirm={handleCustomConfirm}
          onCancel={handleCustomCancel}
        />
      )}
    </div>
  );
}