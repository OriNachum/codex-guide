# Codex Code Guide (Claude → Codex Mirror)

This guide mirrors common **Claude Code** concepts and translates them into practical workflows for **Codex**.

> Intent: give people who know Claude a fast path to working effectively with Codex.

---

## 1) Mental model shift: from “single assistant” to “instruction layers + tools”

In Codex, behavior comes from stacked instructions and tool access:

1. **System instructions** (platform-level, highest priority)
2. **Developer instructions** (project/task-level policy)
3. **User instructions** (your request)
4. **Repository guidance** (for example `AGENTS.md` files in scope)

When these conflict, higher-priority instructions win.

### Claude-style equivalent
- Claude users often rely on `CLAUDE.md` + prompt habits.
- In Codex, the closest pattern is: **explicit task prompt + repo-scoped `AGENTS.md` + tool-aware constraints**.

---

## 2) `CLAUDE.md` equivalent in Codex: `AGENTS.md`

If you used `CLAUDE.md` to define conventions, workflows, or house rules, use `AGENTS.md` in Codex repos.

### Key behavior
- `AGENTS.md` applies to the directory tree rooted at its location.
- Nested `AGENTS.md` files can override broader rules.
- The agent should obey all in-scope `AGENTS.md` instructions for files it touches.

### Practical recommendation
Keep `AGENTS.md` concise and operational:
- coding standards
- test commands
- commit/PR conventions
- architecture boundaries
- “never do X” repo rules

---

## 3) Tooling mindset: Codex is strongest when tool calls are explicit

Claude workflows often feel conversational-first; Codex workflows are often **execution-first**:

- shell execution for inspection and changes
- structured plan updates for multi-step work
- browser/playwright tools when UI validation is needed
- PR composition tools when required by environment

Treat Codex like an engineer with terminal + policy constraints, not just a text model.

---

## 4) Planning behavior: when to plan vs just do

In Codex, plans are useful for multi-step or uncertain tasks. Typical pattern:

- quick repo scan
- short plan with 3–6 concrete steps
- execute, update status, verify, summarize

For simple tasks, skip heavy process and directly implement.

---

## 5) Prompting translation (Claude → Codex)

### A) High-level feature request
**Claude-style:**
> Add OAuth login and update docs.

**Codex-optimized:**
> Add Google OAuth login to the web app using existing auth patterns.  
> Constraints: no new framework, keep current folder layout, add unit tests for token validation, and update `README.md` + `docs/auth.md`.  
> Run project tests and include a concise change summary.

Why this works in Codex:
- explicit scope
- explicit constraints
- explicit validation
- explicit deliverables

### B) Refactor request
**Claude-style:**
> Clean up this service.

**Codex-optimized:**
> Refactor `services/payment_processor.py` to reduce duplication in provider mapping logic. Preserve behavior.  
> Add regression tests for Stripe and PayPal mapping paths.  
> Keep public method signatures unchanged.

### C) Debug request
**Claude-style:**
> Why does this crash?

**Codex-optimized:**
> Investigate the crash in `POST /api/orders` when `coupon_code` is null.  
> Reproduce from existing tests/logs, identify root cause, implement smallest safe fix, and add a test that fails before and passes after.

---

## 6) Code-review and QA mode

A common Codex workflow is static QA review with strict constraints.

When asked for findings:
- prioritize correctness, security, and maintainability
- point to exact files/functions
- provide implementation-ready remediation guidance
- if your environment asks for a specific template (like task stubs), follow it exactly

---

## 7) Safe execution defaults

Whether or not you come from Claude, use this Codex baseline:

1. Inspect before editing.
2. Minimize blast radius.
3. Prefer targeted changes over broad rewrites.
4. Run relevant checks.
5. Summarize what changed + what was validated.

If environment constraints block execution (missing deps / no network), report clearly and provide next-best static validation.

---

## 8) Git workflow translation

Many Codex environments expect strict completion flow:

- make edits
- run checks
- commit with clear message
- create PR text/tool output if required

If automation instructions explicitly require commit + PR artifact, treat that as mandatory completion criteria.

---

## 9) Repository structure suggestions for Codex-first teams

A lightweight setup:

- `AGENTS.md` — operational instructions for agents
- `README.md` — human overview and getting started
- `docs/` — architecture decisions, runbooks, conventions
- `scripts/` — repeatable checks and local automation

Optional:
- small prompt/task templates for recurring work (bugfixes, feature specs, release notes)

---

## 10) Quick “Claude to Codex” cheat sheet

- `CLAUDE.md` guidance → `AGENTS.md` scoped instructions
- chat-first iteration → execution + verification loop
- generic request → constrained, file-aware task prompt
- “looks good” → explicit checks, outputs, and completion artifacts

---

## 11) Example reusable prompt templates

### Feature template
> Implement `<feature>` in `<paths>`.  
> Constraints: `<constraints>`.  
> Add/update tests for `<cases>`.  
> Update docs in `<docs paths>`.  
> Run `<commands>` and summarize results.

### Bugfix template
> Investigate `<symptom>` in `<module/path>`.  
> Find root cause, implement minimal fix, add regression test, and summarize risk/impact.  
> Validate with `<commands>`.

### Refactor template
> Refactor `<target>` to improve `<goal>` without changing behavior.  
> Keep `<public APIs>` stable.  
> Add tests proving no behavior drift in `<key scenarios>`.

---

## 12) Final note

If you're migrating from Claude workflows, don't overthink perfect mapping.

Start with:
- clear constraints
- scoped file targets
- explicit validation commands
- concise final summaries

That alone gets most teams to consistent, high-quality Codex outcomes.
