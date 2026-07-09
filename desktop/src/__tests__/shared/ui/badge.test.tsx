import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { Badge } from "@/shared/ui/badge";

describe("Badge", () => {
  it("should render children", () => {
    render(<Badge>Active</Badge>);
    expect(screen.getByText("Active")).toBeInTheDocument();
  });

  it("should apply variant class", () => {
    render(<Badge variant="secondary">Draft</Badge>);
    const badge = screen.getByText("Draft");
    expect(badge.className).toContain("secondary");
  });
});
