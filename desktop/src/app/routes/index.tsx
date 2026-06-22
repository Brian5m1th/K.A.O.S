import { Suspense } from "react";
import { Routes, Route } from "react-router-dom";
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

export function AppRoutes() {
  return (
    <Routes>
      <Route element={<AppLayout />}>
        <Route
          path="/"
          element={
            <Suspense fallback={<PageFallback />}>
              <DashboardPage />
            </Suspense>
          }
        />
        <Route
          path="/chat"
          element={
            <Suspense fallback={<PageFallback />}>
              <ChatPage />
            </Suspense>
          }
        />
        <Route
          path="/orchestration"
          element={
            <Suspense fallback={<PageFallback />}>
              <OrchestrationPage />
            </Suspense>
          }
        />
        <Route
          path="/agents"
          element={
            <Suspense fallback={<PageFallback />}>
              <AgentsPage />
            </Suspense>
          }
        />
        <Route
          path="/pipelines"
          element={
            <Suspense fallback={<PageFallback />}>
              <PipelinesPage />
            </Suspense>
          }
        />
        <Route
          path="/vault"
          element={
            <Suspense fallback={<PageFallback />}>
              <VaultPage />
            </Suspense>
          }
        />
        <Route
          path="/observability"
          element={
            <Suspense fallback={<PageFallback />}>
              <ObservabilityPage />
            </Suspense>
          }
        />
        <Route
          path="/settings"
          element={
            <Suspense fallback={<PageFallback />}>
              <SettingsPage />
            </Suspense>
          }
        />
      </Route>
    </Routes>
  );
}
