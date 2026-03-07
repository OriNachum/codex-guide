# Troubleshooting and Fallbacks

## Common blockers

- restricted network (cannot fetch remote references)
- missing dependencies for tests/tooling
- unavailable browser automation runtime

## Fallback strategy

1. state the exact failing command and error
2. continue with best offline/static approach
3. minimize assumptions and call them out
4. leave clear next actions for maintainers

## Example wording

- “Could not fetch upstream docs due to network policy; produced local mirror from available repository context.”
- “Type checker unavailable because dependency X is missing; ran tests Y/Z and documented risk.”
