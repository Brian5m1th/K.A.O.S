import { useProviderConfig } from "@/features/configure-providers/hooks/useProviderConfig";
import { ProviderForm } from "@/features/configure-providers/ui/ProviderForm";
import { Button } from "@/shared/ui/button";
import { PROVIDER_ORDER, PROVIDER_LABELS } from "@/entities/provider";
import type { ProviderName } from "@/entities/provider";

interface Props {
  onDone: () => void;
  serverUrl?: string;
  apiKey?: string;
}

export default function ProvidersPage({
  onDone,
  serverUrl = "http://localhost:8000",
  apiKey = "",
}: Props) {
  const {
    config,
    activeProvider,
    statuses,
    saving,
    updateField,
    setActiveProvider,
    handleTest,
    handleSave,
  } = useProviderConfig(onDone);

  return (
    <div className="mx-auto max-w-2xl px-6 py-8">
      <div className="mb-6">
        <h2 className="text-lg font-semibold text-zinc-100">
          Provider Configuration
        </h2>
        <p className="mt-1 text-sm text-zinc-400">
          Select which provider is active and configure their credentials.
        </p>
      </div>

      <div className="mb-6 rounded-lg border border-zinc-700 bg-zinc-800/50 p-4">
        <h3 className="mb-3 text-sm font-medium text-zinc-300">
          Active Provider
        </h3>
        <div className="flex flex-wrap gap-3">
          {PROVIDER_ORDER.map((provider) => (
            <button
              key={provider}
              type="button"
              onClick={() => setActiveProvider(provider as ProviderName)}
              className={`flex items-center gap-2 rounded-lg border px-4 py-2.5 text-sm transition-colors ${
                activeProvider === provider
                  ? "border-emerald-500 bg-emerald-500/10 text-emerald-400"
                  : "border-zinc-600 bg-zinc-800 text-zinc-400 hover:border-zinc-500 hover:text-zinc-300"
              }`}
            >
              <span
                className={`h-2 w-2 rounded-full ${
                  activeProvider === provider
                    ? "bg-emerald-500"
                    : "bg-zinc-600"
                }`}
              />
              {PROVIDER_LABELS[provider as ProviderName]}
            </button>
          ))}
        </div>
      </div>

      {PROVIDER_ORDER.map((provider) => (
        <ProviderForm
          key={provider}
          provider={provider as ProviderName}
          fields={config[provider]}
          status={statuses[provider] || ""}
          active={activeProvider === provider}
          onUpdate={(field, value) =>
            updateField(provider as ProviderName, field, value)
          }
          onTest={() => handleTest(provider as ProviderName)}
        />
      ))}

      <Button
        onClick={() => handleSave(serverUrl, apiKey)}
        disabled={saving}
        isLoading={saving}
        variant="primary"
        size="lg"
        className="mt-2 w-full"
      >
        {saving ? "Saving..." : "Continue"}
      </Button>
    </div>
  );
}
