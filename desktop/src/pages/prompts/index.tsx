import { useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/shared/ui/card";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Badge } from "@/shared/ui/badge";
import { BookOpen, Copy, Check, Search, Plus, Terminal, Edit3 } from "lucide-react";

interface PromptItem {
  id: string;
  title: string;
  category: "coding" | "writing" | "ux" | "system";
  prompt: string;
  description: string;
}

const INITIAL_PROMPTS: PromptItem[] = [
  {
    id: "1",
    title: "Code Reviewer Pro",
    category: "coding",
    description: "Revisa código procurando por bugs, gargalos de performance e riscos de segurança.",
    prompt: "Aja como um engenheiro de software sênior. Revise as alterações de código a seguir analisando: complexidade ciclomática, vazamentos de memória e conformidade com clean code.",
  },
  {
    id: "2",
    title: "Technical Spec Writer (SDD)",
    category: "writing",
    description: "Estrutura discussões e ideias em documentos formais de SDD (Software Design Document).",
    prompt: "Escreva um Software Design Document (SDD) estruturado baseado no seguinte backlog de decisões técnicas. Inclua seções de Objetivo, Requisitos Funcionais, Arquitetura Proposta e Plano de Verificação.",
  },
  {
    id: "3",
    title: "Tailwind UI Designer",
    category: "ux",
    description: "Gera layouts em Tailwind CSS elegantes, responsivos e acessíveis com foco em dark mode.",
    prompt: "Escreva código HTML/JSX com classes utilitárias do Tailwind CSS que crie um componente interativo moderno, utilizando cores frias e efeitos de blur de fundo (glassmorphism).",
  },
  {
    id: "4",
    title: "Commit Message Formatter",
    category: "system",
    description: "Gera mensagens de commit seguindo a especificação de Conventional Commits.",
    prompt: "Com base nas alterações de código fornecidas, gere uma mensagem de commit curta e sem ambiguidades no formato Conventional Commits (ex: feat(ui): add collapse button).",
  },
];

export default function PromptsPage() {
  const [prompts, setPrompts] = useState<PromptItem[]>(INITIAL_PROMPTS);
  const [search, setSearch] = useState("");
  const [selectedCategory, setSelectedCategory] = useState<string>("all");
  const [copiedId, setCopiedId] = useState<string | null>(null);

  const handleCopy = (id: string, text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const filteredPrompts = prompts.filter((p) => {
    const matchesSearch =
      p.title.toLowerCase().includes(search.toLowerCase()) ||
      p.description.toLowerCase().includes(search.toLowerCase());
    const matchesCategory = selectedCategory === "all" || p.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  return (
    <div className="flex h-full flex-col gap-4 p-4">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">Prompt Library</h1>
          <p className="text-xs text-text-muted mt-0.5">
            Gerenciador e hub de prompts de sistema pré-configurados
          </p>
        </div>
        <Button variant="primary" size="sm">
          <Plus className="h-3.5 w-3.5 mr-1.5" />
          Add Prompt
        </Button>
      </div>

      {/* Filter and search bar */}
      <div className="flex gap-2">
        <div className="relative flex-1">
          <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-text-dim" />
          <Input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search prompts..."
            className="pl-8 text-xs bg-surface-raised/40"
          />
        </div>
        <div className="flex gap-1 bg-surface-raised/40 rounded-lg p-1 border border-border-subtle">
          {["all", "coding", "writing", "ux", "system"].map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-2.5 py-1 text-[11px] rounded-md capitalize font-medium transition-colors ${
                selectedCategory === cat
                  ? "bg-bg-active text-text-primary shadow-sm"
                  : "text-text-muted hover:text-text-primary"
              }`}
            >
              {cat}
            </button>
          ))}
        </div>
      </div>

      {/* Prompt cards grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {filteredPrompts.map((p) => (
          <Card key={p.id} className="flex flex-col border border-border-subtle bg-surface-raised/35">
            <CardHeader className="pb-2">
              <div className="flex items-start justify-between">
                <div>
                  <CardTitle className="text-sm font-semibold">{p.title}</CardTitle>
                  <CardDescription className="text-[11px] mt-1 text-text-muted">
                    {p.description}
                  </CardDescription>
                </div>
                <Badge variant="info" className="text-[9px] uppercase font-mono">
                  {p.category}
                </Badge>
              </div>
            </CardHeader>
            <CardContent className="flex-1 flex flex-col gap-3 pt-1">
              <div className="bg-canvas p-3 rounded-lg border border-border-subtle/80 font-mono text-[10px] text-text-muted select-all max-h-24 overflow-y-auto relative scrollbar-thin">
                {p.prompt}
              </div>
              <div className="flex gap-2 justify-end mt-auto pt-2 border-t border-border-subtle/30">
                <Button variant="ghost" size="sm">
                  <Edit3 className="h-3 w-3 mr-1" />
                  Edit
                </Button>
                <Button
                  variant="subtle"
                  size="sm"
                  onClick={() => handleCopy(p.id, p.prompt)}
                  className="min-w-[80px]"
                >
                  {copiedId === p.id ? (
                    <>
                      <Check className="h-3 w-3 mr-1 text-success" />
                      Copied!
                    </>
                  ) : (
                    <>
                      <Copy className="h-3 w-3 mr-1" />
                      Copy
                    </>
                  )}
                </Button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
