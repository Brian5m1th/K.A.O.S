import { isTauri } from "@/infrastructure/ipc";

type TauriStore = {
  get: (key: string) => Promise<unknown>;
  set: (key: string, value: unknown) => Promise<void>;
  save: () => Promise<void>;
  entries: () => Promise<[string, unknown][]>;
};

const STORE_NAME = "settings.json";

export class TauriStoreService {
  private static instance: TauriStore | null = null;

  private static async getStore() {
    if (!isTauri()) {
      return null;
    }
    if (!this.instance) {
      const { Store } = await import("@tauri-apps/plugin-store");
      this.instance = await Store.load(STORE_NAME);
    }
    return this.instance;
  }

  static async get<T>(key: string): Promise<T | null> {
    try {
      const store = await this.getStore();
      if (store) {
        const val = await store.get(key);
        return (val as T) ?? null;
      }
      const val = localStorage.getItem(`${STORE_NAME}:${key}`);
      return val ? (JSON.parse(val) as T) : null;
    } catch {
      return null;
    }
  }

  static async set(key: string, value: unknown): Promise<boolean> {
    try {
      const store = await this.getStore();
      if (store) {
        await store.set(key, value);
        await store.save();
        return true;
      }
      localStorage.setItem(`${STORE_NAME}:${key}`, JSON.stringify(value));
      return true;
    } catch {
      return false;
    }
  }

  static async getAll(): Promise<Record<string, unknown>> {
    try {
      const store = await this.getStore();
      if (store) {
        const entries = (await store.entries()) as [string, unknown][];
        return entries.reduce<Record<string, unknown>>(
          (acc: Record<string, unknown>, [key, val]: [string, unknown]) => ({ ...acc, [key]: val }),
          {},
        );
      }
      const res: Record<string, unknown> = {};
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key && key.startsWith(`${STORE_NAME}:`)) {
          const cleanKey = key.substring(STORE_NAME.length + 1);
          const val = localStorage.getItem(key);
          if (val) {
            res[cleanKey] = JSON.parse(val);
          }
        }
      }
      return res;
    } catch {
      return {};
    }
  }

  static resetInstance() {
    this.instance = null;
  }
}
