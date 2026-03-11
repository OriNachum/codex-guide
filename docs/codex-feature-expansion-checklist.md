# Codex guide feature expansion checklist

This file tracks the content expansion needed to align the guide more closely
with both `claude-code-guide` overlap areas and the official OpenAI Codex docs.

## Overlap pages

- [x] Expand slash commands with Claude overlap and Codex-specific commands
- [x] Expand `AGENTS.md` guidance with overlap and Codex-specific layering
- [x] Expand skills guidance with overlap and official Codex behaviors
- [x] Expand sandboxing and approvals with explicit Codex modes and workflow
- [x] Expand worktrees with overlap and Codex app handoff and background behavior
- [x] Expand multi-agents with comparison framing against Claude agent patterns

## Official Codex additions

- [x] Expand MCP integration guidance
- [x] Expand automations and local environments
- [x] Expand non-interactive mode and GitHub Action guidance
- [x] Keep app-specific features in the appropriate pages
- [x] Add markdown verification guidance for this repo

## Repository automation

- [x] Add a manual and nightly GitHub Actions workflow for docs validation
- [x] Add a repo-local validation script so CI does not depend on local system files

## Verification

- [x] Update the README and ask-skill reference map to include the new pages
- [x] Run `markdownlint-cli2`
- [x] Run local skill and docs validation
