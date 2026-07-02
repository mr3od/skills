---
name: planning
description: "Phase 1 of the delivery pipeline. Use to start or resume product planning from defining docs, notes, rough ideas, brainstorms, or scope documents — create delivery/BACKLOG.md at Phase: planning, confirm the value hypothesis, and capture every capability before the MVP line is drawn. Also handles free capture with `add <idea>`"
argument-hint: "<paths to defining docs, notes, rough idea> | add <idea>"
---

# planning

Phase 1 of the **delivery** pipeline (planning → prioritizing → slicing), a method that
carries a product idea to a shipped MVP using nothing but Markdown in git. Planning creates
`delivery/BACKLOG.md`, frames the problem, confirms the value hypothesis, and captures every
capability before the MVP line is drawn.

`BACKLOG.md` is the single stateful file; it carries a `Phase:` marker so any later run
resumes where the project stands. `planning` never draws the MVP line — that is
`/delivery:prioritizing`.

## Usage

```
/delivery:planning docs/idea.md notes/*.md
/delivery:planning add "customer can repeat a previous order"
```

## Route

Read the `Phase:` marker in `delivery/BACKLOG.md`:

- No file → create it immediately with `Phase: planning`.
- `Phase: planning` → continue planning.
- `Phase: prioritizing` without `add` → point to `/delivery:prioritizing`.
- `Phase: slicing` / `mvp-satisfied` without `add` → point to `/delivery:slicing` for
  delivery, or `/delivery:prioritizing` for line changes.
- Any phase **with** `add` → free capture (see below).

## Steps

### 1. Frame

Read every input at `$ARGUMENTS`. Ask once whether a glossary/terminology doc exists; if yes,
record it in the header and honor its locked terms and usage rules.

Frame before collecting solutions: what are we planning? who has the problem? what are they
doing today? why now? what constraints matter? Where inputs conflict, list each conflict and
let the user resolve it — never silently pick. If an input is already a locked scope doc,
extract and pressure-test rather than invent.

### 2. Explore

Use exploratory thinking as needed, not as a checklist: distinguish symptoms from root
causes; name the assumptions the idea depends on; surface adjacent or opposite approaches
when the input is too solution-led; stop and name missing research when a question cannot be
answered by thinking.

### 3. Confirm the value hypothesis

Draft three lines, then get **explicit** confirmation:

- **Customer** — a role, not a demographic.
- **End-to-end value** — one sentence.
- **Core loop** — the smallest repeatable mechanic that creates value, e.g.
  `request → confirm → receive → record`.

If the user cannot confirm it, keep `Phase: planning`, record the draft and open questions,
and stop. Priority is undefined against a fuzzy hypothesis.

**Completion criterion:** the user has confirmed all three lines in words, not silence.

### 4. Capture

Story-map the core loop step by step. Under each step, list every capability the inputs name
or imply into Captured capabilities. Capabilities under no step still go in. Every item gets
one grounding line: a source citation or `raised by <who>`. Nothing is rejected during
planning.

**Completion criterion:** every capability named or implied by the sources is captured with a
grounding line — none left loose in prose.

### 5. Checkpoint

When the hypothesis is confirmed and capture is complete, set `Phase: prioritizing` and end
with: run `/delivery:prioritizing` to draw the MVP line.

## Add mode

Capture any new idea without gatekeeping. Before prioritizing, add it to Captured
capabilities. After prioritizing, add it below the line with a why-below and source. If the
user wants it above the line, route to `/delivery:prioritizing promote <item>`.

## Output — `delivery/BACKLOG.md`

Create or update this exact shape. Do not invent sections. Later phases fill the empty tables.

```markdown
# <product> — Backlog
Phase: planning
Sources: <input docs> | Glossary: <path or "none"> | Generated: <date>
For scope, this file wins; for vocabulary, the glossary wins.
The single stateful file — slice files under delivery/slices/ hold no state.

## Value hypothesis
Customer: <role, or "unconfirmed">
End-to-end value: <one sentence, or "unconfirmed">
Core loop: <smallest repeatable mechanic>

## Captured capabilities
Everything named or implied by the sources. No MVP line yet.

| Capability | Core-loop step | Grounding |
|---|---|---|

## MVP — above the line
Not drawn yet. Run /delivery:prioritizing after planning is confirmed.

| # | Capability | Core-loop step | Value fails without it because (source) | Status | Size |
|---|---|---|---|---|---|

## Later — below the line
Not drawn yet. Run /delivery:prioritizing after planning is confirmed.

| Capability | Why below (later / manual for now / adjacent / unknown) | Source |
|---|---|---|

## Open questions
Unknowns to observe or decide later — not features.

## Amendments
| Date | Change | What building taught us |
|---|---|---|
```

## Verify before finishing

The reviewer must not be the context that wrote the file. If your host can spawn a
fresh-context subagent (Claude Code: the `Task`/`Agent` tool, granted only `Read, Grep,
Glob`), spawn one to run the checks below; otherwise re-read `BACKLOG.md` from disk, state *"I
did not write this,"* and run them inline. In planning only these apply:

1. **No duplication** — flag passages that restate a source doc instead of citing it. Short
   paraphrase next to a citation is fine; a copied rule is not.
2. **Locked vocabulary** (only if a glossary is declared) — product concepts use the
   glossary's locked terms and usage rules, as written.

Fix violations before finishing. (Line, slice, and status checks belong to later phases.)

## Anti-patterns

- Do not write a spec before the value hypothesis is confirmed.
- Do not reject ideas during planning. Capture first; prioritize later.
- Do not turn a solution request into scope without naming the user problem.
- Do not duplicate source docs — cite and summarize only what the workflow needs.
- Do not advance to prioritizing with unresolved conflicts hidden in the prose.
