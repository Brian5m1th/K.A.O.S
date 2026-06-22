import React, { useEffect } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { useHeatmapStore, useHeatmapHistory, useCurrentScore, useArchAnalysis, levelColors, levelLabels } from "./heatmap-store";
import { HeatmapChart, DriftIndicator, ScoreBar } from "./heatmap-chart";
import { AlertTriangle, TrendingUp, TrendingDown, Activity, FileText } from "lucide-react";

export function ArchitectureHealth() {
  const { fetchHeatmap, fetchAnalysis, fetchHistory, selectedDate, setSelectedDate } = useHeatmapStore();
  const history = useHeatmapHistory();
  const currentScore = useCurrentScore();
  const analysis = useArchAnalysis();

  useEffect(() => {
    fetchHeatmap();
    fetchAnalysis();
    fetchHistory();
  }, [fetchHeatmap, fetchAnalysis, fetchHistory]);

  return (
    <div className="space-y-4">
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-gray-500">Architecture Health</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-2">
              {currentScore ? (
                <DriftIndicator level={currentScore.level} score={currentScore.score} />
              ) : (
                <span className="text-gray-400 text-sm">No data</span>
              )}
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-gray-500">Coverage Score</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-900">
                {analysis?.coverageScore?.toFixed(1) || "—"}%
              </span>
              {(analysis?.coverageScore || 0) >= 90 ? (
                <TrendingUp className="w-5 h-5 text-green-500" />
              ) : (
                <TrendingDown className="w-5 h-5 text-red-500" />
              )}
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-gray-500">Total Issues</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-2">
              <span className="text-3xl font-bold text-red-600">{analysis?.totalIssues || 0}</span>
              <AlertTriangle className="w-5 h-5 text-red-500" />
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardTitle className="text-sm font-medium text-gray-500">Suggestions</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-2">
              <span className="text-3xl font-bold text-blue-600">{analysis?.suggestions?.length || 0}</span>
              <Activity className="w-5 h-5 text-blue-500" />
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-4">
        <div className="lg:col-span-2">
          <Card>
            <CardHeader>
              <CardTitle>Drift History</CardTitle>
            </CardHeader>
            <CardContent>
              <HeatmapChart history={history} selectedDate={selectedDate} onSelectDate={setSelectedDate} />
            </CardContent>
          </Card>
        </div>

        <div className="space-y-4">
          {currentScore && (
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm">Drift Score Breakdown</CardTitle>
              </CardHeader>
              <CardContent className="space-y-3">
                <ScoreBar value={currentScore.missingLinks} max={30} label="Missing Links" />
                <ScoreBar value={currentScore.sddMismatch} max={30} label="SDD Mismatch" />
                <ScoreBar value={currentScore.codeVsVaultDiff} max={30} label="Code vs Vault" />
              </CardContent>
            </Card>
          )}

          {analysis?.warnings && analysis.warnings.length > 0 && (
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm flex items-center gap-2">
                  <AlertTriangle className="w-4 h-4 text-yellow-500" />
                  Warnings
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-2">
                {analysis.warnings.map((w, i) => (
                  <p key={i} className="text-xs text-gray-600 bg-yellow-50 p-2 rounded">{w}</p>
                ))}
              </CardContent>
            </Card>
          )}

          {analysis?.suggestions && analysis.suggestions.length > 0 && (
            <Card>
              <CardHeader className="pb-2">
                <CardTitle className="text-sm flex items-center gap-2">
                  <FileText className="w-4 h-4 text-blue-500" />
                  Suggestions
                </CardTitle>
              </CardHeader>
              <CardContent className="space-y-2">
                {analysis.suggestions.map((s, i) => (
                  <p key={i} className="text-xs text-gray-600 bg-blue-50 p-2 rounded">{s}</p>
                ))}
              </CardContent>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
}
