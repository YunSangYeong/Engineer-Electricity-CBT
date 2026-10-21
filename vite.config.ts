import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
export default defineConfig({
  plugins: [react()],
  base: "/Engineer-Electricity-CBT/",
  build: { rollupOptions: { output: { manualChunks: {
    react: ["react", "react-dom"],
    questions: ["./src/data/questions-main.json"],
  } } } },
});
