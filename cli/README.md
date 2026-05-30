# 🛠️ aboalrejal-skills CLI

> The ultimate interactive Command-Line Interface to query, search, and install AI agent skills across **20+ top AI coding platforms** instantly.

Designed from the ground up for maximum developer performance, **aboalrejal-skills** is built with **zero external dependencies** using pure native Node.js modules. This ensures it downloads and runs globally via `npx` in **under a second** without bloating your system.

---

## ⚡ Quick Start

Run the interactive terminal interface instantly with no installation required:

```bash
npx aboalrejal-skills
```

---

## 💡 Key Features

* **Zero-Dependency Core**: Run instantly worldwide. No massive `node_modules` downloads.
* **Interactive Terminal UI**: Full arrow-key navigation and beautiful color interfaces inside your standard Terminal.
* **Offline-Ready Flow**: Automatically reads from your local repository files if present, otherwise falls back seamlessly to the cloud.
* **20+ Supported Platforms**: Autoconfigures rules and paths for all major agent environments (Claude Code, Antigravity, Cursor, Devin, Aider, and more!).

---

## 📂 Sub-commands

For scriptable workflows, you can trigger specific actions directly:

### 1. List all available skills
Lists the active directory catalog and categories.
```bash
npx aboalrejal-skills list
```

### 2. Search skills by keyword
Finds and prints skills matching your search terms.
```bash
npx aboalrejal-skills search <keyword>
# Example: npx aboalrejal-skills search seo
```

### 3. Install a skill directly
Fetches and copies the skill instructions to your environment immediately.
```bash
npx aboalrejal-skills install <skill-name>
# Example: npx aboalrejal-skills install page-cro
```

---

## 🖥️ Pick Your Platform (Automatic Installation Mappings)

When installing a skill, the CLI prompts you to select one of 20 targets, automatically mapping the instructions to the correct directory structure:

| Platform | Install Command / Action | Configuration Target |
|---|---|---|
| **Google Antigravity** | `npx aboalrejal-skills` | Appends under `~/.gemini/config/plugins/...` |
| **Claude Code (Linux/Mac)** | `npx aboalrejal-skills` | Creates local `.claudecode/skills/...` |
| **Claude Code (Windows)** | `npx aboalrejal-skills` | Creates local `.claudecode/skills/...` |
| **Cursor IDE** | `npx aboalrejal-skills` | Generates a custom rule at `.cursor/rules/<name>.md` |
| **Devin CLI** | `npx aboalrejal-skills` | Places instructions under `.devin/instructions/` |
| **Aider** | `npx aboalrejal-skills` | Saves as a `.aider.instruction.<name>.md` rule |
| **GitHub Copilot CLI** | `npx aboalrejal-skills` | Appends to `.github/copilot-instructions.md` |
| **VS Code Copilot Chat** | `npx aboalrejal-skills` | Appends to `.github/copilot-instructions.md` |
| **Trae & Trae CN** | `npx aboalrejal-skills` | Places rule at `.instructions/<name>.md` |
| **Gemini CLI** | `npx aboalrejal-skills` | Saves inside `.gemini/skills/<name>.md` |
| **Custom CWD** | `npx aboalrejal-skills` | Saves to `/skills/<category>/<name>/SKILL.md` |

---

## 📦 Publishing to NPM

To publish this CLI package globally:

1. Sign in to your NPM account:
   ```bash
   npm login
   ```
2. Publish from the `cli` folder:
   ```bash
   cd cli
   npm publish --access public
   ```

*Now, users can also install it globally!*
```bash
npm install -g aboalrejal-skills
aboalrejal-skills
```
