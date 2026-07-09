/// <reference types="vitest/globals" />
import "@testing-library/jest-dom";

// Mock do localStorage
const createMockStorage = () => {
  const store: Record<string, string> = {};
  return {
    getItem: (key: string): string | null => store[key] ?? null,
    setItem: (key: string, value: string): void => { store[key] = value; },
    removeItem: (key: string): void => { delete store[key]; },
    clear: (): void => { Object.keys(store).forEach(k => delete store[k]); },
    get length(): number { return Object.keys(store).length; },
    key: (index: number): string | null => Object.keys(store)[index] ?? null,
  };
};

Object.defineProperty(window, "localStorage", {
  value: createMockStorage(),
  writable: true,
});

// Mock do matchMedia
Object.defineProperty(window, "matchMedia", {
  writable: true,
  value: (query: string) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: () => {},
    removeListener: () => {},
    addEventListener: () => {},
    removeEventListener: () => {},
    dispatchEvent: () => false,
  }),
});

// Mock do fetch global (tipado manualmente)
const mockFetch = vi.fn();
globalThis.fetch = mockFetch;

// Limpeza automática após cada teste
afterEach(() => {
  vi.clearAllMocks();
  window.localStorage.clear();
});