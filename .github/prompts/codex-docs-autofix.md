# Codex docs autofix

You are fixing a failed `Docs Validation` run in this repository.

Requirements:

- Work only in `codex-guide`.
- Do not add links or dependencies to sibling repositories or local filesystem paths.
- Keep changes minimal and scoped to docs validation, workflow configuration, and the docs or scripts they require.
- Treat `openai/codex-action@v1` as the official Codex GitHub integration for this repo. Do not invent a separate plugin system.

Execution loop:

1. Reproduce the failure locally with:
   - `markdownlint-cli2 "**/*.md"`
   - `python3 scripts/validate-docs.py`
2. Inspect the failing files and make the minimum repo-local fix.
3. Prefer repo-relative links or plain text/code references over repo-external links.
4. Keep the docs validation workflow and the documentation aligned with `markdownlint-cli2`.
5. Before finishing, rerun:
   - `markdownlint-cli2 "**/*.md"`
   - `python3 scripts/validate-docs.py`
6. Stop only when both commands pass.

Failure context will be appended below at runtime.
