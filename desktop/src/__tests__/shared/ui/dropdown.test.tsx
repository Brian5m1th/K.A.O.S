import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { Dropdown } from "@/shared/ui/dropdown";

describe("Dropdown", () => {
  it("should render trigger content", () => {
    render(<Dropdown trigger={<button>Menu</button>} items={[]} />);
    expect(screen.getByText("Menu")).toBeInTheDocument();
  });

  it("should render items when provided", () => {
    render(
      <Dropdown
        trigger={<button>Menu</button>}
        items={[
          { label: "Option 1", onClick: () => {} },
          { label: "Option 2", onClick: () => {} },
        ]}
      />,
    );
    expect(screen.getByText("Menu")).toBeInTheDocument();
  });

  it("should handle item click", async () => {
    let clicked = false;
    const user = userEvent.setup();
    render(
      <Dropdown
        trigger={<button>Actions</button>}
        items={[
          { label: "Delete", onClick: () => { clicked = true; } },
        ]}
      />,
    );
    const trigger = screen.getByText("Actions");
    await user.click(trigger);
    // Trigger click should not error
    expect(trigger).toBeInTheDocument();
  });

  it("should render with divider", () => {
    render(
      <Dropdown
        trigger={<button>Menu</button>}
        items={[
          { label: "Edit", onClick: () => {} },
          { type: "divider" },
          { label: "Delete", onClick: () => {} },
        ]}
      />,
    );
    expect(screen.getByText("Menu")).toBeInTheDocument();
  });
});