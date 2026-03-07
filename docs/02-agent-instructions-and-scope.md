# Agent Instructions, Scope, and Policy

## Instruction priority

When guiding Codex in real repos, assume this order:

1. System instructions
2. Developer instructions
3. User request
4. In-repo instructions (`AGENTS.md` and nested overrides)

## `AGENTS.md` scope model

- `AGENTS.md` applies recursively from its folder downward.
- Nested `AGENTS.md` may override parent scope rules for deeper paths.
- The agent should honor every in-scope instruction for each touched file.

## Authoring guidelines for maintainers

Good `AGENTS.md` files are concise and executable:
- where code belongs (folder boundaries)
- naming/style conventions
- required checks for touched areas
- commit message or PR formatting rules
- prohibitions (for example “don’t edit generated files”)

## Suggested minimal template

```md
# AGENTS.md

## Scope notes
- Applies to this directory tree.

## Coding constraints
- Keep APIs backward compatible unless task says otherwise.
- Prefer targeted edits over broad rewrites.

## Required checks
- Run: <project commands>

## Delivery rules
- Provide summary + test output in final message.
```
