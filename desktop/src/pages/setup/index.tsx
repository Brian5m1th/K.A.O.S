import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuthStore } from "@/application";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Card, CardContent } from "@/shared/ui/card";
import { Loader2 } from "lucide-react";
import { useToast } from "@/shared/components/toast";

export default function SetupPage() {
  const { showToast } = useToast();
  const navigate = useNavigate();
  const register = useAuthStore((s) => s.register);
  const error = useAuthStore((s) => s.error);
  const serverUrl = useAuthStore((s) => s.serverUrl);
  const setServerUrl = useAuthStore((s) => s.setServerUrl);

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirm, setConfirm] = useState("");
  const [loading, setLoading] = useState(false);
  const [localError, setLocalError] = useState("");
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

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLocalError("");

    if (!name.trim() || !email.trim() || !password.trim()) {
      setLocalError("All fields are required");
      return;
    }
    if (password.length < 8) {
      setLocalError("Password must be at least 8 characters");
      return;
    }
    if (password !== confirm) {
      setLocalError("Passwords do not match");
      return;
    }

    setLoading(true);
    await setServerUrl(urlInput);
    await register(name, email, password);
    setLoading(false);

    // If no error, registration succeeded and tokens are stored
    if (!error) {
      navigate("/", { replace: true });
    }
  };

  // If already configured, redirect to login
  const configured = useAuthStore((s) => s.configured);
  if (configured) {
    navigate("/login", { replace: true });
    return null;
  }

  return (
    <div className="flex h-full items-center justify-center bg-canvas p-4">
      <Card className="w-full max-w-md">
        <CardContent className="p-8">
          <div className="mb-6 text-center">
            <h1 className="text-xl font-bold text-text-primary">
              Bem-vindo ao K.A.O.S
            </h1>
            <p className="mt-1 text-sm text-text-muted">
              Configure seu workspace para começar
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
                Name
              </label>
              <Input
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Your name"
                className="text-xs"
                autoFocus
              />
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
              />
            </div>

            <div>
              <label className="mb-1 block text-xs font-medium text-text-muted">
                Password
              </label>
              <Input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Min. 8 characters"
                className="text-xs"
              />
            </div>

            <div>
              <label className="mb-1 block text-xs font-medium text-text-muted">
                Confirm Password
              </label>
              <Input
                type="password"
                value={confirm}
                onChange={(e) => setConfirm(e.target.value)}
                placeholder="Repeat your password"
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
                  Creating workspace...
                </>
              ) : (
                "Criar Workspace"
              )}
            </Button>
          </form>

          <div className="mt-4 text-center">
            <button
              type="button"
              onClick={() => navigate("/login")}
              className="text-xs text-text-muted hover:text-text-primary underline transition-colors"
            >
              Já possui um workspace? Entrar (Login)
            </button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
