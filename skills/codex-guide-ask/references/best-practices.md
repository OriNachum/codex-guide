---
title: Best practices
parent: Working with Codex
nav_order: 3
---

# Best practices

Codex works best when the task is concrete, the repo instructions are clear, and verification is easy.

## Start with reality

Ground Codex in the actual repository:

- point to real files
- name real commands
- mention the exact behavior you want changed

Better:

- `Read the auth handlers, explain the current flow, then plan the fix for the session timeout bug.`

Worse:

- `Improve auth.`

## Use the inspect-plan-implement-verify loop

For non-trivial work:

1. inspect first
2. make a plan
3. implement in steps
4. verify with tests, linters, or targeted commands
5. review the diff

This is usually more reliable than asking for a full solution immediately.

## Keep tasks scoped

Prefer:

- one bug
- one endpoint
- one refactor
- one test file

Large vague requests are harder to verify and easier to derail.

## Make acceptance criteria explicit

If the task matters, define success in concrete terms:

- which files should change
- what behavior should be added or preserved
- what commands should pass
- what should not change

If the criteria are important enough to remember, they are important enough to write down.

## Review the diff, not just the summary

The final explanation is useful, but the diff is the source of truth.

Check:

- whether the right files changed
- whether the scope stayed tight
- whether tests or verification were actually run
- whether the implementation followed repo conventions

## Use git as the safety net

Before broad edits:

- check `git status`
- review `git diff`
- commit a clean baseline if the change is risky

This makes it easier to iterate without anxiety.

## Prefer short loops

A good loop looks like:

1. inspect
2. patch
3. verify
4. review
5. refine

That loop is easier to supervise and easier for Codex to execute well than a single oversized request.
