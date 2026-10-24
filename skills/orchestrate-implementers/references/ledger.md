# Review ledger

Every PR keeps a "Review ledger" section in its body. The implementer maintains it. A PR merges when no row is open.

## Tags

Each finding gets a stable tag `<REVIEWER>-R<round>-<severity><n>`.

- REVIEWER is a short code the owner assigns to each reviewer, one for the owner and one for the coordinator, for example `OWN` and `COO`.
- Severity is `B` blocking, `S` should-fix, or `N` nit.
- Examples: `REV-R2-B1`, `SEC-R1-N5`.

Reviewers start each inline comment and each finding with its tag. Replies quote the tag. When two reviewers find the same thing, the row lists both tags.

## Table

| Tag | Found by (model, version, effort) | Where | Severity | Finding | Status | Fix / reply |
|---|---|---|---|---|---|---|
| REV-R2-B1 | Model A 1.2 · effort high | `path/to/file.js:273` | blocking | drag preview never attached to the DOM | fixed | `<sha>` |

## Statuses

- `open`: not yet handled. Counts as open.
- `fixed`: the fix commit is in the last column.
- `dismissed (<who decided>)`: a reviewer's finding the owner or reviewer withdrew.
- `deferred (#issue)`: code work moved to a named follow-up issue.
- `disputed`: the implementer and the reviewer disagree. Counts as open until one side settles it.
- `unverified (<who> checks <what> on <where>)`: a check nobody could run in this environment. Counts as open. The PR merges with it only on the owner's written grant, and the row stays in the table.

Why `unverified` counts as open: a PR merged with an OS-level drag unchecked, and the bug surfaced when the owner used it.

## Found by

Name the model with its version and the effort, for example "Model A 1.2 · high". A reviewer run through a wrapper tool names the wrapper and its model too.

## Signature

When posts go out from one shared account, each one ends with a line saying who wrote it:

`— Posted for: <role> · <model and version> · effort <level>`

Roles are reviewer, implementer and coordinator. When the coordinator posts a reviewer's findings, the role is still the reviewer's.
