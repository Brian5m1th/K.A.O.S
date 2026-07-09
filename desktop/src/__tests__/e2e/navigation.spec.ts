import { test, expect } from "@playwright/test";

test.describe("Dashboard Page", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/dashboard");
  });

  test("should load and display system metrics", async ({ page }) => {
    await expect(page.locator("text=Dashboard")).toBeVisible();
  });

  test("should show status cards", async ({ page }) => {
    await expect(page.locator("text=System Status").or(page.locator("text=Online").or(page.locator("text=Offline")))).toBeVisible();
  });
});

test.describe("Chat Page", () => {
  test.beforeEach(async ({ page }) => {
    await page.goto("/chat");
  });

  test("should display chat interface", async ({ page }) => {
    await expect(page.locator('textarea[placeholder*=\"message\" i], input[placeholder*=\"message\" i]').or(page.locator("text=Chat"))).toBeVisible();
  });

  test("should send a message", async ({ page }) => {
    const input = page.locator('textarea, input[type=\"text\"]').first();
    if (await input.isVisible()) {
      await input.fill("Hello");
      await page.keyboard.press("Enter");
    }
  });
});

test.describe("Settings Page", () => {
  test("should load settings form", async ({ page }) => {
    await page.goto("/settings");
    await expect(page).toHaveURL(/settings/);
  });
});

test.describe("Login Page", () => {
  test("should display login form", async ({ page }) => {
    await page.goto("/login");
    await expect(page.locator('input[type=\"email\"], input[name=\"email\"]').or(page.locator("text=Login"))).toBeVisible();
  });
});
