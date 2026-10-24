# Model picks

The owner decides which model plays which role. You collect the decision once per session and carry it into every brief.

## Picks file

The owner keeps a short file, named in the project rules file. Any format works if each role has a model and an effort:

```text
implementer: <model and version> · effort <level>
reviewer: <model and version> · effort <level>
second reviewer: <model and version> · effort <level>
```

A ticket override is one more line: `ticket <id> implementer: <model> · effort <level>`. It applies to that ticket only.

Without a file, ask once, in one message, for all three roles. Offer the suggestion below as a default the owner can accept with one word.

## Check availability

List the models your harness reports as available and read the quota or rate-limit state for each. Offer a model only when both say it can run now. Done when each offered model has an availability answer from this session.

When a pick hits a rate limit mid-session, tell the owner the time to reset and offer the next available pick. Record the change in your notes. Done when the owner's answer is recorded before the next brief goes out. Why: a rate-limit stall held a ticket until someone chose a substitute.

## Suggested pairing

Offer this as a suggestion. The owner's picks win.

- Implementer: the owner's strongest available model at high effort.
- Reviewer: a model from a different family than the implementer, so the review does not share the implementer's blind spots.
- Second reviewer: one more independent model that has not seen the first reviewer's findings.

## Record

Keep a "Picks" block in your coordination notes: the three roles, the effort for each, the date, and any ticket overrides. Copy it into every brief and handoff. Done when the block in a handoff matches the notes.

Write the model with its version and the effort in the ledger's "Found by" column and in each post signature, so a finding traces to the run that made it.
