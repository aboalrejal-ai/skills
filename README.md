# 🌱 Abo Alrejal Agentic Skills Hub

> *Curated, high-performance modular skills and prompt guidelines for AI coding agents.*

This repository contains a premium, developer-focused collection of agentic skills optimized for **Claude Code, Cursor, Antigravity IDE, and Gemini CLI**. 

Unlike massive, unorganized prompt libraries, this hub is curated to provide precise instructions and strict quality gates for your daily development workflows.

---

## ⚡ Quick Start & Installation

Install these skills globally or locally into your active developer workspace using the official Vercel **Skills CLI**:

### 1. Interactive Installation (Recommended)
To browse and select which skills to install:
```bash
npx skills add aboalrejal-ai/skills
```

### 2. Direct Skill Installation
To install a specific skill directly (e.g., `clean-code-guard`):
```bash
npx skills add aboalrejal-ai/skills --skill clean-code-guard
```

### 3. List Available Skills
To view all skills in this package without installing them:
```bash
npx skills add aboalrejal-ai/skills --list
```

---

## 🛡️ Curated Core Skills (The 5 Active Guards)

These second-pass quality gates catch systematic failure modes of AI-generated code, tests, and documentation before shipping:

| Skill ID | Command / Trigger | Description |
| :--- | :--- | :--- |
| `clean-code-guard` | `$clean-code-guard` | Applies Clean Code, SOLID, DRY/KISS/YAGNI, and checks for AI code smells. |
| `test-guard` | `$test-guard` | Quality gate for tests (mocking boundaries, duplicate tests, test bloat). |
| `docs-guard` | `$docs-guard` | Verifies doc accuracy and prevents documentation-vs-code drift. |
| `wp-guard` | `$wp-guard` | Enforces WordPress security (nonces, escaping, sanitization, core APIs). |
| `woo-guard` | `$woo-guard` | Enforces WooCommerce standards (HPOS compatibility, CRUD over meta, secure checkout). |

---

## ⚙️ Development & Update Guide (للإضافة والتحديث)

Follow these simple steps when adding new skills or updating the catalog:

### 1. How to Add a New Skill manually
1. Create a new directory under `skills/` using lowercase and hyphens:
   ```text
   skills/my-new-skill/
   ```
2. Inside that directory, create a `SKILL.md` file containing the YAML frontmatter and rules:
   ```markdown
   ---
   name: my-new-skill
   description: "A short description of what this skill does."
   category: "category-name"
   risk: "safe"
   ---
   # My New Skill Rules...
   ```

### 2. How to Update the Indexes and Web UI Catalog
Whenever you add, modify, or delete a skill, run this command in the project root:
```bash
npm run sync:all && npm run app:setup
```

**What this command does:**
* `npm run sync:all`: Validates the skills, updates the main index files (`skills_index.json` and `data/skills_index.json`), and regenerates index metadata.
* `npm run app:setup`: Mirrors the updated database to the web application public directory (`apps/web-app/public/skills.json`) so the changes show up in your local web browser interface immediately.

---

## 📄 License
Released under the [MIT License](LICENSE). Curated by **Mohammed Abo Alrejal**.
