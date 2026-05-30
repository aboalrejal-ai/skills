---
name: shadcn-ui
description: Give your AI assistant deep knowledge of shadcn/ui components, patterns, and best practices. Applies when working with shadcn/ui, registries, presets, or any project with a components.json file.
argument-hint: "[--preset <preset-code>] [--all] — e.g. npx skills add shadcn/ui"
---

# shadcn/ui AI Skill

Expert assistance with `shadcn/ui` — the premier open-source component distribution framework. This skill provides deep project-aware context, enabling your AI assistant to search, install, customize, compose, and migrate components matching your exact workspace configuration.

---

## 1. When to Trigger This Skill

This skill activates when:
- Initializing or configuring `shadcn/ui` in a project.
- Finding, adding, or updating UI components (e.g. Button, Dialog, Form, Table, Charts).
- Upgrading styling pipelines (e.g. migrating to Tailwind CSS v4 or setting up dark mode themes).
- Troubleshooting import path configurations, TypeScript compilers, or CSS styling issues.
- Building, registering, or hosting custom component registries.
- Customizing component files, presets, or extending visual CVA variants.
- Interacting with the shadcn Model Context Protocol (MCP) server.

---

## 2. Project Context & Suitability Checker

On every interaction, the assistant performs a dynamic check of the workspace to determine suitability:

### Phase 1: Environment Scanning
1. **Search for `components.json`**: If found, `shadcn/ui` is already initialized. The assistant runs `npx shadcn@latest info --json` to load the current workspace state.
2. **Search for `package.json`**: If no `components.json` is present, the assistant parses `package.json` to verify the project uses a React-compatible framework (e.g. Next.js, Vite/React, Astro with React, Remix, React Router, TanStack Start).
3. **Resolve Package Manager**: The assistant scans for lockfiles (`package-lock.json` $\rightarrow$ `npm`, `pnpm-lock.yaml` $\rightarrow$ `pnpm`, `bun.lockb` $\rightarrow$ `bun`) to select the proper execution commands.

### Phase 2: Suitability Recommendation & Impacts
If `shadcn/ui` is not yet installed, the assistant evaluates the framework and advises the developer:
- **Suitability status**: Suitable if React + Tailwind CSS (v3 or v4) is detected.
- **Initialization Command**: Recommends the specific initialization command based on the package manager:
  ```bash
  npx shadcn@latest init
  ```
- **File Impacts**: Details exactly what will change:
  - Scaffolds a new `components.json` configuration file in the project root.
  - Adds utility helpers under `lib/utils.ts` (e.g. the standard `cn()` utility).
  - Integrates base CSS variables inside the global stylesheet file (e.g., `src/index.css` or `app/globals.css`).
  - Alters import alias rules inside `tsconfig.json` or `jsconfig.json`.

---

## 3. How It Works

1. **Auto-Detection**: The skill activates upon finding `components.json` in your project root.
2. **Configuration Reading**: The skill runs `shadcn info --json` to read aliases, styles (`nova`, `vega`), base framework (`radix` or `base`), icon libraries (`lucide`, `tabler`), package managers, and component destinations.
3. **Composition & Pattern Enforcement**: The assistant automatically follows structure guidelines (e.g. `FieldGroup` for forms, proper `asChild`/`render` triggers, semantic color tokens, and Lucide/Tabler icon sizing).
4. **Documentation Fetching**: Before writing or troubleshooting components, the assistant uses `npx shadcn@latest docs <component>` to fetch official API references and raw usage code.

---

## 4. Key Documentation Guides

This skill is organized into comprehensive, specialized guides. Refer to these files for detailed workflows:

- **[Unified Coding Rules (`rules.md`)](./rules.md)**: Strictly enforced rules for CSS layout margins, accessible forms structure, icons, composition, and Radix vs React Aria (Base) primitive API differences.
- **[CLI Reference (`cli.md`)](./cli.md)**: Command flags reference (`init`, `apply`, `add`, `search`, `docs`), smart merging workflows, monorepos, templates, and base62 shareable preset codes.
- **[Theming & Customization (`customization.md`)](./customization.md)**: Details semantic CSS variables, OKLCH color spacing conventions, dark mode integration, and registering colors in Tailwind v3 and v4.
- **[Scaffolding & Legacy Migrations (`migrations.md`)](./migrations.md)**: Detailed guides on initializing clean Vite/Next.js/Tailwind v4 layouts, and migrating cluttered legacy codebases into modern clean shadcn components.
- **[Model Context Protocol Server (`mcp.md`)](./mcp.md)**: Setup workflows and stdio integration details for editor clients (Claude Code, Cursor, VS Code).
- **[Component Catalog (`references.md`)](./references.md)**: Full list of available shadcn/ui components, utilities, and direct documentation URLs.

---

## 5. Basic Code Reference

### A. Quick Button Component
```tsx
import { Button } from "@/components/ui/button"
import { SearchIcon } from "lucide-react"

export default function ActionButton() {
  return (
    <Button variant="outline">
      <SearchIcon data-icon="inline-start" />
      Search Components
    </Button>
  )
}
```

### B. Standard Form Composition
```tsx
import { FieldGroup, Field, FieldLabel, FieldDescription } from "@/components/ui/field"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"

export default function ContactForm() {
  return (
    <form className="flex flex-col gap-4">
      <FieldGroup>
        <Field>
          <FieldLabel htmlFor="email">Email Address</FieldLabel>
          <Input id="email" type="email" placeholder="you@domain.com" />
          <FieldDescription>We will never share your email address.</FieldDescription>
        </Field>
      </FieldGroup>
      <Button type="submit">Submit Form</Button>
    </form>
  )
}
```

### C. Accessibly Named Dialog
```tsx
import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"

export default function DialogDemo() {
  return (
    <Dialog>
      <DialogTrigger asChild>
        <Button>Open Settings</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Profile Settings</DialogTitle>
          <DialogDescription>
            Update user credentials and notification bounds.
          </DialogDescription>
        </DialogHeader>
        {/* Form content goes here */}
      </DialogContent>
    </Dialog>
  )
}
```

---

## 6. Official Resources & Repositories

- **Main Documentation**: https://ui.shadcn.com
- **Core Components Catalog**: https://ui.shadcn.com/docs/components
- **GitHub Repository**: https://github.com/shadcn-ui/ui
- **CLI Sources**: https://github.com/shadcn-ui/ui/tree/main/packages/shadcn
- **Theme Creator**: https://ui.shadcn.com/themes
