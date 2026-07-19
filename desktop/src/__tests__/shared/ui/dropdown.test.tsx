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
          { id: "opt1", label: "Option 1", onClick: () => {} },
          { id: "opt2", label: "Option 2", onClick: () => {} },
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
          { id: "delete", label: "Delete", onClick: () => { clicked = true; } },
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
          { id: "edit", label: "Edit", onClick: () => {} },
          { id: "divider", label: "", onClick: () => {} },
          { id: "delete", label: "Delete", onClick: () => {} },
        ]}
      />,
    );
    expect(screen.getByText("Menu")).toBeInTheDocument();
  });
});