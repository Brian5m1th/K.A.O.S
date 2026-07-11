import { describe, it, expect, vi, beforeEach } from "vitest";
import { useUpdateStore } from "@/application/stores/update-store";

describe("Update Store", () => {
  beforeEach(() => {
    useUpdateStore.setState({
      phase: "idle", channel: "stable", currentVersion: "2.1.0",
      update: null, progress: 0, lastCheckAt: null, error: null,
    });
  });

  it("should initialize with idle phase", () => {
    const s = useUpdateStore.getState();
    expect(s.phase).toBe("idle");
    expect(s.channel).toBe("stable");
  });

  it("setPhase should change phase", () => {
    useUpdateStore.getState().setPhase("checking");
    expect(useUpdateStore.getState().phase).toBe("checking");
  });

  it("setUpdate should store update info", () => {
    const info = { version: "2.2.0", date: "2025-06-01", body: "Bug fixes" };
    useUpdateStore.getState().setUpdate(info);
    expect(useUpdateStore.getState().update).toEqual(info);
  });

  it("setProgress should update progress", () => {
    useUpdateStore.getState().setProgress(50);
    expect(useUpdateStore.getState().progress).toBe(50);
  });

  it("setError should store error message", () => {
    useUpdateStore.getState().setError("Download failed");
    expect(useUpdateStore.getState().error).toBe("Download failed");
  });

  it("setChannel should change channel", () => {
    useUpdateStore.getState().setChannel("beta");
    expect(useUpdateStore.getState().channel).toBe("beta");
  });

  it("setCurrentVersion should update version", () => {
    useUpdateStore.getState().setCurrentVersion("2.2.0");
    expect(useUpdateStore.getState().currentVersion).toBe("2.2.0");
  });

  it("setLastCheckAt should store timestamp", () => {
    useUpdateStore.getState().setLastCheckAt("2025-06-15T10:00:00Z");
    expect(useUpdateStore.getState().lastCheckAt).toBe("2025-06-15T10:00:00Z");
  });

  it("should clear error when setError(null) is called", () => {
    useUpdateStore.setState({ error: "old error", phase: "error" });
    useUpdateStore.getState().setError(null);
    expect(useUpdateStore.getState().error).toBeNull();
  });
});
