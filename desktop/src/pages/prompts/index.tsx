import { useState, useEffect } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/shared/ui/card";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Badge } from "@/shared/ui/badge";
import { kaosFetch } from "@/shared/api/kaos-client";
import {
  Copy, Check, Search, Plus, Edit3, Trash2, Loader2, X
} from "lucide-react";

interface PromptItem {
  id: string;
  title: string;
  category: "coding" | "writing" | "ux" | "system";
  prompt: string;
  description: string;
}

export default function PromptsPage() {
  const [prompts, setPrompts] = useState<PromptItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");
  const [selectedCategory, setSelectedCategory] = useState<string>("all");
  const [copiedId, setCopiedId] = useState<string | null>(null);

  // Modal / Form state
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [modalMode, setModalMode] = useState<"create" | "edit">("create");
  const [editingId, setEditingId] = useState<string | null>(null);
  const [formError, setFormError] = useState("");
  const [formData, setFormData] = useState({
    title: "",
    category: "coding",
    description: "",
    prompt: ""
  });

  const fetchPrompts = async () => {
    setLoading(true);
    try {
      const res = await kaosFetch("/api/prompts", "");
      if (res.ok) {
        const data = await res.json();
        setPrompts(data || []);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPrompts();
  }, []);

  const handleCopy = (id: string, text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const openCreateModal = () => {
    setFormData({
      title: "",
      category: "coding",
      description: "",
      prompt: ""
    });
    setEditingId(null);
    setModalMode("create");
    setFormError("");
    setIsModalOpen(true);
  };

  const openEditModal = (item: PromptItem) => {
    setFormData({
      title: item.title,
      category: item.category,
      description: item.description,
      prompt: item.prompt
    });
    setEditingId(item.id);
    setModalMode("edit");
    setFormError("");
    setIsModalOpen(true);
  };

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    setFormError("");

    if (!formData.title.trim()) {
      setFormError("Title is required");
      return;
    }
    if (!formData.description.trim()) {
      setFormError("Description is required");
      return;
    }
    if (!formData.prompt.trim()) {
      setFormError("Prompt body is required");
      return;
    }

    try {
      let res;
      if (modalMode === "create") {
        res = await kaosFetch("/api/prompts", "", {
          method: "POST",
          body: JSON.stringify(formData)
        });
      } else {
        res = await kaosFetch(`/api/prompts/${editingId}`, "", {
          method: "PUT",
          body: JSON.stringify(formData)
        });
      }

      if (res.ok) {
        setIsModalOpen(false);
        fetchPrompts();
      } else {
        const data = await res.json();
        setFormError(data.detail || "Failed to save prompt");
      }
    } catch {
      setFormError("Connection error. Please try again.");
    }
  };

  const handleDelete = async (id: string) => {
    if (!confirm("Are you sure you want to delete this prompt?")) return;
    try {
      const res = await kaosFetch(`/api/prompts/${id}`, "", {
        method: "DELETE"
      });
      if (res.ok) {
        fetchPrompts();
      }
    } catch (e) {
      console.error(e);
    }
  };

  const filteredPrompts = prompts.filter((p) => {
    const matchesSearch =
      p.title.toLowerCase().includes(search.toLowerCase()) ||
      p.description.toLowerCase().includes(search.toLowerCase());
    const matchesCategory = selectedCategory === "all" || p.category === selectedCategory;
    return matchesSearch && matchesCategory;
  });

  return (
    <div className="flex h-full flex-col gap-4 p-4 relative overflow-y-auto">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">Prompt Library</h1>
          <p className="text-xs text-text-muted mt-0.5">
            Gerenciador e hub de prompts de sistema pré-configurados
          </p>
        </div>
        <Button variant="primary" size="sm" onClick={openCreateModal}>
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

      {/* Loading indicator */}
      {loading ? (
        <div className="flex flex-col items-center justify-center py-12 gap-2 text-text-muted">
          <Loader2 className="h-6 w-6 animate-spin" />
          <span className="text-xs">Carregando biblioteca...</span>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {filteredPrompts.map((p) => (
            <Card key={p.id} className="flex flex-col border border-border-subtle bg-surface-raised/35">
              <CardHeader className="pb-2">
                <div className="flex items-start justify-between">
                  <div>
                    <CardTitle className="text-sm font-semibold text-text-primary">{p.title}</CardTitle>
                    <CardDescription className="text-[11px] mt-1 text-text-muted leading-relaxed">
                      {p.description}
                    </CardDescription>
                  </div>
                  <Badge variant="info" className="text-[9px] uppercase font-mono px-2 py-0.5">
                    {p.category}
                  </Badge>
                </div>
              </CardHeader>
              <CardContent className="flex-1 flex flex-col gap-3 pt-1">
                <div className="bg-canvas p-3 rounded-lg border border-border-subtle/80 font-mono text-[10px] text-text-muted select-all max-h-24 overflow-y-auto relative scrollbar-thin">
                  {p.prompt}
                </div>
                <div className="flex gap-2 justify-end mt-auto pt-2 border-t border-border-subtle/30">
                  <Button variant="ghost" size="sm" onClick={() => openEditModal(p)} className="text-text-muted hover:text-text-primary">
                    <Edit3 className="h-3 w-3 mr-1" />
                    Edit
                  </Button>
                  <Button variant="ghost" size="sm" onClick={() => handleDelete(p.id)} className="text-text-muted hover:text-error">
                    <Trash2 className="h-3 w-3 mr-1" />
                    Delete
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
          {filteredPrompts.length === 0 && (
            <div className="col-span-full text-center py-8 text-xs text-text-muted">
              Nenhum prompt encontrado nesta categoria.
            </div>
          )}
        </div>
      )}

      {/* Modal Dialog Form */}
      {isModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4 animate-in fade-in duration-200">
          <div className="w-full max-w-md bg-surface border border-border-subtle rounded-xl shadow-2xl overflow-hidden relative">
            <div className="h-1 bg-gradient-to-r from-accent-primary to-accent-neon" />
            <div className="p-5">
              <div className="flex items-center justify-between mb-4">
                <h3 className="text-sm font-semibold text-text-primary">
                  {modalMode === "create" ? "Add New Prompt" : "Edit Prompt"}
                </h3>
                <button
                  onClick={() => setIsModalOpen(false)}
                  className="p-1 rounded hover:bg-bg-active text-text-muted hover:text-text-primary transition-colors"
                >
                  <X className="h-4 w-4" />
                </button>
              </div>

              <form onSubmit={handleSave} className="space-y-4">
                <div className="space-y-1">
                  <label className="text-[11px] font-semibold text-text-muted">Title</label>
                  <Input
                    value={formData.title}
                    onChange={(e) => setFormData((s) => ({ ...s, title: e.target.value }))}
                    placeholder="e.g. Code Reviewer Pro"
                    className="text-xs bg-canvas"
                  />
                </div>

                <div className="space-y-1">
                  <label className="text-[11px] font-semibold text-text-muted">Category</label>
                  <select
                    value={formData.category}
                    onChange={(e) => setFormData((s) => ({ ...s, category: e.target.value }))}
                    className="w-full rounded-lg border border-border-subtle bg-canvas px-3 py-2 text-xs text-text-primary outline-none focus:border-accent-primary"
                  >
                    <option value="coding">Coding</option>
                    <option value="writing">Writing</option>
                    <option value="ux">UX/UI</option>
                    <option value="system">System</option>
                  </select>
                </div>

                <div className="space-y-1">
                  <label className="text-[11px] font-semibold text-text-muted">Description</label>
                  <Input
                    value={formData.description}
                    onChange={(e) => setFormData((s) => ({ ...s, description: e.target.value }))}
                    placeholder="Briefly describe what this prompt does"
                    className="text-xs bg-canvas"
                  />
                </div>

                <div className="space-y-1">
                  <label className="text-[11px] font-semibold text-text-muted">Prompt Body</label>
                  <textarea
                    rows={4}
                    value={formData.prompt}
                    onChange={(e) => setFormData((s) => ({ ...s, prompt: e.target.value }))}
                    placeholder="Enter the system instructions..."
                    className="w-full rounded-lg border border-border-subtle bg-canvas p-3 text-xs text-text-primary outline-none focus:border-accent-primary font-mono"
                  />
                </div>

                {formError && (
                  <p className="text-[11px] font-semibold text-[#EF4444]">{formError}</p>
                )}

                <div className="flex gap-2 justify-end pt-2 border-t border-border-subtle/50">
                  <Button type="button" variant="secondary" size="sm" onClick={() => setIsModalOpen(false)}>
                    Cancel
                  </Button>
                  <Button type="submit" variant="primary" size="sm">
                    {modalMode === "create" ? "Create" : "Save Changes"}
                  </Button>
                </div>
              </form>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
