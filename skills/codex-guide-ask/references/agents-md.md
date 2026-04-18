---
title: AGENTS.md
parent: Configuration and Safety
nav_order: 1
---

# AGENTS.md

`AGENTS.md` is the main place to tell Codex how to work in a repository.

## Overlap with Claude Code

If you are coming from Claude Code, `AGENTS.md` fills much of the same role as
`CLAUDE.md`: it is the project instruction file that keeps Codex grounded in
your repository.

The important Codex-specific difference is that the official docs describe a
layered discovery model rather than only one project file.

## What belongs in it

Keep it short and operational. Include:

- how the project is organized
- how to build, test, and lint
- coding conventions that are not obvious from the code
- review expectations
- constraints that should affect tool use or edits

Good examples:

- `pytest tests/unit`
- `npm run lint` before committing
- `rg` is preferred over slower search tools
- do not edit generated files by hand

## What to avoid

Avoid turning `AGENTS.md` into a general project README.

Do not include:

- long architecture tours
- explanations Codex can infer from reading code
- stale command lists you do not maintain
- broad principles with no operational meaning

## Good shape

The best `AGENTS.md` files are:

- short enough to stay readable
- specific enough to change behavior
- current enough to trust

If Codex keeps missing a rule, either the rule is too vague or the file is overloaded.

## When to update it

Update `AGENTS.md` when:

- the build or test commands change
- the team adopts a new workflow rule
- the repo grows enough that directory-specific guidance matters
- you notice Codex repeatedly making the same avoidable mistake

## Practical pattern

Start with:

1. project structure
2. commands
3. style rules
4. testing expectations
5. contribution and review norms

Then refine it from real usage instead of trying to document everything up front.

For layered discovery, overrides, fallback filenames, and size limits, see [agents-md-advanced.md](agents-md-advanced.md).
