---
title: Starting in a new repo
parent: Stories
nav_order: 1
---

# Starting in a new repo

## The situation

You have a repository, but no useful `AGENTS.md` yet. You want Codex to be productive quickly without handing it a large, risky task on the first turn.

## A good first session

Start with repository context:

```text
Read the repo structure and the main docs. Then draft or improve AGENTS.md with the build, test, and lint commands plus any project-specific workflow rules you can verify.
```

That gives Codex a bounded task with an immediately reviewable output.

## What happens next

After `AGENTS.md` exists, pick a small, verifiable task:

```text
Inspect the tests around user profile updates and add coverage for the missing validation case.
Make a plan first, then implement it, then run the relevant tests.
```

This is a good first task because:

- the scope is narrow
- the success condition is clear
- verification is local
- the diff is easy to review

## Why this works

The first sessions should optimize for trust, not speed.

You want to learn:

- whether Codex reads the repo accurately
- whether `AGENTS.md` changes its behavior in the right way
- whether the verification loop is working
- whether approval requests are appropriately scoped

## What to avoid

Avoid starting with:

- a sweeping refactor
- a new subsystem
- a request with no acceptance criteria
- a production-only debugging task with weak reproduction

Those are fine later, after the repo instructions and working rhythm are solid.

## A simple progression

1. create or improve `AGENTS.md`
2. complete one small verifiable task
3. tighten instructions based on what Codex missed
4. expand to larger changes only after the loop feels predictable
