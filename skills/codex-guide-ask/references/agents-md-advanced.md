# AGENTS.md advanced

Codex does more than read one top-level `AGENTS.md`.

## Layered discovery

Codex reads `AGENTS.md` files before starting work, combining broader guidance with more local guidance as it moves through a repository.

This lets you keep:

- general repo-wide rules at the top
- narrower rules closer to a subsystem

## Nested overrides

When a sub-area needs different rules, you can add `AGENTS.override.md` in a nested directory.

Use this for cases like:

- a service with a different test command
- a folder with stricter deployment rules
- a subsystem with special security or operational constraints

## Fallback filenames

If your repo already uses a different instructions filename, Codex can treat it as a project instructions file by configuring `project_doc_fallback_filenames` in `~/.codex/config.toml`.

This is useful when you need to preserve an existing team convention.

## Size limits

Codex stops loading project instruction files once the combined size reaches the configured `project_doc_max_bytes` limit.

That means long instruction files can silently crowd out more local guidance. If you hit that problem:

- shorten the broad file
- move details into more local instruction files
- raise the limit only when there is a real reason

## Practical rule

Keep broad instructions short. Put specialized rules closer to the code they affect.
