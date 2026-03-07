# Automations and local environments

Codex app automations and local environments are related but different.

## Automations

Automations schedule recurring Codex tasks in the background.

Documented behaviors:

- they run locally in the Codex app
- the app must be running
- the selected project must be available on disk
- Codex can add findings to the inbox or archive runs with nothing to report
- skills can be used inside automations for more complex tasks

For Git repositories, automations run on dedicated background worktrees.

## Automations vs GitHub Actions

Automations are not the same as GitHub Actions.

- Codex automations run locally in the Codex app
- GitHub Actions run on GitHub-hosted or self-hosted runners

The overlap is conceptual: both are useful for recurring unattended checks.

Use app automations when the work should stay close to your local project and
app workflow. Use GitHub Actions when the task belongs in repository CI.

## Local environments

Local environments define project-specific setup steps and common actions.

They are used for:

- setup scripts that prepare new worktrees
- common actions such as starting the app or running tests

This configuration is stored inside the project’s `.codex` folder and can be checked into Git for teammates.

## Overlap with Claude-style workflow automation

If you are coming from the Claude guide, app automations fill some of the same
recurring-maintenance space as scheduled CI workflows, but they are a different
execution environment.

## Why the distinction matters

- automations are for recurring unattended tasks
- local environments are for preparing and operating the project consistently

They fit together well, but they solve different problems.
