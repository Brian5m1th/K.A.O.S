import { Store } from "@tauri-apps/plugin-store";

const STORE_NAME = "settings.json";

export class TauriStoreService {
  private static instance: Awaited<ReturnType<typeof Store.load>> | null = null;

  private static async getStore() {
    if (!this.instance) {
      this.instance = await Store.load(STORE_NAME);
    }
    return this.instance;
  }

  static async get<T>(key: string): Promise<T | null> {
    try {
      const store = await this.getStore();
      return (await store.get<T>(key)) ?? null;
    } catch {
      return null;
    }
  }

  static async set(key: string, value: unknown): Promise<boolean> {
    try {
      const store = await this.getStore();
      await store.set(key, value);
      await store.save();
      return true;
    } catch {
      return false;
    }
  }

  static async getAll(): Promise<Record<string, unknown>> {
    try {
      const store = await this.getStore();
      return (await store.entries()).reduce<Record<string, unknown>>(
        (acc, [key, val]) => ({ ...acc, [key]: val }),
        {},
      );
    } catch {
      return {};
    }
  }

  static resetInstance() {
    this.instance = null;
  }
}
