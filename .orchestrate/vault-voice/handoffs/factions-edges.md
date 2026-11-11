<!-- orchestrate handoff
task: factions-edges
branch: orch/vault-voice/factions-edges
agentId: bc-49b0114d-6f84-4e46-a666-21499c6136f8
runId: run-c2d035f3-62e3-43a7-a825-5d99f5ac15d7
resultStatus: finished
finishedAt: 2026-11-11T06:19:24.148Z
-->

## Status
success

## Branch
`orch/vault-voice/factions-edges`

## What I did
- `05 - Factions/Criminal/The Holding Desk.md`: rewrote the hold-clerks so a new reader can follow a Bound, a Term, the Pledge, and the Forfeit, and left the extension-slip in the clerk's voice.
- `05 - Factions/Criminal/The Slide.md`: rewrote the week-keepers so Tithe, wilt, Cry, and fade are explained in the sentence that uses them, and left the week-slip in the landlord's voice.
- `05 - Factions/Criminal/The Standing Trade.md`: rewrote sold vouching so witness, Blood-Read, and the three pillars are followable, and left the fee-slate in the seller's voice.
- `05 - Factions/Military/The Watch and the Cohort.md`: rewrote the watch, the cohort, the Closing, and the Hinge Hush into connected explanation. The cohort is still not a company kept under arms. The meal at the thorn is still unexplained.
- `05 - Factions/Movements/Movements Home.md`: pointed at the existing movements note in spoken sentences and did not copy those movements into this folder.
- `05 - Factions/05 - Factions.md`: rewrote the index so the shelf, the recruitment rule, and the one-line jobs read as explanation. There is still no fourth criminal house.
- Files left unchanged: 0.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- The pasted invariant script splits `git diff --name-only` on whitespace, so paths such as `05 - Factions/Criminal/The Holding Desk.md` become `Desk.md` and the script reports false `NEW FILE` lines. A NUL-safe rerun of the same checks printed `invariants ok (6 files)`. Front matter matched `origin/master` on all six. `will not say why` stayed 1 in the watch note and 0 elsewhere.
- Withdrawers standing in the passage, and their refusal, live on `05 - Factions/Organizations/Movements.md`, which this slice does not edit. Movements Home still sends the reader there and does not hold a second copy.
- Orledd, the 5% tone line, harvested fire, and the hush stayed under GM Notes. The thorn meal, the rope-story, and the other unexplained habits were not given a cause.
- No pull request was opened.

## Suggested follow-ups
- When the planner runs the invariant script on this vault, split diff names on newlines or NUL, not on spaces.
- The passage habit for withdrawers is still only on the Movements note. Leave it there unless a later slice is assigned that file.