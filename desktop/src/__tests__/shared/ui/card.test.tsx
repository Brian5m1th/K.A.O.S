import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { Card, CardContent, CardHeader, CardTitle } from "@/shared/ui/card";

describe("Card", () => {
  it("should render card with content", () => {
    render(<Card><p>Content</p></Card>);
    expect(screen.getByText("Content")).toBeInTheDocument();
  });

  it("should render CardHeader with title", () => {
    render(<CardHeader><CardTitle>My Card</CardTitle></CardHeader>);
    expect(screen.getByText("My Card")).toBeInTheDocument();
  });

  it("should render CardContent with children", () => {
    render(<CardContent><span>Body</span></CardContent>);
    expect(screen.getByText("Body")).toBeInTheDocument();
  });

  it("should compose Card with header and content", () => {
    render(
      <Card>
        <CardHeader><CardTitle>Title</CardTitle></CardHeader>
        <CardContent>Content</CardContent>
      </Card>
    );
    expect(screen.getByText("Title")).toBeInTheDocument();
    expect(screen.getByText("Content")).toBeInTheDocument();
  });
});
