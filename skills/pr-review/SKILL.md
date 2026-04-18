---
name: pr-review
description: Pull PR feedback from GitHub, Qodo, Copilot, and SonarCloud signals, then triage it into fixes, pushback, replies, resolutions, and follow-up issues. Use when a PR has review comments or failing checks and you want one repeatable workflow to gather and address them.
---

# PR Review

Use the helper scripts in `scripts/` to pull feedback and manage inline review
threads. Treat `gh` as the source of truth for this workflow.

## Prerequisites

Before doing anything else:

1. Confirm `gh --version` works.
2. Confirm `gh auth status` succeeds.
3. Determine the PR number from `$ARGUMENTS` or from the current branch.

## Workflow

### 1. Pull all feedback

Run:

```bash
python3 skills/pr-review/scripts/fetch_feedback.py --pr <number> --format markdown
```

This script gathers:

- PR metadata
- top-level PR comments
- review submissions
- inline review comments
- review threads and their resolution state
- status checks such as SonarCloud

Treat the sources as:

- **Qodo**: bot review summary plus inline comments
- **Copilot**: top-level overview plus inline comments
- **SonarCloud**: check-run failures and top-level quality-gate comments
- **Human GitHub review**: comments and threads from normal users

### 2. Triage the findings

Sort each finding into one of these buckets:

- **Fix now**: correct and in-scope for the current PR
- **Push back**: not correct, conflicts with required conventions, or not worth changing
- **Follow-up issue**: valid, but too broad or external for the current PR

Deduplicate overlapping comments across Qodo, Copilot, and repeated inline
threads before acting.

### 3. Fix what belongs in the PR

Implement the in-scope fixes first. Then re-run the most relevant checks.

Typical examples:

- broken public-site links
- bad nav ordering
- missing workflow guardrails
- template/documentation issues

### 4. Create follow-up issues

For deferred items, create a GitHub issue with:

- the source comment or check URL
- why it is deferred
- the expected next action

Use this especially for:

- SonarCloud hotspots that need dashboard triage
- broader rollout work
- security/workflow hardening that would bloat the current PR

### 5. Reply and resolve

Use:

```bash
python3 skills/pr-review/scripts/thread_actions.py reply-and-resolve \
  --pr <number> --comment-id <comment_id> --body "Handled in <summary>"
```

for inline review comments that have been addressed.

For multiple inline comments at once, create a JSON file like:

```json
[
  {
    "comment_id": 1234567890,
    "body": "Handled by switching the published link to the GitHub README."
  },
  {
    "comment_id": 1234567891,
    "body": "Handled by replacing the broken site-relative SKILL.md link."
  }
]
```

Then run:

```bash
python3 skills/pr-review/scripts/thread_actions.py reply-and-resolve-batch \
  --pr <number> --file /tmp/pr-review-batch.json
```

Use:

```bash
gh pr comment <number> --body "Grouped response..."
```

for top-level bot comments that cannot be resolved as review threads.

When pushing back, be concrete. Reference the repo convention or platform
requirement that makes the suggestion incorrect.

## Response rules

- Prefer fixing the root cause when multiple bots reported the same issue.
- Do not blindly follow bot comments that conflict with Jekyll, GitHub Pages, or
  documented Codex behavior.
- Treat SonarCloud check failures as actionable, but create a follow-up issue if
  the PR does not expose enough detail to fix them safely.
- After applying fixes, reply to the relevant comments and resolve the inline
  threads you actually addressed.
