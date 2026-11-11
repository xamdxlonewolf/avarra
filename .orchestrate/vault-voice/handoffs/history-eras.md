<!-- orchestrate handoff
task: history-eras
branch: orch/vault-voice/history-eras
agentId: bc-0b972df1-4e30-42cd-b1f8-2e00d2bf2f12
runId: run-11fd2a3f-2ebd-43b8-aa3c-ccbb65b3de37
resultStatus: finished
finishedAt: 2026-11-11T06:21:14.356Z
-->

## Status
success

## Branch
`orch/vault-voice/history-eras`

## What I did
- `02 - History/Eras/Before the Walk.md`: rewrote the undated preface so a new reader can follow the Tree, Kinds, the Watching’s layers, and the Old Ways doors, and can see that organizing the tenth-year trip is what starts the next age.
- `02 - History/Eras/The Walking Years.md`: rewrote the road, the one-week door, the three walks, and the inns so the era explains itself from the uncounted start through the First Cut at Cut-year 0.
- `02 - History/Eras/The Years of Hands.md`: rewrote the present age so the three jobs of the walk, what the road left behind, and the live front on Heskoren can be followed from Cut-year 0 to Cut-year 387.
- Files left unchanged: 0 of these three. No other file was edited.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- The published invariant script splits `git diff --name-only` on spaces, so it reports `NEW FILE Walk.md`, `Years.md`, and `Hands.md`. The same check with the paths kept whole prints `invariants ok (3 files)`. Front matter is unchanged. These notes had no “will not say why” before or after.
- In-world slates are still in the speaker’s voice. Tables, headings, dates, and numbers are still there. Refusals stay refusals: the ribbon they will not explain, the held child the innkeeper will not account for, the knife a house will not name a saint for, and the hamlets that have learned not to say queue. No cause was added for any of them.
- GM-only material stayed under GM Notes, including the 5% edge, Clock 1, the open question of why the wood had to be carried, and the fate-table limits.
- Haelren is glossed as Hale-month, Leddorn as Ledger-month, and the Thallow as the worn name of Thaeloren, from player-facing names those notes already use. No new place, number, or power was added.
- The branch name was accepted. No pull request was opened.

## Suggested follow-ups
- Run the invariant check with NUL-separated paths. The space-splitting version will fail this slice even though the front matter and refusals are intact.
- After the note slices are done, rebuild the world book from these notes, then run the same voice pass on the world book and the player primer.