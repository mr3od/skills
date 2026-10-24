# Pace

Each section states the general lesson first, then one project's measured case as an example. The figures come from three PRs on one project. Read them as the reason behind each rule and as a baseline to measure your own host against.

## Gate order

Run the fast static check and the targeted tests on each commit, locally. Run the full gate once per round, on the final head. A gate that dies on infrastructure is no result. Run proof before the final gate. Batch runs that hold the whole machine into one timing run per round.

Done when the log shows one full gate per round, the proof pass precedes the last full gate, and no gate result comes from a dropped connection.

Example, in one project: 21 gate runs over three PRs, 12 of them avoidable. Static failures a local check would catch, runs superseded by a newer push, a flaky test, and re-gates after a proof fix made up most of them. 4 died on a sleeping remote machine or a failed push. 13 exclusive timing runs held every build slot while other work queued.

## Proof scope

Re-prove only the clauses whose screens the fix touched. Give the contract a "touches" column per clause. Give each proof script a timeout and wait for a selector instead of sleeping a fixed time.

Done when each re-proved clause names the screen the fix changed, and every script has a timeout and a selector wait.

Example, in one project: proof took 4 to 11 minutes, except one PR at 48 to 62 minutes with about 25 bespoke scripts. One script hung for 19 minutes. A timeout of 120 seconds would have ended it in 2.

## Draft PR

The implementer opens a draft PR at the first push and marks it ready as its last step. The coordinator finds the draft by checking the branch, and starts reviewers on that head in parallel with the gate and the proof.

Done when reviewer start precedes the gate result in the PR timeline.

Example, in one project: parallel review saved 25 to 45 minutes per PR.

## Reviewer runs

Run the reviewer read-only, in a detached worktree at the PR head. Pin the model and the effort from the picks. Set a timeout longer than the longest review you have measured. Judge success from the run's result record, since a shell exit code can read 0 on a failed run.

Done when the record's status says completed.

Example, in one project: reviews took 5 to 25 minutes. One run stalled 13 minutes with no model calls, and a mistyped flag exited 0 behind a pipe.

## Host load

Cap concurrent agent runs and heavy processes in the rules file, and reap agent sessions idle for a day.

Done when the rules file states the cap and the idle limit.

Example, in one project: three processes were killed for memory after bursts of concurrent agents, browsers and test workers on a 4-core, 8 GB host.
