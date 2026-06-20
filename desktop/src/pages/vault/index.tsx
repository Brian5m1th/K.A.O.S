import { useVaultInit } from "@/features/index-vault/hooks/useVaultInit";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";

interface Props {
  onDone: (path: string) => void;
  initialPath: string;
  serverUrl: string;
  apiKey: string;
}

export default function VaultPage({
  onDone,
  initialPath,
  serverUrl,
  apiKey,
}: Props) {
  const { path, status, setPath, handleInit, loading } = useVaultInit(
    initialPath,
    serverUrl,
    apiKey,
    onDone,
  );

  return (
    <div className="mx-auto max-w-lg px-6 py-8">
      <div className="mb-6">
        <h2 className="text-lg font-semibold text-zinc-100">
          Obsidian Vault
        </h2>
        <p className="mt-1 text-sm text-zinc-400">
          Point to your Obsidian vault folder. KAOS will create its folder
          structure there.
        </p>
      </div>

      <Input
        value={path}
        onChange={(e) => setPath(e.target.value)}
        placeholder="C:\Users\...\Obsidian\Vault"
        className="w-full"
      />

      <Button
        onClick={handleInit}
        disabled={!path || loading}
        isLoading={loading}
        variant="primary"
        size="lg"
        className="mt-3 w-full"
      >
        {loading ? "Initializing..." : "Initialize & Enter"}
      </Button>

      {status && (
        <p
          className={`mt-2 text-center text-sm ${
            status.startsWith("Error") ? "text-error" : "text-success"
          }`}
        >
          {status}
        </p>
      )}
    </div>
  );
}
