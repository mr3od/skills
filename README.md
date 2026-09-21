# skills

Each skill is one folder with a `SKILL.md`, installed with the [skills CLI](https://skills.sh) into Claude Code or any agent that reads skills from disk:

```bash
npx skills add mr3od/skills -s <name> -a claude-code -y
```

Layout follows mattpocock/skills and amelnagdy/delegate-skills: `skills/<name>/SKILL.md` with `references/`, `scripts/`, `assets/`, `agents/` and `evals/` beside it as needed; `skills/in-progress/` holds what has not run in a second repo yet.

## `grill-with-counterpart` (v0, in progress)

One added step inside a [`grill-with-docs`](https://aihero.dev/skills-grill-with-docs) session:
each frontier round is also answered blind by a second agent. The owner then sees every
disagreement with both answers verbatim, and every agreement marked as two samples, unverified.
Everything else is grilling as it already works.

Why this shape: on a settled spec, two blind agents answering the round reached 10 of 16
owner decisions between them; every disagreement held the right answer; half their agreements
were wrong on facts only the owner had. Drafting the spec blind instead followed the loudest
document and contradicted a quarter of the decisions. Those numbers came from two symmetric
blind readers; the skill runs one counterpart against an orchestrator who writes its own answers
down first. Whether that holds is what the per-run note measures. Write-ups in the author's notes.

Install:

```bash
npx skills add mr3od/skills -g -s grill-with-counterpart -a claude-code -y
npx skills add mattpocock/skills -s grill-with-docs grilling domain-modeling research -a claude-code -y
npx skills add amelnagdy/delegate-skills -s agy-delegate claude-delegate -a claude-code -y
```

Invoke inside a grilling session: `/grill-with-counterpart claude-delegate`.

Layout: `SKILL.md` is the six-step round; `assets/round-brief.md` is the brief the counterpart
gets; `scripts/diff-round.py` pairs the two answer files by question and
`scripts/cite-check.sh` says which cited `path:line`s exist at the pinned commit;
`evals/evals.json` is the benchmark, built from the frontier evaluation, to rerun after every edit.

It is versioned by use: after each run, one comment on the issue records deltas, agreements,
struck citations and later-reversed decisions, and the skill is edited from that.

## `behavior-proof` (v1)

Source-blind proof that a screen change works for a user: a contract written before the run, the
running app driven in a browser the way a user would, anti-cheat probes, evidence captured, and one of five outcomes
per clause (pass, fail, blocked with a reason, out of scope, inconclusive). The black-box half of a
pair with `code-review`. Generalised from a project skill with real runs behind it; the repo-specific setup stays in each
repo behind a pointer in its agent docs.

Install: `npx skills add mr3od/skills -g -s behavior-proof -a claude-code -y`, then run it as a fresh
agent given only the contract and an address, never the agent that wrote the change.

## License

MIT
