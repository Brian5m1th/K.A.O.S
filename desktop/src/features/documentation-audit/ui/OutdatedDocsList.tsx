import React from "react";
import { Card, CardContent, CardHeader, CardTitle } from "../../../shared/ui/card";
import { Badge } from "../../../shared/ui/badge";
import { Clock, FileText } from "lucide-react";

interface outdated_docsListProps {
  docs: string[];
}

export function OutdatedDocsList({ docs }: outdated_docsListProps) {
  if (!docs || docs.length === 0) {
    return (
      <Card>
        <CardContent className="py-8 text-center">
          <FileText className="w-12 h-12 text-gray-300 mx-auto mb-2" />
          <p className="text-gray-500">No outdated SDDs detected.</p>
        </CardContent>
      </Card>
    );
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <Clock className="w-5 h-5 text-yellow-500" />
          Outdated SDDs ({docs.length})
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="space-y-2 max-h-96 overflow-y-auto">
          {docs.map((doc, index) => (
            <div key={doc} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div className="flex items-center gap-3">
                <span className="text-sm font-mono text-gray-600 bg-gray-200 px-2 py-1 rounded">
                  #{index + 1}
                </span>
                <span className="font-medium text-gray-900">{doc}</span>
              </div>
              <Badge variant="warning" className="text-xs">
                Stale
              </Badge>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
}

