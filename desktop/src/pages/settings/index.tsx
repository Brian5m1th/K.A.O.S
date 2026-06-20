import { useSettings } from "@/features/manage-settings/hooks/useSettings";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";

interface Props {
  onClose: () => void;
  onKeyChange: (key: string) => void;
}

export default function SettingsPage({ onClose, onKeyChange }: Props) {
  const { apiKey, setApiKey, handleSave, loading } = useSettings(
    onClose,
    onKeyChange,
  );

  return (
    <div className="mx-auto max-w-lg px-6 py-8">
      <div className="mb-6">
        <h2 className="text-lg font-semibold text-zinc-100">Settings</h2>
        <p className="mt-1 text-sm text-zinc-400">
          Configure the API key used to authenticate with the KAOS backend.
        </p>
      </div>

      <label className="mb-1.5 block text-xs font-medium text-zinc-400">
        API Key
      </label>
      <Input
        type="password"
        value={apiKey}
        onChange={(e) => setApiKey(e.target.value)}
        placeholder="Enter KAOS API key"
        className="w-full"
      />

      <div className="mt-4 flex gap-2">
        <Button onClick={onClose} variant="secondary" size="md" className="flex-1">
          Cancel
        </Button>
        <Button
          onClick={handleSave}
          disabled={loading}
          isLoading={loading}
          variant="primary"
          size="md"
          className="flex-1"
        >
          Save
        </Button>
      </div>
    </div>
  );
}
