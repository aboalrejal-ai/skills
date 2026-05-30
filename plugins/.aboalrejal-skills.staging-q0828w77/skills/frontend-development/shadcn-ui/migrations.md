# Project Scaffolding & Migration Guide for shadcn/ui

This guide outlines standard workflows for starting new projects and migrating legacy projects to a unified, modern stack using **Vite/React/Next.js, TypeScript, Tailwind CSS v4, and shadcn/ui**.

---

## 1. Setting Up a New Project

Follow these steps to initialize a fresh, optimized environment with the modern stack from Day 1.

### Step 1: Initialize the Project (Vite + React + TS)
Run the following commands to scaffold a standard React application:
```bash
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install
```

### Step 2: Install Tailwind CSS v4
Tailwind CSS v4 features native lightning-fast Rust-based builds and a CSS-first configuration. Install it via the official Vite plugin:
```bash
npm install tailwindcss @tailwindcss/vite
```

Update your `vite.config.ts` to register the Tailwind CSS plugin:
```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),
  ],
})
```

### Step 3: Configure Entry CSS (index.css)
Clear the contents of `src/index.css` and `src/App.css`. Set up your CSS entry point to import Tailwind:
```css
@import "tailwindcss";
```

### Step 4: Initialize shadcn/ui
Run the shadcn CLI initialization command to configure the library paths and base styles:
```bash
npx shadcn@latest init
```

**Choose the following standard configuration options when prompted:**
- **Style:** `New York` (highly recommended for modern layouts with smaller text, tighter padding, and professional defaults).
- **Base color:** `Zinc` or `Neutral`.
- **CSS variables:** `Yes` (essential for dynamic Light/Dark mode).

### Step 5: Install Essential UI Components
Add a core set of components to begin building your layouts:
```bash
npx shadcn@latest add button card input label sheet
```

### Step 6: Directing AI Builders (Prompt Template)
When delegating visual or feature creation to an AI developer, use this prompt to enforce styling standards:
> "I have initialized a React project with Vite, Tailwind CSS v4, and shadcn/ui. Please build the [Landing Page / Dashboard / Component] using existing shadcn components. Strictly use semantic Tailwind variables (such as `bg-background`, `text-foreground`, `border-border`) and built-in component variants. Under no circumstances should you write custom hex codes or arbitrary spacing styles."

---

## 2. Migrating Legacy Projects to shadcn/ui & Tailwind v4

Use this step-by-step framework to systematically upgrade visual components, clean up arbitrary styles, and standardize legacy frontends without breaking underlying application logic.

### Step 1: Discovery & Audit
Inspect the codebase to identify dependency versions and existing legacy structures:
1. Examine `package.json` to note current versions of React, Tailwind, and Vite.
2. Locate existing UI assets (e.g., custom bootstrap folders, old custom component directories like `src/components/ui`).
3. Read the main stylesheet (e.g. `src/index.css`) to inspect current CSS variables and global overrides.
4. Note key entry layouts (e.g. `App.tsx`, `Layout.tsx`, `Sidebar.tsx`).

### Step 2: Automated Tailwind v4 Upgrade
Run the official Tailwind migration utility, which updates configuration files, CSS directives, and class syntax automatically:
```bash
npx @tailwindcss/upgrade@latest
```
*Note: If the tool encounters package conflicts, manually install `@tailwindcss/vite` (or `@tailwindcss/postcss` if PostCSS is used) and reference the plugin in your bundler config.*

### Step 3: Establish the Semantic Theme
1. Replace legacy color variables (`--brand-color`, `--bg-dark`, etc.) inside the global CSS file.
2. Setup standard shadcn/ui `@theme` utility tokens mapping to the semantic CSS variables.
3. Verify that light/dark toggle configurations are scoped via a `.dark` class on the root element.

### Step 4: Initialize and Merge Components
1. Initialize the CLI if not done already: `npx shadcn@latest init`.
2. Map old custom UI files (e.g. `LegacyButton.tsx`, `OldCard.tsx`) to their modern equivalents.
3. Install shadcn/ui replacements: `npx shadcn@latest add button card`.
4. Systematically swap imports across layout files to use the verified, accessible shadcn/ui components.

### Step 5: Clean Up Arbitrary & Hex Colors
1. Identify raw colors and arbitrary values in the codebase:
   ```bash
   # Find hardcoded hex codes
   grep -rE "#[0-9a-fA-F]{3,6}" src/
   # Find arbitrary Tailwind V3 background/text brackets
   grep -rE "bg-\[#.*\]|text-\[#.*\]" src/
   ```
2. Refactor raw color statements to semantic system utilities:
   - `#FFFFFF` / `bg-white` & `#000000` / `bg-black` $\rightarrow$ `bg-background` or `text-foreground`
   - Custom grays (`#121212`, `#1e1e1e`) $\rightarrow$ `bg-muted` or `bg-card`
   - Borders $\rightarrow$ `border-border`
   - Custom colors for status alerts $\rightarrow$ Use semantic tokens like `text-destructive` or standard `Badge` variants instead.

### Step 6: Build Verification
1. Run `npm run build` to confirm all component dependencies and path aliases resolve correctly.
2. Manually test the theme switcher, ensuring no elements have "invisible text" (light-foreground on light-background) or conflicting dark overrides.
3. Clean up: Delete unreferenced legacy configuration files (e.g., `tailwind.config.js` if fully migrated to v4) and old component files.
