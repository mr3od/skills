# skills

[![skills.sh](https://www.skills.sh/b/mr3od/skills)](https://www.skills.sh/mr3od/skills)
[![License](https://img.shields.io/github/license/mr3od/skills)](LICENSE)

**A second pair of eyes for your coding agent.** A skill for getting a blind second opinion while you design, one for proving a screen actually works before you call it done, and a small crew for the review that comes after.

```bash
npx skills add mr3od/skills
```

Pick the skills you want and the agents to install them on: Codex, Claude Code, Cursor, or any agent that reads skills from disk.

## What's here

| Skill | What it does |
| --- | --- |
| [`behavior-proof`](skills/behavior-proof/SKILL.md) | Drives the running app in a browser against a contract you write first, and tells you pass, fail, blocked, out of scope or inconclusive, clause by clause. Source-blind: the agent that wrote the change never runs it. |
| [`how`](skills/how/SKILL.md) | "How does X work?" A walkthrough of a subsystem at the level of a senior engineer onboarding onto it. |
| [`why`](skills/why/SKILL.md) | "Why is it like this?" The rationale behind a decision, pulled from source control, the tracker, docs and chat, with citations. |
| [`comment-sicko`](skills/comment-sicko/SKILL.md) | A comment-hating subagent. Feed it a diff and it deletes narration, banners and alibi comments, and flags the code that needed the prose in the first place. It never touches the code itself. |
| [`grill-with-counterpart`](skills/in-progress/grill-with-counterpart/SKILL.md) | Inside a `grill-with-docs` session, a second agent answers each round of questions without seeing yours. You see where they disagree, in their own words, and where they agree, marked as unverified. In progress. |

## How I use them

**Before I build.** I grill the design with [mattpocock's `grill-with-docs`](https://github.com/mattpocock/skills). With `grill-with-counterpart` on, every round also goes to a second agent that has not seen my answers. Where the two disagree, one of them is usually right and I get to pick with both arguments in front of me. Where they agree, I have learned not to trust it: two agents agreeing on something only I know is still wrong.

```text
Use grill-with-counterpart for this grilling; the second agent runs through codex-delegate.
```

**Before I say a screen is done.** Tests pass and the button does nothing; it has happened to me. `behavior-proof` makes a fresh agent write down what "working" means first, then drive the app and prove it, with screenshots and the numbers printed off the page.

```text
Run behavior-proof on the upload screen. Contract first, then prove it.
```

**When I read a diff.** `comment-sicko` strips the comments that explain what the code should have said itself and points at the symbol to fix. `how` and `why` are what it reaches for when a comment claims something it cannot see; they are just as useful on their own.

```text
Use comment-sicko on the diff against main.
Use how on the enrollment pipeline before I touch it.
Use why on the retry limit in the batch runner.
```

## Where they come from

`how`, `why` and `comment-sicko` are ports of skills from [pstack](https://github.com/cursor/plugins/tree/main/pstack) by Lauren Tan (MIT), rewritten to run in any harness rather than Cursor only. The reference prompts are hers, verbatim; the licence text ships inside each skill. `behavior-proof` is a skill I have used to gate real pull requests, with the project-specific setup taken out. `grill-with-counterpart` came out of measuring what a second agent actually adds to a design conversation; it is in `in-progress` until it has run in a second project.

## Layout

```text
skills/
├── <name>/SKILL.md          # the skill
│   ├── references/          # loaded on demand
│   ├── scripts/             # deterministic helpers
│   ├── assets/              # templates
│   └── agents/              # harness metadata, and a subagent when the skill spawns one
└── in-progress/             # not yet run in a second project
```

Same shape as [mattpocock/skills](https://github.com/mattpocock/skills) and [delegate-skills](https://github.com/amElnagdy/delegate-skills).

## License

MIT. Ported skills carry their own notice inside.
