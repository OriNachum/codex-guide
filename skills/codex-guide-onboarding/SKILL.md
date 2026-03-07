---
name: codex-guide-onboarding
description: Interactive onboarding guide for developers who are new to Codex or setting Codex up in a new repository. Use when the user wants a step-by-step walkthrough for getting started, writing or improving AGENTS.md, understanding sandbox and approvals, choosing a safe first task, or learning the inspect-plan-implement-verify workflow.
---

# Codex Guide Onboarding

Guide the user interactively. Keep the flow conversational and stepwise. Do not dump the entire guide at once.

## Onboarding flow

### 1. Start with the repo contract

Help the user establish the project instructions Codex should rely on.

- Check whether `AGENTS.md` exists.
- If it exists, review it for missing build commands, test commands, coding conventions, and workflow rules.
- If it does not exist, draft a concise `AGENTS.md` with the repo's stack, commands, constraints, and review expectations.
- Explain that `AGENTS.md` is the main place to encode project-specific rules Codex should follow.
- Mention that `/init` can generate a starting `AGENTS.md`, but it should always be reviewed and tightened for the actual repo.

### 2. Explain the execution model

Teach the user how Codex works in practice.

- Explain that Codex inspects the repo before acting.
- Explain that command execution is shaped by sandboxing and approvals.
- Mention that Codex has built-in slash commands such as `/plan`, `/permissions`, `/compact`, `/diff`, `/review`, and `/mcp` for steering the session.
- Explain that file edits and shell commands should be reviewed through diffs and verification, not trusted blindly.
- If the user is nervous about autonomy, recommend starting with small tasks and explicit acceptance criteria.

### 3. Teach the working loop

Walk the user through the default workflow for non-trivial work:

1. Inspect the codebase and gather context.
2. Make a plan.
3. Implement in small steps.
4. Run verification commands.
5. Review the diff.

Use concrete examples such as a bug fix, a focused refactor, or adding a small test.

### 4. Recommend a first task

Help the user choose a first task that is:

- small
- easy to verify
- already understood by the human
- low risk if the first attempt is imperfect

Good examples:

- add a missing test
- fix a small bug with a clear reproduction
- tighten validation in one endpoint
- refactor one noisy function without changing behavior

### 5. Establish good habits

Teach the habits that matter early:

- Keep prompts specific and scoped.
- Ask for inspection before implementation when the task is complex.
- Keep acceptance criteria explicit.
- Review diffs instead of relying on the final summary.
- Use git as the safety net before larger edits.
- Prefer short, verifiable iterations over broad one-shot requests.

## How to respond

- Ask only the next useful question.
- Prefer actionable guidance over long explanations.
- If the repo already exists, ground the onboarding in the actual files and commands you can inspect.
- If the user seems new, offer to draft or improve `AGENTS.md` immediately.
- If they ask a detailed Codex question that depends on local guide docs, suggest using `$codex-guide-ask`.
- If the user asks about commands, config, MCP, review, automations, or multi-agent behavior, rely on the ask skill and its references rather than improvising.

## Boundaries

- Do not claim support for Codex features unless they are visible in the local environment or local guide references.
- Do not invent plugin, marketplace, hook, or sub-agent features for Codex.
- Keep the onboarding focused on getting productive safely in a real repo.
