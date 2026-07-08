---
name: pr-explainer
description: Generate a single-file interactive HTML page that teaches what a PR, branch, or diff changes — layered concept → flows → detail, with architecture diagrams, state/sequence flows, an animated step-through storyboard, and before/after diffs. Use when the user asks to explain a PR or change-set visually, wants a teaching/walkthrough page for a diff, or asks "what does this PR actually do" as a visual learner.
---

# pr-explainer

Build a self-contained HTML **explainer** that teaches a change-set to a visual learner.
The reader should finish knowing what changed, why, how the new behavior flows, and what
deliberately did not change — without opening the diff themselves.

The explainer is a teaching artifact, not a review artifact: it tells the story of the
merged state, in present tense. No "previously/now" migration narrative outside the
explicit before/after panels.

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

Structure the page in three layers, in this order:

1. **Concept** — what the PR does and why, in one short paragraph, plus one architecture
   diagram of the touched components. Color-code: green = added, amber = changed,
   red = removed; include a legend.
2. **Flows** — one diagram per behavior the PR changes:
   - state machines → Mermaid `stateDiagram-v2` (mark new/changed transitions),
   - request/webhook/job interactions → Mermaid `sequenceDiagram`,
   - the single most important scenario → an animated **storyboard**: a step-through
     with Prev/Next controls that highlights the active node/edge and shows a short
     narration line per step. One storyboard, for the scenario that best teaches the PR
     — more only if the PR genuinely has two independent core flows.
3. **Detail** — changes grouped by concern (mirror the commit grouping when it is
   clean). Each group: a two-or-three-sentence why, a mini-diagram only when it earns
   its place, and a before/after diff panel (collapsed by default) for the key hunks.

Close with two short sections:

- **What did not change** — adjacent behavior a reader might assume moved but didn't,
  and explicit non-goals.
- **Check yourself** — 3–5 questions with click-to-reveal answers, each answerable from
  the page.

Done when: the ledger has a section for every changed file and the storyboard scenario
is chosen.

## 3 — Build the HTML

One self-contained `.html` file. Use well-known libraries from a CDN instead of
hand-rolling visuals — it reads better and costs fewer tokens:

- **Mermaid** (v11, ESM CDN) for all diagrams. Keep each diagram under ~25 nodes;
  quote any label containing punctuation; wrap rendering in a try/catch that falls back
  to showing the diagram source in a `<pre>` so one bad diagram never blanks the page.
- **diff2html** (CSS + JS CDN) for before/after panels. Embed the raw unified-diff hunks
  in `<script type="text/plain">` blocks and render them — do not hand-format diffs.
- **highlight.js** for standalone code snippets.
- Storyboard animation: CSS transitions driven by a small vanilla JS stepper
  (Prev/Next + keyboard arrows) that toggles an `.active` class on SVG nodes and
  narration lines. Reach for anime.js only when motion beyond class toggles genuinely
  teaches something.

Page requirements:

- Sticky table of contents matching the three layers; sections land in ledger order.
- Header: PR/branch title, base→head refs, files/insertions/deletions stats, and a
  one-line reading guide ("skim layer 1, play the storyboard, expand details as needed").
- Respects `prefers-color-scheme`; readable in both modes.
- Narration prose is short and sits beside the visual it explains, never in a wall of
  text below it.

## 4 — Verify and deliver

- Write to `.scratch/pr-explainer-<id>.html` in the repo (create `.scratch/` if needed
  and ensure it is ignored — add to `.git/info/exclude`, never to a tracked file).
  The explainer is never committed.
- Verify before handing over: load the file (browser tool if available, otherwise
  `open <file>` and check for rendering errors by re-reading the console/source). Fix
  until Mermaid and diff2html render with zero errors.
- Walk the coverage ledger once against the finished page: every row rendered.

Done when: the file opens clean and the final reply states the path plus a one-line
coverage summary — "N changed files taught across M sections, storyboard: <scenario>".
