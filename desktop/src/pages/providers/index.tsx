import { useProviderConfig } from "@/features/configure-providers/hooks/useProviderConfig";
import { ProviderForm } from "@/features/configure-providers/ui/ProviderForm";
import { Button } from "@/shared/ui/button";
import { PROVIDER_ORDER } from "@/entities/provider";
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
  const { config, statuses, saving, updateField, handleTest, handleSave } =
    useProviderConfig(onDone);

  return (
    <div className="mx-auto max-w-2xl px-6 py-8">
      <div className="mb-6">
        <h2 className="text-lg font-semibold text-zinc-100">
          Provider Configuration
        </h2>
        <p className="mt-1 text-sm text-zinc-400">
          Configure all LLM providers. API keys are stored locally and sent to
          the KAOS backend.
        </p>
      </div>

      {PROVIDER_ORDER.map((provider) => (
        <ProviderForm
          key={provider}
          provider={provider as ProviderName}
          fields={config[provider]}
          status={statuses[provider] || ""}
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
