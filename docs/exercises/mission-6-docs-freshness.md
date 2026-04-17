---
title: Mission 6 - Add docs freshness audits
parent: Exercises
nav_order: 6
---

# Mission 6: Add docs freshness audits

## Objective

Create a workflow that checks the guide against official OpenAI Codex sources
and leaves an audit trail even when no changes are needed.

## What this teaches

- how to constrain an AI workflow to factual maintenance work
- how to make CI produce issues and PRs intentionally
- how to separate source-of-truth docs from community interpretation

## Suggested Codex prompt

```text
Inspect the current validation and autofix workflows.
Add a weekly docs-freshness audit that checks only official OpenAI Codex sources,
opens an issue with findings, and opens a PR only when factual corrections are
required.
```

## Expected deliverable

A manual and scheduled workflow plus a prompt that constrains the audit scope.

## Verification commands

```bash
python3 scripts/validate-docs.py
```

## Stretch goal

Add a short maintainer doc explaining which OpenAI pages the audit should treat
as authoritative.
