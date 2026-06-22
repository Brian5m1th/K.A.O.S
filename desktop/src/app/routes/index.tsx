import { Suspense } from "react";
import { Routes, Route, useLocation } from "react-router-dom";
import { AnimatePresence, motion } from "framer-motion";
import { AppLayout } from "@/app/layouts/AppLayout";
import { Skeleton } from "@/shared/ui/skeleton";
import DashboardPage from "./pages/dashboard";
import ChatPage from "./pages/chat";
import VaultPage from "./pages/vault";
import SettingsPage from "./pages/settings";
import OrchestrationPage from "./pages/orchestration";
import AgentsPage from "./pages/agents";
import PipelinesPage from "./pages/pipelines";
import ObservabilityPage from "./pages/observability";

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

export function AppRoutes() {
  const location = useLocation();

  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route element={<AppLayout />}>
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
            element={
              <Suspense fallback={<PageFallback />}>
                <AnimatedPage><OrchestrationPage /></AnimatedPage>
              </Suspense>
            }
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
        </Route>
      </Routes>
    </AnimatePresence>
  );
}
