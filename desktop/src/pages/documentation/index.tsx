import React, { useEffect, useState, useCallback } from "react";
import { useSearchParams } from "react-router-dom";
import { useSystemStore } from "@/application";
import { useDriftStore } from "../../features/documentation-audit/store/drift-store";
import { DocSyncEngine } from "../../features/documentation-audit/auto-doc/doc-sync-engine";
import { ArchitectureHealth } from "../../features/documentation-audit/heatmap/architecture-health";
import { CoverageChart } from "../../features/documentation-audit/ui/CoverageChart";
import { MissingFeaturesList } from "../../features/documentation-audit/ui/MissingFeaturesList";
import { OutdatedDocsList } from "../../features/documentation-audit/ui/OutdatedDocsList";
import { DriftTimeline } from "../../features/documentation-audit/ui/DriftTimeline";
import { Tabs } from "../../shared/ui/tabs";
import { Card, CardContent, CardHeader, CardTitle } from "../../shared/ui/card";
import { AlertTriangle, RefreshCw, TrendingUp, FileText, Clock, Download, Upload } from "lucide-react";
import { kaosFetch } from "@/infrastructure";

export function DocumentationPage() {
  const { documentation, setDocumentation } = useSystemStore();
  const { driftReport, isLoading, runAudit, loadSnapshot, lastScan } = useDriftStore();
  const [searchParams] = useSearchParams();
  const defaultTab = searchParams.get("tab") || "overview";
  const validTabs = ["overview", "missing", "outdated", "timeline", "health"];
  const [activeTab, setActiveTab] = useState(validTabs.includes(defaultTab) ? defaultTab : "overview");

  useEffect(() => {
    loadSnapshot();
  }, [loadSnapshot]);

  useEffect(() => {
    setDocumentation({
      coverage: driftReport?.coverage || 0,
      driftLevel: driftReport?.driftLevel || "low",
      lastScan: lastScan,
      missingCount: driftReport?.missing_features?.length || 0,
      outdatedCount: driftReport?.outdated_docs?.length || 0,
    });
  }, [driftReport, lastScan, setDocumentation]);

  const handleRunAudit = async () => {
    await runAudit();
  };

  const handleExportArch = useCallback(() => {
    if (!driftReport) return;
    const blob = new Blob([JSON.stringify(driftReport, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `kaos-audit-${Date.now()}.json`;
    a.click();
    URL.revokeObjectURL(url);
  }, [driftReport]);

  const handleSyncVault = useCallback(async () => {
    try {
      await kaosFetch("/api/audit/scan-commits", "", { method: "POST" });
      await runAudit();
    } catch {
    }
  }, [runAudit]);

  const handleGenerateDocs = useCallback(async () => {
    try {
      await DocSyncEngine.runOnce();
      await loadSnapshot();
    } catch {
    }
  }, [loadSnapshot]);

  const getDriftColor = (level: string) => {
    switch (level) {
      case "high": return "bg-error/10 text-error border-error/30";
      case "medium": return "bg-warning/10 text-warning border-warning/30";
      default: return "bg-success/10 text-success border-success/30";
    }
  };

  return (
    <div className="p-6 space-y-6 bg-canvas text-text-primary">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-text-primary">Documentation Health</h1>
          <p className="text-text-muted mt-1">Real-time architectural documentation audit</p>
        </div>
        <div className="flex items-center gap-3">
          <div className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium border ${getDriftColor(documentation.driftLevel)}`}>
            <AlertTriangle className="w-4 h-4 mr-1" />
            Drift: {documentation.driftLevel}
          </div>
          <button
            onClick={handleRunAudit}
            disabled={isLoading}
            className="px-4 py-2 bg-primary text-white rounded-lg hover:bg-primary/90 disabled:opacity-50 flex items-center gap-2"
          >
            <RefreshCw className={`w-4 h-4 ${isLoading ? "animate-spin" : ""}`} />
            {isLoading ? "Scanning..." : "Run Audit"}
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card className="border border-border-subtle bg-surface-raised/40">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Coverage</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-text-primary">{documentation.coverage.toFixed(1)}%</span>
              <TrendingUp className="w-5 h-5 text-success" />
            </div>
          </CardContent>
        </Card>
        <Card className="border border-border-subtle bg-surface-raised/40">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Missing Docs</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-2">
              <span className="text-3xl font-bold text-error">{documentation.missingCount}</span>
              <FileText className="w-5 h-5 text-error" />
            </div>
          </CardContent>
        </Card>
        <Card className="border border-border-subtle bg-surface-raised/40">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Outdated SDDs</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-2">
              <span className="text-3xl font-bold text-warning">{documentation.outdatedCount}</span>
              <Clock className="w-5 h-5 text-warning" />
            </div>
          </CardContent>
        </Card>
        <Card className="border border-border-subtle bg-surface-raised/40">
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-text-muted">Last Scan</CardTitle>
          </CardHeader>
          <CardContent>
            <span className="text-lg font-medium text-text-primary font-mono">
              {documentation.lastScan ? new Date(documentation.lastScan).toLocaleTimeString() : "Never"}
            </span>
          </CardContent>
        </Card>
      </div>

      <div className="mb-4">
          <Tabs
            tabs={[
              { id: "overview", label: "Overview" },
              { id: "missing", label: "Missing Features" },
              { id: "outdated", label: "Outdated SDDs" },
              { id: "timeline", label: "Drift Timeline" },
              { id: "health", label: "Arch Health" },
            ]}
          activeTab={activeTab}
          onTabChange={setActiveTab}
          className="w-full"
        />
      </div>

      {activeTab === "overview" && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
          <Card className="border border-border-subtle bg-surface-raised/40">
            <CardHeader>
              <CardTitle className="text-text-primary">Coverage Trend</CardTitle>
            </CardHeader>
            <CardContent>
              <CoverageChart data={driftReport?.coverageHistory || []} />
            </CardContent>
          </Card>
          <Card className="border border-border-subtle bg-surface-raised/40">
            <CardHeader>
              <CardTitle className="text-text-primary">Quick Actions</CardTitle>
            </CardHeader>
            <CardContent className="space-y-2">
              <button onClick={() => setActiveTab("missing")} className="w-full px-4 py-2 bg-surface hover:bg-surface-hover rounded-lg flex items-center justify-center gap-2 text-left text-text-primary border border-border-subtle transition-colors">
                <FileText className="w-4 h-4 text-text-muted" />
                View Undocumented Features
              </button>
              <button onClick={() => setActiveTab("outdated")} className="w-full px-4 py-2 bg-surface hover:bg-surface-hover rounded-lg flex items-center justify-center gap-2 text-left text-text-primary border border-border-subtle transition-colors">
                <Clock className="w-4 h-4 text-text-muted" />
                View Outdated SDDs
              </button>
              <button onClick={handleGenerateDocs} className="w-full px-4 py-2 bg-surface hover:bg-surface-hover rounded-lg flex items-center justify-center gap-2 text-left text-text-primary border border-border-subtle transition-colors">
                <Upload className="w-4 h-4 text-text-muted" />
                Generate Documentation
              </button>
              <button onClick={handleSyncVault} className="w-full px-4 py-2 bg-surface hover:bg-surface-hover rounded-lg flex items-center justify-center gap-2 text-left text-text-primary border border-border-subtle transition-colors">
                <RefreshCw className="w-4 h-4 text-text-muted" />
                Sync Documentation
              </button>
              <button onClick={handleExportArch} className="w-full px-4 py-2 bg-surface hover:bg-surface-hover rounded-lg flex items-center justify-center gap-2 text-left text-text-primary border border-border-subtle transition-colors">
                <Download className="w-4 h-4 text-text-muted" />
                Export Architecture
              </button>
            </CardContent>
          </Card>
        </div>
      )}

      {activeTab === "missing" && (
        <MissingFeaturesList features={driftReport?.missing_features || []} />
      )}

      {activeTab === "outdated" && (
        <OutdatedDocsList docs={driftReport?.outdated_docs || []} />
      )}

      {activeTab === "timeline" && (
        <DriftTimeline history={driftReport?.driftHistory || []} />
      )}

      {activeTab === "health" && (
        <ArchitectureHealth />
      )}
    </div>
  );
}
