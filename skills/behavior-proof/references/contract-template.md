# Behavior Contract Template

Fill this in **before** driving the app. Keep it short enough that someone who has not read the source can execute it.

```md
# Behavior Contract

## User-Visible Goal
<What must be true for the user in their own role.>

## Target
- Access: <URL of the screen>
- Account: <seeded username; never a real credential>
- Fixtures: <the seeded records this run needs>

## User Tasks
1. <Something a real user does, in their words.>
2. <...>

## Expected Observable Behavior
- <What is on screen, or in the store, afterwards.>
- <What happens on invalid or empty input.>

## Anti-Cheat Probes
- <Change the input data; the output must change with it.>
- <Reload; state that should persist must persist.>
- <Empty and invalid input; the promised handling must appear.>
- <The control must do real work, not only render.>

## Evidence Required
- <Screenshot, recording, or printed page state, per task.>

## Out Of Scope
- <What this run must not judge.>
```

Complete when every task and probe has an expected observable result and an evidence type.

## Worked example

A record of one real run, kept because it shows why the probes exist. It describes that pull request, not any current product.

The whole suite passed and the control did nothing:

```md
## User-Visible Goal
A worker reading a scanned document can fill the viewer with one column of the scan.

## User Tasks
1. Open a document with extracted data, then press the focus control.

## Expected Observable Behavior
- The first column fills the viewer and is large enough to read against the form.
- Pressing again shows the second column; a third press restores the whole page.

## Anti-Cheat Probes
- Compare the image before and after the press. It must change.
- Print the zoom ratio. A ratio near 1.0 means the control did nothing.

## Evidence Required
- A screenshot per press, and the viewer size and zoom ratio printed from the page.
```

The zoom ratio probe was the one that mattered. The button rendered correctly, 43 of 43 tests passed, and the ratio was 1.12: no visible zoom. A screenshot alone showed something was wrong; the printed ratio said why, in the same run.
