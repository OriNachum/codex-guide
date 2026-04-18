---
name: codex-guide-introspect
description: Audit a repository's Codex readiness and propose the next high-value improvements. Use when the user wants to review AGENTS.md, commands, verification, docs quality, CI, MCP usage, worktrees, or exercise ideas before deciding what to improve next.
---

# Codex Guide Introspect

Inspect the repository first, then produce a structured improvement plan. Do not
make repo changes until the user explicitly asks you to apply part of the plan.

## Workflow

### 1. Ground in the repo

Inspect the current repository before giving advice.

Look for:

- `AGENTS.md` quality and coverage
- build, test, lint, and site commands
- docs structure and internal consistency
- local skills and whether their descriptions still match reality
- CI workflows and validation coverage
- MCP, worktrees, review, and automation signals where relevant

### 2. Evaluate the current Codex workflow

Assess whether the repo supports a clean inspect-plan-implement-verify loop.

Focus on:

- whether Codex can discover the right commands quickly
- whether validation is documented and runnable
- whether instructions are specific instead of generic
- whether site and docs structure are legible to both humans and Codex
- whether there are obvious missing exercises or stories

### 3. Produce a plan-first report

Return a concise audit with:

- strengths already present
- gaps or risks
- the next 3 to 5 improvements in priority order
- which changes are small enough to do now versus issue-worthy

Use this shape:

```markdown
## Codex Readiness Audit

### Strengths
- ...

### Gaps
- ...

### Recommended next steps
1. ...
2. ...
3. ...

### Verification
- ...
```

### 4. Only apply after approval

If the user explicitly asks you to implement one of the recommended changes, do
that work next. Keep the implementation scoped to the approved items.

## Response rules

- Ground the audit in files and commands from the repo.
- Prefer specific fixes over abstract advice.
- Treat hooks as documented but experimental. Do not assume they replace skills,
  automations, or broader policy enforcement.
- Do not invent Claude-only features such as plugins or sub-agents.
- If the user wants deeper explanation of a specific Codex feature, suggest
  `$codex-guide-ask`.
- If the user wants guided practice, point them to the missions under
  `docs/exercises/`.
