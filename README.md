# codex-guide

Community guide for learning Codex through local skills, reference docs, and
real-repo exercises.

The public site target for this repo is
[`codex.agentic-guides.com`](https://codex.agentic-guides.com). The repo remains
the source of truth for the published docs and the installable skills.

## What this repo contains

- a static docs site built from the repo content
- local Codex skills for onboarding, Q&A, and repo introspection
- reference docs on workflow, configuration, review, automation, and advanced
  usage
- exercise missions that teach Codex by improving this repo itself

## Current skills

- `codex-guide-onboarding` - interactive first-run walkthrough for using Codex
  in a repository
- `codex-guide-ask` - answer Codex workflow questions from the local guide
  references
- `codex-guide-introspect` - audit a repo's Codex readiness and propose the next
  improvements

## Install locally

Official Codex docs describe skills as living in repository `.agents/skills`
folders and in the user-level `$HOME/.agents/skills` folder. This guide follows
that docs-first layout.

To install these skills for yourself:

```bash
mkdir -p ~/.agents/skills
cp -R skills/codex-guide-onboarding ~/.agents/skills/
cp -R skills/codex-guide-ask ~/.agents/skills/
cp -R skills/codex-guide-introspect ~/.agents/skills/
```

Then invoke them from Codex with `$codex-guide-onboarding`,
`$codex-guide-ask`, or `$codex-guide-introspect`.

If your local environment already exposes bundled skills under
`~/.codex/skills`, treat that as an environment-specific detail rather than the
canonical install path.

## Local development

Install the docs-site dependencies:

```bash
bundle install
```

The Jekyll stack for this repo is expected to run on Ruby `3.3`, which is the
same version used in the GitHub workflows.

Useful commands:

```bash
bundle exec jekyll build
markdownlint-cli2 "**/*.md"
python3 scripts/validate-docs.py
uv run --with pytest pytest
```

## Publishing model

- GitHub Pages serves the site for this repo
- `CNAME` sets the custom domain to `codex.agentic-guides.com`
- Cloudflare DNS remains a manual maintainer step outside the repo

## Repository structure

```text
codex-guide/
├── AGENTS.md
├── README.md
├── CNAME
├── Gemfile
├── _config.yml
├── index.md
├── docs/
│   ├── getting-started.md
│   ├── working-with-codex.md
│   ├── configuration-and-safety.md
│   ├── advanced-workflows.md
│   ├── stories.md
│   └── exercises/
├── scripts/
│   └── validate-docs.py
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── prompts/
│   └── workflows/
└── skills/
    ├── codex-guide-onboarding/
    ├── codex-guide-ask/
    └── codex-guide-introspect/
```

## Validation and automation

GitHub Actions runs docs validation, Pages deployment, and Codex-assisted
maintenance workflows from `.github/workflows/`.

If `Docs Validation` fails on the default branch, `Codex Docs Autofix` runs
`openai/codex-action@v1`, reruns the checks, and opens or updates a PR with the
smallest repo-local fix.

The Codex workflows require:

- an `OPENAI_API_KEY` repository secret
- GitHub Actions permissions that allow issue and pull request creation

## License

Apache License 2.0 - see [LICENSE](LICENSE) for details. Privacy notes for the
repository contents are in [PRIVACY.md](PRIVACY.md).
