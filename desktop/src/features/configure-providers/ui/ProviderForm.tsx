import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Badge } from "@/shared/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import type { ProviderFields, ProviderName } from "@/entities/provider";
import { PROVIDER_LABELS } from "@/entities/provider";

interface Props {
  provider: ProviderName;
  fields: ProviderFields;
  status: string;
  active?: boolean;
  onUpdate: (field: string, value: string) => void;
  onTest: () => void;
}

export function ProviderForm({
  provider,
  fields,
  status,
  active,
  onUpdate,
  onTest,
}: Props) {
  const statusVariant = status === "Connected" ? "success" : status.startsWith("Error") || status === "Connection failed" ? "error" : undefined;

  return (
    <Card className={`mb-3 transition-colors ${active ? "ring-1 ring-emerald-500/50" : "opacity-60"}`}>
      <CardHeader>
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            {active && (
              <span className="h-2 w-2 rounded-full bg-emerald-500" />
            )}
            <CardTitle>{PROVIDER_LABELS[provider]}</CardTitle>
            {active && (
              <Badge variant="success" className="text-[10px]">Active</Badge>
            )}
          </div>
          {status && (
            <Badge variant={statusVariant}>{status}</Badge>
          )}
        </div>
      </CardHeader>
      <CardContent>
        <div className="flex flex-col gap-2">
          <Input
            value={fields.url}
            onChange={(e) => onUpdate("url", e.target.value)}
            placeholder="Server URL"
          />
          {provider !== "ollama" && (
            <Input
              type="password"
              value={fields.apiKey}
              onChange={(e) => onUpdate("apiKey", e.target.value)}
              placeholder="API Key"
            />
          )}
          <Input
            value={fields.model}
            onChange={(e) => onUpdate("model", e.target.value)}
            placeholder="Model name"
          />
          <Input
            value={fields.fastModel}
            onChange={(e) => onUpdate("fastModel", e.target.value)}
            placeholder="Fast Model (optional)"
          />
          <Button
            onClick={onTest}
            variant="secondary"
            size="sm"
            className="self-start"
          >
            Test Connection
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}
