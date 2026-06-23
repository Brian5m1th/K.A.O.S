import { Card, CardContent } from "@/shared/ui/card";
import { Button } from "@/shared/ui/button";
import { Badge } from "@/shared/ui/badge";
import { useUpdateStore } from "@/shared/lib/stores";
import { useUpdaterService } from "../hooks/useUpdaterService";
import { Loader2, Download, RotateCcw, AlertCircle } from "lucide-react";

/**
 * Card de atualizacao para a pagina de Configuracoes.
 * Renderizacao condicional por phase.
 *
 * G-05: chamada manual (handleCheck) usa force=true para bypassar cooldown.
 */
export function UpdateCard() {
  const store = useUpdateStore();
  const { checkForUpdates, downloadUpdate, installUpdate } = useUpdaterService();

  const handleCheck = () => {
    // G-05: forcar verificacao manual independente do cooldown
    // A logica esta em useUpdateScheduler, mas aqui usamos checkForUpdates direto
    // que nao tem cooldown (o scheduler que controla isso)
    checkForUpdates();
  };

  return (
    <Card>
      <CardContent className="p-4 space-y-3">
        {/* Versao atual — sempre visivel */}
        <div className="flex items-center justify-between">
          <p className="text-sm font-medium text-text-primary">Vers&atilde;o atual</p>
          <span className="text-xs font-mono text-text-muted">
            {store.currentVersion}
          </span>
        </div>

        {/* Estado idle / sem atualizacao */}
        {(store.phase === "idle" || store.phase === "not-available") && (
          <div className="flex items-center justify-between">
            <p className="text-xs text-text-muted">
              {store.phase === "not-available"
                ? "Voc&ecirc; est&aacute; na vers&atilde;o mais recente"
                : "Nenhuma verifica&ccedil;&atilde;o recente"}
            </p>
            <Button variant="secondary" size="sm" onClick={handleCheck}>
              <RotateCcw className="h-3 w-3 mr-1" /> Verificar
            </Button>
          </div>
        )}

        {/* Verificando */}
        {store.phase === "checking" && (
          <div className="flex items-center gap-2 text-text-muted">
            <Loader2 className="h-4 w-4 animate-spin" />
            <span className="text-xs">Verificando...</span>
          </div>
        )}

        {/* Atualizacao disponivel */}
        {store.phase === "available" && store.update && (
          <div className="space-y-3">
            <div className="flex items-center gap-2">
              <Badge variant="success">
                v{store.update.version} dispon&iacute;vel
              </Badge>
            </div>
            {store.update.body && (
              <pre className="text-xs text-text-muted whitespace-pre-wrap font-sans bg-canvas/50 rounded-lg p-3 border border-border-subtle max-h-40 overflow-y-auto">
                {store.update.body}
              </pre>
            )}
            <Button
              variant="primary"
              size="sm"
              onClick={downloadUpdate}
            >
              <Download className="h-3 w-3 mr-1" /> Baixar Atualiza&ccedil;&atilde;o
            </Button>
          </div>
        )}

        {/* Download em progresso */}
        {store.phase === "downloading" && (
          <div className="space-y-2">
            <div className="flex items-center justify-between text-xs text-text-muted">
              <span>Baixando...</span>
              <span>{store.progress}%</span>
            </div>
            <div className="h-2 rounded-full bg-bg-active overflow-hidden">
              <div
                className="h-full bg-accent-primary transition-all duration-300 rounded-full"
                style={{ width: `${store.progress}%` }}
              />
            </div>
          </div>
        )}

        {/* Pronto para instalar */}
        {store.phase === "ready" && store.update && (
          <div className="space-y-3">
            {store.update.body && (
              <pre className="text-xs text-text-muted whitespace-pre-wrap font-sans bg-canvas/50 rounded-lg p-3 border border-border-subtle max-h-40 overflow-y-auto">
                {store.update.body}
              </pre>
            )}
            <Button
              variant="primary"
              size="sm"
              onClick={installUpdate}
              className="animate-pulse"
            >
              <Loader2 className="h-3 w-3 mr-1" /> Reiniciar e Instalar
            </Button>
          </div>
        )}

        {/* Erro */}
        {store.phase === "error" && (
          <div className="space-y-3">
            <div className="flex items-start gap-2 text-error">
              <AlertCircle className="h-4 w-4 mt-0.5 shrink-0" />
              <p className="text-xs">
                {store.error || "Erro desconhecido"}
              </p>
            </div>
            <Button
              variant="secondary"
              size="sm"
              onClick={handleCheck}
            >
              <RotateCcw className="h-3 w-3 mr-1" /> Tentar Novamente
            </Button>
          </div>
        )}
      </CardContent>
    </Card>
  );
}
