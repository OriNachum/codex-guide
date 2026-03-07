# Daily workflow

## Morning: establish context

You open a repository and want to pick up a bug fix from yesterday.

A good starting prompt is:

```text
Read AGENTS.md and inspect the auth-related files involved in session refresh.
Summarize the current flow and identify where the timeout bug is most likely coming from.
Do not edit anything yet.
```

This keeps the first turn focused on understanding, not premature editing.

## Mid-morning: plan before changing code

Once Codex has the relevant context, ask for a bounded plan:

```text
Create a plan for fixing the timeout bug with the smallest behavior change possible.
List the files to edit and the tests to run.
```

Now you can review the shape of the work before any patch lands.

## Late morning: implement and verify

After the plan looks right:

```text
Implement the fix from the plan.
Stay within the identified files unless you find a hard blocker.
Run the targeted tests afterward.
```

This keeps the implementation tied to the agreed scope.

## Afternoon: review another change

Codex is also useful for read-heavy review work:

```text
Review the current branch against main.
Focus on error handling, test gaps, and any obvious behavioral regression risks.
```

This works well because the task is explicit and the output can be checked directly against the diff.

## End of day: improve the repo contract

If you notice repeated friction, encode it:

- add the missing command to `AGENTS.md`
- record a workflow rule Codex should follow
- tighten a skill if you are repeating the same instructions

The workflow gets better when the repo instructions improve alongside the code.

## Why this pattern scales

The day works well when each task follows the same rhythm:

1. inspect
2. plan
3. implement
4. verify
5. review

That rhythm is simple, but it prevents a large share of avoidable mistakes.
