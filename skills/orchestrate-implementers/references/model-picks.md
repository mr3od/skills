# Model picks

The owner decides which model plays which role. You collect the decision once per session and carry it into every brief.

## Picks file

The owner keeps a short file, named in the project rules file. Any format works if each role has a model, the harness that runs it, and an effort:

```text
implementer: <model and version> · <harness> · effort <level>
reviewer: <model and version> · <harness> · effort <level>
second reviewer: <model and version> · <harness> · effort <level>
```

A ticket override is one more line: `ticket <id> implementer: <model> · <harness> · effort <level>`. It applies to that ticket only.

Without a file, ask once, in one message, for all three roles. Offer the suggestion below as a default the owner can accept with one word.

## Spawn with the picks

A pick is a spawn parameter, not a sentence in the brief.

1. Read the harness's live capability list: its models, their efforts and their quota or rate-limit state. Offer a model only when it can run now.
2. Pass the model, the harness and the effort as the harness's model options at spawn.
3. Check the spawn result against the pick: the harness, the model and the options it echoes. Done when all three match, or the difference is recorded.
4. If the harness rejects an effort, use the role's default effort and say so to the owner. The ledger records what actually ran, not what you asked for. Why: a pick that is rejected or ignored without notice leaves a ledger naming a run that never happened.

When a pick hits a rate limit mid-session, tell the owner the time to reset and offer the next available pick. Record the change in your notes. Done when the owner's answer is recorded before the next brief goes out. Why: a rate-limit stall held a ticket until someone chose a substitute.

## Suggested pairing

Offer this as a suggestion. The owner's picks win.

- Implementer: the owner's strongest available model at high effort.
- Reviewer: a model from a different family than the implementer, so the review does not share the implementer's blind spots.
- Second reviewer: one more independent model that has not seen the first reviewer's findings.

## Record

Keep a "Picks" block in your coordination notes: the three roles, the harness and effort for each, the date, and any ticket overrides. Copy it into every brief and handoff. Done when the block in a handoff matches the notes.

Write the model with its version, the harness and the effort in the ledger's columns, in each post signature and in the PR's closing attribution line, so a finding traces to the run that made it.
