---
title: Slash commands
parent: Working with Codex
nav_order: 2
---

# Slash commands

Codex CLI has a built-in slash-command surface for steering an interactive session without leaving the terminal.

## Commands worth knowing first

- `/init` creates a starter `AGENTS.md`
- `/plan` switches the session into planning mode
- `/permissions` changes approval behavior for the current session
- `/compact` summarizes a long conversation to free context
- `/diff` shows the current Git diff, including untracked files
- `/review` asks Codex to review the current working tree
- `/mcp` lists configured MCP tools
- `/experimental` toggles experimental features such as multi-agents
- `/agent` switches to an active agent thread

## Overlap with Claude Code

If you used Claude Code before, several commands will feel familiar:

- `/init`
- `/compact`
- `/diff`
- `/review`
- `/mcp`

The concepts overlap, but the Codex command surface is still its own product
surface. The most visibly Codex-specific commands in this group are
`/experimental`, `/agent`, and the tighter connection between `/permissions`
and Codex sandbox settings.

## Recommended early workflow

For a new repo:

1. `/init`
2. review and tighten `AGENTS.md`
3. `/plan` for the first non-trivial task
4. `/permissions` if you need a different approval posture
5. `/diff` and `/review` before you keep the change

## What the key commands do

### `/init`

Use `/init` when a repo does not have a useful `AGENTS.md` yet. Treat the output as a scaffold, not final truth.

### `/plan`

Use `/plan` when you want Codex to think before acting. This is the safest way to start a complex or unfamiliar task.

### `/permissions`

Use `/permissions` to relax or tighten how much Codex can do without asking. This is the quickest way to move between cautious and faster workflows during a session.

### `/compact`

Use `/compact` after a long exchange to keep the critical context while reducing transcript weight.

### `/diff`

Use `/diff` whenever you want to inspect the actual file changes instead of relying on the final summary.

### `/review`

Use `/review` to have Codex inspect the working tree for issues, with `/diff` as the follow-up when you want exact file-level inspection.

### `/mcp`

Use `/mcp` to confirm which MCP tools are available before you ask Codex to use them.

### `/experimental`

Use `/experimental` only when you explicitly want a feature that is still marked experimental, such as multi-agents.

### `/agent`

Use `/agent` to inspect or continue work from an active agent thread.

## Related pages

- See [sandbox-and-approvals.md](sandbox-and-approvals.md) for the approval and
  sandbox model behind `/permissions`.
- See [multi-agents.md](multi-agents.md) for the experimental features surfaced
  through `/experimental`.
