# OpenAI docs gap summary

## Closed in this pass

The guide now covers official Codex docs for:

- slash commands
- config and trusted project behavior
- advanced `AGENTS.md` discovery and overrides
- MCP
- multi-agents
- review and diff workflows
- worktrees
- automations and local environments
- non-interactive mode and the GitHub Action

It also corrects the skill install story to use the documented `.agents/skills` locations rather than treating the local `~/.codex/skills` layout as canonical.

## Still intentionally missing

The guide still does not claim parity for features that are documented in Claude but not documented as Codex counterparts:

- Claude plugin packaging and marketplace flows
- Claude hooks
- any undocumented one-to-one Codex replacement for those features

That omission is intentional.

## Still open after this pass

Even after this docs-based pass, `codex-guide` will still not be a one-to-one mirror of `claude-code-guide`.

The remaining gap is structural:

- Claude and Codex expose different extension and automation models
- some Codex features are app-specific rather than generic repo features
- some local environment details can still differ from the official docs surface

The right goal is not word-for-word parity. It is accurate Codex-native coverage of the documented product surface.
