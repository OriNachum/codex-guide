# Review and diff

Codex supports both CLI and app review flows.

## In the CLI

- `/diff` shows the current Git diff, including untracked files
- `/review` asks Codex to review the current working tree and highlight likely issues

Use these together:

1. run or inspect the change
2. `/review` for issue finding
3. `/diff` for exact file-level inspection

## In the app

The app review pane is for understanding what changed, giving targeted feedback, and deciding what to keep.

Important documented behaviors:

- it only works inside Git repositories
- it reflects the repository state, not only what Codex changed
- it can show uncommitted changes, all branch changes, or only the last turn
- it supports inline comments, staging, unstaging, and reverting

## Best use

Use review and diff as the source of truth before you keep a change.

The final summary is helpful, but the actual diff and review findings matter more.
