---
name: pr-explainer
description: Generate a single-file interactive HTML page that teaches what a PR, branch, or diff changes — layered concept → flows → detail, with architecture, ERD, state-machine, sequence, transaction-boundary, and recovery/failure diagrams plus an animated step-through storyboard. Use when the user asks to explain a PR or change-set visually, wants a teaching/walkthrough page for a diff, or asks "what does this PR actually do" as a visual learner.
---

# pr-explainer

Build a self-contained HTML **explainer** that teaches a change-set to a visual learner.
The reader should finish knowing what changed, why, how the new behavior flows, and what
deliberately did not change — without opening the diff themselves.

The explainer is a teaching artifact, not a review artifact: it tells the story of the
merged state, in present tense, through diagrams. Never render raw diffs or before/after
diff panels — a diff is the input you read, not the output you teach with. No
"previously/now" migration narrative outside an explicit before→after diagram pair.

## 1 — Gather the change-set

Resolve scope from the argument:

- PR number → `gh pr view <n> --json title,body,baseRefName,headRefName,files` and `gh pr diff <n>`.
- Branch or ref → diff against `merge-base` with the default branch.
- No argument → current branch vs `merge-base` with the default branch; if the tree is
  dirty, include uncommitted changes and say so in the page header.

Then gather the **why**, not just the diff: read the PR body, any linked issue or
`plans/*.md`, and the commit messages. For every load-bearing hunk, read enough
surrounding source to explain it in context — never narrate a hunk from the diff alone.

Done when: you hold the full changed-file list, the stated motivation, and the
base/head refs.

## 2 — Plan the story on a coverage ledger

Before writing any HTML, build a **coverage ledger**: every changed file mapped to the
section that will teach it. No file may be unaccounted for — pure noise (lockfiles,
generated snapshots) goes to a one-line "mechanical changes" row rather than being
dropped silently.

Then choose diagrams from the SWE-analysis menu. Each row states when it is
**required** — skipping a required diagram is a coverage failure:

| Diagram | Mermaid type | Required when the PR touches |
|---|---|---|
| Architecture | `flowchart` | always — the one overview of touched components |
| ERD | `erDiagram` | schema, migrations, or any data-model shape |
| State machine | `stateDiagram-v2` | any status/phase/lifecycle field or FSM transition |
| Sequence flow | `sequenceDiagram` | request, webhook, job, or cross-service interaction |
| Transaction boundary | `flowchart` with subgraphs marking each DB-transaction scope | transactional writes, locks, guarded updates |
| Recovery / failure view | `flowchart` or `sequenceDiagram` of the failure paths | retries, sweeps, timeouts, compensation, idempotency |

State machines must be real ones: every state a node, every transition a labeled edge
with its trigger/guard, new or changed transitions visually marked — not a flowchart
with status names in boxes.

Structure the page in three layers, in this order:

1. **Concept** — what the PR does and why, in one short paragraph, plus the
   architecture diagram. Color-code: green = added, amber = changed, red = removed;
   include a legend.
2. **Flows** — every other diagram the menu requires, plus the single most important
   scenario as an animated **storyboard**: a step-through with Prev/Next controls that
   highlights the active node/edge and shows a short narration line per step. One
   storyboard — more only if the PR genuinely has two independent core flows.
3. **Detail** — changes grouped by concern (mirror the commit grouping when it is
   clean). Each group: a few sentences of why, and a small annotated code snippet only
   when prose and diagrams genuinely cannot carry it. No diff panels.

Close with two short sections:

- **What did not change** — adjacent behavior a reader might assume moved but didn't,
  and explicit non-goals.
- **Check yourself** — 3–5 questions with click-to-reveal answers, each answerable from
  the page.

Done when: the ledger has a section for every changed file, every required diagram from
the menu is planned, and the storyboard scenario is chosen.

## 3 — Build the HTML

One self-contained `.html` file. Use well-known libraries from a CDN instead of
hand-rolling visuals — it reads better and costs fewer tokens:

- **Mermaid** (v11, ESM CDN) for all diagrams. Keep each diagram under ~25 nodes;
  quote any label containing punctuation; wrap rendering in a try/catch that falls back
  to showing the diagram source in a `<pre>` so one bad diagram never blanks the page.
- **highlight.js** for the rare annotated snippet.
- Storyboard animation: CSS transitions driven by a small vanilla JS stepper
  (Prev/Next + keyboard arrows) that toggles an `.active` class on SVG nodes and
  narration lines. Reach for anime.js only when motion beyond class toggles genuinely
  teaches something.

Layout — the page must breathe; crowding is a defect:

- **One diagram per section.** A section = heading, two-or-three-sentence lead-in, the
  diagram at full width, then its narration. Never two diagrams sharing a viewport.
- **Collapsible sidebar** table of contents (hamburger toggle, collapsed by default on
  narrow screens) listing the three layers and every diagram section; the main column
  takes the full remaining width.
- Generous whitespace: comfortable section padding, max one idea per screenful.
  Narration sits beside or directly under the visual it explains, never in a wall of
  text.

Style — clean developer-docs aesthetic:

- Font **Readex Pro** via the Google Fonts CDN (system-ui fallback); monospace stack
  for code.
- Primary accent `#4a5bc7`, clean docs-site aesthetic: white/near-black backgrounds,
  subtle borders, no gradients or decoration that doesn't teach.
- Respects `prefers-color-scheme`; readable in both modes.
- Header: PR/branch title, base→head refs, files/insertions/deletions stats, and a
  one-line reading guide ("skim layer 1, play the storyboard, expand details as needed").

## 4 — Verify and deliver

- Write to `.scratch/pr-explainer-<id>.html` in the repo (create `.scratch/` if needed
  and ensure it is ignored — add to `.git/info/exclude`, never to a tracked file).
  The explainer is never committed.
- Verify before handing over: load the file (browser tool if available, otherwise
  `open <file>` and check for rendering errors by re-reading the console/source). Fix
  until every Mermaid diagram renders with zero errors.
- Walk the coverage ledger once against the finished page: every row rendered, every
  required diagram present.

Done when: the file opens clean and the final reply states the path plus a one-line
coverage summary — "N changed files taught across M sections, diagrams: <list>,
storyboard: <scenario>".
