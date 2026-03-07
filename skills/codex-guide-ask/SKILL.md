---
name: codex-guide-ask
description: Answer questions about using Codex in a repository by reading the local guide references. Use when the user asks about AGENTS.md, sandbox and approvals, day-to-day Codex workflow, best practices, or the onboarding path in this repo. Also use when a user wants a grounded explanation based on the guide docs rather than a generic answer.
---

# Codex Guide Ask

Answer questions about Codex by reading the local reference files in `references/` as needed. Keep answers direct, practical, and grounded in the available docs.

## Workflow

1. Identify the user's topic.
2. Read the relevant reference file or files from `references/`.
3. Answer directly.
4. If the user appears new to Codex, mention `$codex-guide-onboarding` as the guided path.

## Reference map

Read only what is relevant:

| File | Use for |
|---|---|
| `references/getting-started.md` | First sessions, first tasks, and how to get productive safely |
| `references/working-with-codex.md` | Day-to-day workflow, planning, intervention, and review patterns |
| `references/slash-commands.md` | What the main Codex CLI slash commands do and when to use them |
| `references/config-and-trust.md` | `config.toml`, project trust, and configuration precedence |
| `references/agents-md.md` | What `AGENTS.md` is, what to put in it, and how to keep it useful |
| `references/agents-md-advanced.md` | Layering, overrides, fallback filenames, and advanced `AGENTS.md` behavior |
| `references/sandbox-and-approvals.md` | How Codex command execution and approvals shape workflow |
| `references/best-practices.md` | Prompting, planning, verification, diff review, and iteration habits |
| `references/markdown-verification.md` | How this repo uses `markdownlint` and Markdown verification |
| `references/skills.md` | What Codex skills are, where they live, and when they are worth creating |
| `references/mcp.md` | How Codex connects to MCP servers and when MCP is worth using |
| `references/multi-agents.md` | Experimental parallel multi-agent workflows in Codex CLI |
| `references/review-and-diff.md` | Review pane behavior and CLI `/review` and `/diff` workflows |
| `references/worktrees.md` | App worktrees, background isolation, and handoff behavior |
| `references/automations-and-local-environments.md` | Scheduled app automations and project-specific local environment setup |
| `references/non-interactive-and-github-action.md` | `codex exec` and the official GitHub Action path |
| `references/stories/starting-new-repo.md` | A concrete example of getting started in a real repo |
| `references/stories/daily-workflow.md` | A day-to-day example of working with Codex in an existing repo |

## Response rules

- Prefer concise, actionable answers.
- Use examples when they make the answer faster to apply.
- If the answer depends on product capabilities not covered by the local references, say that clearly.
- Do not invent Codex counterparts for Claude-specific features such as plugins, hooks, or sub agents.
