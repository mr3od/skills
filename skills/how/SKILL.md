---
name: how
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use why for motivation."
disable-model-invocation: true
metadata:
  origin: pstack `how` (github.com/cursor/plugins, MIT); reference prompts verbatim; harness-specific mechanics (Cursor subagent config, model labels) replaced with harness-neutral wording on 2026-09-19
---

# How

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

## Step 1. Assess Complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. One explainer explores and explains in a single pass. Go to Step 2b.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): spawn parallel explorers first, then hand off to the explainer. Go to Step 2a.

When in doubt, take the simple path.

## Step 2a. Explore (complex questions only)

Decompose the question into 2 to 4 exploration angles, each a distinct slice of the subsystem. Spawn all explorers in a single message, using your harness's subagent facility:

- Type: a general-purpose agent, or the harness's read-only exploration agent if it has one.
- Model: your configured how-explorer model (the harness's default subagent model unless the user names one; a fast model suits this role).
- Mode: read-only. No edits, no commits.

Each explorer gets the prompt in `references/explorer-prompt.md` with its angle filled in. Then go to Step 3.

If your harness has no subagent facility, explore each angle yourself in turn and write the findings block for each before moving on; the explanation is only as good as what was actually read.

## Step 2b. Direct Explain (simple questions)

Spawn one subagent that explores and explains in one pass:

- Type: a general-purpose agent.
- Model: your configured how-explainer model (the harness's default subagent model unless the user names one; this is the role for a stronger reasoning model when one is offered).
- Mode: read-only.

Build its prompt from `references/explainer-prompt.md` without the explorer-findings section. Go to Step 4. Without a subagent facility, do this pass yourself.

## Step 3. Synthesize (complex questions only)

Once all explorers have returned, spawn one subagent to synthesize their findings into one explanation:

- Type: a general-purpose agent.
- Model: your configured how-explainer model.
- Mode: read-only.

Build its prompt from `references/explainer-prompt.md` with every explorer's findings filled in. Without a subagent facility, write the explanation yourself from the findings blocks.

## Step 4. Present

Present the explainer's output to the user. Light edits for clarity or context from the conversation are fine. Do not substantially rewrite it.

## Output Format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
