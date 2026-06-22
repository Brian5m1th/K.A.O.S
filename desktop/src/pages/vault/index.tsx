import { useState } from "react";
import { Card } from "@/shared/ui/card";
import { Input } from "@/shared/ui/input";
import { Button } from "@/shared/ui/button";
import { ScrollArea } from "@/shared/ui/scroll-area";
import { BookOpen, FileText, Search, Plus, ChevronRight } from "lucide-react";

interface Note {
  id: string;
  title: string;
  path: string;
  content: string;
}

const MOCK_NOTE: Note = {
  id: "1",
  title: "Architecture Overview",
  path: "docs/architecture.md",
  content: `# K.A.O.S Architecture

## Overview
K.A.O.S is an AI Operating System designed for local-first agent orchestration.

## Core Components
- **Orchestrator**: Workflow engine for agent graphs
- **RAG Pipeline**: Document ingestion and hybrid search
- **Agent System**: Modular AI agents with tool access

## Tech Stack
- Frontend: React + Tauri
- Backend: FastAPI + Python
- Vector Store: Qdrant
- LLM: Ollama (local)

## Data Flow
1. User input → Agent router
2. Agent → Tool selection
3. Tool execution → Context injection
4. LLM response → Stream to UI`,
};

const MOCK_FILES = [
  { name: "docs", type: "folder" as const, children: [
    { name: "architecture.md", type: "file" as const },
    { name: "api-reference.md", type: "file" as const },
    { name: "deployment.md", type: "file" as const },
  ]},
  { name: "agents", type: "folder" as const, children: [
    { name: "memory-agent.md", type: "file" as const },
    { name: "code-reviewer.md", type: "file" as const },
  ]},
  { name: "notes", type: "folder" as const, children: [
    { name: "meeting-notes.md", type: "file" as const },
    { name: "research-logs.md", type: "file" as const },
  ]},
];

export default function VaultPage() {
  const [note] = useState<Note>(MOCK_NOTE);
  const [search, setSearch] = useState("");
  const [editing, setEditing] = useState(false);

  return (
    <div className="flex h-full">
      {/* File Tree */}
      <div className="w-56 shrink-0 border-r border-border-subtle bg-surface flex flex-col">
        <div className="p-3 border-b border-border-subtle">
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs font-semibold text-text-primary uppercase tracking-wider flex items-center gap-1.5">
              <BookOpen className="h-3.5 w-3.5" />
              Vault
            </span>
            <Button variant="ghost" size="sm" className="h-6 px-1">
              <Plus className="h-3.5 w-3.5" />
            </Button>
          </div>
          <div className="relative">
            <Search className="absolute left-2 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-text-dim" />
            <Input
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Search notes..."
              className="h-7 pl-7 text-[11px]"
            />
          </div>
        </div>
        <ScrollArea className="flex-1 p-2">
          {MOCK_FILES.map((folder) => (
            <div key={folder.name}>
              <button className="flex w-full items-center gap-1.5 rounded-md px-2 py-1.5 text-xs text-text-muted hover:bg-bg-active hover:text-text-primary transition-colors">
                <ChevronRight className="h-3 w-3" />
                <FileText className="h-3 w-3" />
                <span>{folder.name}</span>
              </button>
              <div className="ml-3">
                {folder.children.map((file) => (
                  <button
                    key={file.name}
                    className="flex w-full items-center gap-1.5 rounded-md px-2 py-1 text-[11px] text-text-muted hover:bg-bg-active hover:text-text-primary transition-colors"
                  >
                    <FileText className="h-3 w-3" />
                    <span>{file.name}</span>
                  </button>
                ))}
              </div>
            </div>
          ))}
        </ScrollArea>
      </div>

      {/* Editor + Preview */}
      <div className="flex-1 flex flex-col">
        <div className="flex items-center justify-between border-b border-border-subtle px-4 py-2">
          <div className="flex items-center gap-2">
            <span className="text-xs font-medium text-text-primary">{note.title}</span>
            <span className="text-[10px] text-text-dim">{note.path}</span>
          </div>
          <div className="flex gap-2">
            <Button
              variant={editing ? "primary" : "secondary"}
              size="sm"
              onClick={() => setEditing(!editing)}
            >
              {editing ? "Preview" : "Edit"}
            </Button>
          </div>
        </div>

        <ScrollArea className="flex-1">
          {editing ? (
            <textarea
              className="h-full w-full resize-none border-none bg-canvas p-4 font-mono text-sm text-text-primary outline-none"
              defaultValue={note.content}
            />
          ) : (
            <div className="p-4">
              <pre className="font-mono text-sm text-text-primary leading-6 whitespace-pre-wrap">
                {note.content}
              </pre>
            </div>
          )}
        </ScrollArea>
      </div>
    </div>
  );
}
