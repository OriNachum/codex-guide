# Getting started

If you are new to Codex in a repository, focus on three things first:

1. make the repo legible with `AGENTS.md`
2. choose a small first task
3. work in a visible inspect-plan-implement-verify loop

## First setup pass

Start by checking:

- top-level docs such as `README.md`
- build and test commands
- whether `AGENTS.md` already exists

If `AGENTS.md` is missing or weak, fix that before asking for broader implementation work.

## What a good first task looks like

Choose a task that is:

- easy to explain
- narrow in scope
- easy to verify
- low cost to redo if needed

Examples:

- add one missing test
- fix a small bug with a clear reproduction
- improve validation in one handler
- clean up one function without changing behavior

## Good first prompt shape

Use prompts that tell Codex how to approach the task, not just what outcome you want.

Example:

```text
Inspect the current implementation of profile validation.
Explain the bug surface first, then make a plan, then implement the smallest fix and run the relevant tests.
```

That is better than:

```text
Fix profile validation.
```

## What to watch during the first sessions

Pay attention to:

- whether Codex reads the right files
- whether the plan matches the actual repo
- whether approval requests are appropriately scoped
- whether verification commands are relevant and sufficient

The goal of the first sessions is to establish trust and rhythm, not to maximize throughput.

## After the first task

Once the first task lands cleanly:

1. tighten `AGENTS.md` based on what Codex missed
2. keep tasks modest until the workflow feels predictable
3. expand into broader refactors or features only after the verification loop is solid

## Where to go next

- See [slash-commands.md](slash-commands.md) for `/init`, `/plan`, `/permissions`, `/compact`, `/diff`, `/review`, and `/mcp`.
- See [config-and-trust.md](config-and-trust.md) for `config.toml` and trusted project behavior.
- See [agents-md-advanced.md](agents-md-advanced.md) for layered instruction discovery and overrides.
