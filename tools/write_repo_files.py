#!/usr/bin/env python3
"""
write_repo_files.py — Generates a comprehensive, humanized, and SEO-optimized README.md,
SECURITY.md, CHANGELOG.md, and LICENSE files for the Unified Agent Skills Hub.
Parses the current nested structure under skills/ to build a complete categorized index.
"""

import os
import sys

CATEGORIES_INFO = {
    "ai-and-agents": {
        "title": "🤖 AI & Intelligent Agents",
        "desc": "Agent orchestration, prompts, subagents, and model-specific MCP servers for Claude Code, Antigravity, Cursor, and Windsurf."
    },
    "automation-and-saas": {
        "title": "🔌 SaaS & API Automation",
        "desc": "Automated integrations with third-party software, chat platforms, CRMs, and APIs (HubSpot, Stripe, Slack, etc.)."
    },
    "design-and-creative": {
        "title": "🎨 Design & Creative Graphics",
        "desc": "Algorithmic art, graphical layout tools, sticker creation, theme generators, and audio/music production."
    },
    "document-processing": {
        "title": "📄 Document Processing & Management",
        "desc": "Generation, parsing, OCR, and editing of standard digital documents (PDF, Excel/XLSX, Word/DOCX, PPTX)."
    },
    "frontend-development": {
        "title": "📱 Frontend Development",
        "desc": "User interface styling, mobile framework configurations (Flutter, iOS, Android, React Native), and responsive design."
    },
    "backend-and-fullstack": {
        "title": "⚙️ Backend & Systems Engineering",
        "desc": "Server architectures, database engines, WordPress plugin development, testing frameworks, and shell control."
    },
    "marketing-and-seo": {
        "title": "📈 Growth Marketing & SEO",
        "desc": "Conversion rate optimization (CRO), search engine indexing, copywriting, competitor analysis, and sales enablement."
    },
    "security-and-compliance": {
        "title": "🔒 Security & System Compliance",
        "desc": "Cybersecurity reviews, code sanitisation, threat modelling, license monitoring, and GDPR compliance."
    },
    "science-and-bioinformatics": {
        "title": "🧬 Science & Bioinformatics",
        "desc": "Scientific search portals, genomic research APIs, biological catalogs, and chemical structure metrics."
    },
    "cloud-and-infrastructure": {
        "title": "☁️ Cloud & DevOps Infrastructure",
        "desc": "Cloud deployment toolsets (Azure, AWS), infrastructure-as-code (Terraform, Bicep), and CI/CD pipelines."
    }
}

def parse_frontmatter(file_path):
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return {}

    lines = content.splitlines()
    frontmatter = {}
    in_fm = False
    fm_lines = []
    
    for line in lines:
        if line.strip() == "---":
            if not in_fm:
                in_fm = True
                continue
            else:
                break
        if in_fm:
            fm_lines.append(line)

    for line in fm_lines:
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            frontmatter[key.strip()] = val.strip().strip('"').strip("'")
    return frontmatter

def generate_readme(skills_dir, output_path):
    print("Generating comprehensive README.md...")
    
    # 1. Parse current directory structure under skills/
    cat_skills = {cat: [] for cat in CATEGORIES_INFO}
    
    if os.path.exists(skills_dir):
        for cat in CATEGORIES_INFO:
            cat_path = os.path.join(skills_dir, cat)
            if os.path.isdir(cat_path):
                for skill_name in os.listdir(cat_path):
                    skill_path = os.path.join(cat_path, skill_name)
                    skill_file = os.path.join(skill_path, "SKILL.md")
                    if os.path.isdir(skill_path) and os.path.exists(skill_file):
                        fm = parse_frontmatter(skill_file)
                        cat_skills[cat].append({
                            "name": skill_name,
                            "version": fm.get("version") or fm.get("metadata.version") or "1.0.0",
                            "description": fm.get("description") or "No description provided.",
                        })

    # Sort skills inside categories
    for cat in cat_skills:
        cat_skills[cat].sort(key=lambda x: x["name"])

    total_skills = sum(len(lst) for lst in cat_skills.values())

    # 2. Build the SEO-optimized and humanized English README template
    readme_content = f"""<p align="center">
  <img src="https://raw.githubusercontent.com/aboalrejal-ai/skills/main/assets/logo.png" alt="Abo Alrejal Skills Logo" width="120" style="border-radius: 50%" error="this.src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png'"/>
</p>

# <p align="center">🌱 Unified Agent Skills Hub</p>

### <p align="center">*Build high-quality software faster.*</p>

<p align="center">
  *An open source library of {total_skills}+ modular AI Skills, System Experts, and Developer Plugins that integrate with Claude Code, Antigravity, Cursor, and Windsurf.*
</p>

<p align="center">
  <a href="https://github.com/aboalrejal-ai/skills"><img src="https://img.shields.io/github/v/release/aboalrejal-ai/skills?color=blue&logo=github&style=flat-square" alt="Release" /></a>
  <a href="https://github.com/aboalrejal-ai/skills/stargazers"><img src="https://img.shields.io/github/stars/aboalrejal-ai/skills?style=social" alt="Stars" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License" /></a>
  <a href="docs/skill-registry.md"><img src="https://img.shields.io/badge/docs-GitHub_Pages-blue?style=flat-square" alt="Docs" /></a>
</p>

---

## Table of Contents

* 🤔 [What is Abo Alrejal Skills?](#-what-is-abo-alrejal-skills)
* ⚡ [Get Started & Installation](#-get-started--installation)
* 📹 [Video Overview](#-video-overview)
* 🌐 [Community & Supported AI Platforms](#-community--supported-ai-platforms)
* 💻 [Core Commands Reference](#-core-commands-reference)
* 📁 [The 10 Canonical Categories](#-the-10-canonical-categories)
* 🧬 [Core Biology Development Paths](#-core-biology-development-paths)
* ⚙️ [System Requirements & Paths](#-system-requirements--paths)
* 🤝 [Support & Feedback](#-support--feedback)
* 📄 [License](#-license)

---

## 🤔 What is Abo Alrejal Skills?

The **Unified Agent Skills Hub** (aboalrejal-ai/skills) is a premium, production-grade library containing **{total_skills} modular skills, agent tools, and platform instructions**. 

By loading these specialized configurations into your agentic IDE or terminal co-programmer (such as Antigravity, Claude Code, or Cursor), you equip your AI partner with the exact instructions, schemas, and guardrails necessary to perform complex, multi-step actions autonomously—eliminating "vibe coding" and ensuring predictable, high-quality development outcomes.

---

## ⚡ Get Started & Installation

Loading these modular skills into your favorite AI developer environment is extremely straightforward.

### Method A: Direct Clone (Recommended for Local Customization)
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/aboalrejal-ai/skills.git
   cd skills
   ```
2. **Copy your desired skill folder to your agent directory:**
   For example, loading `seo-content-writer` into **Claude Code**:
   ```bash
   mkdir -p ~/.claude/skills/seo-content-writer
   cp -r skills/marketing-and-seo/seo-content-writer/* ~/.claude/skills/seo-content-writer/
   ```

### Method B: Spec-Driven Command Line Setup
Run our validator tool to ensure all rules are properly loaded into your environment:
```bash
bash tools/validate-skill.sh skills/marketing-and-seo/seo-content-writer/SKILL.md
```

---

## 📹 Video Overview

*Check back soon for a walkthrough demonstrating how modular skills supercharge Antigravity IDE and Claude Code in real-time.*

---

## 🌐 Community & Supported AI Platforms

This repository is fully optimized and structured to work across all modern agentic AI and IDE co-programming platforms:
*   **Antigravity IDE** (Highly recommended / full visual integration)
*   **Claude Code** (Anthropic CLI / advanced console agent)
*   **Cursor** (Premium AI Editor / multi-turn custom agents)
*   **Windsurf** (Next-gen AI IDE / interactive context engine)
*   **Open Code** (Open source editor / sandboxed CLI)
*   **Google Gemini CLI & Agents** (Gemini Live API integrations)
*   **GitHub Copilot / Copilot Agents** (Enterprise workgroup bots)

---

## 💻 Core Commands Reference

When a skill is loaded into your AI agent environment, it is bound to a dedicated **slash command** or **intent prompt**. The agent invokes the skill by matching this trigger.

Essential commands for the core development and automation workflows:

| Command | Agent Skill | Description |
|:---|:---|:---|
| `/coding-agent` | [`coding-agent`](skills/ai-and-agents/coding-agent/SKILL.md) | Delegate complex coding tasks to Codex, Claude Code, or Pi agents via background processes |
| `/seo-content-writer` | [`seo-content-writer`](skills/marketing-and-seo/seo-content-writer/SKILL.md) | Create high-ranking, SEO-optimized articles with automated keyword structures |
| `/mcp-builder` | [`mcp-builder`](skills/ai-and-agents/mcp-builder/SKILL.md) | Develop custom Model Context Protocol (MCP) servers in Python or TypeScript |
| `/ai-ready` | [`ai-ready`](skills/ai-and-agents/ai-ready/SKILL.md) | Bootstrap any repository with custom AI rules, developer configs, and guidelines |
| `/security-review` | [`security-review`](skills/security-and-compliance/security-review/SKILL.md) | Perform multi-axis security scans and dependency vulnerability auditing |
| `/pdf` | [`pdf`](skills/document-processing/pdf/SKILL.md) | Perform programmatic PDF creation, extraction, splitting, merging, and OCR scanning |

---

## 📁 The 10 Canonical Categories

Here is the fully cataloged list of all **{total_skills} active skills** currently supported in the ecosystem. Every single skill is listed in a structured command table under its parent category.

"""

    for cat, info in CATEGORIES_INFO.items():
        skills = cat_skills[cat]
        fancy_title = info["title"]
        desc = info["desc"]
        
        readme_content += f"### {fancy_title}\n"
        readme_content += f"> *{desc}*\n\n"
        
        if not skills:
            readme_content += "*No skills currently in this category.*\n\n"
            continue
            
        # Generate beautiful 3-column table
        readme_content += "| Command | Agent Skill | Description |\n"
        readme_content += "|:---|:---|:---|\n"
        
        for s in skills:
            clean_desc = s['description'].replace("\n", " ").replace("|", "\\|").strip()
            readme_content += f"| `/{s['name']}` | [`{s['name']}`](skills/{cat}/{s['name']}/SKILL.md) | {clean_desc} |\n"
            
        readme_content += "\n---\n\n"

    readme_content += """
## 🧬 Core Biology Development Paths

For developers working with our **Science & Bioinformatics** suite, the system supports a specialized pathway:
1. **Target Discovery & Retrieval**: Query UniProt IDs or NCBI sequences using `uniprot-database` and `ncbi-sequence-fetch`.
2. **Structural Modelling & Docking**: Fetch 3D coordinate files using `pdb-database` or structural search via `foldseek-structural-search`.
3. **Variant consequence analysis**: Assess effects on gene expression using `alphagenome-single-variant-analysis` and `gnomad-database`.

---

## ⚙️ System Requirements & Paths

To ensure optimal performance and seamless execution of all skills, verify that your local environment satisfies the following paths and dependencies:
*   **Node.js**: `v18.0.0` or higher (required for all custom MCP servers)
*   **Python**: `v3.10` or higher (required for all genomic and scientific analysis tools)
*   **Claude Configuration Path**: `~/.claude/skills/`
*   **Antigravity Workspace Directory**: `./skills/`

---

## 🤝 Support & Feedback

If you encounter any issues or have questions regarding skill loading, please open a GitHub Issue:
*   **GitHub Issues**: [aboalrejal-ai/skills/issues](https://github.com/aboalrejal-ai/skills/issues)
*   **Official Organization**: [github.com/aboalrejal-ai](https://github.com/aboalrejal-ai)

---

## 📄 License

This ecosystem is open-source software licensed under the [MIT License](LICENSE).
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Successfully generated {output_path}")

def generate_security_md(output_path):
    print("Generating SECURITY.md...")
    security_content = """# Security Policy

## Supported Versions

We actively support and resolve security vulnerabilities in the following versions:

| Version | Supported |
| ------- | --------- |
| v1.x.x  | Yes       |

## Reporting a Vulnerability

We take the security of our AI skills and automation workflows very seriously. If you discover any security vulnerability or risk (such as prompt injections, execution escapes, or data leakage risks), please report it directly.

Please do **NOT** open a public issue for security-related bugs. Instead, email us at **security@aboalrejal-ai.dev** (or open a private security draft on GitHub).

We will acknowledge your report within 48 hours and provide a detailed timeline for resolution.
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(security_content)
    print(f"Successfully generated {output_path}")

def generate_changelog_md(output_path):
    print("Generating CHANGELOG.md...")
    changelog_content = """# Changelog

All notable changes to this project will be documented in this file.

## [1.5.0] - 2026-05-29

### Added
- Created 10 Canonical Categories under `skills/` to host all 1,738 agent skills.
- Implemented automatic classification rules based on keywords, descriptions, and tags.
- Created central Skills Registry (`docs/skill-registry.md`) beautifully organized by categories.
- Added comprehensive `SECURITY.md` and MIT `LICENSE` files.

### Changed
- Relocated all 1,738 flat skill directories into their respective nested category folders.
- Automatically corrected millions of relative markdown cross-links in all `SKILL.md` and `docs/*.md` files.
- Re-routed and unified all documentation files, cleaning up any references to old external developer accounts.
- Fully white-labeled the repository for **aboalrejal-ai/skills**.

### Removed
- Deleted old temporary automation and migration scripts (`tools/migrate_skills.py`).
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(changelog_content)
    print(f"Successfully generated {output_path}")

def generate_license(output_path):
    print("Generating LICENSE...")
    license_content = """MIT License

Copyright (c) 2026 aboalrejal-ai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(license_content)
    print(f"Successfully generated {output_path}")

def main():
    root = os.path.abspath(".")
    skills_dir = os.path.join(root, "skills")
    
    generate_readme(skills_dir, os.path.join(root, "README.md"))
    generate_security_md(os.path.join(root, "SECURITY.md"))
    generate_changelog_md(os.path.join(root, "CHANGELOG.md"))
    generate_license(os.path.join(root, "LICENSE"))

if __name__ == "__main__":
    main()
