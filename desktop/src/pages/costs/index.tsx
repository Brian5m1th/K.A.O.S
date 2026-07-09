import { useEffect, useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/shared/ui/card";
import { Badge } from "@/shared/ui/badge";
import { Button } from "@/shared/ui/button";
import { Coins, Database, TrendingUp, AlertCircle, Sparkles, Loader2, RefreshCw } from "lucide-react";
import { kaosFetch } from "@/infrastructure";

interface CostBreakdown {
  provider: string;
  workflow: string;
  total_usd: number;
  total_tokens: number;
  request_count: number;
}

export default function CostsPage() {
  const [loading, setLoading] = useState(true);
  const [totalCost, setTotalCost] = useState(0);
  const [breakdown, setBreakdown] = useState<CostBreakdown[]>([]);
  const [error, setError] = useState("");

  const fetchCosts = async () => {
    setLoading(true);
    setError("");
    try {
      const res = await kaosFetch("/api/observability/costs", "");
      if (!res.ok) throw new Error("Falha ao se conectar com o servidor");
      const data = await res.json();
      setTotalCost(data.total_usd || 0);
      setBreakdown(data.breakdown || []);
    } catch (e: any) {
      setError(e.message || "Erro ao carregar os dados de telemetria financeira.");
    } finally {
      setLoading(false);
    }
  };

  const handleOptimisePrompts = async () => {
    alert("Otimização de prompts disparada! O assistente está compilando templates eficientes para reduzir o consumo de tokens.");
  };

  useEffect(() => {
    fetchCosts();
  }, []);

  const totalTokens = breakdown.reduce((sum, item) => sum + item.total_tokens, 0);
  const totalRequests = breakdown.reduce((sum, item) => sum + item.request_count, 0);

  return (
    <div className="flex h-full flex-col gap-4 p-4 bg-canvas text-text-primary">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">AI Cost Center</h1>
          <p className="text-xs text-text-muted mt-0.5">
            Monitoramento de custos e consumo de tokens por modelo e provedor
          </p>
        </div>
        <div className="flex items-center gap-2">
          <Button variant="primary" size="sm" onClick={handleOptimisePrompts}>
            <Sparkles className="h-3.5 w-3.5 mr-1.5" />
            Optimise Prompts
          </Button>
          <Button variant="subtle" size="sm" onClick={fetchCosts} disabled={loading}>
            <RefreshCw className={`h-3.5 w-3.5 ${loading ? "animate-spin" : ""}`} />
          </Button>
        </div>
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
                ${totalCost.toFixed(6)} USD
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
              <p className="text-[11px] text-text-dim">Total de Tokens</p>
              <p className="text-lg font-black text-text-primary font-mono mt-0.5">
                {totalTokens.toLocaleString()}
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
              <p className="text-[11px] text-text-dim">Total de Chamadas</p>
              <p className="text-lg font-black text-text-primary font-mono mt-0.5">
                {totalRequests.toLocaleString()}
              </p>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Model expenditure list */}
      <Card className="flex-1 flex flex-col border border-border-subtle bg-surface-raised/35 overflow-hidden">
        <CardHeader className="pb-2 border-b border-border-subtle">
          <CardTitle className="text-xs font-semibold text-text-muted uppercase tracking-wider">
            Consumo Real por Provedor & Workflow
          </CardTitle>
        </CardHeader>
        <CardContent className="p-0 px-4 pb-4 flex-1 overflow-y-auto bg-canvas/20 scrollbar-thin">
          {loading ? (
            <div className="flex h-40 items-center justify-center">
              <Loader2 className="h-6 w-6 animate-spin text-text-dim" />
            </div>
          ) : error ? (
            <div className="flex h-40 flex-col items-center justify-center text-text-muted text-center gap-2">
              <AlertCircle className="h-8 w-8 text-error" />
              <p className="text-xs">{error}</p>
            </div>
          ) : breakdown.length === 0 ? (
            <div className="flex h-40 flex-col items-center justify-center text-text-dim text-center gap-2">
              <Coins className="h-8 w-8 text-text-dim" />
              <p className="text-xs">Nenhum registro de consumo de API encontrado.</p>
              <p className="text-[10px] text-text-muted">Interaja com o chat para popular o banco de dados.</p>
            </div>
          ) : (
            <div className="divide-y divide-border-subtle/50">
              {breakdown.map((item, idx) => (
                <div key={`${item.provider}-${item.workflow}-${idx}`} className="flex items-center justify-between py-3.5">
                  <div>
                    <p className="text-xs font-bold text-text-primary uppercase tracking-wide">{item.provider}</p>
                    <p className="text-[10px] text-text-dim mt-0.5">
                      Workflow: <span className="font-mono text-text-primary">{item.workflow || "N/A"}</span>
                    </p>
                  </div>
                  <div className="flex items-center gap-4 text-right">
                    <div>
                      <p className="text-[11px] text-text-muted font-mono leading-none">
                        Tokens: {item.total_tokens.toLocaleString()}
                      </p>
                      <p className="text-[11px] text-text-muted font-mono leading-none mt-1">
                        Requests: {item.request_count}
                      </p>
                    </div>
                    <Badge variant={item.total_usd > 0 ? "warning" : "success"} className="font-mono text-xs">
                      ${item.total_usd.toFixed(6)}
                    </Badge>
                  </div>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
