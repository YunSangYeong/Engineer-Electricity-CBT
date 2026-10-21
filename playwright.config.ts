import { existsSync } from "node:fs";
import { defineConfig, devices } from "@playwright/test";
export default defineConfig({
  testDir: "./tests/e2e",
  fullyParallel: true,
  workers: 2,
  timeout: 45000,
  use: {
    baseURL: "http://127.0.0.1:4173/Engineer-Electricity-CBT/",
    headless: true,
    launchOptions: { executablePath: process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH || (existsSync("/usr/bin/chromium") ? "/usr/bin/chromium" : undefined) },
  },
  projects: [
    { name: "desktop", use: { ...devices["Desktop Chrome"] } },
    { name: "mobile", use: { ...devices["Pixel 7"] } },
  ],
  webServer: {
    command: "npm run preview -- --port 4173 --strictPort",
    url: "http://127.0.0.1:4173/Engineer-Electricity-CBT/",
    reuseExistingServer: !process.env.CI,
  },
});
