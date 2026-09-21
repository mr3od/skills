This is {orchestrator}, grilling round {N} for {issue or topic}. Owner: {handle}. You answer independently; the orchestrator diffs your answers against its own and takes the deltas to the owner. Read-only turn at commit {commit}: inspect, do not edit.

<context>
Records to read first: {issue link}, CONTEXT.md, docs/adr/*, {code paths in play}. The records settle what they settle; where they are silent, say so.
</context>

<questions>
{numbered questions, exactly as the frontier states them, with no recommendations}
</questions>

<report>
Per question, in order:
### Q{n}
Recommendation: one definite answer.
Reason: why, in the repo's vocabulary.
Citation: `path:line` at commit {commit}, an ADR number, or a comment URL. Cite only what you opened this turn. If nothing supports it, write "no record; judgment".
Then: "Deviations or decisions needed: <list or none>".
Reply in the message only.
</report>

<turn>
Foreground only. If you must stop early, end with "EARLY-STOP: <reason>" as the last line.
</turn>
