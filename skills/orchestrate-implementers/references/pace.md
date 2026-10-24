# Pace

Each section states a general rule and its reason. Set every limit, timeout and capacity figure in your own environment rules file, since they depend on your host.

## Gate order

Run the fast static check and the targeted tests on each commit, locally. Run the full gate once per round, on the final head. A gate that dies on infrastructure (a dropped connection, a sleeping remote machine, a failed push) is no result, so rerun it and say so in the PR. Run proof before the final gate. Batch runs that hold the whole machine into one timing run per round.

Done when the log shows one full gate per round, the proof pass precedes the last full gate, and no gate result comes from a dropped connection.

Why: a full gate after every fix multiplies runner time. Static failures a local check catches, runs superseded by a newer push, a flaky test, and re-gates after a proof fix were most of the avoidable runs in the project this was drawn from. Exclusive-use runs held every build slot while other work queued.

## Proof scope

Re-prove only the clauses whose screens the fix touched. Give the contract a "touches" column per clause. Give each proof script a timeout from your rules file, and wait for a selector instead of sleeping a fixed time.

Done when each re-proved clause names the screen the fix changed, and every script has a timeout and a selector wait.

Why: re-proving every clause after each fix, with many hand-written scripts, made proof the slowest step of a round. One script with no timeout hung until someone noticed.

## Draft PR

The implementer opens a draft PR at the first push and marks it ready as its last step. The coordinator finds the draft by checking the branch, and starts reviewers on that head in parallel with the gate and the proof.

Done when reviewer start precedes the gate result in the PR timeline.

Why: review time then overlaps gate and proof time instead of following it.

## Reviewer runs

Run the reviewer read-only, in a detached worktree at the PR head. Pin the model and the effort from the picks. Set a timeout from your rules file, longer than the longest review you have seen. Judge success from the run's result record, since a shell exit code can read 0 on a failed run.

Done when the record's status says completed.

Why: one run stalled with no model calls until it timed out, and a mistyped flag exited 0 behind a pipe.

## Host load

Cap concurrent agent runs and heavy processes in the rules file, and reap idle agent sessions on the schedule it sets.

Done when the rules file states the cap and the idle limit.

Why: bursts of concurrent agents, browsers and test workers got processes killed for memory on a small host.

## Failure handling

- **A child drops out.** Stop it, confirm it stopped, and retry once with the same brief. A second miss is recorded as a gap in your notes and the PR, and the work carries on without that child. Done when the notes name the child, the retry and the outcome. Why: a dead child that no one stopped keeps its slot and its queue, and a wait on it never ends.
- **A child asks a blocking question.** Answer from the brief and the standing rules if they cover it. Otherwise put the question to the owner with the cost of each option, and tell the child you are waiting. Done when the child has an answer or a stated wait. Why: a child left with an open question guesses.
- **A review gate cannot close.** Mark it `BLOCKED: independent review` with the reason, for example no reviewer was available or both failed twice. The PR does not merge on a self-review. Done when the PR body names the blocked gate and its reason. Why: a gate quietly dropped looks the same as a gate passed.
