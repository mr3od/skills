---
name: orchestrate-implementers
description: "Use when you hand a ticket to a child agent, send a review or fix round to a thread, choose implementer and reviewer models for a session, tell the owner why work waits or runs slow, or ask the owner to decide. Coordinates implementer and reviewer agents from ticket to merge."
license: MIT
metadata:
  version: "1.0.0"
  origin: generalised from a coordinator skill with real runs behind it, 2026-10
---

# Orchestrate implementers

You coordinate. Child agent threads build and review. You brief, gate and merge, and you keep every pull request that can move moving.

Map each mechanism below to your harness: a child thread, a queued message, a task record, a prompt-cache lifetime. Where the harness has a named tool, use it. One example from a harness that has them: `delegate_task` starts a child, `t3_thread_send` messages one, `t3_queue_edit` edits a queued message.

Each rule ends on a check you can run, and its reason is an incident that happened.

## Project rules file

The host and project rules live in the reader's own rules file, the one their agent docs name (for example `AGENTS.md`). It holds the gate command, the test runner, the proof step, the host memory budget, the cap on concurrent agent runs, and the location of the picks file. Read it before the first brief.

Without one, ask the owner for those items once and write them there. Done when the file names each of them.

## Model picks

At the start of a session, get the implementer and reviewer models and efforts from the owner. `references/model-picks.md` has the file format and the suggested pairing.

1. Read the picks file if one exists. Otherwise ask once.
2. Offer only models that are available and within quota right now. Done when each offered model answered a live availability check this session.
3. Record the picks in your coordination notes. Done when a fresh handoff brief can state every pick without asking you.
4. Take a per-session or per-ticket override from the owner as given. Record it on the ticket's row.

Why: a pick that was out of quota stalled a ticket until someone chose a substitute. A review run with no pinned model recorded "model: none" and could not be attributed.

## Brief every child

Write each brief per the `writing-for-agents` skill: positive targets, one checkable completion criterion per step, and pointers to files instead of restated rules.

A brief names the ticket, PR, branch, worktree, head SHA, the picks, the owner's decisions so far, and the files that hold the standing rules. Done when a reader with no other context could start work from it.

- Ask for a draft PR at the first push, with the closing keyword for the ticket. A child often cannot message you mid-run, so the draft PR is the signal. Done when the brief says so. Why: reviewers that run in parallel with the gate and proof take review time off the critical path.
- Ask each fix round for targeted tests on each fix and one full gate on the round's final head. Done when the gate log shows one full run at that head. Why: a full gate after every fix multiplies runner time, and most of those runs are superseded by the next push.
- Ask that each new test fails with the guarded behavior reverted. Done when the implementer names the revert it tried. Why: a modal test passed with its guard removed.

## Send to a thread

1. Read when the thread's last turn ended. Done when you have the time.
2. If it ended within your harness's prompt-cache lifetime, less a safety margin, send in the thread. Otherwise start a fresh child with the same model and effort and a self-contained handoff brief. Done when the message reaches a warm thread or a new child. Why: a late resume re-reads the whole thread uncached.
3. Hold one queued message per child. To add to it, edit it. Done when the child's queue length is one. Why: each extra queued message makes its own task card, so two agents showed a card each per message.

## Before a heavy start

Compare free memory and the running gates, proofs and agents against the budget in the rules file. Done when the start fits, or it waits and your notes say why. Why: three processes were killed for memory after bursts of concurrent agents on a small host.

## Review rounds

- While an implementer runs, check its branch for a draft PR on each wait (`gh pr list --head <branch> --json number,isDraft,headRefOid`). When one appears, start both reviewers on that head. An explicit message from the child is an optional extra where the harness supports it. Done when the check ran on every wait and reviewers started on the first draft head.
- Start every reviewer for the round in the turn the PR URL appears. Done when all starts share one turn. Why: reviewers return on their own schedules, so starting them one by one adds the waits together.
- End each turn on a PR in review or fix with a wait on its implementer. Done when no PR in flight lacks a pending wait. Why: coordinator idle time was the largest share of PR-to-merge time in one measured project, including a PR that sat green and unmerged.
- Merge in the turn the last gate is green at the head and the ledger has no open row. `references/ledger.md` defines the tags, rows, statuses, signature and closing attribution line.
- Run a second review round at the fix head. Done when every reviewer has posted at that SHA. Why: a second round at the fix head catches defects that round one missed or the fixes introduced.
- Reproduce a pushback before you accept it. Done when you ran the test at the boundary the finding names, or read the code path. Why: a boundary test passed only at the hour it ran, and the coordinator accepted the pushback.
- Treat a check nobody could run as `unverified`, which counts as open. Done when merge waits for the owner's written grant. Why: a PR merged with a native drag unchecked, and the owner's first use found the bug.
- Run reviewers read-only, with pinned model and effort, and judge success from the run's result record. `references/pace.md` has the rest.

## Numbers and causes you give the owner

- A numeric threshold that gates merge cites the owner's words or a measured baseline. Any other number is marked advisory in the brief. Done when each gating number has its citation. Why: a latency target the coordinator chose cost review rounds and was waived.
- Before you say why work waits or runs slow, read the code that decides it and quote the line. Done when the quote is in your message. Why: "one build slot" was wrong, the host had three, and timing runs held all of them.

## Questions to the owner

- Give each option its measured cost: time, review rounds, speed at the ticket's scale, or lines of code. Done when no option lacks one. Why: answers came back as "I do not know the cost".
- Run any prototype, chart or page you show the owner, and click each control, before you publish it. When the preferred preview fails, drive the file in a headless browser. Done when each control has been clicked once. Why: a variable named `open` broke every click, and the owner found it.

## Pace

`references/pace.md` covers gate order, proof scope and reviewer-run mechanics, each with the measurement behind it.
