import { useState } from "react";

interface Props {
  models: string[];
  selectedModel: string;
  display: string;
  onSelect: (model: string) => void;
  onCustomRequest: () => void;
}

export function ModelDropdown({ models, selectedModel, display, onSelect, onCustomRequest }: Props) {
  const [open, setOpen] = useState(false);

  const handleBlur = () => {
    setTimeout(() => setOpen(false), 200);
  };

  return (
    <div className="relative">
      <button
        type="button"
        onClick={() => setOpen(!open)}
        onBlur={handleBlur}
        className="flex items-center gap-1 rounded-lg border border-zinc-700 bg-zinc-800/50 px-2 py-1.5 text-[11px] text-zinc-300 hover:bg-zinc-700/50 transition-colors"
      >
        {display}
        <svg className="h-3 w-3 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>
      {open && (
        <div className="absolute left-0 top-full z-20 mt-1 w-52 max-h-60 overflow-y-auto rounded-lg border border-zinc-700 bg-zinc-900 py-1 shadow-xl">
          {models.map((model) => (
            <button
              key={model}
              type="button"
              className={`w-full px-3 py-1.5 text-left text-[11px] transition-colors ${
                model === selectedModel
                  ? "bg-accent-primary/20 text-accent-primary"
                  : "text-zinc-300 hover:bg-zinc-800"
              }`}
              onMouseDown={() => {
                onSelect(model);
                setOpen(false);
              }}
            >
              {model}
            </button>
          ))}
          {models.length > 0 && <div className="border-t border-zinc-700 my-1" />}
          <button
            type="button"
            className="w-full px-3 py-1.5 text-left text-[11px] text-zinc-500 hover:bg-zinc-800 transition-colors italic"
            onMouseDown={() => {
              setOpen(false);
              onCustomRequest();
            }}
          >
            Type custom model...
          </button>
        </div>
      )}
    </div>
  );
}