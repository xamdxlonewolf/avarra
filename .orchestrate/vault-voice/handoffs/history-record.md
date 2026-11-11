<!-- orchestrate handoff
task: history-record
branch: orch/vault-voice/history-record
agentId: bc-da9efa69-c289-4612-8243-b9854c9e88d5
runId: run-bb934227-a9a0-4a07-92bf-08ec925ab955
resultStatus: finished
finishedAt: 2026-11-11T06:23:26.060Z
-->

## Status
success

## Branch
`orch/vault-voice/history-record`

## What I did
- `02 - History/A History of the Turning.md`: Glossed the Tree, Kinds, Conditions, the First Seat, and the memory cup in place, and joined the stacked sentences. Dates, figures, and the open questions stayed.
- `02 - History/The Library Pages.md`: Rewrote the frame around the six pages so each one says what it is, who keeps it, and what a reader is meant to take from it. Keeper quotations and the GM Notes section stayed as they were.
- `02 - History/02 - History.md`: Turned the index lines into sentences a new reader can follow.
- `02 - History/Timelines/The Ages of the Turning.md`: Rewrote the two clocks, the year-counts, and their consequences as continuous explanation. Tables, pronunciations, Ledan's letter, and the GM limits stayed.
- `02 - History/Timelines/The Other Count.md`: Rewrote the chronicle the same way. The unsigned conversion table, the kitchen that cannot say which fear, and the quay that will not call the hush a victory stayed unexplained.
- `02 - History/Archaeology/Archaeology.md`: Said that the page only points at the three existing sites.
- `02 - History/Historical Figures/Historical Figures.md`: Said that the page only points at the notes under People.
- Left unchanged: 0 of these 7 notes.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Front matter matches `origin/master` on all 7 files. Headings, wikilink strings, and digit counts were checked and held. The library GM Notes block is byte-identical. No library handout, setting book, primer, roadmap, or audit was edited.
- The published invariant script splits `git diff --name-only` on spaces, so every path under `02 - History/` is reported as a new file. With names kept whole, the same checks print `invariants ok (7 files)`.
- Glosses use facts already in each note (Kind, Condition, Tithe, Leaf-Fall, Long-Lived, Taken-In, First Seat). Nothing was taken from `11 - Secrets`. The poem still will not say whether it is about the cup. Brenthael still cannot say when the seating started. The memory cup still has no start year.
- Push of `orch/vault-voice/history-record` was accepted. No pull request was opened.

## Suggested follow-ups
- The era and event notes under `02 - History` are still in the older compressed voice. They were outside this slice.
- Fix the invariant script to split diff names on newlines before the next history slice, or it will false-fail every path that contains a space.