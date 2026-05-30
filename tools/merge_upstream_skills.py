#!/usr/bin/env python3
"""
tools/merge_upstream_skills.py — Merges, classifies, and resolves conflicts
of skills from the upstream repository into our organized 10 canonical categories.
"""

import os
import sys
import hashlib
import shutil
import re
import argparse

# Add current directory to path so we can import classify_skills
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from classify_skills import SkillClassifier, parse_frontmatter, log_info, log_success, log_warn, log_error, CATEGORIES, CATEGORY_NAMES
import write_repo_files

def md5_hash(file_path):
    if not os.path.exists(file_path):
        return ""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except Exception:
        return ""
    return hash_md5.hexdigest()

def parse_version(v_str):
    if not v_str:
        return (0, 0, 0)
    parts = re.findall(r'\d+', str(v_str))
    if not parts:
        return (0, 0, 0)
    return tuple(int(x) for x in parts[:3])

class UpstreamMerger:
    def __init__(self, root_dir, dry_run=False, conflict_policy="report"):
        self.root = os.path.abspath(root_dir)
        self.skills_dir = os.path.join(self.root, "skills")
        self.upstream_dir = os.path.join(self.root, "antigravity-awesome-skills-main", "skills")
        self.dry_run = dry_run
        self.conflict_policy = conflict_policy # "report", "overwrite", "keep-ours"
        
        self.classifier = SkillClassifier(self.root, dry_run=self.dry_run)
        self.workspace_skills = {} # name_lower -> { "name": "...", "category": "...", "path": "..." }

    def scan_workspace_skills(self):
        """
        Builds a map of all currently existing skills in our workspace.
        """
        if not os.path.exists(self.skills_dir):
            os.makedirs(self.skills_dir, exist_ok=True)
            return

        for name in os.listdir(self.skills_dir):
            cat_path = os.path.join(self.skills_dir, name)
            if name in CATEGORY_NAMES and os.path.isdir(cat_path):
                for skill_name in os.listdir(cat_path):
                    skill_path = os.path.join(cat_path, skill_name)
                    if os.path.isdir(skill_path):
                        self.workspace_skills[skill_name.lower()] = {
                            "name": skill_name,
                            "category": name,
                            "path": skill_path
                        }

    def run_merge(self):
        log_info("Scanning workspace and upstream skills...")
        self.scan_workspace_skills()
        
        if not os.path.exists(self.upstream_dir):
            log_error(f"Upstream skills directory not found at {self.upstream_dir}")
            return False

        # Identify all skills in the upstream folder
        upstream_skills = []
        for name in os.listdir(self.upstream_dir):
            upstream_path = os.path.join(self.upstream_dir, name)
            # Skip non-directories or standard markdown files
            if os.path.isdir(upstream_path) and name not in CATEGORY_NAMES and not name.startswith('.'):
                upstream_skills.append(name)

        log_info(f"Found {len(self.workspace_skills)} skills in workspace and {len(upstream_skills)} skills in upstream.")

        new_count = 0
        identical_count = 0
        conflict_count = 0
        updated_count = 0

        # Perform comparison and merging
        for skill_name in sorted(upstream_skills):
            skill_name_lower = skill_name.lower()
            src_path = os.path.join(self.upstream_dir, skill_name)
            
            # Case 1: Skill is missing from our workspace
            if skill_name_lower not in self.workspace_skills:
                # Classify using classifier scoring
                category = self.classifier.classify_skill(skill_name, src_path)
                dest_dir = os.path.join(self.skills_dir, category, skill_name)
                
                new_count += 1
                if self.dry_run:
                    print(f"{src_path} -> [NEW IMPORT] Category: {category}")
                else:
                    try:
                        os.makedirs(os.path.dirname(dest_dir), exist_ok=True)
                        shutil.copytree(src_path, dest_dir, dirs_exist_ok=True)
                        log_success(f"Imported '{skill_name}' to category '{category}'")
                        # Add to classifier internal map for link correction later
                        self.classifier.skill_to_category[skill_name] = category
                    except Exception as e:
                        log_error(f"Failed to copy '{skill_name}': {e}")
            
            # Case 2: Skill exists in both places
            else:
                existing = self.workspace_skills[skill_name_lower]
                dest_dir = existing["path"]
                category = existing["category"]
                
                # Check SKILL.md hash in both locations
                src_skill_md = os.path.join(src_path, "SKILL.md")
                dest_skill_md = os.path.join(dest_dir, "SKILL.md")
                
                src_hash = md5_hash(src_skill_md)
                dest_hash = md5_hash(dest_skill_md)
                
                if src_hash == dest_hash:
                    identical_count += 1
                    # Skip since content matches perfectly
                    continue
                
                # Content differs
                conflict_count += 1
                src_fm = parse_frontmatter(src_skill_md)
                dest_fm = parse_frontmatter(dest_skill_md)
                
                src_version_str = src_fm.get("version") or src_fm.get("metadata.version") or "0.0.0"
                dest_version_str = dest_fm.get("version") or dest_fm.get("metadata.version") or "0.0.0"
                
                src_version = parse_version(src_version_str)
                dest_version = parse_version(dest_version_str)
                
                is_upstream_newer = src_version > dest_version
                
                version_info = f"({dest_version_str} vs upstream {src_version_str})"
                
                if self.dry_run:
                    status = "[NEWER UPSTREAM]" if is_upstream_newer else "[MODIFIED CONTENT]"
                    print(f"{skill_name} -> {status} conflict in {category} {version_info}")
                else:
                    # Apply conflict resolution policies
                    if self.conflict_policy == "overwrite" or (self.conflict_policy == "report" and is_upstream_newer):
                        try:
                            shutil.copytree(src_path, dest_dir, dirs_exist_ok=True)
                            log_success(f"Updated '{skill_name}' in '{category}' to upstream {version_info}")
                            updated_count += 1
                        except Exception as e:
                            log_error(f"Failed to update '{skill_name}': {e}")
                    elif self.conflict_policy == "keep-ours":
                        log_info(f"Skipped updating '{skill_name}' (policy: keep-ours) {version_info}")
                    else:
                        log_warn(f"Conflict detected in '{skill_name}' in category '{category}' {version_info}. Use --overwrite to update.")

        # Print summary report
        log_info("--- Merge Summary ---")
        log_info(f"Total missing skills imported: {new_count}")
        log_info(f"Total identical skills skipped: {identical_count}")
        log_info(f"Total conflicting/differing skills: {conflict_count}")
        if not self.dry_run:
            log_info(f"Total skills successfully updated: {updated_count}")
        log_info("---------------------")

        if self.dry_run:
            log_info("[DRY-RUN] No files were copied or modified.")
            return True

        # Perform Post-Merge Sync
        if new_count > 0 or updated_count > 0:
            log_info("Running Post-Merge synchronization...")
            
            # Step 1: Update markdown relative links
            self.classifier.update_markdown_links()
            
            # Step 2: Regenerate docs/skill-registry.md and skills-registry.json
            self.classifier.regenerate_skills_registry()
            
            # Step 3: Update skill-resolver.md routes
            self.classifier.update_resolver_routes()
            
            # Step 4: Regenerate README.md, SECURITY.md, CHANGELOG.md, LICENSE
            write_repo_files.generate_readme(self.skills_dir, os.path.join(self.root, "README.md"))
            write_repo_files.generate_changelog_md(os.path.join(self.root, "CHANGELOG.md"))
            log_success("Post-merge synchronization complete.")
            
        return True

def main():
    parser = argparse.ArgumentParser(description="Merge skills from upstream into categorized layout.")
    parser.add_argument("--root", default=".", help="Workspace root directory.")
    parser.add_argument("--dry-run", action="store_true", help="Preview moves and conflicts without copying.")
    parser.add_argument("--policy", choices=["report", "overwrite", "keep-ours"], default="report",
                        help="Conflict resolution policy for differing skills. 'report' auto-updates if upstream version is newer.")
    args = parser.parse_args()

    merger = UpstreamMerger(args.root, dry_run=args.dry_run, conflict_policy=args.policy)
    merger.run_merge()

if __name__ == "__main__":
    main()
