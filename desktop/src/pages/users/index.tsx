import { useEffect, useState } from "react";
import { useAuthStore } from "@/shared/lib/stores";
import { kaosFetch } from "@/shared/api/kaos-client";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";
import { Button } from "@/shared/ui/button";
import { Input } from "@/shared/ui/input";
import { Badge } from "@/shared/ui/badge";
import { UserPlus, UserMinus, Shield, Loader2 } from "lucide-react";

interface UserRecord {
  id: string;
  name: string;
  email: string;
  role: string;
  created_at: string;
}

export default function UsersPage() {
  const user = useAuthStore((s) => s.user);

  const [users, setUsers] = useState<UserRecord[]>([]);
  const [loading, setLoading] = useState(true);

  // Create user form
  const [showForm, setShowForm] = useState(false);
  const [newName, setNewName] = useState("");
  const [newEmail, setNewEmail] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [newRole, setNewRole] = useState("editor");
  const [formError, setFormError] = useState("");

  const fetchUsers = async () => {
    try {
      const res = await kaosFetch("/api/admin/users", "");
      if (res.ok) {
        const data = await res.json();
        setUsers(data.users || []);
      }
    } catch {}
    finally { setLoading(false); }
  };

  useEffect(() => { fetchUsers(); }, []);

  const handleCreate = async () => {
    setFormError("");
    if (!newName.trim()) {
      setFormError("Name is required");
      return;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(newEmail)) {
      setFormError("Please enter a valid email address");
      return;
    }
    if (newPassword.length < 8) {
      setFormError("Password must be at least 8 characters");
      return;
    }

    try {
      const res = await kaosFetch("/api/admin/users", "", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: newName, email: newEmail, password: newPassword, role: newRole }),
      });
      if (res.ok) {
        setShowForm(false);
        setNewName(""); setNewEmail(""); setNewPassword("");
        fetchUsers();
      } else {
        const data = await res.json();
        setFormError(data.detail || "Failed to create user");
      }
    } catch {
      setFormError("Connection error. Could not create user.");
    }
  };

  const handleDelete = async (userId: string) => {
    await kaosFetch(`/api/admin/users/${userId}`, "", { method: "DELETE" });
    fetchUsers();
  };

  const handleRoleChange = async (userId: string, role: string) => {
    await kaosFetch(`/api/admin/users/${userId}/role`, "", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ role }),
    });
    fetchUsers();
  };

  const isAdmin = user?.role === "admin";

  return (
    <div className="flex h-full flex-col gap-4 p-4 overflow-y-auto">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-base font-semibold text-text-primary">Users</h1>
          <p className="text-xs text-text-muted mt-0.5">User management and roles</p>
        </div>
        {isAdmin && (
          <Button variant="primary" size="sm" onClick={() => setShowForm(!showForm)}>
            <UserPlus className="h-3.5 w-3.5 mr-1" />
            Add User
          </Button>
        )}
      </div>

      {showForm && (
        <Card>
          <CardContent className="p-4 space-y-3">
            <p className="text-sm font-medium text-text-primary">New User</p>
            <Input placeholder="Name" value={newName} onChange={(e) => setNewName(e.target.value)} className="text-xs" />
            <Input placeholder="Email" value={newEmail} onChange={(e) => setNewEmail(e.target.value)} className="text-xs" />
            <Input type="password" placeholder="Password (min 8 chars)" value={newPassword} onChange={(e) => setNewPassword(e.target.value)} className="text-xs" />
            {formError && <p className="text-xs font-semibold text-[#EF4444]">{formError}</p>}
            <div className="flex gap-2">
              <select value={newRole} onChange={(e) => setNewRole(e.target.value)} className="rounded-lg border border-border-subtle bg-canvas px-2 py-1 text-xs text-text-primary">
                <option value="admin">Admin</option>
                <option value="editor">Editor</option>
                <option value="viewer">Viewer</option>
              </select>
              <Button variant="primary" size="sm" onClick={handleCreate}>Create</Button>
              <Button variant="secondary" size="sm" onClick={() => setShowForm(false)}>Cancel</Button>
            </div>
          </CardContent>
        </Card>
      )}

      {loading ? (
        <div className="flex justify-center py-8"><Loader2 className="h-5 w-5 animate-spin text-text-dim" /></div>
      ) : (
        <div className="space-y-2">
          {users.map((u) => (
            <Card key={u.id}>
              <CardContent className="p-4 flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="rounded-lg bg-bg-active p-2">
                    <Shield className="h-4 w-4 text-accent-primary" />
                  </div>
                  <div>
                    <p className="text-sm font-medium text-text-primary">{u.name}</p>
                    <p className="text-xs text-text-muted">{u.email}</p>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <Badge variant={u.role === "admin" ? "info" : u.role === "editor" ? "success" : "neutral"}>
                    {u.role.toUpperCase()}
                  </Badge>
                  {isAdmin && u.id !== user?.id && (
                    <>
                      <select
                        value={u.role}
                        onChange={(e) => handleRoleChange(u.id, e.target.value)}
                        className="rounded border border-border-subtle bg-canvas px-1 py-0.5 text-[10px] text-text-primary"
                      >
                        <option value="admin">admin</option>
                        <option value="editor">editor</option>
                        <option value="viewer">viewer</option>
                      </select>
                      <Button variant="danger" size="sm" onClick={() => handleDelete(u.id)}>
                        <UserMinus className="h-3 w-3" />
                      </Button>
                    </>
                  )}
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  );
}
