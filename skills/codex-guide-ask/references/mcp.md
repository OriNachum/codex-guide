# MCP

MCP lets Codex call external tools and services through the Model Context Protocol.

## Overlap with Claude Code

The reasoning is similar to Claude Code: use MCP when Codex needs a durable,
structured tool integration with an external system, not for every simple task.

The Codex-specific details are the shared CLI and IDE configuration in
`config.toml`, the `codex mcp` commands, and the `/mcp` slash command.

## When MCP is worth it

Reach for MCP when Codex needs structured access to an external system such as:

- documentation
- design tools
- issue trackers
- browser/devtools integrations

If a simple local CLI already solves the problem, that is often the lower-friction option.

Typical cases where MCP is a good fit:

- GitHub and issue-tracker integrations
- browser and devtools integrations
- hosted documentation or design systems
- remote services where the tool menu should stay available across sessions

## Where MCP lives

Codex stores MCP configuration in `config.toml`, usually `~/.codex/config.toml`, and can also scope it to a trusted project with `.codex/config.toml`.

The CLI and IDE extension share this configuration.

## Ways to configure it

You can:

- use `codex mcp` commands
- use `/mcp` inside the CLI to inspect active tools
- edit `config.toml` directly with `[mcp_servers.<name>]` tables

## Practical rule

Prefer the simplest tool that reliably solves the problem:

- local CLI when available
- skill instructions for repeated local workflows
- MCP when the external integration should be a first-class tool surface

## Why this matters for workflow

MCP should be visible and deliberate:

- confirm the tool is configured
- confirm the right tools are enabled
- understand whether the task really needs external access

That keeps the workflow predictable and easier to review.
