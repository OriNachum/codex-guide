# Review, Testing, and Validation

## Validation stack

Prefer deterministic checks in this order:

1. unit/integration tests for changed area
2. lint/style checks
3. type/static analysis
4. build/package checks
5. broader regression suite (if available)

## Regression discipline

For bug fixes, enforce “fail before / pass after” where possible.

## Review checklist

- correctness of logic
- data validation and null/edge handling
- backwards compatibility
- security-sensitive code paths
- docs updated when behavior changes

## Reporting format

Final summaries should include:
- what changed
- exactly which commands ran
- pass/fail/warn status
- blockers and why they occurred
