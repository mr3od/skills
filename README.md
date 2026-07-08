# mr3od/skills

Public skills by **mr3od**. Portable by design: each skill is a **self-contained** set of
instructions with no cross-file dependencies, so a single `SKILL.md` runs on **Claude Code**
(as a plugin) and on **Codex** (or any agent) once dropped into its prompts. Where a skill
benefits from an independent reviewer, it spawns a fresh-context subagent when the host
supports one and does the same review inline when it doesn't — same checklist either way.

## Plugins

### `delivery` — planning → prioritizing → slicing

One pipeline that carries a product idea to a shipped MVP, using nothing but Markdown in git.
Skills live under [`skills/in-progress/`](skills/in-progress/) (v0.1 — still stabilizing).

| Phase | Command | Does |
|---|---|---|
| Planning | `/delivery:planning <docs…>` | Captures everything, pins the value hypothesis |
| | `/delivery:planning add <idea>` | Free capture, any time |
| Prioritizing | `/delivery:prioritizing` | Draws and approves the MVP line, adversarially minimized |
| | `/delivery:prioritizing promote <item>` | Crossing the line — the gate runs |
| | `/delivery:prioritizing amend` | Building proved the line wrong |
| Slicing | `/delivery:slicing plan` | Slice plan to MVP — or cut one at a time |
| | `/delivery:slicing done <#>` | Slice demoed → items done, coverage report |

**Output:** `delivery/BACKLOG.md` is the one stateful file — it carries the `Phase:` marker so
any later run resumes where the project stands. `delivery/slices/NN-*.md` are stateless slice
contracts, cheap to re-cut.

**How it works:** capture is free and everything lands in `BACKLOG.md`; the MVP line is
guarded and each item above it is attacked (below / manual / hardcode / merge) until only what
value-creation fails without survives; then vertical slices — walking skeleton first — are cut
and demoed until every above-the-line item is `done`. Each skill carries its own schema and
review checklist, so nothing depends on a shared file.

## Skills

### `pr-explainer` — visual teaching page for any change-set

Generates a single self-contained HTML page that teaches what a PR, branch, or diff does —
layered concept → flows → detail, with Mermaid architecture/state/sequence diagrams, an
animated step-through storyboard of the key scenario, and diff2html before/after panels.
Built for visual learners; a coverage ledger guarantees every changed file is taught.
Lives at [`skills/pr-explainer/`](skills/pr-explainer/).

```
npx skills add mr3od/skills
```

The [skills CLI](https://skills.sh) installs it for Claude Code, Codex, and 70+ other agents.
Then ask: *"explain PR 42 visually"* or *"build a pr-explainer for this branch"*.

## Install

### Claude Code

```
/plugin marketplace add mr3od/skills
/plugin install delivery
```

### Codex (and other agents)

Each skill is self-contained, so copy the phase files into your Codex prompts directory and
invoke them as slash prompts:

```
cp skills/in-progress/planning/SKILL.md      ~/.codex/prompts/delivery-planning.md
cp skills/in-progress/prioritizing/SKILL.md  ~/.codex/prompts/delivery-prioritizing.md
cp skills/in-progress/slicing/SKILL.md       ~/.codex/prompts/delivery-slicing.md
```

Then invoke `/delivery-planning`, etc. Nothing else needs to travel with the file.

## License

MIT © mr3od
