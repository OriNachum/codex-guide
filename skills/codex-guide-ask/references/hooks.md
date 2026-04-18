---
title: Hooks
parent: Advanced Workflows
nav_order: 7
---

# Hooks

Codex now documents hooks as an experimental extensibility framework for running
deterministic scripts during the agent lifecycle.

Official source:
[OpenAI Codex hooks docs](https://developers.openai.com/codex/hooks)

## Current status

- Hooks are experimental and under active development.
- They are behind a feature flag in `config.toml`:

```toml
[features]
codex_hooks = true
```

- Hooks are currently disabled on Windows.

## Where Codex looks for hooks

Codex discovers `hooks.json` next to active config layers.

In practice, the main locations are:

- `~/.codex/hooks.json`
- `<repo>/.codex/hooks.json`

If more than one `hooks.json` file exists, matching hooks from multiple files
all run.

## Current events

The hooks docs currently describe these events:

- `SessionStart`
- `PreToolUse`
- `PostToolUse`
- `UserPromptSubmit`
- `Stop`

Important current limitation:

- `PreToolUse` and `PostToolUse` currently only intercept `Bash`
- `UserPromptSubmit` and `Stop` ignore `matcher` today

Treat hooks as useful guardrails and automation points, not as a complete
security boundary.

## Config shape

Hooks are organized as:

1. an event
2. a matcher group
3. one or more handlers

Handlers are typically command hooks that receive JSON on `stdin`.

Useful fields in the input payload include:

- `session_id`
- `cwd`
- `hook_event_name`
- `model`

Turn-scoped hooks also include `turn_id` in the event-specific payload.

## Practical use cases

Hooks are a good fit for:

- prompt or command policy checks before risky shell usage
- post-command review or annotation after Bash completes
- loading session context on startup or resume
- logging and analytics around prompts and turns
- deterministic reminders or validations when a turn stops

## Hooks vs skills

Keep the split clean:

- use **hooks** for deterministic lifecycle automation
- use **skills** for reusable judgment-heavy workflows

If the behavior should always run at a lifecycle event, it is probably a hook.
If the behavior should be invoked when a task calls for it, it is probably a
skill.

## Hooks vs app automations

Hooks and app automations solve different problems.

- hooks run inline around session and tool events
- automations schedule background work over time

They can complement each other, but they are not substitutes.
