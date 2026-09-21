#!/usr/bin/env python3
"""Split two answer files into deltas and agreements by question number.

Usage: diff-round.py orchestrator.md counterpart.md

Each file holds sections headed "### Q<n>" with a "Recommendation:" line, the
shape assets/round-brief.md asks for. Output is a side-by-side Markdown table,
one row per question, with a column saying whether the two recommendations are
the same text. Free text rarely is, so the delta or agreement call on each row
is the orchestrator's, made from the table; the script never hides a
disagreement behind a match.
"""
import re
import sys


def sections(path):
    text = open(path, encoding="utf-8").read()
    out = {}
    for m in re.finditer(r"^###\s*Q(\d+)\b(.*?)(?=^###\s*Q\d+\b|\Z)", text, re.S | re.M):
        body = m.group(2)
        rec = re.search(r"Recommendation:\**\s*(.+)", body)
        out[int(m.group(1))] = (rec.group(1).strip() if rec else "").rstrip(".")
    return out


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    a, b = sections(sys.argv[1]), sections(sys.argv[2])
    print("| Q | same text | orchestrator | counterpart |")
    print("|---|---|---|---|")
    deltas = agreements = 0
    for q in sorted(set(a) | set(b)):
        ra, rb = a.get(q), b.get(q)
        if not ra or not rb:
            cls = "missing"
        elif norm(ra) == norm(rb):
            cls, agreements = "yes", agreements + 1
        else:
            cls, deltas = "no", deltas + 1
        print(f"| {q} | {cls} | {ra or '—'} | {rb or '—'} |")
    print(f"\n{len(set(a) | set(b))} questions, {agreements} identical, {len(set(a) | set(b)) - deltas - agreements} missing; mark each row delta or agreement")


if __name__ == "__main__":
    main()
