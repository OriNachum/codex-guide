---
title: Mission 3 - Publish the custom domain
parent: Exercises
nav_order: 3
---

# Mission 3: Publish the custom domain

## Objective

Wire the repo for `codex.agentic-guides.com` and document the manual steps that
live outside Git.

## What this teaches

- the split between repo automation and external DNS control
- how to make deployment changes reviewable
- how to document manual rollout steps cleanly

## Suggested Codex prompt

```text
Inspect the site configuration and GitHub workflows.
Add the repo-side changes needed for codex.agentic-guides.com, including CNAME,
Pages deployment, and a concise note for the Cloudflare DNS step.
```

## Expected deliverable

`CNAME`, a deploy workflow, and short rollout notes in the repo.

## Verification commands

```bash
bundle exec jekyll build
```

## Reflection

Which parts of deployment belong in the repo, and which do not?
