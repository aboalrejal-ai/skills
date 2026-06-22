# shadcn Model Context Protocol (MCP) Server Guide

The `shadcn` CLI includes a Model Context Protocol (MCP) server. This lets AI coding assistants (such as Claude Code, Cursor, and Copilot) search, browse, view, and install shadcn components from registries directly using natural language.

---

## 1. Setting Up the MCP Server

Initialize the MCP configuration for your workspace:
```bash
npx shadcn@latest mcp        # Runs the MCP server (STDIO)
npx shadcn@latest mcp init   # Generates integration settings for editors
```

### Editor Configuration Registry Paths

The initialization command writes settings to the editor config directories:

| Editor | Configuration File |
| :--- | :--- |
| **Claude Code** | `.mcp.json` |
| **Cursor** | `.cursor/mcp.json` |
| **VS Code** | `.vscode/mcp.json` |
| **OpenCode** | `opencode.json` |
| **Codex** | `~/.codex/config.toml` (Requires manual registration) |

---

## 2. Integrated MCP Tools Reference

AI assistants call the following tools to manage component registries:

### `shadcn:get_project_registries`
Returns a list of registry names configured in the project's local `components.json`.
- **Input**: None

### `shadcn:list_items_in_registries`
Lists all components and helpers published in one or more registries.
- **Input parameters**:
  - `registries` (`string[]`): The target registries.
  - `limit` (`number`, optional): Max results per registry.
  - `offset` (`number`, optional): Pagination offset.

### `shadcn:search_items_in_registries`
Fuzzy search across registries to find matching components.
- **Input parameters**:
  - `registries` (`string[]`): Registries to search.
  - `query` (`string`): Search string.
  - `limit` (`number`, optional): Max results.

### `shadcn:view_items_in_registries`
Retrieves raw file contents and code structure of specific registry components.
- **Input parameters**:
  - `items` (`string[]`): Components to inspect (e.g. `["@shadcn/button", "@shadcn/card"]`).

### `shadcn:get_item_examples_from_registries`
Retrieves demo examples and sample codes for target components.
- **Input parameters**:
  - `registries` (`string[]`): Registries to search.
  - `query` (`string`): Example query (e.g. `"button-demo"`).

### `shadcn:get_add_command_for_items`
Retrieves the package runner command needed to install specific components.
- **Input parameters**:
  - `items` (`string[]`): Target components.

### `shadcn:get_audit_checklist`
Retrieves a verification checklist to inspect installed components (checking path aliases, Lucide icons configuration, TypeScript support, and lint issues).
- **Input**: None

---

## 3. Custom Registry Settings

Registries are registered inside `components.json`. The official `@shadcn` registry is always enabled by default.

```json
{
  "registries": {
    "@acme": "https://acme.com/r/{name}.json",
    "@private-registry": {
      "url": "https://private.com/r/{name}.json",
      "headers": {
        "Authorization": "Bearer ${REGISTRY_API_TOKEN}"
      }
    }
  }
}
```

*   **Syntax Rules**:
    *   Registry identifiers must begin with a `@` symbol.
    *   URLs must contain `{name}`.
    *   `${ENV_VAR}` variables are resolved from the local environment.
