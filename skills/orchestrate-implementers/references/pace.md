# Rounds and failures

## Start reviewers early

Reviewers can start as soon as there is a reviewable head, which is a pushed branch or a PR, draft or not, as the project defines it. The coordinator finds that head by checking the branch, since a child often cannot message mid-run. Done when reviewers start on the first reviewable head, without waiting for the child's final report. Why: review time then overlaps the child's remaining work instead of following it.

## Reviewer runs

Run the reviewer read-only, in a detached worktree at the head under review. Pin the model and the effort from the picks. Set a timeout from your rules file. Judge success from the run's result record, since a shell exit code can read 0 on a failed run. Done when the record's status says completed. Why: one run stalled with no model calls until it timed out, and a mistyped flag exited 0 behind a pipe.

## Failure handling

- **A child drops out.** Stop it, confirm it stopped, and retry once with the same brief. A second miss is recorded as a gap, in your notes and in a PR comment, and the work carries on without that child. Done when the notes name the child, the retry and the outcome. Why: a dead child that no one stopped keeps its place and its queue, and a wait on it never ends.
- **A child asks a blocking question.** Answer from the brief and the standing rules if they cover it. Otherwise put the question to the owner with a default and the cost of each option, and tell the child you are waiting. Done when the child has an answer or a stated wait. Why: a child left with an open question guesses.
- **A review cannot close.** Post a review comment that starts `BLOCKED: independent review` and gives the reason, for example no reviewer was available or both failed twice. The PR does not merge on a self-review. Done when the comment exists and names its reason. Why: a review quietly dropped looks the same as a review passed.
