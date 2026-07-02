---
name: prioritizing
description: Phase 2 of the delivery pipeline. Use after planning to draw, review, and approve the MVP line in delivery/BACKLOG.md — attack every above-the-line item down to the absolute minimum, and promote, amend, or reorder line decisions after slicing has started.
argument-hint: "[nothing | promote <item> | reorder | amend]"
---

# prioritizing

Phase 2 of the **delivery** pipeline (planning → prioritizing → slicing). Prioritizing
converts the captured capabilities in `delivery/BACKLOG.md` into an approved MVP line: what
value fails without, what stays later/manual/deferred, and what must move when the line
changes. `BACKLOG.md` already exists (planning created it); read it first.

## Usage

```
/delivery:prioritizing
/delivery:prioritizing promote "bulk import customers"
/delivery:prioritizing amend
/delivery:prioritizing reorder
```

## Route

Read the `Phase:` marker in `delivery/BACKLOG.md`:

- No file or `Phase: planning` → stop, point to `/delivery:planning`.
- `Phase: prioritizing` → draw or resume the MVP line (steps below).
- `Phase: slicing` / `mvp-satisfied` with no mode → point to `/delivery:slicing`.
- `Phase: slicing` / `mvp-satisfied` with `promote` / `reorder` / `amend` → run that mode.

## Steps (draw the line)

### 1. Split

Using the confirmed value hypothesis and the Captured capabilities:

- **Above the line** — only items where value creation fails without them. State the concrete
  failure in one line with a source. Default to below when the failure is weak.
- **Below the line** — everything else, each with a why-below: later / manual for now /
  adjacent / unknown.

Challenge anything that can be manual, seeded, hardcoded, delayed, merged, or made thinner
while the core loop still works.

### 2. Order and size

Order MVP items by: (1) completes the core loop earliest, (2) unblocks what is next, (3)
earliest real customer value. Size each `S` / `M` / `L`, relative to each other.

### 3. Minimize the line (adversarial)

The drafter is attached to every line, so the line needs a counterweight that argues to
**shrink** it. Run this attack with independence: if your host can spawn a fresh-context
subagent (Claude Code: the `Task`/`Agent` tool, granted only `Read, Grep, Glob`), spawn one
to attack the proposed MVP section; otherwise re-read the section from disk, state *"I did not
write this; my job is to make it smaller,"* and attack inline.

For each above-the-line item, try in order — nothing attacked is deleted, it moves below the
line, so argue without mercy:

1. **Below** — the hypothesis still holds without it: the customer completes the core loop;
   something is uglier or manual, but value is created.
2. **Manual** — a human does it behind the scenes during early usage (evidence-gathering).
3. **Hardcode / seed** — a static or seeded version creates the same value for the first customers.
4. **Merge** — fold it into another item and push the remainder below.

Only if all four fail does the item survive — with a one-line concession: the concrete way the
core loop breaks without it. Judge **only** against the stated hypothesis, not polish; "users
will expect it" is not a core-loop failure. Read a cited source when a line leans on it — a
citation that doesn't support the line is itself grounds to attack.

Accept attacks you cannot defend. Where you can defend an item, present the attack **and** the
defense to the user; the user decides. An item stays above only with a defense actually made.

**Completion criterion:** every above-the-line item has either survived a made defense or moved below.

### 4. Checkpoint

Present the line — this is the Phase-2 checkpoint; the line is the user's to approve. On
approval: set `Phase: slicing`, ensure every MVP row has status `waiting`, run **Verify**
(below), and offer to start `/delivery:slicing`. If the user rejects the line, keep
`Phase: prioritizing`, record the disagreement in Open questions or Amendments, and revise.

## Maintenance modes

### promote

Never move an item above the line directly. Gate questions in order:
1. Does the value hypothesis fail without it?
2. Can it stay below — deferred, manual, seeded, or hardcoded?
3. If it comes up, what moves down or becomes thinner?

On PASS: move the row up with its failure line, size it, order it, log the promotion in
Amendments, and reopen `Phase: mvp-satisfied` → `Phase: slicing`. On fail: it stays below;
give the user one sentence on what would change the decision.

### amend

Use when building proves `BACKLOG.md` wrong — an MVP item is unnecessary, a Later item blocks
the core loop, the hypothesis shifts, or a slice exposes a bad boundary. Propose the change
and what was learned; on approval, log it in Amendments and update the tables.

### reorder

Adjust order only for `waiting` MVP items and anything below the line. Keep every grounding
line intact. Never delete a `done` row.

## Output — MVP / Later sections of `delivery/BACKLOG.md`

```markdown
## MVP — above the line
Only items value-creation fails without. Crossing the line requires promote.
Satisfied when every row here is covered by a demoed slice. Status: waiting → slice NN → done.

| # | Capability | Core-loop step | Value fails without it because (source) | Status | Size |
|---|---|---|---|---|---|

## Later — below the line
Everything else. Adding here is free — nothing is rejected, only prioritized.

| Capability | Why below (later / manual for now / adjacent / unknown) | Source |
|---|---|---|
```

## Verify before finishing

Independently (subagent if the host supports one, else a fresh re-read of `BACKLOG.md`), check:

1. **Line integrity** — every above-the-line item carries a concrete "value fails without it
   because" line referencing the hypothesis or a cited source that actually supports it (read
   the citation; an unsupported one is a violation). A preference ("important", "expected")
   instead of a failure is a violation.
2. **Amendments logged** — every promotion/demotion appears in Amendments; a line-crossing
   with no log entry is a violation.
3. **No duplication** — cite sources, don't restate them.
4. **Locked vocabulary** (only if a glossary is declared) — use its terms and usage rules.
5. **Status legality** — MVP statuses only `waiting` / `slice NN` / `done`; no deleted `done` rows.

Report `PASS` or a numbered `VIOLATIONS:` list (offending line quoted short, which check, the
fix). Do not soften; a soft guard is no guard. Fix violations before finishing.

## Anti-patterns

- Do not promote because something is expected, polished, or competitive.
- Do not add scope without asking what comes off or moves below.
- Do not solve capacity problems by pretending the MVP can absorb more.
- Do not hide line changes outside Amendments.
- Do not build a roadmap here; prioritizing only draws the MVP line.
- If everything is MVP, nothing is MVP.
