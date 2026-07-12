import { useEffect, useState } from "react";
import { useAuthStore, useUpdateStore } from "@/application";
import { useUpdateCheck } from "@/features/auto-update/hooks/useUpdateCheck";
import { invokeIpc } from "@/infrastructure";
import { DocSyncEngine } from "@/features/documentation-audit/auto-doc/doc-sync-engine";

// ── Bootstrap State Machine (Singleton) ──────────────────────────────────────
type BootstrapStep =
  | "idle"
  | "check_docker_cli"
  | "check_docker_engine"
  | "start_docker_compose"
  | "wait_backend_health"
  | "wait_bootstrap_ready"
  | "done"
  | "error";

interface BootstrapProgress {
  step: BootstrapStep;
  message: string;
  error?: string;
  /** Per-stage timing in ms: { "Backend": 3200, "Auth": 420 } */
  timings?: Record<string, number>;
}

// Estado singleton do bootstrap — so roda uma vez
let _bootstrapStarted = false;
let _currentProgress: BootstrapProgress = { step: "idle", message: "Aguardando inicializacao..." };
let _bootstrapListeners: Array<(p: BootstrapProgress) => void> = [];

function notifyListeners(progress: BootstrapProgress) {
  _currentProgress = progress;
  _bootstrapListeners.forEach((fn) => fn(progress));
}
export function onBootstrapProgress(fn: (p: BootstrapProgress) => void) {
  _bootstrapListeners.push(fn);
  // Envia estado atual para o novo listener
  fn(_currentProgress);
  return () => {
    _bootstrapListeners = _bootstrapListeners.filter((f) => f !== fn);
  };
}
export function getBootstrapProgress(): BootstrapProgress {
  return _currentProgress;
}

const POLL_INTERVAL = 2000;  // 2s entre polls
const MAX_BOOTSTRAP_POLLS = 60;  // 2 min max

async function runBootstrapPipeline(serverUrl: string) {
  if (_bootstrapStarted) return;
  _bootstrapStarted = true;

  const stageTimings: Record<string, number> = {};
  let stageStart = performance.now();

  const progress = (step: BootstrapStep, message: string, error?: string) => {
    const now = performance.now();
    const elapsed = now - stageStart;
    stageTimings[step] = (stageTimings[step] || 0) + elapsed;
    stageStart = now;

    const p: BootstrapProgress = { step, message, error, timings: { ...stageTimings } };
    console.log(`[bootstrap] ${step}: ${message}${error ? ` (${error})` : ""} (${elapsed.toFixed(0)}ms)`);
    notifyListeners(p);
  };

  // 1. Verificar Docker CLI
  progress("check_docker_cli", "Verificando instalacao do Docker...");
  let dockerAvailable = false;
  try {
    const docker = await invokeIpc<{ available: boolean; version?: string }>("check_docker");
    dockerAvailable = docker.available;
    if (docker.available) {
      progress("check_docker_cli", `Docker encontrado: ${docker.version || "disponivel"}`);
    } else {
      progress("check_docker_cli", "Docker CLI nao encontrado. Continuando sem Docker...");
    }
  } catch (e) {
    progress("check_docker_cli", "Falha ao verificar Docker. Continuando sem Docker...", String(e));
  }

  // 2. Verificar Docker Engine (se CLI existe)
  if (dockerAvailable) {
    progress("check_docker_engine", "Verificando se o Docker Engine esta rodando...");
    try {
      const engine = await invokeIpc<{ running: boolean }>("check_docker_engine");
      if (!engine.running) {
        progress("check_docker_engine", "Docker Engine nao esta rodando. Inicie o Docker Desktop.");
      } else {
        progress("check_docker_engine", "Docker Engine operacional.");
      }
    } catch (e) {
      progress("check_docker_engine", "Falha ao verificar Docker Engine.", String(e));
    }
  }

  // 3. Iniciar Docker Compose
  progress("start_docker_compose", "Iniciando servicos do K.A.O.S (Postgres, Qdrant, Ollama)...");
  try {
    await invokeIpc<string>("ensure_docker_services");
    progress("start_docker_compose", "Comando Docker Compose executado com sucesso.");
  } catch (e) {
    progress("start_docker_compose", "Falha ao iniciar servicos Docker.", String(e));
    // Nao critico — o backend pode ja estar rodando
  }

  // 4. Aguardar healthcheck do backend
  progress("wait_backend_health", "Aguardando backend K.A.O.S ficar saudavel...");
  let backendReachable = false;
  for (let i = 0; i < 15; i++) {
    await new Promise((r) => setTimeout(r, 2000));
    try {
      const health = await invokeIpc<{ reachable: boolean; status?: string }>("check_backend_health", { serverUrl });
      if (health.reachable) {
        progress("wait_backend_health", `Backend respondendo: ${health.status || "ok"}`);
        backendReachable = true;
        break;
      }
    } catch {
      // tentar de novo
    }
    if (i % 3 === 0) {
      progress("wait_backend_health", `Aguardando backend (tentativa ${i + 1}/15)...`);
    }
  }

  if (!backendReachable) {
    progress("wait_backend_health", "Backend nao respondeu apos 30s. Sistema ficara offline.", "timeout");
    // Set system store to offline — triggers full-screen offline overlay in AuthGate
    try {
      const { useSystemStore } = await import("@/application/stores/system-store");
      useSystemStore.getState().setStatus("offline");
    } catch {}
    progress("error", "Nao foi possivel conectar ao backend K.A.O.S.");
    return;
  }

  // 4.5. Aguardar readiness check (Postgres + Qdrant)
  progress("wait_backend_health", "Verificando readiness do backend (Postgres, Qdrant)...");
  let readinessOk = false;
  for (let i = 0; i < 10; i++) {
    await new Promise((r) => setTimeout(r, 2000));
    try {
      const r = await fetch(`${serverUrl}/api/system/readiness`);
      if (r.ok) {
        const data = await r.json();
        if (data.ready) {
          progress("wait_backend_health", `Readiness: ${data.message}`);
          readinessOk = true;
          break;
        }
        if (i % 2 === 0) {
          progress("wait_backend_health", `Aguardando readiness: ${data.message} (tentativa ${i + 1}/10)...`);
        }
      }
    } catch {
      // Backend pode ainda estar subindo
    }
  }
  if (!readinessOk) {
    progress("wait_backend_health", "Servicos do backend nao estao prontos. Continuando...", "degraded");
  }

  // 5. Aguardar bootstrap completo
  progress("wait_bootstrap_ready", "Aguardando bootstrap do backend...");
  let bootstrapComplete = false;
  for (let i = 0; i < MAX_BOOTSTRAP_POLLS; i++) {
    await new Promise((r) => setTimeout(r, POLL_INTERVAL));
    try {
      const state = await invokeIpc<{
        is_ready: boolean; degraded: boolean; state: string;
        stages: Array<{ stage: string; success: boolean; error?: string }>;
      }>("get_bootstrap_state", { serverUrl });

      if (state.is_ready) {
        progress("wait_bootstrap_ready", `Bootstrap concluido (${state.degraded ? "degradado" : "saudavel"})`);
        console.log("[bootstrap] Stages:", JSON.stringify(state.stages));
        bootstrapComplete = true;
        break;
      }

      // Atualizar stages atuais
      const stages = state.stages || [];
      const lastStage = stages.length > 0 ? stages[stages.length - 1] : null;
      if (lastStage) {
        progress("wait_bootstrap_ready", `Bootstrap em progresso: ${lastStage.stage}...`);
      }
    } catch {
      // tentar de novo
    }
  }

  if (!bootstrapComplete) {
    progress("wait_bootstrap_ready", "Bootstrap nao concluiu no tempo limite. Continuando...", "timeout");
  }

  progress("done", "Inicializacao completa.");
}

export function useAppInit(): BootstrapProgress {
  const checkSetupStatus = useAuthStore((s) => s.checkSetupStatus);
  const accessToken = useAuthStore((s) => s.accessToken);
  const serverUrl = useAuthStore((s) => s.serverUrl);
  const [bootProgress, setBootProgress] = useState<BootstrapProgress>(getBootstrapProgress);
  useUpdateCheck();

  // Sincroniza com o singleton
  useEffect(() => {
    const unsub = onBootstrapProgress(setBootProgress);
    return unsub;
  }, []);

  useEffect(() => {
    if (accessToken) {
      console.log("[useAppInit] User authenticated, starting DocSyncEngine...");
      DocSyncEngine.start(60000);
    } else {
      console.log("[useAppInit] No user session, stopping DocSyncEngine...");
      DocSyncEngine.stop();
    }
    return () => {
      DocSyncEngine.stop();
    };
  }, [accessToken]);

  useEffect(() => {
    checkSetupStatus();

    // Pipeline de bootstrap (singleton — roda uma vez)
    const run = async () => {
      await runBootstrapPipeline(serverUrl);

      // Buscar versao real do binario
      try {
        const version = await invokeIpc<string>("get_app_version");
        useUpdateStore.getState().setCurrentVersion(version);
        console.log(`[useAppInit] Dynamic version retrieved: ${version}`);
      } catch (e) {
        console.error("[useAppInit] Failed to get real app version:", e);
      }
    };
    void run();
  }, [checkSetupStatus, serverUrl]);

  return bootProgress;
}
