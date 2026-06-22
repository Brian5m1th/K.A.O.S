import React from "react";
import { Card, CardContent } from "@/shared/ui/card";
import { levelColors, levelBgColors, levelTextColors, levelLabels, HeatmapEntry } from "./heatmap-store";

interface HeatmapChartProps {
  history: HeatmapEntry[];
  selectedDate: string | null;
  onSelectDate: (date: string | null) => void;
}

export function HeatmapChart({ history, selectedDate, onSelectDate }: HeatmapChartProps) {
  if (!history || history.length === 0) {
    return (
      <Card>
        <CardContent className="h-48 flex items-center justify-center text-gray-500">
          No heatmap data available. Run architecture analysis first.
        </CardContent>
      </Card>
    );
  }

  const maxScore = Math.max(...history.map((h) => h.score), 1);
  const cellHeight = 24;
  const cellGap = 2;
  const chartHeight = history.length * (cellHeight + cellGap) + 40;
  const chartWidth = 600;

  return (
    <Card>
      <CardContent>
        <svg width="100%" height={chartHeight} viewBox={`0 0 ${chartWidth} ${chartHeight}`}>
          <text x="0" y="16" fontSize="12" fill="#6b7280">Data</text>
          <text x="100" y="16" fontSize="12" fill="#6b7280">Score</text>
          <text x="280" y="16" fontSize="12" fill="#6b7280">Missing Links</text>
          <text x="390" y="16" fontSize="12" fill="#6b7280">SDD Mismatch</text>
          <text x="500" y="16" fontSize="12" fill="#6b7280">Code Diff</text>

          {history.map((entry, i) => {
            const y = 30 + i * (cellHeight + cellGap);
            const scoreWidth = Math.max(10, (entry.score / maxScore) * 120);
            const isSelected = selectedDate === entry.date;

            return (
              <g
                key={entry.date}
                onClick={() => onSelectDate(isSelected ? null : entry.date)}
                style={{ cursor: "pointer" }}
              >
                <rect
                  x="0"
                  y={y}
                  width={chartWidth}
                  height={cellHeight}
                  fill={isSelected ? "#f3f4f6" : "transparent"}
                  rx="4"
                />
                <text x="5" y={y + 16} fontSize="10" fill="#374151">
                  {entry.date.slice(5)}
                </text>
                <rect
                  x="85"
                  y={y + 4}
                  width={scoreWidth}
                  height={16}
                  fill={levelColors[entry.level] || "#6b7280"}
                  rx="8"
                />
                <text x="92" y={y + 15} fontSize="9" fill="white" fontWeight="bold">
                  {entry.score.toFixed(2)}
                </text>
                <rect
                  x="280"
                  y={y + 6}
                  width={Math.min(entry.missingLinks * 5, 80)}
                  height={12}
                  fill="#f97316"
                  rx="6"
                />
                <text x="285" y={y + 15} fontSize="9" fill="white">{entry.missingLinks}</text>
                <rect
                  x="390"
                  y={y + 6}
                  width={Math.min(entry.sddMismatch * 5, 80)}
                  height={12}
                  fill="#ef4444"
                  rx="6"
                />
                <text x="395" y={y + 15} fontSize="9" fill="white">{entry.sddMismatch}</text>
                <rect
                  x="500"
                  y={y + 6}
                  width={Math.min(entry.codeVsVaultDiff * 5, 80)}
                  height={12}
                  fill="#8b5cf6"
                  rx="6"
                />
                <text x="505" y={y + 15} fontSize="9" fill="white">{entry.codeVsVaultDiff}</text>
              </g>
            );
          })}
        </svg>
      </CardContent>
    </Card>
  );
}

export function DriftIndicator({ level, score }: { level: string; score?: number }) {
  return (
    <span className={`inline-flex items-center gap-1 px-3 py-1 rounded-full text-xs font-medium border ${levelBgColors[level] || "bg-gray-50 border-gray-200"} ${levelTextColors[level] || "text-gray-800"}`}>
      <span className={`w-2 h-2 rounded-full ${levelColors[level] || "bg-gray-500"}`} />
      {levelLabels[level] || level} {score !== undefined ? `(${score.toFixed(2)})` : ""}
    </span>
  );
}

export function ScoreBar({ value, max = 3, label }: { value: number; max?: number; label: string }) {
  const pct = Math.min((value / max) * 100, 100);
  const color = value > 2.5 ? "bg-purple-600" : value > 1.5 ? "bg-red-500" : value > 0.5 ? "bg-yellow-500" : "bg-green-500";
  return (
    <div className="space-y-1">
      <div className="flex justify-between text-xs text-gray-600">
        <span>{label}</span>
        <span>{value.toFixed(2)}</span>
      </div>
      <div className="w-full bg-gray-200 rounded-full h-2.5">
        <div className={`h-2.5 rounded-full ${color}`} style={{ width: `${pct}%` }} />
      </div>
    </div>
  );
}
