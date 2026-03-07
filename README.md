# codex-guide

Codex onboarding and Q&A as local skills, backed by a small set of practical reference docs.

## What this repo is

This repo is a Codex-native guide repo, not a Claude plugin mirror. It is built around:

- `AGENTS.md` for repo-specific instructions
- local Codex skills for onboarding and Q&A
- concise reference docs for workflow, configuration, review, and automation

## Current skills

- `codex-guide-onboarding` - interactive getting-started walkthrough for using Codex in a repo
- `codex-guide-ask` - answer Codex workflow questions from the local guide references

## Install locally

Official Codex docs describe skills as living in repository `.agents/skills` folders and in the user-level `$HOME/.agents/skills` folder. This guide follows that docs-first layout.

To install these skills for yourself:

```bash
mkdir -p ~/.agents/skills
cp -R skills/codex-guide-onboarding ~/.agents/skills/
cp -R skills/codex-guide-ask ~/.agents/skills/
```

Then invoke them from Codex with `$codex-guide-onboarding` or `$codex-guide-ask`.

If your local environment already exposes bundled skills under `~/.codex/skills`, treat that as an environment-specific detail rather than the canonical install path.

## Repository structure

```text
codex-guide/
├── AGENTS.md
├── PRIVACY.md
├── LICENSE
├── README.md
├── scripts/
│   └── validate-docs.py
├── docs/
│   ├── claude-to-codex-conversion-plan.md
│   ├── codex-feature-expansion-checklist.md
│   └── openai-docs-gap-summary.md
├── .github/
│   └── workflows/
│       └── docs-validation.yml
└── skills/
    ├── codex-guide-onboarding/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    └── codex-guide-ask/
        ├── SKILL.md
        ├── agents/openai.yaml
        └── references/
            ├── getting-started.md
            ├── working-with-codex.md
            ├── slash-commands.md
            ├── config-and-trust.md
            ├── agents-md.md
            ├── agents-md-advanced.md
            ├── sandbox-and-approvals.md
            ├── best-practices.md
            ├── markdown-verification.md
            ├── skills.md
            ├── mcp.md
            ├── multi-agents.md
            ├── review-and-diff.md
            ├── worktrees.md
            ├── automations-and-local-environments.md
            ├── non-interactive-and-github-action.md
            └── stories/
                ├── daily-workflow.md
                └── starting-new-repo.md
```

## Next steps

- expand the ask references carefully as Codex-specific guidance is verified
- keep `AGENTS.md` and the skill prompts aligned with real usage
- avoid porting Claude-only concepts unless a verified Codex counterpart exists

## Validation

Local docs checks:

```bash
markdownlint "**/*.md"
python3 scripts/validate-docs.py
```

GitHub Actions also runs the same docs validation workflow manually on
`workflow_dispatch` and nightly on a cron schedule.

## License

CC BY 4.0 - see [LICENSE](LICENSE) for details. Privacy notes for the repository contents are in [PRIVACY.md](PRIVACY.md).
