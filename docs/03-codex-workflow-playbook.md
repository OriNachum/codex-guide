# Codex Workflow Playbook

## 1) Intake

Turn broad intent into precise tasks:
- identify target paths
- list hard constraints
- list required validation commands
- define expected output (files/tests/PR note)

## 2) Repo scan

Quickly inspect structure before editing:
- read root README and in-scope `AGENTS.md`
- locate implementation files and tests
- confirm command(s) used for verification

## 3) Plan only when needed

Use a short plan for multi-step tasks or uncertainty.
Skip heavy planning for trivial one-file edits.

## 4) Implement with minimal blast radius

- avoid unrelated churn
- preserve public interfaces unless instructed
- add tests for changed behavior

## 5) Validate

Run the smallest sufficient suite first, then broader checks:
1. targeted tests
2. package/module checks
3. full suite if needed

## 6) Deliver

- summarize what changed
- list commands run and status
- call out risk, assumptions, and blockers
