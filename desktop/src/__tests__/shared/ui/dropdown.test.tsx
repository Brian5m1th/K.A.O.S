import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { Dropdown } from "@/shared/ui/dropdown";

describe("Dropdown", () => {
  it("should render trigger content", () => {
    render(<Dropdown trigger={<button>Menu</button>} items={[]} />);
    expect(screen.getByText("Menu")).toBeInTheDocument();
  });
});