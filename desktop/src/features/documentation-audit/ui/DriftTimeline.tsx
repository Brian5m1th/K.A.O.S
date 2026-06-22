import React from "react";
import { Card, CardContent, CardHeader, CardTitle } from "../../../shared/ui/card";
import { Clock, TrendingUp, TrendingDown, Minus } from "lucide-react";

interface DriftTimelineProps {
  history: { date: string; level: string; missing: number }[];
}

const levelConfig = {
  high: { color: "bg-red-100 text-red-800 border-red-200", icon: TrendingUp, label: "High" },
  medium: { color: "bg-yellow-100 text-yellow-800 border-yellow-200", icon: Minus, label: "Medium" },
  low: { color: "bg-green-100 text-green-800 border-green-200", icon: TrendingDown, label: "Low" },
};

export function DriftTimeline({ history }: DriftTimelineProps) {
  if (!history || history.length === 0) {
    return (
      <Card>
        <CardContent className="py-8 text-center">
          <Clock className="w-12 h-12 text-gray-300 mx-auto mb-2" />
          <p className="text-gray-500">No drift history available yet.</p>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Clock className="w-5 h-5 text-blue-500" />
          Drift Timeline
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-3">
          {history.slice().reverse().map((entry, index) => {
            const config = levelConfig[entry.level as keyof typeof levelConfig] || levelConfig.low;
            const Icon = config.icon;
            return (
              <div key={entry.date} className="flex items-center gap-4 p-3 bg-gray-50 rounded-lg">
                <div className="flex-shrink-0 w-10 h-10 rounded-full bg-gray-200 flex items-center justify-center">
                  <Icon className="w-5 h-5 text-gray-600" />
                </div>
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2">
                    <span className="font-medium text-gray-900">
                      {new Date(entry.date).toLocaleString()}
                    </span>
                    <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${config.color}`}>
                      {config.label} Drift
                    </span>
                  </div>
                  <div className="text-sm text-gray-500">
                    {entry.missing} missing features
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </CardContent>
    </Card>
  );
}