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
  onUpdate: (field: string, value: string) => void;
  onTest: () => void;
}

export function ProviderForm({
  provider,
  fields,
  status,
  onUpdate,
  onTest,
}: Props) {
  const statusVariant = status === "Connected" ? "success" : status.startsWith("Error") || status === "Connection failed" ? "error" : undefined;

  return (
    <Card className="mb-3">
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle>{PROVIDER_LABELS[provider]}</CardTitle>
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
