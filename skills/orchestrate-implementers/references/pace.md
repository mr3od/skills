# Pace

Measurements from three PRs on one project, 21 gate runs and a set of proof runs. Read them as the reason behind each rule and as a baseline to measure your own host against.

## Gate order

- Run the fast static check and the targeted tests on each commit, locally. Run the full gate once per round, on the final head. Done when the log shows one full gate per round. Why: 12 of 21 gate runs were avoidable. Static failures a local check would catch, runs superseded by a newer push, a flaky test, and re-gates after a proof fix accounted for most of them.
- Count a gate that died on the connection, a sleeping remote machine or a failed push as no result. Rerun it, and say so in the PR. Why: 4 of 21 gate runs died that way.
- Run proof before the final gate. Done when the proof pass precedes the last full gate in the log. Why: a proof fix after the gate forced a second full run.
- Batch runs that hold the whole machine into one timing run. Done when no more than one exclusive-use run happens per round. Why: 13 exclusive timing runs held every build slot while other work queued.

## Proof scope

- Re-prove only the clauses whose screens the fix touched. Give the contract a "touches" column per clause. Done when each re-proved clause names the screen the fix changed. Why: proof took 4 to 11 minutes, except one PR at 48 to 62 minutes with about 25 bespoke scripts.
- Give each proof script a timeout, for example 120 seconds, and wait for a selector instead of sleeping a fixed time. Done when every script has both. Why: one script hung for 19 minutes.

## Draft PR

The implementer opens a draft PR at the first push and reports `review-ready <pr> <sha>`. Reviewers start on that report, in parallel with the gate and the proof. The implementer marks the PR ready as its last step. Done when reviewer start precedes the gate result in the PR timeline. Why: parallel review saved 25 to 45 minutes per PR.

## Reviewer runs

- Run the reviewer read-only, in a detached worktree at the PR head.
- Pin the model and the effort from the picks.
- Set a timeout longer than the longest review you have measured. Reviews took 5 to 25 minutes.
- Judge success from the run's result record, since a shell exit code can read 0 on a failed run. Done when the record's status says completed. Why: one run stalled 13 minutes with no model calls, and a mistyped flag exited 0 behind a pipe.

## Host load

Cap concurrent agent runs and heavy processes in the rules file, and reap agent sessions idle for a day. Why: three processes were killed for memory after bursts of concurrent agents, browsers and test workers on a 4-core, 8 GB host.
