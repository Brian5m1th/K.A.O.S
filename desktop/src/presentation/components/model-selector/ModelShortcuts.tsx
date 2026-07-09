interface Props {
  defaultModel: string;
  fastModel: string | undefined;
  fastMode: boolean;
  custom: boolean;
  currentModel: string;
  onDefaultModel: () => void;
  onFastMode: () => void;
  onCustomRequest: () => void;
}

export function ModelShortcuts({
  defaultModel,
  fastModel,
  fastMode,
  custom,
  currentModel,
  onDefaultModel,
  onFastMode,
  onCustomRequest,
}: Props) {
  return (
    <div className="flex gap-0.5">
      <button
        type="button"
        onClick={onDefaultModel}
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
          onClick={onFastMode}
          className={`rounded px-1.5 py-0.5 text-[10px] transition-colors ${
            fastMode ? "bg-amber-600/30 text-amber-400" : "text-zinc-500 hover:text-zinc-300"
          }`}
          title="Fast model"
        >
          ⚡
        </button>
      )}
      <button
        type="button"
        onClick={onCustomRequest}
        className={`rounded px-1.5 py-0.5 text-[10px] transition-colors ${
          custom ? "bg-zinc-600 text-zinc-100" : "text-zinc-500 hover:text-zinc-300"
        }`}
        title="Custom model"
      >
        ✏
      </button>
    </div>
  );
}