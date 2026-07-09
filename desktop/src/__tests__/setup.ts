/// <reference types="vitest/globals" />
import "@testing-library/jest-dom";

// Mock do localStorage
const localStorageMock = (() => {
  let store: Record<string, string> = {};
  return {
    getItem: (key: string): string | null => store[key] ?? null,
    setItem: (key: string, value: string): void => {
      store[key] = value;
    },
    removeItem: (key: string): void => {
      delete store[key];
    },
    clear: (): void => {
      store = {};
    },
    get length(): number {
      return Object.keys(store).length;
    },
    key: (index: number): string | null => {
      return Object.keys(store)[index] ?? null;
    },
  };
})();

Object.defineProperty(window, "localStorage", {
  value: localStorageMock,
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

// Mock do fetch global
const mockFetch = vi.fn();
globalThis.fetch = mockFetch;

// Mock do AbortController
class MockAbortController {
  signal: AbortSignal = {
    aborted: false,
    reason: undefined,
    onabort: null,
    throwIfAborted: () => {},
    addEventListener: () => {},
    removeEventListener: () => {},
    dispatchEvent: () => false,
  };
  abort(): void {
    this.signal.aborted = true;
  }
}

globalThis.AbortController = MockAbortController as unknown as typeof AbortController;

// Limpeza automática após cada teste
afterEach(() => {
  vi.clearAllMocks();
  localStorageMock.clear();
});