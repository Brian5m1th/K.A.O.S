import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuthStore } from "@/shared/lib/stores";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Card, CardContent } from "@/shared/ui/card";
import { Loader2 } from "lucide-react";
import { kaosFetch } from "@/shared/api/kaos-client";

export default function LoginPage() {
  const navigate = useNavigate();
  const login = useAuthStore((s) => s.login);
  const error = useAuthStore((s) => s.error);
  const accessToken = useAuthStore((s) => s.accessToken);

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

  // If already logged in, redirect to dashboard
  if (accessToken) {
    navigate("/", { replace: true });
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
