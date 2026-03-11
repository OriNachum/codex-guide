# Non-interactive mode and GitHub Action

Codex has an official non-interactive path for automation and an official GitHub Action for CI workflows.

## `codex exec`

Use `codex exec` when you want Codex to:

- run in pipelines or scheduled jobs
- produce output that can be piped into other tools
- run with explicit sandbox and approval settings

Important documented behaviors:

- progress streams to `stderr`
- the final agent message goes to `stdout`
- read-only sandbox is the default
- `--json` turns output into a JSON Lines stream
- `--output-schema` can constrain the final result to structured JSON

## Safety posture

For automation, keep permissions narrow:

- use read-only when the job is analysis only
- use `--full-auto` when edits in the workspace are needed
- use `danger-full-access` only in controlled environments

## GitHub Action

OpenAI provides `openai/codex-action@v1` for GitHub Actions workflows.

This is the official path to run Codex in GitHub-hosted automation with prompt files, output capture, and explicit sandbox settings.

## Overlap with Claude Code GitHub Actions

If you used the Claude guide’s GitHub Actions patterns, the mental model carries
over:

- CI is still the place for repository-wide automated checks
- manual `workflow_dispatch` runs are still useful for ad-hoc maintenance
- scheduled runs are still useful for freshness checks and recurring audits

The main difference is the Codex-specific automation surface: `codex exec` for
generic non-interactive use and `openai/codex-action@v1` for GitHub-hosted
workflows.

## Example use cases

- PR review helpers
- scheduled doc freshness checks
- recurring audits of repo instructions and guide content
- manual on-demand maintenance runs

In `codex-guide`, that maps cleanly to a failure-triggered remediation workflow:
`Docs Validation` stays deterministic, and `Codex Docs Autofix` uses
`openai/codex-action@v1` to repair a failed run and open a PR.

## Recommended framing

If the user wants Codex in CI, point them to:

1. `codex exec` for generic automation
2. `openai/codex-action@v1` for GitHub-specific workflows
