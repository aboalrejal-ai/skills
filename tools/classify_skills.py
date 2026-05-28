#!/usr/bin/env python3
"""
classify_skills.py — Reorganizes flat skills into 10 canonical categories.
Automates classification, folder movements, relative markdown link updates, and
regenerating a beautifully formatted docs/skill-registry.md directory catalog.
"""

import os
import sys
import shutil
import re
import argparse

# Color constants for terminal output
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
RED = "\033[0;31m"
BLUE = "\033[0;34m"
NC = "\033[0m"

def log_info(msg):
    print(f"{BLUE}[INFO]{NC} {msg}")

def log_success(msg):
    print(f"{GREEN}[SUCCESS]{NC} {msg}")

def log_warn(msg):
    print(f"{YELLOW}[WARNING]{NC} {msg}")

def log_error(msg):
    print(f"{RED}[ERROR]{NC} {msg}")

CATEGORIES = {
    "ai-and-agents": [
        "mcp", "llm", "claude", "gemini", "agent", "prompt", "subagent", "ai-overview", 
        "geo-content-optimizer", "ai-seo", "v0-automation", "openai", "anthropic", "gpt", 
        "co-authoring", "using-skills", "subagent-driven-development", "sharing-skills", 
        "testing-skills-with-subagents", "gardening-skills-wiki", "remembering-conversations"
    ],
    "automation-and-saas": [
        "automation", "api", "hubspot", "stripe", "slack", "composio", "activecampaign", 
        "pipedrive", "clickup", "monday", "zoom", "freshbooks", "clockify", "freshdesk", 
        "mailgun", "twilio", "zapier", "make.com", "trello", "jira", "salesforce", "zendesk", 
        "intercom", "asana", "notion", "github-automation", "gitlab-automation", "airtable", 
        "mailchimp", "sendgrid", "klaviyo", "mail", "sms", "integration", "webhook"
    ],
    "design-and-creative": [
        "design", "art", "graphic", "gif", "sticker", "theme", "video", "music", "playlist", 
        "canvas", "p5js", "shader", "creative", "logo", "banner", "poster", "visual", "color", 
        "animation", "rendering", "sound", "audio", "voice", "speech", "elevenlabs", "heygen"
    ],
    "document-processing": [
        "pdf", "docx", "xlsx", "pptx", "excel", "word", "powerpoint", "csv", "document", 
        "markitdown", "sheet", "spreadsheet", "txt", "markdown-to-html", "text-to-pdf"
    ],
    "frontend-development": [
        "frontend", "html", "css", "react", "vue", "flutter", "ios", "android", "mobile", 
        "responsive", "component", "tailwind", "ui", "ux", "styling", "layout", "web-perf", 
        "bootstrap", "material", "nextjs", "vite", "javascript", "typescript", "npm", "yarn"
    ],
    "backend-and-fullstack": [
        "backend", "fullstack", "database", "sql", "nosql", "git", "docker", "wordpress", 
        "wp-", "testing", "express", "node", "unix", "shell", "bash", "server", "django", 
        "flask", "python", "php", "java", "dotnet", "csharp", "rust", "go-lang", "postgres", 
        "mysql", "mongodb", "redis", "graphql", "rest-api", "api-development", "prisma"
    ],
    "marketing-and-seo": [
        "seo", "cro", "copywriting", "marketing", "competitor", "keyword", "paid-ads", 
        "social-content", "pricing-strategy", "referral", "sales", "analytics", "funnel", 
        "audience", "lead", "email-sequence", "outreach", "cold-email", "pitch", "proposal", 
        "gsc", "google-analytics", "tagmanager", "semrush", "ahrefs"
    ],
    "security-and-compliance": [
        "security", "threat", "compliance", "gdpr", "license", "defense", "penetration", 
        "auth", "login", "encryption", "ssl", "oauth", "jwt", "hashing", "cors", "injection"
    ],
    "science-and-bioinformatics": [
        "uniprot", "gene", "protein", "clinical-trials", "clinvar", "dbsnp", "gnomad", 
        "alphafold", "chembl", "pubmed", "biology", "science", "scientific", "dna", "rna", 
        "sequence", "biomedical", "medical", "disease", "pathology", "cell", "tissue"
    ],
    "cloud-and-infrastructure": [
        "cloud", "azure", "aws", "terraform", "bicep", "devops", "cicd", "deploy", "coolify", 
        "docker-compose", "kubernetes", "hosting", "s3", "lambda", "ec2", "gcp", "serverless"
    ]
}

CATEGORY_NAMES = list(CATEGORIES.keys())

def parse_frontmatter(file_path):
    """
    Parses YAML frontmatter between the first two '---' lines.
    """
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

class SkillClassifier:
    def __init__(self, workspace_root, dry_run=False):
        self.root = os.path.abspath(workspace_root)
        self.skills_dir = os.path.join(self.root, "skills")
        self.docs_dir = os.path.join(self.root, "docs")
        self.dry_run = dry_run
        self.skill_to_category = {} # Map: skill_dir_name -> category

    def classify_skill(self, dir_name, skill_path):
        """
        Classifies a single skill using scoring based on name, description, and tags.
        """
        skill_file = os.path.join(skill_path, "SKILL.md")
        fm = parse_frontmatter(skill_file) if os.path.exists(skill_file) else {}
        
        name = fm.get("name", dir_name).lower()
        description = fm.get("description", "").lower()
        tags = fm.get("when_to_use", "").lower() + " " + fm.get("class", "").lower()

        scores = {cat: 0 for cat in CATEGORIES}

        for cat, keywords in CATEGORIES.items():
            for kw in keywords:
                # Direct match in folder name (highest weight)
                if kw in dir_name.lower():
                    scores[cat] += 5
                # Match in frontmatter name
                if kw in name:
                    scores[cat] += 4
                # Match in tags / class
                if kw in tags:
                    scores[cat] += 3
                # Match in description
                if kw in description:
                    scores[cat] += 1

        max_score = max(scores.values())
        if max_score > 0:
            # Return category with highest score
            best_cats = [cat for cat, score in scores.items() if score == max_score]
            return best_cats[0]

        # Fallbacks for zero-scores
        lower_dir = dir_name.lower()
        if "automation" in lower_dir or lower_dir.endswith("-automation"):
            return "automation-and-saas"
        if "azure" in lower_dir or "aws" in lower_dir or "cloud" in lower_dir:
            return "cloud-and-infrastructure"
        if lower_dir.startswith("wp-") or "wordpress" in lower_dir:
            return "backend-and-fullstack"
        if "test" in lower_dir or "testing" in lower_dir:
            return "backend-and-fullstack"
            
        return "backend-and-fullstack"

    def run_reorganization(self):
        """
        Executes the categorisation and file movements.
        """
        if not os.path.exists(self.skills_dir):
            log_error(f"Skills directory not found at {self.skills_dir}")
            return

        # 1. Identify all skills to classify
        skills_to_process = []
        for name in os.listdir(self.skills_dir):
            skill_path = os.path.join(self.skills_dir, name)
            # Skip category folders themselves to ensure idempotence
            if name in CATEGORY_NAMES:
                continue
            if os.path.isdir(skill_path):
                skills_to_process.append(name)

        log_info(f"Found {len(skills_to_process)} flat skills to classify.")

        # 2. Compute classification map
        for name in skills_to_process:
            skill_path = os.path.join(self.skills_dir, name)
            category = self.classify_skill(name, skill_path)
            self.skill_to_category[name] = category

        # 3. Create folders and perform moves (if not dry_run)
        moved_count = 0
        for name, category in self.skill_to_category.items():
            src_dir = os.path.join(self.skills_dir, name)
            dest_cat_dir = os.path.join(self.skills_dir, category)
            dest_dir = os.path.join(dest_cat_dir, name)

            if self.dry_run:
                print(f"[DRY-RUN] Move {name} -> skills/{category}/{name}")
                moved_count += 1
            else:
                try:
                    os.makedirs(dest_cat_dir, exist_ok=True)
                    if os.path.exists(dest_dir):
                        shutil.rmtree(dest_dir)
                    shutil.move(src_dir, dest_dir)
                    moved_count += 1
                except Exception as e:
                    log_error(f"Failed to move {name}: {e}")

        log_success(f"Successfully processed {moved_count} skills into their categories.")

        # 4. Correct relative markdown links
        self.update_markdown_links()

        # 5. Regenerate Skills Registry
        self.regenerate_skills_registry()

        # 6. Update routes in Resolver
        self.update_resolver_routes()

    def update_markdown_links(self):
        """
        Updates all relative markdown links referencing skills to point to their new nested folder.
        """
        log_info("Updating relative markdown links across docs/ and skills/...")
        
        # Build a list of files to search and replace inside
        files_to_update = []
        
        # Files under docs/
        if os.path.exists(self.docs_dir):
            for root_dir, _, filenames in os.walk(self.docs_dir):
                for f in filenames:
                    if f.endswith(".md"):
                        files_to_update.append(os.path.join(root_dir, f))

        # Files under skills/ (category subfolders)
        if os.path.exists(self.skills_dir):
            for root_dir, _, filenames in os.walk(self.skills_dir):
                for f in filenames:
                    if f.endswith(".md"):
                        files_to_update.append(os.path.join(root_dir, f))

        # Perform link corrections
        corrected_count = 0
        for filepath in files_to_update:
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue

            original_content = content
            
            # 1. Update relative links from docs: `[skill](../skills/skill)` -> `[skill](../skills/category/skill)`
            for skill_name, category in self.skill_to_category.items():
                old_link_pattern = rf'\[([^\]]+)\]\(\.\./skills/{re.escape(skill_name)}\)'
                new_link = f"[\\1](../skills/{category}/{skill_name})"
                content = re.sub(old_link_pattern, new_link, content)
                
                old_link_pattern_full = rf'\[([^\]]+)\]\(skills/{re.escape(skill_name)}\)'
                new_link_full = f"[\\1](skills/{category}/{skill_name})"
                content = re.sub(old_link_pattern_full, new_link_full, content)

            # 2. Update relative links inside skills: `[other](../other)` -> `[other](../category/other)`
            # Since skills are now inside `skills/<category>/<skill>`, sibling links must go up one folder.
            if "skills" in filepath:
                # Extract the current skill's folder name and its category
                parts = os.path.normpath(filepath).split(os.sep)
                # Sibling links inside SKILL.md are of form `[name](../name)` or `[name](../name/SKILL.md)`
                for skill_name, category in self.skill_to_category.items():
                    old_sibling_pattern = rf'\[([^\]]+)\]\(\.\./{re.escape(skill_name)}\)'
                    new_sibling_link = f"[\\1](../{category}/{skill_name})"
                    content = re.sub(old_sibling_pattern, new_sibling_link, content)
                    
                    old_sibling_pattern_md = rf'\[([^\]]+)\]\(\.\./{re.escape(skill_name)}/SKILL\.md\)'
                    new_sibling_link_md = f"[\\1](../{category}/{skill_name}/SKILL.md)"
                    content = re.sub(old_sibling_pattern_md, new_sibling_link_md, content)

            if content != original_content:
                if self.dry_run:
                    log_info(f"[DRY-RUN] Would update links in {os.path.basename(filepath)}")
                else:
                    try:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(content)
                        corrected_count += 1
                    except Exception as e:
                        log_error(f"Failed to write updated links in {filepath}: {e}")

        if not self.dry_run:
            log_success(f"Corrected relative links in {corrected_count} files.")

    def regenerate_skills_registry(self):
        """
        Regenerates docs/skill-registry.md with beautiful categorised sections.
        """
        log_info("Regenerating categorized docs/skill-registry.md...")
        
        # Build category lists
        cat_skills = {cat: [] for cat in CATEGORIES}
        
        for name in os.listdir(self.skills_dir):
            cat_path = os.path.join(self.skills_dir, name)
            if name in CATEGORY_NAMES and os.path.isdir(cat_path):
                for skill_name in os.listdir(cat_path):
                    skill_path = os.path.join(cat_path, skill_name)
                    skill_file = os.path.join(skill_path, "SKILL.md")
                    if os.path.isdir(skill_path) and os.path.exists(skill_file):
                        fm = parse_frontmatter(skill_file)
                        cat_skills[name].append({
                            "name": skill_name,
                            "version": fm.get("version") or fm.get("metadata.version") or "1.0.0",
                            "description": fm.get("description") or "No description provided.",
                            "class": fm.get("class") or "standard"
                        })

        # Sort within each category
        for cat in cat_skills:
            cat_skills[cat].sort(key=lambda x: x["name"])

        total_skills = sum(len(lst) for lst in cat_skills.values())

        # Build markdown catalog
        md = f"""# Skills Registry & Catalog

Welcome to the **Unified Agent Skills Hub**! This registry alphabetically indexes all **{total_skills} active skills** currently supported, beautifully organized into **10 Canonical Categories** for easy access. Click any skill's name to navigate directly to its implementation directory and instruction block.

---

## 📂 Category Quick-Links
"""
        # Add category anchors
        for cat in CATEGORIES:
            fancy_name = cat.replace("-", " ").title().replace("Seo", "SEO").replace("Saas", "SaaS").replace("Ai", "AI")
            count = len(cat_skills[cat])
            md += f"*   **[# {fancy_name}](#-{cat})** ({count} Skills)\n"

        md += "\n---\n"

        # Generate tables for each category
        for cat in CATEGORIES:
            fancy_name = cat.replace("-", " ").title().replace("Seo", "SEO").replace("Saas", "SaaS").replace("Ai", "AI")
            skills = cat_skills[cat]
            
            md += f"\n## 📁 {fancy_name} ({len(skills)} Skills)\n\n"
            md += "| Name | Class | Version | Description |\n"
            md += "|------|-------|---------|-------------|\n"
            
            for s in skills:
                class_badge = f"`{s['class']}`" if s['class'] == 'auditor' else "Standard"
                desc = s['description']
                if len(desc) > 120:
                    desc = desc[:117] + "..."
                
                md += f"| **[{s['name']}](../skills/{cat}/{s['name']}/SKILL.md)** | {class_badge} | v{s['version']} | {desc} |\n"
            
            md += "\n---\n"

        md += """
## 📄 Core Architecture & Decisions
*   **[Skill Contract](skill-contract.md)**: The strict skeleton that every skill must follow (Quick Start, reads, writes, promotes, and next best skill).
*   **[Skill Resolver](skill-resolver.md)**: Resolves user intent to the primary skill and sequence handoff rules.
*   **[Auditor Runbook](auditor-runbook.md)**: Rules and protocols for auditor-class gate reviews.
"""

        if self.dry_run:
            log_info(f"[DRY-RUN] Would write docs/skill-registry.md with {total_skills} categorized entries.")
            return

        registry_path = os.path.join(self.docs_dir, "skill-registry.md")
        try:
            with open(registry_path, "w", encoding="utf-8") as f:
                f.write(md)
            log_success(f"Successfully generated {registry_path}")
        except Exception as e:
            log_error(f"Failed to write skill registry: {e}")

    def update_resolver_routes(self):
        """
        Updates the primary routes inside docs/skill-resolver.md to point to their new nested folder path.
        """
        log_info("Updating skill-resolver.md routes...")
        resolver_path = os.path.join(self.docs_dir, "skill-resolver.md")
        if not os.path.exists(resolver_path):
            return

        try:
            with open(resolver_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception:
            return

        original_content = content

        # Replace plaintext skill routes in tables to point to correct subfolders
        # The skill name inside the primary route column is matched.
        for skill_name, category in self.skill_to_category.items():
            # Match `| skill-name |` or similar in resolver tables and replace with relative link or nested route
            pattern = rf'\|\s*{re.escape(skill_name)}\s*\|'
            replacement = f"| [{skill_name}](../skills/{category}/{skill_name}) |"
            content = re.sub(pattern, replacement, content)

        if content != original_content:
            if self.dry_run:
                log_info("[DRY-RUN] Would update docs/skill-resolver.md routes")
            else:
                try:
                    with open(resolver_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    log_success("Successfully updated docs/skill-resolver.md routes.")
                except Exception as e:
                    log_error(f"Failed to write skill resolver: {e}")

def main():
    parser = argparse.ArgumentParser(description="Categorise and Reorganize Agent Skills.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument("--dry-run", action="store_true", help="Print operations without performing them.")
    args = parser.parse_args()

    classifier = SkillClassifier(args.root, dry_run=args.dry_run)
    classifier.run_reorganization()

if __name__ == "__main__":
    main()
