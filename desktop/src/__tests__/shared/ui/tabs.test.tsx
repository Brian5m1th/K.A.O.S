import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { Tabs } from "@/shared/ui/tabs";

describe("Tabs", () => {
  const tabs = [
    { id: "tab-a", label: "Tab A" },
    { id: "tab-b", label: "Tab B" },
  ];

  it("should render tab labels with active state", () => {
    render(<Tabs tabs={tabs} activeTab="tab-a" onTabChange={vi.fn()} />);
    expect(screen.getByText("Tab A")).toBeInTheDocument();
    expect(screen.getByText("Tab B")).toBeInTheDocument();
  });

  it("should call onTabChange when clicking a tab", () => {
    const onChange = vi.fn();
    render(<Tabs tabs={tabs} activeTab="tab-a" onTabChange={onChange} />);
    fireEvent.click(screen.getByText("Tab B"));
    expect(onChange).toHaveBeenCalledWith("tab-b");
  });
});