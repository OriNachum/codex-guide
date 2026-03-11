# Claude to Codex conversion plan

## Goal

Convert `../claude-code-guide` from a Claude Code plugin into a Codex-native guide repo that helps new users onboard to Codex and use Codex itself as the guide.

Keep the parts that are structurally strong:

- an interactive onboarding entry point
- a Q&A entry point backed by reference docs
- topic-based references
- scenario-based stories

Replace the parts that are product-specific:

- Claude plugin packaging
- Claude slash-command UX
- Claude-only automation primitives
- Claude-specific configuration files, models, and modes

## What carries over cleanly

- The two-skill shape is still right: one onboarding skill and one ask/reference skill.
- The reference-heavy layout is still right: a lean skill that loads detailed docs only when needed matches Codex skill design well.
- The story format is still useful because onboarding users need scenarios, not just feature lists.
- The repo can stay content-first. No app code or build system is needed unless you later add install helpers.

## What does not map 1:1

### 1. Plugin packaging is the wrong target

`claude-code-guide` is framed as a plugin from the first lines of the repo and README. That assumption appears in install steps, repo structure, and extension docs. Relevant source locations in the original repo include `README.md` lines 3, 5, and 70 plus `CLAUDE.md` line 9.

In this local Codex environment, the native extension concepts I can verify are:

- `AGENTS.md` for repo instructions
- skills under `~/.codex/skills`

I do not see a parallel local Codex plugin or marketplace layer. Treat this as a skill pack and guide repo first, not as a plugin clone.

### 2. Most of the guide teaches Claude-only primitives

Large parts of the docs are organized around Claude-only capabilities:

- hooks, skills, and sub agents as the three automation primitives in `skills/guide/ask/references/automating-your-workflows.md` line 9
- plugin packaging as a first-class distribution mechanism in `skills/guide/ask/references/plugins.md` line 5
- built-in slash commands, hooks, sub agents, and built-in tools in `skills/guide/ask/references/built-ins.md` line 5
- custom sub agents and agent teams in `skills/guide/ask/references/sub-agents.md` line 5 and `skills/guide/ask/references/team-mode.md` line 5

That is not a terminology swap. It is a content rewrite.

### 3. Onboarding depends on Claude-specific commands and modes

The onboarding flow assumes:

- `CLAUDE.md`
- `/init`
- `/model`
- `/compact`
- Shift+Tab mode switching
- permission modes like Accept Edits and bypass permissions

See the original `skills/guide/onboarding/SKILL.md` line 16, `skills/guide/ask/references/setting-your-environment.md` line 37, and `skills/guide/ask/references/starting-to-work.md` line 7.

For Codex, the onboarding center of gravity should shift to:

- `AGENTS.md`
- sandbox and approval behavior
- the explore, plan, implement, verify loop
- skill usage
- practical repo workflows

### 4. The ask skill index is tightly coupled to Claude docs

The current ask skill enumerates Claude-specific reference files directly in its prompt contract. See the original `skills/guide/ask/SKILL.md` line 16.

That means the ask skill should be ported last, after the reference tree is redesigned.

## Codex-native target

### Content model

Build the Codex guide around these concepts:

- `AGENTS.md` as the main project instruction surface
- Codex skills as the reusable guidance mechanism
- sandboxing and approval as the main safety model
- plan-first workflows for non-trivial work
- repo-aware coding habits: inspect, plan, patch, test, review

Avoid claiming support for features unless you can verify them in Codex docs or the local environment.

## Proposed repo structure

```text
codex-guide/
├── AGENTS.md
├── README.md
├── docs/
│   └── claude-to-codex-conversion-plan.md
└── skills/
    ├── codex-guide-onboarding/
    │   ├── SKILL.md
    │   └── agents/
    │       └── openai.yaml
    └── codex-guide-ask/
        ├── SKILL.md
        ├── agents/
        │   └── openai.yaml
        └── references/
            ├── getting-started.md
            ├── working-with-codex.md
            ├── best-practices.md
            ├── skills.md
            ├── agents-md.md
            ├── sandbox-and-approvals.md
            └── stories/
```

## Recommended file mapping

| Claude source | Codex target | Notes |
|---|---|---|
| `CLAUDE.md` | `AGENTS.md` | Direct conceptual replacement, but rewrite examples and rules |
| `skills/guide/onboarding/SKILL.md` | `skills/codex-guide-onboarding/SKILL.md` | Keep interactive flow, rewrite content |
| `skills/guide/ask/SKILL.md` | `skills/codex-guide-ask/SKILL.md` | Keep retrieval pattern, rewrite reference index |
| `skills/guide/ask/references/*.md` | `skills/codex-guide-ask/references/*.md` | Selective port; most files need rewrite |
| `.claude-plugin/*` | remove | No verified Codex equivalent in local env |
| `PRIVACY.md` | optional, rewrite later | Only needed if you publish with a clear install/distribution story |

## Recommended doc set for v1

Start with a smaller, accurate Codex set instead of porting all 16+ Claude reference docs immediately.

### Keep and rewrite first

- `getting-started.md`
- `working-with-codex.md`
- `best-practices.md`
- `agents-md.md`
- `skills.md`
- `sandbox-and-approvals.md`
- `stories/starting-new-repo.md`
- `stories/daily-workflow.md`

### Delay until verified

- external tool integration guidance that depends on specific Codex support
- CI automation guidance
- any Codex equivalent to hooks
- any Codex equivalent to sub agents or agent teams
- model-selection advice beyond what Codex officially exposes

### Drop unless a verified Codex counterpart exists

- plugin marketplace docs
- hook docs
- hook HTTP docs
- sub-agent docs as a named product feature
- agent-team docs as a named product feature

## Concrete concept mapping

| Claude concept | Codex replacement | Conversion note |
|---|---|---|
| `CLAUDE.md` | `AGENTS.md` | Make this the first concept every new user learns |
| `/guide:onboarding` | onboarding skill trigger | Do not depend on slash-command names unless Codex explicitly supports them |
| `/guide:ask` | ask skill trigger | Same note as above |
| `/init` | manual `AGENTS.md` bootstrap guidance | If Codex later gets an init command, add it only after verification |
| Plan Mode | explicit planning workflow | Teach users to ask Codex to inspect first and produce a plan |
| Accept Edits / permission modes | sandbox and approval model | Rewrite around Codex terminology |
| Plugins | installable skill repo | The repo itself should be the distribution unit |
| Built-in sub agents | none assumed | Do not imply a native Codex equivalent |
| Hooks | none assumed | Treat as unsupported until verified |

## Porting sequence

### Phase 1: Reshape the repo

1. Add `skills/` with two Codex-native skill folders.
2. Keep `README.md` human-facing and installation-focused.
3. Use `AGENTS.md` as the contributor and repo-agent contract.
4. Remove all plugin-manifest assumptions from the target repo structure.

### Phase 2: Port onboarding first

Write `codex-guide-onboarding` from scratch rather than translating line by line.

The onboarding flow should teach:

- what `AGENTS.md` is and how to write one
- how Codex reads and edits a repo
- how sandboxing and approvals affect command execution
- how to ask for exploration first, then a plan, then implementation
- how to review diffs and ask for verification
- how to keep tasks scoped and acceptance criteria explicit

This skill is the best first deliverable because it can guide the rest of the repo buildout.

### Phase 3: Build the ask skill shell

Create `codex-guide-ask/SKILL.md` with a narrow reference list at first. Do not point it at missing or half-ported docs.

Initial references should cover only:

- getting started
- `AGENTS.md`
- sandbox and approvals
- Codex best practices
- local skills

### Phase 4: Rewrite reference docs by theme

Rewrite, do not mechanically port, in this order:

1. environment and `AGENTS.md`
2. how to work with Codex day to day
3. best practices
4. skills
5. stories
6. advanced topics only after verification

### Phase 5: Rebuild installation and distribution docs

Once the skills exist, update the README to explain one clear path:

- clone the repo
- install or copy the skills into `~/.codex/skills`
- or use a Codex-native installer flow if you later verify one

Do not write marketplace or plugin language into v1.

## First implementation pass I would make

If you want the smallest useful Codex mirror quickly, ship this:

1. `skills/codex-guide-onboarding/SKILL.md`
2. `skills/codex-guide-ask/SKILL.md`
3. `skills/codex-guide-ask/references/agents-md.md`
4. `skills/codex-guide-ask/references/sandbox-and-approvals.md`
5. `skills/codex-guide-ask/references/best-practices.md`
6. `skills/codex-guide-ask/references/stories/starting-new-repo.md`
7. `README.md` with local install instructions

That gives you a usable onboarding guide without blocking on every advanced feature mismatch.

## Risks

- A literal mirror will be misleading because users will assume Codex supports Claude plugin semantics.
- A broad first port will create stale or speculative docs quickly.
- If you keep the Claude information architecture unchanged, the Codex guide will spend too much space explaining what Codex is not.

## Recommendation

Do not convert this repo by renaming terms.

Use `claude-code-guide` as a content source and structural reference, but rebuild the Codex version around:

- `AGENTS.md`
- Codex skills
- sandbox and approvals
- inspect, plan, implement, verify

That will feel like a true mirror in intent, not a misleading port in wording.
