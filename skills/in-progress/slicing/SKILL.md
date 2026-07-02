---
name: slicing
description: "Phase 3 of the delivery pipeline. Use after the MVP line is approved to cut, plan, complete, or recut demoable vertical slices from delivery/BACKLOG.md — walking skeleton first, each cut attacked for thinness — until every above-the-line item is demoed and the pipeline reaches Phase: mvp-satisfied."
argument-hint: "[nothing | plan | done <#> | recut <#>]"
---

# slicing

Phase 3 of the **delivery** pipeline (planning → prioritizing → slicing). Slicing turns the
approved MVP line in `delivery/BACKLOG.md` into demoable vertical slice contracts under
`delivery/slices/`. `BACKLOG.md` already exists with an approved line; read it first.

State stays in `BACKLOG.md`. Slice files are stateless contracts — cheap to re-cut.

## Usage

```
/delivery:slicing
/delivery:slicing plan
/delivery:slicing done 2
/delivery:slicing recut 2
```

## Route

Read the `Phase:` marker in `delivery/BACKLOG.md`:

- No file or `Phase: planning` → stop, point to `/delivery:planning`.
- `Phase: prioritizing` → stop, point to `/delivery:prioritizing`.
- `Phase: slicing` → cut, plan, done, or recut.
- `Phase: mvp-satisfied` → only continue for recut, amend, or a reopened line.

## Steps

### 1. Cut vertically

A slice is named after **what the customer can do** after it ships. It cuts through every
layer the product needs and demos to a non-builder. It is not a component, task list, or sprint.

**Skeleton first:** if no MVP item is `done` or assigned to a slice, slice 1 is the walking
skeleton — the thinnest ribbon across all steps of the core loop, even with hardcoded paths,
seeded data, or no edge cases. It should feel almost embarrassingly small.

For each cut, define **In** (the thinnest version that demos), **Out** (the remainder, where
it lives, whether it stays waiting or below the line), and write **acceptance as a demo script
a non-builder can watch**. Refuse horizontal cuts named after layers or components.

**Plan mode** (`plan`): cut a full provisional slice plan to MVP satisfaction. Unstarted slice
plans are provisional; recut them when learning changes the shape.

### 2. Minimize the cut (adversarial thinness)

The drafter is attached to the slice, so it needs a counterweight that argues to make it
**thinner**. Run this with independence: if your host can spawn a fresh-context subagent
(Claude Code: the `Task`/`Agent` tool, granted only `Read, Grep, Glob`), spawn one to attack
each draft slice; otherwise re-read the draft from disk, state *"I did not write this; my job
is to make it thinner,"* and attack inline.

The slice's customer action must still demo to a non-builder. Under that constraint, argue:
fewer items IN (move to Out), a narrower version of each (one path, no edge cases, hardcoded
variants), any demo-script step not needed to prove the action. A slice padded to batch extra
work into one cut is a finding, not a defense. The walking skeleton should survive trivially —
say so and move on. Accept attacks you cannot defend; the user decides the rest.

### 3. Write the contract

Write each slice to `delivery/slices/NN-<slug>.md`:

```markdown
# Slice NN: <what the customer can do>
Cut: <date> | Covers MVP items: <#s from BACKLOG.md>

## In (thinnest version)
- ...

## Out (explicitly — and where it lives)
- ...

## Demo script (= done)
1. ...
```

Set covered MVP items to status `slice NN` in `BACKLOG.md`. Slice files hold no state.

### 4. Close or recut

**`done <#>`** — only after the slice demoed end-to-end to a non-builder → set covered MVP
items to `done`. Not demoed → keep it open, record one line on why. If the slice grew, recut.
If it proved `BACKLOG.md` wrong, route to `/delivery:prioritizing amend`.

**`recut <#>`** — shrink In to what actually demos, return the rest to `waiting`, rewrite the
slice file, renumber only unstarted slices.

### 5. Report coverage

End every run with MVP coverage: `n of m MVP items done`. When every MVP item is `done`, set
`Phase: mvp-satisfied` and say the pipeline is complete.

## Verify before finishing

Independently (subagent if the host supports one, else a fresh re-read of `BACKLOG.md` and the
touched slice files), check:

1. **Slice tracing** — every slice covers MVP items by number and nothing below the line;
   covered items carry status `slice NN`; each slice's Out list says where the rest lives.
2. **Vertical shape** — flag slices named after components or layers instead of customer
   action, and any demo script a non-builder couldn't follow.
3. **No state in slice files** — all state stays in `BACKLOG.md`.
4. **Status legality** — MVP statuses only `waiting` / `slice NN` / `done`; `done` only via a
   demoed slice; no deleted `done` rows.
5. **Locked vocabulary** (only if a glossary is declared) — use its terms and usage rules.

Report `PASS` or a numbered `VIOLATIONS:` list (offending line quoted short, which check, the
fix). Do not soften. Fix violations before finishing.

## Anti-patterns

- Do not let sprint cadence decide slice boundaries.
- Do not create horizontal slices (named after layers, not customer action).
- Do not mark a slice done because code merged; done means demoed end-to-end.
- Do not put state in slice files.
- Do not smuggle Later items into a slice.
- Do not keep building a slice that grew; recut it.
- One thin demo beats a complete layer.
