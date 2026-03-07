# Markdown verification

Markdown linting is part of the repo verification loop for this guide.

## Primary command

Run:

```bash
markdownlint "**/*.md"
```

This checks the Markdown files in the repository against the active lint rules.

The repo also includes a local validation script:

```bash
python3 scripts/validate-docs.py
```

That script checks skill structure and local Markdown links so documentation CI
does not depend on machine-specific Codex system files.

## CI workflow

This repository also includes `.github/workflows/docs-validation.yml`.

It runs:

- manually with `workflow_dispatch`
- nightly on a cron schedule

The workflow runs the same two checks as the local loop:

- `markdownlint "**/*.md"`
- `python3 scripts/validate-docs.py`

## Repo policy

This repo includes a [`.markdownlint.json`](../../../.markdownlint.json)
configuration file.

Current policy choices:

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
  `.markdownlint.json`

If `markdownlint` reports a rule that should stay disabled for this repo, update the
lint config deliberately rather than ignoring the tool.

## Related workflow

Markdown lint is one part of documentation verification.

The broader loop is:

1. edit the doc
2. run `markdownlint`
3. run `python3 scripts/validate-docs.py`
4. review the diff
5. fix style, structure, or broken-link issues
6. rerun the checks
