# Claude → Codex Concept Map

## 1) System behavior model

Codex behavior follows layered instructions with clear precedence:

1. system
2. developer
3. user
4. repository instructions (for example `AGENTS.md` in scope)

In practice: if two instructions conflict, the higher layer wins.

## 2) Repository guidance file

- Claude ecosystems often use `CLAUDE.md`.
- Codex ecosystems commonly use `AGENTS.md`.

The Codex mindset is to keep this file operational:
- architecture boundaries
- code style constraints
- required checks
- commit/PR protocol
- environment caveats

## 3) Conversational vs execution-first

Claude usage is often conversation-heavy.
Codex usage is strongest when requests are execution-ready:
- exact files or folders
- acceptance criteria
- commands to run
- expected output artifacts

## 4) “Looks good” vs “validated”

Codex workflows should end with explicit checks:
- tests
- lint/type/static checks
- build/verifier commands
- concise report of what passed/failed/was blocked

## 5) Completion artifact expectations

Many Codex environments require completion artifacts beyond code changes:
- commit on branch
- PR title/body entry (or tool submission)
- final summary that includes commands run
