---
title: Worktrees
parent: Advanced Workflows
nav_order: 3
---

# Worktrees

The Codex app uses Git worktrees to let Codex work on parallel tasks without
interfering with your current checkout.

## Overlap with Claude Code

The core Git idea overlaps with the Claude guide: worktrees are the isolation
mechanism for parallel work, not a separate coordination system.

The Codex-specific layer is app behavior around:

- background work
- automations
- Handoff between Local and Worktree contexts

## What they are for

Worktrees are the app-level isolation mechanism for background or parallel work in Git repositories.

In the app:

- multiple independent tasks can run in the same project
- automations run on dedicated background worktrees
- you can move a thread between Local and Worktree with Handoff

## Local vs Worktree

Think of:

- Local as the foreground checkout you are actively using
- Worktree as a background checkout where Codex can keep working

Handoff uses Git operations to move work safely between those contexts.

## Important constraint

A branch can only be checked out in one place at a time. That is why worktree handoff matters and why Git behavior can be surprising if you try to use the same branch in multiple places.

## Why this page matters

When you need background work or parallelism in the app, worktrees are the documented Codex mechanism to understand first.

See [automations-and-local-environments.md](automations-and-local-environments.md)
for how Codex app automations build on top of worktrees.
