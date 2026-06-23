import { BookOpen, FileText, Search } from "lucide-react";

export default function VaultPage() {
  return (
    <div className="flex h-full items-center justify-center">
      <div className="text-center">
        <BookOpen className="h-12 w-12 text-text-dim mx-auto mb-4" />
        <h2 className="text-base font-semibold text-text-primary mb-1">Knowledge Vault</h2>
        <p className="text-xs text-text-muted max-w-xs mx-auto">
          Documentation is served from the <code className="text-accent-primary">docs/</code> submodule.
        </p>
        <p className="text-xs text-text-dim mt-2">
          Vault Explorer coming in a future phase — for now, browse the documentation via the Documentation page or directly in the <code className="text-accent-primary">docs/</code> directory.
        </p>
      </div>
    </div>
  );
}
