# Findings

Findings live as review comments on the PR. The PR body stays short for every human and agent who reads it, and carries only the closing attribution line.

## Dimensions

A finding records four separate facts about who made it.

- **Role:** reviewer, implementer, coordinator or owner.
- **Model**, with its version.
- **Harness:** the agent runtime that ran the model, for example Claude Code, Antigravity CLI, OpenCode or Codex. Some projects call it the provider.
- **Effort**, as the harness names it.

The tag carries the role and the model. The signature on each comment carries all four.

## Tags

A model's finding is tagged `<role>-<model>-r<round>-<severity><n>`, for example `reviewer-sonnet-r2-b1`. An owner decision is `owner-<n>`. A coordinator finding is `coordinator-<n>`.

- Severity is `b` blocking, `s` should-fix, or `n` nit.
- Use the model's plain name in the tag, without its version.

Each finding is an inline review comment that starts with its tag. Replies quote the tag. When two reviewers find the same thing, the later comment names the earlier tag. Where the harness cannot post inline comments, for example a read-only reviewer the coordinator posts for, the coordinator posts one review with the findings as separate comments, each starting with its tag. Done when every finding has its own comment with its tag first.

## Fan-in

Each reviewer returns one verdict, `PASS`, `ISSUES` or `BLOCKED`, with evidence: the command run, the output, the file and line. A reviewer that can prove a defect lists every defect it can prove, not only the first. The coordinator turns the returns into review comments and leaves raw reports out of the PR. Done when every comment traces to a returned report and no report is pasted into the PR body.

## Reply and resolve

The implementer answers each finding with a reply, then resolves the conversation with the platform's resolve control. The reply wording is the status.

- `Fixed in <sha>.` Resolve.
- `Dismissed by <who>: <reason>.` Resolve, when the reviewer or the owner dismissed it.
- `Deferred to #<issue>.` Resolve, once the follow-up issue exists.
- `Disputed: <reason>.` Leave unresolved until the reviewer or the owner settles it.
- `Unverified: <who> checks <what> on <where>.` Leave unresolved until the owner grants it in writing.

Why `unverified` stays unresolved: a PR merged with a check nobody could run, and the bug surfaced when the owner used it.

## Merge check

Merge when no review thread is unresolved, no reviewer verdict is `BLOCKED`, and the project's own verification has passed at the head. Done when you can name the head SHA, the count of unresolved threads (zero) and each reviewer's last verdict.

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

Done when the written-by side names the implementer and the reviewed-by side names each reviewer, matching what actually ran.
