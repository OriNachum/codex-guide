---
title: Working with Codex Reference
parent: Working with Codex
nav_order: 1
---

# Working with Codex

The most reliable way to work with Codex is to treat it like a fast repo-aware engineer that still benefits from supervision, clear constraints, and feedback loops.

## Default workflow

For most non-trivial tasks, use this shape:

1. inspect the relevant code
2. summarize what matters
3. produce a plan
4. implement in small steps
5. run verification
6. review the diff

This keeps the work observable and easier to correct.

## When to ask for inspection first

Ask for inspection before implementation when:

- the codebase is unfamiliar
- the bug is ambiguous
- the change touches multiple files
- the repo has strong conventions you want followed

Example:

```text
Read the billing module and trace how invoice retries are scheduled.
Do not change code yet. Explain the current flow and propose a plan.
```

## When to skip straight to implementation

It is reasonable to skip deep planning when:

- the task is truly small
- the scope is obvious
- verification is simple

Example:

```text
Add a test for the empty input case in parser_test.go and run that test file.
```

## How to ask for useful plans

Good plans usually answer:

- which files need to change
- what behavior will change
- what risks exist
- how the change will be verified

If the plan is too broad, narrow it before implementation starts.

## How to review Codex output

Review in this order:

1. scope of changed files
2. correctness of the implementation
3. adequacy of tests or verification
4. alignment with repo conventions

The explanation is helpful, but the diff and command results matter more.

## When to intervene

Redirect Codex when:

- it starts changing unrelated files
- it reaches for broad commands without need
- the plan no longer matches the stated goal
- verification is missing or weak

Intervention works best when it is concrete:

```text
Stay within these two files.
Do not refactor adjacent code.
Run only the targeted tests for this package.
```

## Long-running work

For larger efforts, keep the work segmented:

- one subsystem at a time
- one verification loop at a time
- one reviewable diff at a time

This reduces drift and makes recovery easier if the direction needs to change.

## Related guides

- See [review-and-diff.md](review-and-diff.md) for the app review pane and CLI diff/review commands.
- See [slash-commands.md](slash-commands.md) for the built-in control surface that supports this workflow.
