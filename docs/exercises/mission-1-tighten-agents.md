---
title: Mission 1 - Tighten AGENTS.md
parent: Exercises
nav_order: 1
---

# Mission 1: Tighten `AGENTS.md`

## Objective

Improve `AGENTS.md` so Codex can work more safely and predictably on docs, site,
and automation tasks in this repo.

## What this teaches

- how repo instructions affect execution quality
- how to encode validation commands and workflow constraints
- how to keep instructions concise and actionable

## Suggested Codex prompt

```text
Inspect AGENTS.md and the current repo workflows.
Propose the smallest useful improvements for documentation, Jekyll site work,
and GitHub automation tasks, then update AGENTS.md and run validation.
```

## Expected deliverable

A tighter `AGENTS.md` that covers site tooling, content conventions, and review
expectations without turning into a long policy document.

## Verification commands

```bash
markdownlint-cli2 "**/*.md"
python3 scripts/validate-docs.py
```

## Diff checklist

- instructions are repo-specific
- commands are runnable
- no duplicated policy from generic tool docs

## Reflection

What did Codex need to know that was previously implicit?
