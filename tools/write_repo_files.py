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
        "title": "🤖 AI & Intelligent Agents (الذكاء الاصطناعي والعملاء الأذكياء)",
        "desc": "Agent orchestration, prompts, subagents, and model-specific MCP servers for Claude Code, Antigravity, Cursor, and Windsurf."
    },
    "automation-and-saas": {
        "title": "🔌 SaaS & API Automation (أتمتة الأنظمة والـ SaaS)",
        "desc": "Automated integrations with third-party software, chat platforms, CRMs, and APIs (HubSpot, Stripe, Slack, etc.)."
    },
    "design-and-creative": {
        "title": "🎨 Design & Creative Graphics (التصميم والفنون الإبداعية)",
        "desc": "Algorithmic art, graphical layout tools, sticker creation, theme generators, and audio/music production."
    },
    "document-processing": {
        "title": "📄 Document Processing & Management (معالجة وإدارة المستندات)",
        "desc": "Generation, parsing, OCR, and editing of standard digital documents (PDF, Excel/XLSX, Word/DOCX, PPTX)."
    },
    "frontend-development": {
        "title": "📱 Frontend Development (برمجة وتطوير الواجهات)",
        "desc": "User interface styling, mobile framework configurations (Flutter, iOS, Android, React Native), and responsive design."
    },
    "backend-and-fullstack": {
        "title": "⚙️ Backend & Systems Engineering (هندسة الخلفية والأنظمة)",
        "desc": "Server architectures, database engines, WordPress plugin development, testing frameworks, and shell control."
    },
    "marketing-and-seo": {
        "title": "📈 Growth Marketing & SEO (التسويق الرقمي والـ SEO)",
        "desc": "Conversion rate optimization (CRO), search engine indexing, copywriting, competitor analysis, and sales enablement."
    },
    "security-and-compliance": {
        "title": "🔒 Security & System Compliance (الأمن والحماية الرقمية)",
        "desc": "Cybersecurity reviews, code sanitisation, threat modelling, license monitoring, and GDPR compliance."
    },
    "science-and-bioinformatics": {
        "title": "🧬 Science & Bioinformatics (العلوم والمعلوماتية الحيوية)",
        "desc": "Scientific search portals, genomic research APIs, biological catalogs, and chemical structure metrics."
    },
    "cloud-and-infrastructure": {
        "title": "☁️ Cloud & DevOps Infrastructure (الحوسبة السحابية والبنية التحتية)",
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

    # 2. Build the SEO-optimized and humanized Arabic/English README template
    readme_content = f"""# 🚀 Unified Agent Skills Hub | مستودع المهارات الموحد للعملاء الأذكياء

Welcome to the **Unified Agent Skills Hub**—the largest, most comprehensive open source library of modular AI Skills, System Experts, and Developer Plugins.

مرحباً بكم في **مستودع المهارات الموحد للعملاء الأذكياء**—أضخم مكتبة مفتوحة المصدر لمهارات الذكاء الاصطناعي، والخبراء الأنظمة، وإضافات المطورين في العالم. تم إعداد وتوثيق هذه المهارات بعناية فائقة لتتوافق برمجياً وتعمل بسلاسة تامة مع كبرى منصات وبيئات التطوير الذكية.

---

## 🌟 Supported Environments & Providers | البيئات والمنصات المدعومة

This repository is fully optimized and structured to work across all modern agentic AI and IDE co-programming platforms:
*   **Antigravity IDE** (Highly recommended / موصى به بشدة)
*   **Claude Code** (Anthropic CLI / واجهة أوامر كلود)
*   **Cursor** (Premium AI Editor / محرّر كرسر الذكي)
*   **Windsurf** (Next-gen AI IDE / الجيل الجديد من بيئات التطوير)
*   **Open Code** (Open source editor / المحرّر المفتوح)
*   **Google Gemini CLI & Agents** (Gemini eco-system / منظومة جيميني)
*   **GitHub Copilot / Copilot Agents** (Microsoft Copilot / كوبايلوت)

---

## 🏗️ Repository Architecture | هيكلية المستودع

The directory has a clean, production ready, and highly modular design:
*   **`skills/`**: The core directory housing all individual skill folders, neatly organized into 10 canonical categories.
*   **`docs/`**: Global architectural guidelines, scoring benchmarks (CORE-EEAT, CITE), ADRs, and intent resolvers.
*   **`agents/`**: Core specialist agent profiles (Coding, Security, Automation, Research, Content, and Marketing).
*   **`tools/`**: Local validation tools and compliance checker scripts.

---

## 💡 The Complete Skills Directory ({total_skills} Skills) | دليل المهارات الكامل

Here is the fully cataloged list of all active skills in the repository, grouped into **10 Canonical Categories** for instant discoverability. Click any skill's name to navigate directly to its specific implementation folder and `SKILL.md` file:

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
            
        for s in skills:
            readme_content += f"*   **[{s['name']}](skills/{cat}/{s['name']}/SKILL.md)** (v{s['version']}): {s['description']}\n"
            
        readme_content += "\n---\n\n"

    readme_content += """
## 🚀 How to Load and Use Skills | كيفية تحميل واستخدام المهارات

Loading these modular skills into your favorite AI developer environment is extremely simple:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/aboalrejal-ai/skills.git
   cd skills
   ```

2. **Load a Skill into your local Agent (e.g., Claude Code):**
   Copy the target skill directory to your local configuration folder:
   ```bash
   mkdir -p ~/.claude/skills/seo-content-writer
   cp -r skills/marketing-and-seo/seo-content-writer/* ~/.claude/skills/seo-content-writer/
   ```

3. **Verify Compliance:**
   Run the local validation script to ensure frontmatter and format compliance:
   ```bash
   bash tools/validate-skill.sh skills/marketing-and-seo/seo-content-writer/SKILL.md
   ```

---

## 🤝 Contributing & Community | المساهمة والمجتمع

We welcome contributions to scale and improve this repository!
1. Fork this repository.
2. Create a new branch (`git checkout -b feature/NewAmazingSkill`).
3. Add your modular skill inside the correct category under `skills/<category>/`.
4. Validate compliance using `tools/validate-skill.sh`.
5. Submit a Pull Request!
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
