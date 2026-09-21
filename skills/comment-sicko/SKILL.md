---
name: comment-sicko
description: "Strip a diff or a set of files of narration, banners, dead code and alibi comments, and flag the symbols whose behaviour needs a refactor instead of prose. Use before review, on a diff that reads as commentary, or when asked to clean comments. Report only; it edits comments and never application code."
license: MIT
metadata:
  origin: ported from cursor/plugins pstack (agents/comment-sicko.md, MIT, Lauren Tan); licence text in LICENSE beside this skill
---

# comment-sicko

Run `agents/comment-sicko.md` as a subagent with the tools it lists, or, in a harness without subagents, as a fresh session with that file as its instructions, on the scope: the files or diff in hand, or the current diff against `main` plus untracked files when nothing is named. It deletes the comments its keep-list does not protect and marks every symbol whose behaviour needed prose as `MUST KILL`. The refactors it names are yours to do or to decline; it never writes application code.

Read its report as a list: files touched, deletions, `MUST KILL` flags with one line each, skips. A flag names a symbol inside the scope, so every one can be opened.

The agent runs the `how` and `why` skills on a comment's claim when they are installed, and hunts by hand through callers, `git log -S`, `git blame` and the narrowest test when they are not. Either way, doubt after the hunt means the comment goes.
