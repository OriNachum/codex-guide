---
title: Sandbox and approvals
parent: Configuration and Safety
nav_order: 4
---

# Sandbox and approvals

Codex does not operate as an unrestricted shell by default. Command execution
depends on sandboxing and, when needed, explicit approval.

## Overlap with Claude Code

The high-level idea overlaps with Claude Code: the agent can inspect, edit, and
run commands under a safety model rather than acting as a raw unrestricted
shell.

What Codex documents more explicitly is the concrete sandbox and approval
surface.

## Documented modes

Sandbox modes:

- `read-only`
- `workspace-write`
- `danger-full-access`

Approval policies:

- `untrusted`
- `on-request`
- `never`

Common shortcuts:

- `--full-auto` for workspace-write plus no prompts
- `--dangerously-bypass-approvals-and-sandbox` or `--yolo` for the least
  restricted mode

## What this means in practice

- reading repo files is usually straightforward
- editing files is constrained to allowed writable areas
- some commands can run directly in the sandbox
- commands that need broader access, network access, or riskier effects may require approval

This is a feature, not a nuisance. It lets you use Codex aggressively without giving up all control.

## How to work well with it

### Prefer inspect first

Ask Codex to inspect the codebase and explain what it found before asking for broad changes. This reduces wasted edits and unnecessary approvals.

### Keep commands purposeful

The best approval requests are narrow and easy to judge:

- run the test suite
- install dependencies for this repo
- fetch remote documentation

Vague or overly broad commands create unnecessary friction.

### Expect escalation for a reason

Approval is commonly needed when a command:

- needs network access
- writes outside the workspace
- opens GUI tools
- performs potentially destructive actions

If the request is justified, approve it. If it is broader than necessary, tighten the task.

## Recommended workflow

1. Inspect the repo.
2. Ask for a plan.
3. Make edits inside the workspace.
4. Run the smallest useful verification commands.
5. Approve broader commands only when they clearly advance the task.

## Human role

The human should review:

- what command is being requested
- why it is needed
- whether the scope matches the task

The right default is not blind approval or blanket refusal. It is scoped approval aligned to the work.

## Practical default

For most real repositories, the best default is:

- sandboxed access
- explicit approvals for broader operations
- small verification commands after each focused change
