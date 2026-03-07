# Config and trust

Codex stores user-level configuration in `~/.codex/config.toml` and can load project-specific overrides from `.codex/config.toml`.

## Trust matters

Project config files are only loaded for trusted projects. This is a security boundary, not a convenience detail.

If a project is not trusted, Codex falls back to user and system defaults instead of applying project overrides.

## Configuration precedence

The main order is:

1. CLI flags and explicit `--config` overrides
2. selected profile values
3. project `.codex/config.toml` files from project root downward, with the closest file winning
4. user `~/.codex/config.toml`
5. system config
6. built-in defaults

## What belongs in config

Use config for:

- default model and provider choices
- sandbox and approval defaults
- MCP server definitions
- profiles for common working modes
- feature flags such as multi-agent enablement

## Repo guidance vs config

Keep the split clean:

- `AGENTS.md` is for project instructions Codex should follow
- `config.toml` is for client behavior and environment configuration

If a setting changes how Codex runs, it belongs in config. If it changes how Codex should behave in this repository, it usually belongs in `AGENTS.md`.
