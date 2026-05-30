#!/usr/bin/env python3
import os
import json
import pathlib
import shutil
import re
import sys
from collections.abc import Mapping
from datetime import date, datetime

import yaml
from _project_paths import find_repo_root
from plugin_compatibility import build_report as build_plugin_compatibility_report
from plugin_compatibility import compatibility_by_path as plugin_compatibility_by_path

# Ensure UTF-8 output for Windows compatibility
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def normalize_category(category):
    if not isinstance(category, str):
        return category
    return category.strip().lower()


def normalize_yaml_value(value):
    if isinstance(value, Mapping):
        return {key: normalize_yaml_value(val) for key, val in value.items()}
    if isinstance(value, list):
        return [normalize_yaml_value(item) for item in value]
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, (bytes, bytearray)):
        return bytes(value).decode("utf-8", errors="replace")
    return value


def coerce_metadata_text(value):
    if value is None or isinstance(value, (Mapping, list, tuple, set)):
        return None
    if isinstance(value, str):
        return value
    return str(value)


def parse_frontmatter(content):
    fm_match = re.search(r'^---\s*\n(.*?)\n?---(?:\s*\n|$)', content, re.DOTALL)
    if not fm_match:
        return {}
    
    yaml_text = fm_match.group(1)
    
    # Process line by line to handle values containing @ and commas
    sanitized_lines = []
    for line in yaml_text.splitlines():
        match = re.match(r'^(\s*[\w-]+):\s*(.*)$', line)
        if match:
            key, val = match.groups()
            val_s = val.strip()
            if '@' in val_s and not (val_s.startswith('"') or val_s.startswith("'")):
                safe_val = val_s.replace('"', '\\"')
                line = f'{key}: "{safe_val}"'
        sanitized_lines.append(line)
    
    sanitized_yaml = '\n'.join(sanitized_lines)
    
    try:
        parsed = yaml.safe_load(sanitized_yaml) or {}
        parsed = normalize_yaml_value(parsed)
        if not isinstance(parsed, Mapping):
            return {}
        return dict(parsed)
    except yaml.YAMLError:
        # Robust regex-based fallback to avoid crashing on unquoted colons or parsing errors
        parsed = {}
        for line in yaml_text.splitlines():
            m = re.match(r'^([\w-]+):\s*(.*)$', line.strip())
            if m:
                k, v = m.groups()
                v_clean = v.strip().strip('"\'')
                parsed[k] = v_clean
        return parsed


def generate_index(skills_dir, output_file, compatibility_report=None):
    print(f"🏗️ Generating index from: {skills_dir}")
    skills = []
    if compatibility_report is None:
        compatibility_report = build_plugin_compatibility_report(pathlib.Path(skills_dir))
    compatibility_lookup = plugin_compatibility_by_path(compatibility_report)

    for root, dirs, files in os.walk(skills_dir):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        if "SKILL.md" in files:
            skill_path = os.path.join(root, "SKILL.md")
            if os.path.islink(skill_path):
                print(f"⚠️ Skipping symlinked SKILL.md: {skill_path}")
                continue
            dir_name = os.path.basename(root)
            parent_dir = os.path.basename(os.path.dirname(root))
            
            # Rel path from the skills folder root
            rel_path = os.path.relpath(root, skills_dir).replace(os.sep, '/')
            
            # Default values
            skill_info = {
                "id": rel_path, # Rel path guarantees 100% unique IDs across nested categories
                "path": f"skills/{rel_path}",
                "category": parent_dir if parent_dir != "skills" else "uncategorized",
                "name": dir_name.replace("-", " ").title(),
                "description": "",
                "risk": "unknown",
                "source": "unknown",
                "date_added": None,
                "plugin": {
                    "targets": {
                        "codex": "supported",
                        "claude": "supported",
                    },
                    "setup": {
                        "type": "none",
                        "summary": "",
                        "docs": None,
                    },
                    "reasons": [],
                },
            }
            
            try:
                with open(skill_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception as e:
                print(f"⚠️ Error reading {skill_path}: {e}")
                continue

            # Parse Metadata
            metadata = parse_frontmatter(content)
            
            # Merge Metadata
            name = coerce_metadata_text(metadata.get("name"))
            description = coerce_metadata_text(metadata.get("description"))
            risk = coerce_metadata_text(metadata.get("risk"))
            source = coerce_metadata_text(metadata.get("source"))
            date_added = coerce_metadata_text(metadata.get("date_added"))
            category = coerce_metadata_text(metadata.get("category"))

            if name is not None:
                skill_info["name"] = name
            if description is not None:
                skill_info["description"] = description
            if risk is not None:
                skill_info["risk"] = risk
            if source is not None:
                skill_info["source"] = source
            if date_added is not None:
                skill_info["date_added"] = date_added
            if category is not None:
                skill_info["category"] = category
            
            skill_info["category"] = normalize_category(skill_info["category"])

            plugin_info = compatibility_lookup.get(skill_info["path"])
            if plugin_info:
                skill_info["plugin"] = {
                    "targets": dict(plugin_info["targets"]),
                    "setup": dict(plugin_info["setup"]),
                    "reasons": list(plugin_info["reasons"]),
                }
            
            # Fallback for description
            if not skill_info["description"]:
                body = content
                fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
                if fm_match:
                    body = content[fm_match.end():].strip()
                
                lines = body.split('\n')
                desc_lines = []
                for line in lines:
                    if line.startswith('#') or not line.strip():
                        if desc_lines: break
                        continue
                    desc_lines.append(line.strip())
                
                if desc_lines:
                    skill_info["description"] = " ".join(desc_lines)[:250].strip()

            skills.append(skill_info)

    seen_ids: dict[str, str] = {}
    duplicate_ids: list[tuple[str, str, str]] = []
    for skill in skills:
        existing_path = seen_ids.get(skill["id"])
        if existing_path is not None:
            duplicate_ids.append((skill["id"], existing_path, skill["path"]))
        else:
            seen_ids[skill["id"]] = skill["path"]
    if duplicate_ids:
        details = "; ".join(
            f"{skill_id}: {first_path} conflicts with {second_path}"
            for skill_id, first_path, second_path in duplicate_ids
        )
        raise ValueError(f"Duplicate skill ids in generated index: {details}")

    skills.sort(key=lambda x: (x["name"].lower(), x["id"].lower()))

    with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(skills, f, indent=2)
    
    print(f"✅ Generated rich index with {len(skills)} skills at: {output_file}")
    return skills


def mirror_canonical_index(output_path):
    output_path = pathlib.Path(output_path)
    root = pathlib.Path(find_repo_root(__file__))
    root_index = root / "skills_index.json"
    if output_path.resolve() != root_index.resolve():
        return None

    data_index = root / "data" / "skills_index.json"
    data_index.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(output_path, data_index)
    print(f"✅ Mirrored canonical index to: {data_index}")
    return data_index


if __name__ == "__main__":
    base_dir = str(find_repo_root(__file__))
    skills_path = os.path.join(base_dir, "skills")
    output_path = os.path.join(base_dir, "skills_index.json")
    generate_index(skills_path, output_path)
    mirror_canonical_index(output_path)
