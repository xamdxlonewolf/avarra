<!-- orchestrate handoff
task: settlements-cities
branch: orch/vault-voice/settlements-cities
agentId: bc-b1d93b11-fc94-4a08-a320-c4d8895f7aba
runId: run-56c7da08-47db-4e91-b95e-75373187a73b
resultStatus: finished
finishedAt: 2026-11-11T06:18:35.872Z
-->

## Status
success

## Branch
`orch/vault-voice/settlements-cities`

## What I did
- `04 - Settlements/Cities/Braetu.md`: rewrote the harbour account so the far crossing, the dark book, and the unlit berth follow from one another.
- `04 - Settlements/Cities/Larbril.md`: rewrote the road-and-wash account and left both unexplained habits in place.
- `04 - Settlements/Cities/Lunbra.md`: rewrote the roll and the shown money so a new reader can follow the room.
- `04 - Settlements/Cities/Maiethlir.md`: rewrote the counted hearth, the layout, and the offices, and left the in-world slip in the speakers' words.
- `04 - Settlements/Cities/Naenor.md`: rewrote the signing-watch account, including the term won and the berth lost.
- `04 - Settlements/Cities/Orentel.md`: rewrote the salt quay, the hill, and the three desks, and left the salt and the eight habits unexplained.
- `04 - Settlements/Cities/Raitin.md`: rewrote the hearth-league account and left all eight habits unexplained.
- `04 - Settlements/Cities/Rothallo.md`: rewrote the walled capital, the Book, and the beds outside the gate.
- `04 - Settlements/Cities/Seinbrun.md`: rewrote the furnished city and left all seven habits unexplained.
- `04 - Settlements/Cities/Votaer.md`: rewrote the classification quay and left all four habits unexplained.
- Files left unchanged: 0.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- No pull request opened. The branch pushed as `orch/vault-voice/settlements-cities`.
- Front matter, headings, table rows, habit blocks, in-world quotations, and number tokens match the base. All 48 "will not say why" refusals are still there. Player-facing text did not pick up GM-only lines.
- The planner's invariant script splits `git diff --name-only` on whitespace, so paths like `04 - Settlements/Cities/Braetu.md` are reported as new files. A line-based read of the same diff passes.
- Glosses use only facts already in each note. Liren was not redefined as a whole year. Habits were not given causes.

## Suggested follow-ups
- Point the invariant check at whole path lines, or at null-delimited names, before it scores this slice.
- The setting book and the player primer are still waiting on the later pass.