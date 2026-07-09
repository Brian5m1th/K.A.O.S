import { useState } from "react";

interface ProviderOption {
  id: string;
  name: string;
  models: string[];
}

interface Props {
  providers: ProviderOption[];
  selectedProvider: string;
  onSelect: (id: string) => void;
}

export function ProviderDropdown({ providers, selectedProvider, onSelect }: Props) {
  const [open, setOpen] = useState(false);

  const currentName = providers.find((p) => p.id === selectedProvider)?.name || selectedProvider;

  const handleBlur = () => {
    setTimeout(() => setOpen(false), 200);
  };

  const handleSelect = (id: string) => {
    onSelect(id);
    setOpen(false);
  };

  return (
    <div className="relative">
      <button
        type="button"
        onClick={() => setOpen(!open)}
        onBlur={handleBlur}
        className="flex items-center gap-1 rounded-lg border border-zinc-700 bg-zinc-800/50 px-2 py-1.5 text-[11px] text-zinc-300 hover:bg-zinc-700/50 transition-colors"
      >
        {currentName}
        <svg className="h-3 w-3 text-zinc-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>
      {open && (
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
              onMouseDown={() => handleSelect(p.id)}
            >
              {p.name}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}