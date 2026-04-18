---
title: Mission 5 - Build the Introspection Skill
parent: Exercises
nav_order: 5
---

# Mission 5: Build the Introspection Skill

## Objective

Add a Codex-native introspection skill that audits repo readiness and proposes
the next high-value improvements.

## What this teaches

- how to write a skill that stays grounded in the local repo
- how to keep a skill plan-first instead of overreaching
- how to translate repeated friction into reusable guidance

## Suggested Codex prompt

```text
Inspect the existing codex-guide skills and references.
Add a new introspection skill that audits AGENTS.md, verification commands, docs,
automation, and advanced Codex workflows, then returns a plan-first report.
```

## Expected deliverable

A new skill folder with `SKILL.md`, `agents/openai.yaml`, and docs that explain
how to use the skill well.

## Verification commands

```bash
python3 scripts/validate-docs.py
```

## Reflection

What should stay in the skill versus being moved into regular docs?
