#!/usr/bin/env python3

from __future__ import annotations

import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
WINDOWS_ABS_RE = re.compile(r"^[A-Za-z]:[\\/]")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def validate_skill(skill_dir: pathlib.Path) -> None:
    skill_md = skill_dir / "SKILL.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"

    if not skill_md.exists():
        fail(f"missing {skill_md.relative_to(ROOT)}")
    if not openai_yaml.exists():
        fail(f"missing {openai_yaml.relative_to(ROOT)}")

    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{skill_md.relative_to(ROOT)} is missing YAML frontmatter")

    _, _, remainder = text.partition("---\n")
    frontmatter, _, _ = remainder.partition("---\n")
    if "name:" not in frontmatter:
        fail(f"{skill_md.relative_to(ROOT)} frontmatter is missing name")
    if "description:" not in frontmatter:
        fail(f"{skill_md.relative_to(ROOT)} frontmatter is missing description")


def validate_markdown_links(markdown_file: pathlib.Path) -> None:
    text = markdown_file.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("#"):
            continue

        path_part = target.split("#", 1)[0]
        if not path_part:
            continue

        if path_part.startswith("/") or WINDOWS_ABS_RE.match(path_part):
            fail(
                f"{markdown_file.relative_to(ROOT)} uses absolute filesystem link "
                f"{path_part}; use a repo-relative path or https URL"
            )

        resolved = (markdown_file.parent / path_part).resolve()
        if ROOT not in (resolved, *resolved.parents):
            fail(
                f"{markdown_file.relative_to(ROOT)} links outside the repo "
                f"{path_part}; use a repo-relative path or https URL"
            )

        if not resolved.exists():
            fail(
                f"{markdown_file.relative_to(ROOT)} links to missing path "
                f"{path_part}"
            )


def main() -> int:
    if not SKILLS_DIR.exists():
        fail("skills directory is missing")

    for skill_dir in sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir()):
        validate_skill(skill_dir)

    for markdown_file in sorted(ROOT.rglob("*.md")):
        validate_markdown_links(markdown_file)

    print("Docs validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
