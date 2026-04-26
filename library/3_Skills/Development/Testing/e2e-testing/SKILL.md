---
title: "E2E Testing"
tags: ["playwright", "e2e", "testing", "ci", "frontend"]
category: "Skills"
subcategory: "Development"
source: "https://skillsmp.com/skills/affaan-m-everything-claude-code-skills-e2e-testing-skill-md"
source_author: "affaan-m"
source_repository: "affaan-m/everything-claude-code"
source_stars: 162855
source_updated: "2026-02-23"
---

# E2E Testing

## Overview
Design and maintain Playwright end-to-end test suites for critical user flows. Use this skill when adding browser tests, stabilizing flaky tests, introducing Page Object Model structure, or wiring E2E results into CI.

## When to Use
- Building or refactoring Playwright test coverage.
- Testing authentication, checkout, trading, dashboard, or other critical browser flows.
- Creating Page Object Models or reusable fixtures.
- Debugging flaky waits, race conditions, and CI-only failures.
- Capturing screenshots, traces, videos, and reports for review.

## Recommended Structure
```text
tests/
  e2e/
    auth/
    features/
    api/
  fixtures/
  pages/
playwright.config.ts
```

## Page Object Pattern
```ts
import { Page, Locator } from "@playwright/test";

export class ItemsPage {
  readonly page: Page;
  readonly searchInput: Locator;
  readonly itemCards: Locator;

  constructor(page: Page) {
    this.page = page;
    this.searchInput = page.getByTestId("search-input");
    this.itemCards = page.getByTestId("item-card");
  }

  async goto() {
    await this.page.goto("/items");
    await this.page.waitForLoadState("networkidle");
  }

  async search(query: string) {
    await this.searchInput.fill(query);
    await this.page.waitForResponse((resp) => resp.url().includes("/api/search"));
  }
}
```

## Stability Rules
- Prefer locators and auto-waiting over raw selectors and arbitrary timeouts.
- Wait for meaningful application signals, such as a response, URL change, or visible state.
- Use `data-testid` or accessible roles for stable selectors.
- Quarantine known flaky tests with an issue reference rather than silently ignoring them.
- Reproduce flakiness with `--repeat-each` and retries before changing assertions.

## CI Pattern
```yaml
name: E2E Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npx playwright install --with-deps
      - run: npx playwright test
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: playwright-report
          path: playwright-report/
```

## Artifact Checklist
- HTML report for full navigation.
- Screenshots for failed or important checkpoints.
- Traces for retry failures.
- Videos only when the storage and review value justify them.
- A short failure summary with file, line, error, and suggested fix.

## Source Notes
Adapted from the SkillsMP `e2e-testing` skill, selected for high popularity and practical coverage around Playwright, browser QA, and CI artifacts.
