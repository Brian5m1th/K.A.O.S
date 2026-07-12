import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuthStore } from "@/application";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Card, CardContent } from "@/shared/ui/card";
import { Loader2 } from "lucide-react";
import { kaosFetch } from "@/infrastructure";
import { useToast } from "@/shared/components/toast";

export default function LoginPage() {
  const { showToast } = useToast();
  const navigate = useNavigate();
  const login = useAuthStore((s) => s.login);
  const error = useAuthStore((s) => s.error);
  const accessToken = useAuthStore((s) => s.accessToken);
  const serverUrl = useAuthStore((s) => s.serverUrl);
  const setServerUrl = useAuthStore((s) => s.setServerUrl);

  const [mode, setMode] = useState<"login" | "forgot">("login");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  
  // Forgot password states
  const [apiKey, setApiKey] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  
  const [loading, setLoading] = useState(false);
  const [localError, setLocalError] = useState("");
  const [localSuccess, setLocalSuccess] = useState("");
  const [showServerUrl, setShowServerUrl] = useState(false);
  const [urlInput, setUrlInput] = useState(serverUrl);

  useEffect(() => {
    setUrlInput(serverUrl);
  }, [serverUrl]);

  const handleTestConnection = async () => {
    try {
      const cleanUrl = urlInput.replace(/\/+$/, "");
      const res = await fetch(`${cleanUrl}/health`);
      if (res.ok) {
        showToast("Conexão estabelecida com sucesso!", "success");
      } else {
        showToast("Servidor respondeu, mas com status inválido.", "warning");
      }
    } catch (e: any) {
      showToast(`Falha ao conectar: ${e.message || String(e)}`, "error");
    }
  };

  // Redirect when accessToken is populated
  useEffect(() => {
    if (accessToken) {
      navigate("/", { replace: true });
    }
  }, [accessToken, navigate]);

  // If already logged in, do not render login form
  if (accessToken) {
    return null;
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLocalError("");

    if (!email.trim() || !password.trim()) {
      setLocalError("Email and password are required");
      return;
    }

    setLoading(true);
    await setServerUrl(urlInput);
    await login(email, password);
    setLoading(false);

    // If login succeeded, token is set and redirect happens
    if (useAuthStore.getState().accessToken) {
      navigate("/", { replace: true });
    }
  };

  const handleResetPassword = async (e: React.FormEvent) => {
    e.preventDefault();
    setLocalError("");
    setLocalSuccess("");

    if (!email.trim() || !apiKey.trim() || !newPassword.trim()) {
      setLocalError("Email, Master API Key, and new password are required");
      return;
    }

    if (newPassword.length < 8) {
      setLocalError("Password must be at least 8 characters");
      return;
    }

    if (newPassword !== confirmPassword) {
      setLocalError("Passwords do not match");
      return;
    }

    setLoading(true);
    try {
      const response = await kaosFetch("/auth/reset-password", "", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: email.trim(),
          api_key: apiKey.trim(),
          new_password: newPassword,
        }),
      });

      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.detail || "Failed to reset password");
      }

      setLocalSuccess("Senha redefinida com sucesso! Redirecionando para login...");
      setApiKey("");
      setNewPassword("");
      setConfirmPassword("");
      
      setTimeout(() => {
        setMode("login");
        setLocalSuccess("");
      }, 2500);
    } catch (err: any) {
      setLocalError(err.message || "Erro ao tentar redefinir senha");
    } finally {
      setLoading(false);
    }
  };

  if (mode === "forgot") {
    return (
      <div className="flex h-full items-center justify-center bg-canvas p-4">
        <Card className="w-full max-w-sm">
          <CardContent className="p-8">
            <div className="mb-6 text-center">
              <h1 className="text-xl font-bold text-text-primary">Redefinir Senha</h1>
              <p className="mt-1 text-xs text-text-muted leading-relaxed">
                Informe a chave de API mestra do arquivo <code className="bg-canvas-subtle px-1 py-0.5 rounded font-mono text-[10px]">data/api_key.txt</code> do seu projeto para redefinir.
              </p>
            </div>

            <form onSubmit={handleResetPassword} className="space-y-4">
              <div>
                <label className="mb-1 block text-xs font-medium text-text-muted">
                  Email do Administrador
                </label>
                <Input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@example.com"
                  className="text-xs"
                  autoFocus
                />
              </div>

              <div>
                <label className="mb-1 block text-xs font-medium text-text-muted">
                  Master API Key
                </label>
                <Input
                  type="password"
                  value={apiKey}
                  onChange={(e) => setApiKey(e.target.value)}
                  placeholder="Colar api_key.txt aqui"
                  className="text-xs"
                />
              </div>

              <div>
                <label className="mb-1 block text-xs font-medium text-text-muted">
                  Nova Senha
                </label>
                <Input
                  type="password"
                  value={newPassword}
                  onChange={(e) => setNewPassword(e.target.value)}
                  placeholder="Mínimo 8 caracteres"
                  className="text-xs"
                />
              </div>

              <div>
                <label className="mb-1 block text-xs font-medium text-text-muted">
                  Confirmar Nova Senha
                </label>
                <Input
                  type="password"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                  placeholder="Confirmar senha"
                  className="text-xs"
                />
              </div>

              {localError && (
                <p className="text-xs text-error">{localError}</p>
              )}

              {localSuccess && (
                <p className="text-xs text-success font-medium">{localSuccess}</p>
              )}

              <Button
                type="submit"
                variant="primary"
                className="w-full"
                disabled={loading}
              >
                {loading ? (
                  <>
                    <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                    Redefinindo...
                  </>
                ) : (
                  "Redefinir Senha"
                )}
              </Button>
            </form>

            <div className="mt-4 text-center">
              <button
                type="button"
                onClick={() => {
                  setMode("login");
                  setLocalError("");
                  setLocalSuccess("");
                }}
                className="text-xs text-text-muted hover:text-text-primary underline transition-colors"
              >
                Voltar para o Login
              </button>
            </div>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="flex h-full items-center justify-center bg-canvas p-4">
      <Card className="w-full max-w-sm">
        <CardContent className="p-8">
          <div className="mb-6 text-center">
            <h1 className="text-xl font-bold text-text-primary">K.A.O.S</h1>
            <p className="mt-1 text-sm text-text-muted">
              Entre com suas credenciais
            </p>
          </div>

          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="border-b border-border-subtle/50 pb-3 mb-2">
              <button
                type="button"
                onClick={() => setShowServerUrl(!showServerUrl)}
                className="text-xs text-text-muted hover:text-text-primary flex items-center gap-1.5 focus:outline-none"
              >
                <span>⚙️ Configurações do Servidor:</span>
                <span className="font-mono text-[10px] bg-canvas px-1.5 py-0.5 rounded text-accent-primary">
                  {urlInput}
                </span>
              </button>
              
              {showServerUrl && (
                <div className="mt-2.5 p-3 rounded-lg border border-border-subtle bg-canvas space-y-2 animate-in fade-in duration-200">
                  <label className="block text-[10px] font-semibold text-text-muted uppercase tracking-wider">
                    URL do Servidor Backend
                  </label>
                  <div className="flex gap-2">
                    <Input
                      value={urlInput}
                      onChange={(e) => setUrlInput(e.target.value)}
                      placeholder="http://localhost:8000"
                      className="text-xs font-mono"
                    />
                    <Button 
                      type="button" 
                      variant="subtle" 
                      size="sm" 
                      onClick={handleTestConnection}
                      className="text-[11px]"
                    >
                      Testar
                    </Button>
                  </div>
                </div>
              )}
            </div>

            <div>
              <label className="mb-1 block text-xs font-medium text-text-muted">
                Email
              </label>
              <Input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="you@example.com"
                className="text-xs"
                autoFocus
              />
            </div>

            <div>
              <div className="flex justify-between items-center mb-1">
                <label className="block text-xs font-medium text-text-muted">
                  Password
                </label>
                <button
                  type="button"
                  onClick={() => {
                    setMode("forgot");
                    setLocalError("");
                    setLocalSuccess("");
                  }}
                  className="text-[10px] text-text-muted hover:text-text-primary underline transition-colors"
                >
                  Esqueci minha senha
                </button>
              </div>
              <Input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Your password"
                className="text-xs"
              />
            </div>

            {(localError || error) && (
              <p className="text-xs text-error">{localError || error}</p>
            )}

            <Button
              type="submit"
              variant="primary"
              className="w-full"
              disabled={loading}
            >
              {loading ? (
                <>
                  <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                  Entrando...
                </>
              ) : (
                "Entrar"
              )}
            </Button>
          </form>

          <div className="mt-4 text-center">
            <button
              type="button"
              onClick={() => navigate("/setup")}
              className="text-xs text-text-muted hover:text-text-primary underline transition-colors"
            >
              Não possui um workspace? Criar workspace (Cadastro)
            </button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
