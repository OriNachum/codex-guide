---
title: Markdown verification
parent: Working with Codex
nav_order: 5
---

# Markdown verification

Markdown linting is part of the repo verification loop for this guide.

## Primary command

Run:

```bash
markdownlint-cli2 "**/*.md"
```

This checks the Markdown files in the repository against the active lint rules.
`markdownlint-cli2` auto-discovers the repo's `.markdownlint-cli2.yaml`, so no
extra `--config` flag is needed for the normal local workflow.

The repo also includes a local validation script:

```bash
python3 scripts/validate-docs.py
```

That script checks skill structure and local Markdown links so documentation CI
does not depend on machine-specific Codex system files. It rejects absolute
filesystem links and links that resolve outside the repository so local runs
match GitHub Actions behavior.

## CI workflow

This repository also includes `.github/workflows/docs-validation.yml`.

It runs:

- manually with `workflow_dispatch`
- nightly on a cron schedule

The workflow runs the same two checks as the local loop:

- `markdownlint-cli2 "**/*.md"`
- `python3 scripts/validate-docs.py`

If that workflow fails on the default branch, `.github/workflows/codex-docs-autofix.yml`
uses `openai/codex-action@v1` to reproduce the failure, apply the minimum
repo-local fix, rerun the same checks, and open or update a pull request.

That remediation workflow requires:

- an `OPENAI_API_KEY` repository secret
- GitHub Actions permissions that allow PR creation

## Repo policy

This repo includes a
[`.markdownlint-cli2.yaml`](../../../.markdownlint-cli2.yaml) configuration file.

Current policy choices:

- `default: true` keeps the standard markdownlint rule set enabled by default
- `MD013` is disabled because this repo allows longer lines in prose-heavy docs
- `MD060` is disabled because this repo allows compact Markdown tables

Treat those as repo style decisions, not as reasons to skip linting.

## When to run it

Run Markdown linting:

- after editing docs
- before opening a PR
- after adding new reference pages or stories

## How to use failures

Use lint output to separate:

- real structural issues, such as missing blank lines around headings or lists
- repo policy issues, which may already be intentionally disabled in
  `.markdownlint-cli2.yaml`

If `markdownlint-cli2` reports a rule that should stay disabled for this repo,
update the lint config deliberately rather than ignoring the tool.

## Related workflow

Markdown lint is one part of documentation verification.

The broader loop is:

1. edit the doc
2. run `markdownlint-cli2`
3. run `python3 scripts/validate-docs.py`
4. review the diff
5. fix style, structure, or broken-link issues
6. rerun the checks
