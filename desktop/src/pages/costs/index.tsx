import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { Coins, Database, TrendingUp, AlertCircle, Sparkles } from "lucide-react";

interface ModelCost {
  model: string;
  provider: string;
  promptTokens: number;
  completionTokens: number;
  totalCostUsd: number;
}

const INITIAL_MODEL_COSTS: ModelCost[] = [
  { model: "qwen3:14b", provider: "ollama (local)", promptTokens: 41250, completionTokens: 18400, totalCostUsd: 0.0000 },
  { model: "llama3.3-70b", provider: "ollama (local)", promptTokens: 12500, completionTokens: 4200, totalCostUsd: 0.0000 },
  { model: "claude-3-5-sonnet", provider: "anthropic", promptTokens: 3800, completionTokens: 1200, totalCostUsd: 0.0234 },
  { model: "gpt-4o-mini", provider: "openai", promptTokens: 9500, completionTokens: 3400, totalCostUsd: 0.0029 },
];

export default function CostsPage() {
  const [costs, setCosts] = useState<ModelCost[]>(INITIAL_MODEL_COSTS);
  const totalCost = costs.reduce((sum, item) => sum + item.totalCostUsd, 0);
  const totalPromptTokens = costs.reduce((sum, item) => sum + item.promptTokens, 0);
  const totalCompletionTokens = costs.reduce((sum, item) => sum + item.completionTokens, 0);

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">AI Cost Center</h1>
          <p className="text-xs text-text-muted mt-0.5">
            Monitoramento de custos e consumo de tokens por modelo e provedor
          </p>
        </div>
        <Button variant="primary" size="sm">
          <Sparkles className="h-3.5 w-3.5 mr-1.5" />
          Optimise Prompts
        </Button>
      </div>

      {/* Summary Row */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
        <Card className="border border-border-subtle bg-surface-raised/40 shadow-md">
          <CardContent className="p-4 flex items-center gap-3">
            <div className="bg-accent-primary/10 p-2.5 rounded-lg text-accent-primary">
              <Coins className="h-5 w-5" />
            </div>
            <div>
              <p className="text-[11px] text-text-dim">Custo Acumulado</p>
              <p className="text-lg font-black text-text-primary font-mono mt-0.5">
                ${totalCost.toFixed(4)} USD
              </p>
            </div>
          </CardContent>
        </Card>

        <Card className="border border-border-subtle bg-surface-raised/40 shadow-md">
          <CardContent className="p-4 flex items-center gap-3">
            <div className="bg-accent-neon/10 p-2.5 rounded-lg text-accent-neon">
              <Database className="h-5 w-5" />
            </div>
            <div>
              <p className="text-[11px] text-text-dim">Tokens de Prompt</p>
              <p className="text-lg font-black text-text-primary font-mono mt-0.5">
                {totalPromptTokens.toLocaleString()}
              </p>
            </div>
          </CardContent>
        </Card>

        <Card className="border border-border-subtle bg-surface-raised/40 shadow-md">
          <CardContent className="p-4 flex items-center gap-3">
            <div className="bg-success/10 p-2.5 rounded-lg text-success">
              <TrendingUp className="h-5 w-5" />
            </div>
            <div>
              <p className="text-[11px] text-text-dim">Tokens de Resposta</p>
              <p className="text-lg font-black text-text-primary font-mono mt-0.5">
                {totalCompletionTokens.toLocaleString()}
              </p>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Model expenditure list */}
      <Card className="flex-1 flex flex-col border border-border-subtle bg-surface-raised/35 overflow-hidden">
        <CardHeader className="pb-2 border-b border-border-subtle">
          <CardTitle className="text-xs font-semibold text-text-muted uppercase tracking-wider">
            Consumo por Modelo
          </CardTitle>
        </CardHeader>
        <CardContent className="p-0 px-4 pb-4 flex-1 overflow-y-auto bg-canvas/20 scrollbar-thin">
          <div className="divide-y divide-border-subtle/50">
            {costs.map((item) => (
              <div key={item.model} className="flex items-center justify-between py-3.5">
                <div>
                  <p className="text-xs font-bold text-text-primary">{item.model}</p>
                  <p className="text-[10px] text-text-dim mt-0.5 font-mono">{item.provider}</p>
                </div>
                <div className="flex items-center gap-4 text-right">
                  <div>
                    <p className="text-[11px] text-text-muted font-mono leading-none">
                      Prompt: {item.promptTokens.toLocaleString()}
                    </p>
                    <p className="text-[11px] text-text-muted font-mono leading-none mt-1">
                      Reply: {item.completionTokens.toLocaleString()}
                    </p>
                  </div>
                  <Badge variant={item.totalCostUsd > 0 ? "warning" : "success"} className="font-mono text-xs">
                    ${item.totalCostUsd.toFixed(4)}
                  </Badge>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
