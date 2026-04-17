---
title: Mission 2 - Add the Site Skeleton
parent: Exercises
nav_order: 2
---

# Mission 2: Add the Site Skeleton

## Objective

Turn the repo into a browsable static site without duplicating the guide corpus.

## What this teaches

- how to scaffold a focused feature in a docs-first repo
- how to reuse existing source files instead of copying them
- how to add build verification for a new subsystem

## Suggested Codex prompt

```text
Inspect the current docs and skills layout.
Add a minimal Jekyll site with a landing page, navigation hubs, and a build
workflow that publishes the existing guide content instead of duplicating it.
```

## Expected deliverable

Site config, landing page, hub pages, and a passing local `jekyll build`.

## Verification commands

```bash
bundle exec jekyll build
markdownlint-cli2 "**/*.md"
python3 scripts/validate-docs.py
```

## Stretch goal

Add a short contributor note explaining which docs are public-site content and
which are internal planning notes.
