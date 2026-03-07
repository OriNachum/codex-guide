# Bugfix Request Template

Investigate **<symptom>** in **<module/path>**.

## Required workflow
1. Reproduce failure from tests/logs.
2. Identify root cause.
3. Implement minimal safe fix.
4. Add regression test.

## Constraints
- Keep public behavior unchanged except for the fix.
- Avoid unrelated refactors.

## Validation commands
- `<command 1>`
- `<command 2>`
