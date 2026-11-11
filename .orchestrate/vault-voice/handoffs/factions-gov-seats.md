<!-- orchestrate handoff
task: factions-gov-seats
branch: orch/vault-voice/factions-gov-seats
agentId: bc-b77aec62-2187-4b4b-8094-82b6108ae1c7
runId: run-ebd3a132-db6a-402d-b4f5-7dedba4e45af
resultStatus: finished
finishedAt: 2026-11-11T06:18:14.540Z
-->

## Status
success

## Branch
`orch/vault-voice/factions-gov-seats`

## What I did
- `05 - Factions/Governments/The Walled Book.md`: rewrote the note in explanatory prose, including GM Notes, and kept the manners, the unexplained Brenthael seating, the in-world leaf, and every heading and number.
- `05 - Factions/Governments/Powers of the Turning.md`: rewrote the fifteen-power catalogue so a new reader can follow the seats, names, and inheritances, and left the in-world minute and docket in the speakers' voices.
- `05 - Factions/Governments/The Reckoned Offices.md`: rewrote the four offices so the roll, the channel, and the gap with Rithim can be followed on the page, and left GM-only constraints under GM Notes.
- Unchanged files in this slice: 0.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Front matter, headings, and table-row counts match `origin/master`. In-world quotations were left as spoken. A space-safe rerun of the invariant check reports `invariants ok (3 files)`.
- The brief's script does `git diff --name-only` and then `.split()`, which breaks these paths on spaces and false-reports `NEW FILE Book.md`, `NEW FILE Offices.md`, and `NEW FILE Turning.md`. Read names as lines, or use `-z`.
- Brenthael still has no cause for the seating. No "will not say why" line existed in these notes, and none was added.
- Player text did not gain the bounded-reach cause, the Trenledd pun, the cutter, fire stored in the Close, or the three opposition groups. Those stayed under GM Notes.
- No pull request was opened.

## Suggested follow-ups
- Point the verifier at newline-safe diff names before it scores this slice.
- Leave the setting book and the player primer for the later pass, after the vault notes are done.