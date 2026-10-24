# Review ledger

Every PR keeps a "Review ledger" section in its body. The implementer maintains it. A PR merges when no row is open.

## Dimensions

A finding records four separate facts about who made it.

- **Role:** reviewer, implementer, coordinator or owner.
- **Model**, with its version.
- **Harness:** the agent runtime that ran the model, for example Claude Code, Antigravity CLI, OpenCode or Codex. Some projects call it the provider.
- **Effort**, as the harness names it.

## Tags

A model's finding is tagged `<role>-<model>-r<round>-<severity><n>`, for example `reviewer-sonnet-r2-b1`. An owner decision is `owner-<n>`. A coordinator finding is `coordinator-<n>`.

- Severity is `b` blocking, `s` should-fix, or `n` nit.
- Use the model's plain name in the tag, without its version. The table carries the version.

Reviewers start each inline comment and each finding with its tag. Replies quote the tag. When two reviewers find the same thing, the row lists both tags.

## Table

| Tag | Role | Model | Harness | Effort | Where | Severity | Finding | Status | Fix |
|---|---|---|---|---|---|---|---|---|---|
| reviewer-sonnet-r2-b1 | reviewer | Sonnet 5.5 | Claude Code | high | `path/to/file.js:273` | blocking | drag preview never attached to the DOM | fixed | `<sha>` |
| owner-1 | owner | | | | `path/to/file.js` | should-fix | move the handler into the component | open | |

Owner rows leave model, harness and effort empty.

## Fan-in

Each reviewer returns one verdict, `PASS`, `ISSUES` or `BLOCKED`, with evidence: the command run, the output, the file and line. A reviewer that can prove a defect lists every defect it can prove, not only the first. The coordinator summarizes the returns into ledger rows and leaves raw reports out of the PR body. Done when every row traces to a returned report and the PR body holds no pasted report.

## Statuses

- `open`: not yet handled. Counts as open.
- `fixed`: the fix commit is in the last column.
- `dismissed (<who decided>)`: a reviewer's finding the owner or reviewer withdrew.
- `deferred (#issue)`: code work moved to a named follow-up issue.
- `disputed`: the implementer and the reviewer disagree. Counts as open until one side settles it.
- `unverified (<who> checks <what> on <where>)`: a check nobody could run in this environment. Counts as open. The PR merges with it only on the owner's written grant, and the row stays in the table.

Why `unverified` counts as open: a PR merged with an OS-level drag unchecked, and the bug surfaced when the owner used it.

## Signature

When posts go out from one shared account, each one ends with a line saying who wrote it:

`— Posted for: <role> · <model + version> · <harness> · effort <level>`

For example: `— Posted for: reviewer · Sonnet 5.5 · Claude Code · effort high`.

When the coordinator posts a reviewer's findings, the role is still the reviewer's, and the model, harness and effort are the reviewer's.

## Closing attribution

When an agent did the work, the PR body ends with one line that separates who wrote the code from who reviewed it. Each side names its model and harness, and its effort when you know it. Projects can read this line for policy, so keep the two roles apart.

Short form:

`Written by: Model A 1.2, Harness X. Reviewed by: Model B 3.0, Harness Y.`

Fuller form:

`Written by Model A 1.2 at high effort through Harness X. Reviewed independently by Model B 3.0 at xhigh effort and Model C 2.1 at high effort.`

Done when the written-by side names the implementer and the reviewed-by side names each reviewer, matching the picks recorded for the session and any ticket override.
