# shadcn CLI Command & Preset Reference

The `shadcn` CLI allows developers to initialize, configure, search, and manage component registries directly from the terminal. The CLI parses configuration rules from the project's local `components.json`.

---

## 1. Dynamic Command Runners

Always run commands using the project's appropriate package manager. The CLI auto-detects this from your lockfiles (e.g. `package-lock.json`, `pnpm-lock.yaml`, `bun.lockb`).

*   **npm**: `npx shadcn@latest <command>`
*   **pnpm**: `pnpm dlx shadcn@latest <command>`
*   **bun**: `bunx --bun shadcn@latest <command>`

---

## 2. Command Reference

### `init` (or `create`) — Initialize or Create a Project
Used to configure shadcn/ui in an existing project or scaffold a brand-new project from scratch.
```bash
npx shadcn@latest init [components...] [options]
```

| Flag | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--name <name>` | `-n` | Scaffolds a new project directory with this name | — |
| `--template <tpl>` | `-t` | Select framework template (`next`, `vite`, `start`, `react-router`, `astro`) | — |
| `--preset <code/name>`| `-p` | Applies a preset style configuration on initialization | — |
| `--defaults` | `-d` | Quickly scaffolds using standard default styles (`next` + `nova`) | `false` |
| `--yes` | `-y` | Skip all interactive selection prompts | `true` |
| `--force` | `-f` | Forces initialization and overwrites existing configurations | `false` |
| `--monorepo` | | Automatically configures paths for a monorepo architecture | — |
| `--no-monorepo` | | Bypasses monorepo prompts | — |
| `--reinstall` | | Force-reinstalls existing UI component files | `false` |

---

### `apply` — Apply Preset Configurations
Applies a visual theme preset to an existing project. This overwrites theme configurations, CSS variables, and target components.
```bash
npx shadcn@latest apply [preset] [options]
```

| Flag | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--preset <preset>` | — | The preset to apply (named, shareable code, or URL) | — |
| `--only <parts>` | — | Partial updates only (`theme`, `font`, or `theme,font`) | — |
| `--yes` | `-y` | Bypasses confirmations | `false` |

*Note: If no preset parameter is provided, the CLI will output a shortcut URL to launch the preset designer at `ui.shadcn.com/create`.*

---

### `add` — Add Components
Downloads component source files into your local codebase.
```bash
npx shadcn@latest add [components...] [options]
```

| Flag | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--all` | `-a` | Installs all components matching the active preset registry | `false` |
| `--overwrite` | `-o` | Overwrites existing files in the destination path | `false` |
| `--path <path>` | `-p` | Installs components to a custom directory path | — |
| `--dry-run` | | Simulates installation steps without making filesystem writes | `false` |
| `--diff [file]` | | Generates Git-style diff of files before applying (implies dry-run) | — |
| `--view [file]` | | Renders raw source code directly to standard output (implies dry-run) | — |

#### Upstream Updates & Smart Merging
When updating components, avoid using `--overwrite` directly on modified local files. Instead, leverage `--dry-run` and `--diff`:
1. Run `npx shadcn@latest add <component> --dry-run` to identify which files would update.
2. For edited components, run `npx shadcn@latest add <component> --diff <filename.tsx>` to inspect incoming updates.
3. Incorporate updates manually, ensuring custom local logic is not overwritten.

---

### `search` (or `list`) — Search Registries
Queries configured registries for components matching a search string.
```bash
npx shadcn@latest search <registries...> [options]
```
*   **Example**: `npx shadcn@latest search @shadcn -q "sidebar"`

---

### `view` — View Raw Registry Details
Renders schema metadata and raw source definitions of registry components without installing them locally.
```bash
npx shadcn@latest view <items...> [options]
```
*   **Example**: `npx shadcn@latest view @shadcn/button`

---

### `docs` — Retrieve Component Documentation URLs
Retrieves online documentation links and raw examples matching specific components. Very useful for fetching reference code.
```bash
npx shadcn@latest docs [components...]
```
*   **Example**: `npx shadcn@latest docs dialog select`

---

### `info` — Inspect Project Configuration
Prints the project's current workspace configurations, environment settings, and aliases resolved from `components.json`.
```bash
npx shadcn@latest info
```

---

### `build` — Compile Registry Indexes
Compiles a local `registry.json` file into individual item schemas. Used by developers when building custom or private component distributions.
```bash
npx shadcn@latest build [registry] [options]
```
*   **Example**: `npx shadcn@latest build --output ./dist/r`

---

## 3. Presets & Shareable Styling Codes

Presets encapsulate visual theme choices (border-radius, fonts, CSS variables, base styling styles) and can be shared using:
1.  **Named Presets**: `nova`, `vega`, `maia`, `lyra`, `mira`, `luma`.
2.  **Opaque Base62 Share Codes**: (e.g. `a2r6bw` or `b0`) created via the shadcn theme builder.
3.  **URLs**: Custom builder links (e.g. `https://ui.shadcn.com/init?base=radix&style=nova&theme=zinc...`).

### How to Apply Custom Presets
- To apply onto an existing project:
  ```bash
  npx shadcn@latest apply a2r6bw
  ```
- To update only specific attributes (like fonts and variables) without reinstalling UI code files:
  ```bash
  npx shadcn@latest apply a2r6bw --only theme,font
  ```
