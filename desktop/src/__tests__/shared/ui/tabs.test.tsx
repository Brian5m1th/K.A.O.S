import { describe, it, expect, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { Tabs } from "@/shared/ui/tabs";

describe("Tabs", () => {
  it("should render tab labels", () => {
    render(<Tabs tabs={[{ label: "Tab A", content: <p>A</p> }, { label: "Tab B", content: <p>B</p> }]} />);
    expect(screen.getByText("Tab A")).toBeInTheDocument();
    expect(screen.getByText("Tab B")).toBeInTheDocument();
  });

  it("should show first tab content by default", () => {
    render(<Tabs tabs={[{ label: "Tab A", content: <p>Content A</p> }, { label: "Tab B", content: <p>Content B</p> }]} />);
    expect(screen.getByText("Content A")).toBeInTheDocument();
  });
});
