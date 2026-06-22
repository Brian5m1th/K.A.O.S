import React from "react";
import { Card, CardContent, CardHeader, CardTitle } from "../../../shared/ui/card";
import { Badge } from "../../../shared/ui/badge";
import { FileText, AlertTriangle } from "lucide-react";

interface MissingFeaturesListProps {
  features: string[];
}

export function MissingFeaturesList({ features }: MissingFeaturesListProps) {
  if (!features || features.length === 0) {
    return (
      <Card>
        <CardContent className="py-8 text-center">
          <FileText className="w-12 h-12 text-gray-300 mx-auto mb-2" />
          <p className="text-gray-500">No undocumented features detected. Great job!</p>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <AlertTriangle className="w-5 h-5 text-red-500" />
          Undocumented Features ({features.length})
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-2 max-h-96 overflow-y-auto">
          {features.map((feature, index) => (
            <div key={feature} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div className="flex items-center gap-3">
                <span className="text-sm font-mono text-gray-600 bg-gray-200 px-2 py-1 rounded">
                  #{index + 1}
                </span>
                <span className="font-medium text-gray-900">{feature}</span>
              </div>
              <Badge variant="error" className="text-xs">
                Missing SDD
              </Badge>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}