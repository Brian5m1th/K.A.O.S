import { Suspense, lazy } from "react";
import { Routes, Route, useLocation, Navigate } from "react-router-dom";
import { AnimatePresence, motion } from "framer-motion";
import { AppLayout } from "@/app/layouts/AppLayout";
import { useAuthStore, useSystemStore } from "@/application";
import { Skeleton } from "@/shared/ui/skeleton";
import { Button } from "@/shared/ui/button";
import { Loader2, ServerCrash, RefreshCw } from "lucide-react";

const DashboardPage = lazy(() => import("@/pages/dashboard"));
const ChatPage = lazy(() => import("@/pages/chat"));
const VaultPage = lazy(() => import("@/pages/vault"));
const SettingsPage = lazy(() => import("@/pages/settings"));
const AgentsPage = lazy(() => import("@/pages/agents"));
const PipelinesPage = lazy(() => import("@/pages/pipelines"));
const ObservabilityPage = lazy(() => import("@/pages/observability"));
const DocumentationPage = lazy(() => import("@/pages/documentation").then(m => ({ default: m.DocumentationPage })));
const ArchitecturePage = lazy(() => import("@/pages/architecture").then(m => ({ default: m.ArchitecturePage })));
const GraphifyPage = lazy(() => import("@/pages/graphify"));
const KnowledgeGraphPage = lazy(() => import("@/pages/knowledge-graph"));
const SetupPage = lazy(() => import("@/pages/setup"));
const LoginPage = lazy(() => import("@/pages/login"));
const UsersPage = lazy(() => import("@/pages/users"));
const ToolsPage = lazy(() => import("@/pages/tools"));
const WelcomePage = lazy(() => import("@/pages/welcome"));
const PromptsPage = lazy(() => import("@/pages/prompts"));
const EventsPage = lazy(() => import("@/pages/events"));
const CostsPage = lazy(() => import("@/pages/costs"));
const AutomationStudioPage = lazy(() => import("@/pages/automation/automation-studio"));
const AutomationMarketplacePage = lazy(() => import("@/pages/automation/marketplace"));

function PageFallback() {
  return (
    <div className="flex h-full items-center justify-center p-8">
      <div className="flex flex-col gap-4 w-full max-w-2xl">
        <Skeleton className="h-6 w-48" />
        <Skeleton className="h-4 w-32" />
        <div className="grid grid-cols-4 gap-3 mt-4">
          {Array.from({ length: 4 }).map((_, i) => (
            <Skeleton key={i} className="h-24 rounded-xl" />
          ))}
        </div>
        <div className="grid grid-cols-2 gap-3 mt-2 flex-1">
          <Skeleton className="h-48 rounded-xl" />
          <Skeleton className="h-48 rounded-xl" />
        </div>
      </div>
    </div>
  );
}

function AnimatedPage({ children }: { children: React.ReactNode }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 6 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -4 }}
      transition={{ type: "spring", stiffness: 380, damping: 35 }}
      className="h-full"
    >
      {children}
    </motion.div>
  );
}

function AuthGate({ children }: { children: React.ReactNode }) {
  const checking = useAuthStore((s) => s.checking);
  const configured = useAuthStore((s) => s.configured);
  const accessToken = useAuthStore((s) => s.accessToken);
  const serverUrl = useAuthStore((s) => s.serverUrl);
  const systemStatus = useSystemStore((s) => s.status);

  if (checking) {
    return (
      <div className="flex h-full items-center justify-center bg-canvas">
        <Loader2 className="h-6 w-6 animate-spin text-text-dim" />
      </div>
    );
  }

  if (!configured) {
    return <Navigate to="/setup" replace />;
  }

  if (!accessToken) {
    return <Navigate to="/login" replace />;
  }

  // Offline gate: block all protected pages when backend is unreachable
  if (systemStatus === "offline") {
    return (
      <div className="flex h-full flex-col items-center justify-center bg-canvas p-8">
        <div className="flex flex-col items-center gap-6 max-w-md text-center">
          <ServerCrash className="h-16 w-16 text-error" />
          <div>
            <h1 className="text-xl font-bold text-text-primary">Servidor K.A.O.S Offline</h1>
            <p className="text-sm text-text-muted mt-2">
              Nao foi possivel conectar ao backend em{" "}
              <code className="rounded bg-surface-raised px-1.5 py-0.5 text-xs font-mono text-accent-primary">
                {serverUrl}
              </code>
            </p>
            <p className="text-xs text-text-dim mt-3">
              Verifique se o backend esta rodando e tente novamente.
            </p>
          </div>
          <Button variant="primary" size="sm" onClick={() => window.location.reload()}>
            <RefreshCw className="h-3.5 w-3.5 mr-1.5" />
            Tentar Novamente
          </Button>
        </div>
      </div>
    );
  }

  return <>{children}</>;
}

import { useAppInit } from "@/shared/lib/use-init";

export function AppRoutes() {
  useAppInit();
  const location = useLocation();

  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        {/* Public routes (no sidebar, no auth) */}
        <Route path="/setup" element={<Suspense fallback={<PageFallback />}><SetupPage /></Suspense>} />
        <Route path="/login" element={<Suspense fallback={<PageFallback />}><LoginPage /></Suspense>} />
        <Route path="/welcome" element={<Suspense fallback={<PageFallback />}><WelcomePage /></Suspense>} />

        {/* Protected routes (sidebar + auth gate) */}
        <Route
          element={
            <AuthGate>
              <AppLayout />
            </AuthGate>
          }
        >
          <Route
            path="/"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><DashboardPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/chat"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><ChatPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/orchestration"
            element={<Navigate to="/automation/studio" replace />}
          />
          <Route
            path="/agents"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><AgentsPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/pipelines"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><PipelinesPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/vault"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><VaultPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/observability"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><ObservabilityPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/settings"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><SettingsPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/tools"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><ToolsPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/users"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><UsersPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/documentation"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><DocumentationPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/architecture"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><ArchitecturePage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/graphify"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><GraphifyPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/knowledge-graph"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><KnowledgeGraphPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/prompts"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><PromptsPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/events"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><EventsPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/costs"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><CostsPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/automation/studio"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><AutomationStudioPage /></AnimatedPage>
              </Suspense>
            }
          />
          <Route
            path="/automation/marketplace"
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><AutomationMarketplacePage /></AnimatedPage>
              </Suspense>
            }
          />
        </Route>
      </Routes>
    </AnimatePresence>
  );
}
