import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Card, CardContent, CardHeader, CardTitle, CardDescription, CardFooter } from "@/shared/ui/card";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Badge } from "@/shared/ui/badge";
import { CheckCircle2, ChevronRight, Server, Cpu, Play, Loader2 } from "lucide-react";
import { useAuthStore } from "@/shared/lib/stores";
import { kaosFetch } from "@/shared/api/kaos-client";

export default function WelcomePage() {
  const navigate = useNavigate();
  const serverUrl = useAuthStore((s) => s.serverUrl);

  const [step, setStep] = useState(1);
  const [urlInput, setUrlInput] = useState(serverUrl || "http://localhost:8000");
  const [checking, setChecking] = useState(false);
  const [provider, setProvider] = useState("ollama");
  const [testResult, setTestResult] = useState<string | null>(null);

  const handleNextStep1 = async () => {
    setChecking(true);
    setTestResult(null);
    const targetUrl = urlInput.replace(/\/+$/, "");
    try {
      // Temporarily write target URL to store so kaosFetch uses it
      useAuthStore.setState({ serverUrl: targetUrl });
      
      const res = await kaosFetch("/api/setup/provider/active", "");
      if (res.ok) {
        setStep(2);
      } else {
        throw new Error("O servidor respondeu com status inválido");
      }
    } catch (e: any) {
      alert(`Falha de conexão com o K.A.O.S Backend em "${targetUrl}". Certifique-se de que o backend está rodando.\n\nDetalhes: ${e.message || String(e)}`);
      // Restore previous url
      useAuthStore.setState({ serverUrl });
    } finally {
      setChecking(false);
    }
  };

  const handleNextStep2 = async () => {
    setChecking(true);
    try {
      const res = await kaosFetch("/api/setup/provider/active", "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ provider })
      });
      if (!res.ok) throw new Error("Erro ao definir o provedor ativo");
      setStep(3);
    } catch (e: any) {
      alert(`Não foi possível salvar o provedor no backend:\n${e.message || String(e)}`);
    } finally {
      setChecking(false);
    }
  };

  const handleFinish = () => {
    setChecking(true);
    try {
      useAuthStore.setState({ configured: true });
      setChecking(false);
      navigate("/");
    } catch (e: any) {
      alert(`Erro ao finalizar setup: ${e.message || String(e)}`);
      setChecking(false);
    }
  };

  return (
    <div className="flex h-screen w-screen items-center justify-center bg-canvas p-4 text-text-primary">
      <div className="relative w-full max-w-lg">
        {/* Decorative ambient background glows */}
        <div className="absolute -left-16 -top-16 h-48 w-48 rounded-full bg-accent-primary/10 blur-3xl pointer-events-none" />
        <div className="absolute -right-16 -bottom-16 h-48 w-48 rounded-full bg-accent-neon/10 blur-3xl pointer-events-none" />

        <Card className="border border-border-subtle bg-surface-raised/40 backdrop-blur-md shadow-2xl relative overflow-hidden">
          <div className="h-1.5 w-full bg-gradient-to-r from-accent-primary via-accent-neon to-success" />
          
          <CardHeader className="pt-6">
            <div className="flex items-center gap-2 mb-1">
              <svg className="h-6 w-6 text-accent-primary animate-pulse" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5">
                <path d="M4 4v16h4v-8l6 8h5l-7-9 7-7h-5l-6 8V4H4z" />
              </svg>
              <span className="text-xs font-black tracking-widest text-text-primary uppercase">K.A.O.S</span>
            </div>
            <CardTitle className="text-lg">First Run Onboarding Wizard</CardTitle>
            <CardDescription className="text-xs">
              Configurando seu workspace de agentes em 3 passos simples.
            </CardDescription>

            {/* Stepper indicators */}
            <div className="flex items-center gap-1 mt-4">
              {[1, 2, 3].map((s) => (
                <div
                  key={s}
                  className={`h-1.5 flex-1 rounded-full transition-all duration-300 ${
                    s <= step ? "bg-accent-primary" : "bg-bg-active"
                  }`}
                />
              ))}
            </div>
          </CardHeader>

          <CardContent className="py-4 min-h-[180px]">
            {step === 1 && (
              <div className="space-y-4 animate-in fade-in slide-in-from-bottom-2 duration-200">
                <div className="flex items-start gap-3 rounded-lg border border-border-subtle bg-surface p-3">
                  <Server className="h-5 w-5 text-accent-primary shrink-0 mt-0.5" />
                  <div>
                    <h3 className="text-xs font-semibold text-text-primary">Conectar ao servidor do K.A.O.S</h3>
                    <p className="text-[11px] text-text-muted mt-0.5">
                      Insira o endereço do servidor backend central do K.A.O.S.
                    </p>
                  </div>
                </div>

                <div className="space-y-1.5">
                  <label className="text-xs font-semibold text-text-muted">URL do Servidor</label>
                  <Input
                    value={urlInput}
                    onChange={(e) => setUrlInput(e.target.value)}
                    placeholder="http://localhost:8000"
                    className="text-xs font-mono bg-surface"
                    disabled={checking}
                  />
                </div>
              </div>
            )}

            {step === 2 && (
              <div className="space-y-4 animate-in fade-in slide-in-from-bottom-2 duration-200">
                <div className="flex items-start gap-3 rounded-lg border border-border-subtle bg-surface p-3">
                  <Cpu className="h-5 w-5 text-accent-neon shrink-0 mt-0.5" />
                  <div>
                    <h3 className="text-xs font-semibold text-text-primary">Ativar provedor de IA</h3>
                    <p className="text-[11px] text-text-muted mt-0.5">
                      Escolha o provedor de modelos LLM principal para reasoning dos agentes.
                    </p>
                  </div>
                </div>

                <div className="grid grid-cols-2 gap-2 pt-1">
                  {["ollama", "openai", "claude", "openrouter"].map((prov) => (
                    <button
                      key={prov}
                      onClick={() => setProvider(prov)}
                      className={`px-3 py-2.5 rounded-lg border text-left transition-all ${
                        provider === prov
                          ? "border-accent-neon bg-accent-neon/5"
                          : "border-border-subtle bg-surface hover:bg-surface-hover"
                      }`}
                    >
                      <span className="text-xs font-bold capitalize text-text-primary block">{prov}</span>
                      <span className="text-[10px] text-text-dim block mt-0.5">
                        {prov === "ollama" ? "Modelos Locais" : "Modelos em Nuvem"}
                      </span>
                    </button>
                  ))}
                </div>
              </div>
            )}

            {step === 3 && (
              <div className="space-y-4 animate-in fade-in slide-in-from-bottom-2 duration-200">
                <div className="flex items-start gap-3 rounded-lg border border-border-subtle bg-surface p-3">
                  <CheckCircle2 className="h-5 w-5 text-success shrink-0 mt-0.5" />
                  <div>
                    <h3 className="text-xs font-semibold text-text-primary">Pronto para iniciar!</h3>
                    <p className="text-[11px] text-text-muted mt-0.5">
                      Sua configuração básica está completa. Clique abaixo para rodar um teste.
                    </p>
                  </div>
                </div>

                <div className="flex flex-col gap-2 rounded-lg border border-border-subtle bg-surface p-3">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-semibold text-text-muted">Status do workspace</span>
                    <Badge variant="success">READY</Badge>
                  </div>
                  <p className="text-[10px] text-text-dim mt-1 font-mono">
                    Backend: {serverUrl} <br />
                    Active Provider: {provider.toUpperCase()}
                  </p>
                </div>
              </div>
            )}
          </CardContent>

          <CardFooter className="flex items-center justify-end gap-2 border-t border-border-subtle/50 pt-4">
            {step > 1 && (
              <Button
                variant="subtle"
                size="sm"
                onClick={() => setStep(step - 1)}
                disabled={checking}
              >
                Voltar
              </Button>
            )}
            
            {step < 3 ? (
              <Button
                variant="primary"
                size="sm"
                onClick={step === 1 ? handleNextStep1 : handleNextStep2}
                disabled={checking}
              >
                {checking ? (
                  <Loader2 className="h-3.5 w-3.5 animate-spin mr-1.5" />
                ) : (
                  <ChevronRight className="h-3.5 w-3.5 mr-1.5" />
                )}
                Avançar
              </Button>
            ) : (
              <Button
                variant="primary"
                size="sm"
                onClick={handleFinish}
                disabled={checking}
              >
                {checking ? (
                  <Loader2 className="h-3.5 w-3.5 animate-spin mr-1.5" />
                ) : (
                  <Play className="h-3.5 w-3.5 mr-1.5" />
                )}
                Concluir & Entrar
              </Button>
            )}
          </CardFooter>
        </Card>
      </div>
    </div>
  );
}
