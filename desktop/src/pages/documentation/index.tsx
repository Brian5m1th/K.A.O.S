import React, { useEffect, useState, useCallback } from "react";
import { useSearchParams } from "react-router-dom";
import { useSystemStore } from "../../shared/lib/stores/system-store";
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
      missingCount: driftReport?.missingFeatures?.length || 0,
      outdatedCount: driftReport?.outdatedDocs?.length || 0,
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
      await fetch("/api/audit/scan-commits", { method: "POST" });
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
      case "high": return "bg-red-100 text-red-800 border-red-200";
      case "medium": return "bg-yellow-100 text-yellow-800 border-yellow-200";
      default: return "bg-green-100 text-green-800 border-green-200";
    }
  };

  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Documentation Health</h1>
          <p className="text-gray-500 mt-1">Real-time architectural documentation audit</p>
        </div>
        <div className="flex items-center gap-3">
          <div className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium border ${getDriftColor(documentation.driftLevel)}`}>
            <AlertTriangle className="w-4 h-4 mr-1" />
            Drift: {documentation.driftLevel}
          </div>
          <button
            onClick={handleRunAudit}
            disabled={isLoading}
            className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 flex items-center gap-2"
          >
            <RefreshCw className={`w-4 h-4 ${isLoading ? "animate-spin" : ""}`} />
            {isLoading ? "Scanning..." : "Run Audit"}
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-gray-500">Coverage</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-900">{documentation.coverage.toFixed(1)}%</span>
              <TrendingUp className="w-5 h-5 text-green-500" />
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-gray-500">Missing Docs</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-2">
              <span className="text-3xl font-bold text-red-600">{documentation.missingCount}</span>
              <FileText className="w-5 h-5 text-red-500" />
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-gray-500">Outdated SDDs</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-2">
              <span className="text-3xl font-bold text-yellow-600">{documentation.outdatedCount}</span>
              <Clock className="w-5 h-5 text-yellow-500" />
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-gray-500">Last Scan</CardTitle>
          </CardHeader>
          <CardContent>
            <span className="text-lg font-medium text-gray-900">
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
          <Card>
            <CardHeader>
              <CardTitle>Coverage Trend</CardTitle>
            </CardHeader>
            <CardContent>
              <CoverageChart data={driftReport?.coverageHistory || []} />
            </CardContent>
          </Card>
          <Card>
            <CardHeader>
              <CardTitle>Quick Actions</CardTitle>
            </CardHeader>
            <CardContent className="space-y-2">
              <button onClick={() => setActiveTab("missing")} className="w-full px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg flex items-center justify-center gap-2 text-left">
                <FileText className="w-4 h-4" />
                View Undocumented Features
              </button>
              <button onClick={() => setActiveTab("outdated")} className="w-full px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg flex items-center justify-center gap-2 text-left">
                <Clock className="w-4 h-4" />
                View Outdated SDDs
              </button>
              <button onClick={handleGenerateDocs} className="w-full px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg flex items-center justify-center gap-2 text-left">
                <Upload className="w-4 h-4" />
                Generate Documentation
              </button>
              <button onClick={handleSyncVault} className="w-full px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg flex items-center justify-center gap-2 text-left">
                <RefreshCw className="w-4 h-4" />
                Sync Documentation
              </button>
              <button onClick={handleExportArch} className="w-full px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg flex items-center justify-center gap-2 text-left">
                <Download className="w-4 h-4" />
                Export Architecture
              </button>
            </CardContent>
          </Card>
        </div>
      )}

      {activeTab === "missing" && (
        <MissingFeaturesList features={driftReport?.missingFeatures || []} />
      )}

      {activeTab === "outdated" && (
        <OutdatedDocsList docs={driftReport?.outdatedDocs || []} />
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