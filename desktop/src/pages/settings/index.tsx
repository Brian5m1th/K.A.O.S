import { useState } from "react";
import { useSettings } from "@/features/manage-settings/hooks/useSettings";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Badge } from "@/shared/ui/badge";

interface Props {
  onClose: () => void;
  onKeyChange: (key: string) => void;
}

export default function SettingsPage({ onClose, onKeyChange }: Props) {
  const { apiKey, setApiKey, handleSave, loading, testStatus, testConnection } =
    useSettings(onClose, onKeyChange);

  const [serverUrl, setServerUrl] = useState("http://localhost:8000");

  const testVariant =
    testStatus === "Connected"
      ? "success"
      : testStatus === "Testing..."
        ? "info"
        : testStatus
          ? "error"
          : undefined;

  return (
    <div className="mx-auto max-w-lg px-6 py-8">
      <div className="mb-6">
        <h2 className="text-lg font-semibold text-zinc-100">Settings</h2>
        <p className="mt-1 text-sm text-zinc-400">
          Configure the API key used to authenticate with the KAOS backend.
        </p>
      </div>

      <label className="mb-1.5 block text-xs font-medium text-zinc-400">
        Backend URL
      </label>
      <Input
        value={serverUrl}
        onChange={(e) => setServerUrl(e.target.value)}
        placeholder="http://localhost:8000"
        className="mb-4 w-full"
      />

      <label className="mb-1.5 block text-xs font-medium text-zinc-400">
        API Key
      </label>
      <div className="flex items-center gap-2">
        <Input
          type="password"
          value={apiKey}
          onChange={(e) => setApiKey(e.target.value)}
          placeholder="Enter KAOS API key"
          className="flex-1"
        />
        <Button
          onClick={() => testConnection(serverUrl)}
          variant="secondary"
          size="sm"
        >
          Test
        </Button>
      </div>
      {testStatus && (
        <div className="mt-2">
          <Badge variant={testVariant}>{testStatus}</Badge>
        </div>
      )}

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
