# Codex docs freshness prompt

You are maintaining the `codex-guide` repository.

Your job is to compare the guide's published Codex reference docs against
official OpenAI Codex sources and fix factual inaccuracies only.

Constraints:

- Check only these official sources:
  - <https://help.openai.com/en/articles/11096431-openai-codex-ci-getting-started>
  - <https://platform.openai.com/docs/docs-mcp>
  - <https://developers.openai.com/codex/hooks>
  - <https://openai.com/codex>
  - <https://openai.com/index/introducing-the-codex-app/>
- Restrict edits to the guide's user-facing Codex references under
  `skills/codex-guide-ask/references/`.
- Do not add new feature claims that are not grounded in those sources or in the
  local repo.
- Do not make formatting-only changes.
- Do not touch `README.md`, `AGENTS.md`, or skill prompts unless a factual
  correction in the references requires a matching wording update.

Process:

1. Read the references under `skills/codex-guide-ask/references/`.
2. Fetch the official OpenAI sources and compare them against the references.
3. If every checked page is current, create a GitHub issue titled
   `docs-freshness: weekly check (YYYY-MM-DD)` summarizing the audit and stop.
4. If any checked page is outdated:
   - make the smallest factual corrections
   - rerun the repo validation commands
   - create the same audit issue with the findings
   - leave the workspace ready for a pull request

When creating the issue, include:

- files checked
- current versus outdated files
- which official source justified each change
- any URLs that failed
