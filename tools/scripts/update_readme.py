#!/usr/bin/env python3
import os
import json
import re
import sys
from pathlib import Path
from _project_paths import find_repo_root


def configure_utf8_output() -> None:
    """Best-effort UTF-8 stdout/stderr on Windows without dropping diagnostics."""
    if sys.platform != "win32":
        return

    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name)
        try:
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
            continue
        except Exception:
            pass

        buffer = getattr(stream, "buffer", None)
        if buffer is not None:
            setattr(
                sys,
                stream_name,
                io.TextIOWrapper(buffer, encoding="utf-8", errors="backslashreplace"),
            )


def load_metadata(base_dir: str) -> dict:
    package_path = os.path.join(base_dir, "package.json")
    index_path = os.path.join(base_dir, "skills_index.json")

    with open(index_path, "r", encoding="utf-8") as file:
        skills = json.load(file)

    with open(package_path, "r", encoding="utf-8") as file:
        package = json.load(file)

    total_skills = len(skills)
    version = str(package.get("version", "1.0.0"))

    return {
        "version": version,
        "total_skills": total_skills,
        "total_skills_label": f"{total_skills:,}",
    }


def format_skill_count(count: int) -> str:
    return f"{count:,}"


def main() -> None:
    root = find_repo_root(__file__)
    readme_path = root / "README.md"
    metadata = load_metadata(str(root))

    version = metadata["version"]
    total_skills = metadata["total_skills"]
    skills_label = metadata["total_skills_label"]

    print(f"📖 Reading README from: {readme_path}")
    print(f"🔢 Total skills found: {total_skills}")
    print(f"🏷️ Version found: {version}")

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update version badges in README
    content = re.sub(
        r"\b\d+[\d,]*\+?\b(\s+modular\s+AI\s+Skills)",
        f"{skills_label}+\\1",
        content,
        flags=re.IGNORECASE
    )

    content = re.sub(
        r"\b\d+[\d,]*\+?\b(\s+modular\s+skills)",
        f"{skills_label}\\1",
        content,
        flags=re.IGNORECASE
    )

    content = re.sub(
        r"\b\d+[\d,]*\+?\b(\s+skills\s+directly)",
        f"{skills_label}+\\1",
        content,
        flags=re.IGNORECASE
    )

    content = re.sub(
        r"\b\d+[\d,]*\+?\b(\s+active\s+skills)",
        f"{skills_label}\\1",
        content,
        flags=re.IGNORECASE
    )

    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    print("✅ README.md updated successfully.")


if __name__ == "__main__":
    configure_utf8_output()
    main()
