# Multi-agents

Codex has an experimental multi-agent workflow in the CLI.

## Overlap with Claude agent workflows

This is the nearest documented Codex analogue to the parallel agent workflows
described in `claude-code-guide`, but it should not be described as exact
feature parity with Claude sub-agents or agent teams.

The safe framing is:

- both systems support parallel agent-style work
- Codex documents multi-agents as experimental
- the UX and configuration model are Codex-specific

## What it is

Multi-agents let Codex spawn specialized agents in parallel and collect their results into one response.

This is useful for:

- parallel codebase exploration
- decomposing a complex task into several focused tracks
- separating specialized roles with different instructions or model settings

## Status

This feature is experimental and must be explicitly enabled.

You can enable it with:

- `/experimental` in the CLI
- a `multi_agent = true` feature flag in `~/.codex/config.toml`

## How to talk about it

Treat multi-agents as documented Codex functionality, but do not describe it as direct parity with Claude sub-agents or agent teams.

The correct framing is:

- Codex supports experimental parallel agent workflows
- the exact UX and surface area are still evolving

## Configuration

Agent roles can be configured in the `[agents]` section of config, either in user config or project config for trusted projects.
