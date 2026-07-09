import { describe, it, expect, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { Dropdown } from "@/shared/ui/dropdown";

describe("Dropdown", () => {
  it("should render trigger content", () => {
    render(<Dropdown trigger={<button>Menu</button>}><div>Item</div></Dropdown>);
    expect(screen.getByText("Menu")).toBeInTheDocument();
  });
});
