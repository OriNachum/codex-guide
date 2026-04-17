---
title: Skills
parent: Working with Codex
nav_order: 4
---

# Skills

Codex skills are reusable instruction bundles that let you package a workflow,
playbook, or domain-specific guidance so another Codex instance can apply it
repeatedly.

## Overlap with Claude Code

Skills are one of the clearest shared concepts between Claude Code and Codex:
both use Markdown instruction bundles to package reusable workflows.

The main Codex-specific differences are:

- installation through `.agents/skills` and `$HOME/.agents/skills`
- explicit invocation with `$skill-name`
- optional `agents/openai.yaml` metadata for UI and invocation policy

## When a skill is worth creating

Create a skill when you notice a repeated pattern such as:

- the same onboarding guidance across repos
- the same review checklist across tasks
- the same deployment or release procedure
- the same domain-specific explanation or workflow

If you have explained the same process several times, it is probably a skill.

## What a skill should contain

At minimum, a skill has:

- a `SKILL.md`

Often it also has:

- `references/` for larger docs loaded on demand
- `scripts/` for deterministic helper logic
- `agents/openai.yaml` for UI metadata

## Good skill design

Good skills are:

- narrow enough to trigger for the right tasks
- clear about when to use them
- lean in the main `SKILL.md`
- willing to push detail into `references/`

The goal is not to restate everything Codex already knows. The goal is to encode project or workflow knowledge that improves execution.

## What not to do

Avoid skills that are:

- vague enough to trigger on everything
- huge reference dumps in the main `SKILL.md`
- full of speculative product features
- disconnected from real workflows

## Example pattern

A strong skill usually says:

- what it does
- when to use it
- what steps to follow
- what references to load only when needed

That is the pattern this repo uses for:

- `codex-guide-onboarding`
- `codex-guide-ask`

## How this repo uses skills

This repo treats skills as the main distribution unit.

Instead of assuming a plugin system, it packages Codex guidance as local skills you can install into repository `.agents/skills` folders or into `$HOME/.agents/skills` and invoke directly.

## Official behaviors to remember

- Skills can be invoked explicitly with `$skill-name`.
- Codex can also invoke a skill implicitly when the task matches the skill description.
- The built-in `$skill-installer` can install additional skills.
- `agents/openai.yaml` can control optional UI metadata, dependencies, and invocation policy.

## Practical guidance

Use a skill when the workflow is stable enough to reuse but still benefits from
Codex judgment. If the task needs strict deterministic logic, move the
mechanics into `scripts/` and keep the skill as the orchestrator.
