# Repository Guidelines

## Project Structure & Module Organization

This repository is currently documentation-first.

- `README.md`: primary project overview and entry point.
- `AGENTS.md`: contributor and agent workflow guidance.
- `.git/`: repository metadata.

When adding content, keep files at the root only when they are top-level guides. For larger additions, prefer clear folders such as `docs/`, `examples/`, or `assets/`.

## Build, Test, and Development Commands

There is no build pipeline yet. Use these baseline commands while contributing:

- `git status` - check local changes before and after edits.
- `git diff` - review exact modifications.
- `markdownlint "**/*.md"` - lint Markdown if `markdownlint` is installed.
- `python3 scripts/validate-docs.py` - verify skill structure and local Markdown links.
- `vale .` - optional prose/style linting if configured locally.

If you introduce tooling (e.g., `Makefile`, npm scripts), document it in `README.md` and keep command names explicit (`test`, `lint`, `build`).

## Coding Style & Naming Conventions

- Use Markdown with ATX headings (`#`, `##`, `###`).
- Keep sections short, actionable, and scannable.
- Use sentence case for paragraph text and consistent title case for headings.
- Prefer kebab-case for new file names (example: `quick-start.md`).
- Wrap commands, paths, and identifiers in backticks.

## Testing Guidelines

Validation is currently content quality focused:

- Check links, command accuracy, and internal consistency.
- Run Markdown linting before opening a PR.
- For examples, ensure commands are copy-paste ready and use realistic paths.

If code or scripts are added later, place tests beside code or under a `tests/` directory and document how to run them.

## Commit & Pull Request Guidelines

Git history is minimal (`Initial commit`), so use a clear, imperative commit style going forward.

- Commit format: `docs: add contributor workflow section`
- Keep commits focused to one logical change.

PRs should include:

- What changed and why.
- Any follow-up work.
- Screenshots only when visual output changes.
- Links to related issues or discussions when applicable.
