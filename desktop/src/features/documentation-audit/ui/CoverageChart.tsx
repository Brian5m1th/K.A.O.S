import React from "react";
import { Card, CardContent } from "../../../shared/ui/card";

interface CoverageChartProps {
  data: { date: string; coverage: number }[];
}

export function CoverageChart({ data }: CoverageChartProps) {
  if (!data || data.length === 0) {
    return (
      <Card>
        <CardContent className="h-48 flex items-center justify-center">
          <p className="text-gray-500">No coverage data available. Run an audit to see trends.</p>
        </CardContent>
      </Card>
    );
  }

  const maxCoverage = Math.max(...data.map(d => d.coverage), 100);
  const minCoverage = Math.min(...data.map(d => d.coverage), 0);
  const linePath = data.map((point, i) => {
    const x = (i / (data.length - 1)) * 380 + 10;
    const y = 170 - ((point.coverage - minCoverage) / (maxCoverage - minCoverage || 1)) * 150;
    return `${i === 0 ? "M" : "L"} ${x} ${y}`;
  }).join(" ");
  const areaPath = linePath + ` L${380 + 10} 170 L10 170 Z`;

  return (
    <Card>
      <CardContent className="h-48">
        <svg width="100%" height="100%" viewBox="0 0 400 180" preserveAspectRatio="none">
          <defs>
            <linearGradient id="coverageGradient" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#3b82f6" stopOpacity="0.3" />
              <stop offset="100%" stopColor="#3b82f6" stopOpacity="0" />
            </linearGradient>
          </defs>
          <path
            d={linePath}
            stroke="#3b82f6"
            strokeWidth="2"
            fill="none"
          />
          <path
            d={areaPath}
            fill="url(#coverageGradient)"
          />
          {data.map((point, i) => {
            const x = (i / (data.length - 1)) * 380 + 10;
            const y = 170 - ((point.coverage - minCoverage) / (maxCoverage - minCoverage || 1)) * 150;
            return (
              <circle key={i} cx={x} cy={y} r="4" fill="#3b82f6" />
            );
          })}
        </svg>
      </CardContent>
    </Card>
  );
}