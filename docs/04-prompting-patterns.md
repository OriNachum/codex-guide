# Prompting Patterns for Codex

## What makes a Codex prompt effective

A strong prompt includes:
- exact scope
- non-negotiable constraints
- acceptance tests/checks
- output requirements

## Feature prompt pattern

```md
Implement <feature> in <paths>.
Constraints:
- <constraint 1>
- <constraint 2>
Validation:
- Run <commands>
Deliverables:
- Update <files>
- Summarize behavior and test results
```

## Bugfix prompt pattern

```md
Investigate <symptom> in <path/module>.
Steps:
1) Reproduce from existing tests/logs.
2) Identify root cause.
3) Implement minimal safe fix.
4) Add regression test.
Validation: <commands>
```

## Refactor prompt pattern

```md
Refactor <target> to improve <goal>.
Do not change external behavior.
Keep <public APIs> stable.
Add tests for <critical scenarios>.
Run <commands> and report results.
```

## Review prompt pattern

```md
Review <diff/files> for correctness, security, and maintainability.
Prioritize high-severity findings.
For each issue: location, impact, and concrete remediation.
```
