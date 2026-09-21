# Report Schema

Use this shape when another agent reads the report. Prose is fine for a person.

`SKILL.md` owns what the outcomes mean. This file owns how they are written down.

```json
{
  "overall_behavior": "satisfies_contract",
  "head_sha": "0041382b",
  "target": {
        "access": "http://127.0.0.1:8080/app/records/<id>",
    "account": "seeded-manager"
  },
  "checks": [
    {
      "contract_clause": "User task 1",
      "status": "pass",
      "severity": null,
      "blocked_reason": null,
      "evidence": ".proof/<run>/03-focus.png",
      "observed": "Pressed تركيز البيانات. The Arabic column filled the viewer at 2.56x.",
      "reproduction_steps": [
        "Open a document with extracted data",
        "Press تركيز البيانات",
        "Read the printed zoom ratio"
      ],
      "confidence": 0.9
    }
  ],
  "anti_cheat_probes": [
    {
      "probe": "Compared the viewer image before and after the press",
      "result": "Image changed; zoom ratio went 1.00 to 2.56"
    }
  ]
}
```

`overall_behavior`: `satisfies_contract`, `violates_contract`, `blocked`, `inconclusive`.

`status`: the five outcomes in `SKILL.md`, as `pass`, `fail`, `blocked`, `out_of_scope`,
`inconclusive`.

## Three rules a reader can check

Nothing validates this file. These are the rules a reader applies by hand, so keep them checkable.

1. **A `blocked` or `inconclusive` check forbids `satisfies_contract`.** An unobserved clause is not a
   pass for the run that contains it.
2. **`evidence` names a path that exists.** A claim with no artifact behind it is `inconclusive`, not
   a pass. Put the description in `observed`.
3. **`head_sha` is the commit the run drove.** It is self-reported. The proof is stale once the head
   moves, and a reader compares it against the branch.

## Fields

`blocked_reason` is `human`, `tooling`, or `source`, and `null` unless the status is `blocked`. It
belongs on the check and not on the run, because two clauses can block for different reasons in one
run. A run that never started has no separate field: every clause it could not judge is `blocked`.

`severity` only on a `fail`, `null` otherwise.

`confidence` is a real number from 0 to 1, per check. The run has no combined score; `inconclusive`
already says nothing was established.

Redact credentials, tokens, cookies and personal data from every field.

`inconclusive` is ours. The source this schema follows has four statuses and no word for a run that
timed out: not `blocked`, because access was fine, and not `fail`, because nothing was observed.
