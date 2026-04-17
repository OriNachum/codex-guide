---
title: Mission 4 - Improve GitHub Issue Hygiene
parent: Exercises
nav_order: 4
---

# Mission 4: Improve GitHub Issue Hygiene

## Objective

Make it easier to track site, content, skill, and audit work with consistent
templates and labels.

## What this teaches

- how to encode project management conventions in-repo
- how to scope issues so Codex can work against them cleanly
- how to separate epic planning from implementation tasks

## Suggested Codex prompt

```text
Inspect the current GitHub metadata.
Add issue templates and supporting repo files for epics, tasks, exercise ideas,
and docs-freshness audits. Keep the template fields concise and actionable.
```

## Expected deliverable

Issue templates that produce high-signal issue bodies and reduce ambiguous work.

## Verification commands

```bash
python3 scripts/validate-docs.py
```

## Stretch goal

Use the GitHub integration to create the matching labels after the repo files
are merged.
