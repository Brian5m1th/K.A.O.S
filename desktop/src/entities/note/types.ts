export interface VaultNote {
  id: string;
  title: string;
  path: string;
  content?: string;
  tags?: string[];
  updatedAt?: string;
}
