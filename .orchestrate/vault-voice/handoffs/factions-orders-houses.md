<!-- orchestrate handoff
task: factions-orders-houses
branch: orch/vault-voice/factions-orders-houses
agentId: bc-591d2d18-ffeb-4bac-b783-c97d632e4610
runId: run-5d684e89-fb40-475d-a0f1-70a51cb73500
resultStatus: finished
finishedAt: 2026-11-11T06:17:53.335Z
-->

## Status
success

## Branch
`orch/vault-voice/factions-orders-houses`

## What I did
- `05 - Factions/Religious Orders/The Door-Keepers.md`: rewrote the walk, kin-naming, and grove fight into connected explanation. The water, hill, then stone order is still unexplained.
- `05 - Factions/Religious Orders/The Pourers.md`: rewrote the cup, the ask, and the gift so a new reader can follow. The second cup is still something nobody will talk about, and the taking stays in GM Notes.
- `05 - Factions/Religious Orders/The Remainder.md`: unfolded the side-yard desk from telegram lines into prose. Bury-or-walk and the hug filing stay as they were.
- `05 - Factions/Religious Orders/The Shore-Sitters.md`: rewrote the beach watch so it stays a separate house from the table. They still do not swim the wall, and no cause was added.
- `05 - Factions/Religious Orders/The Table-Keepers.md`: rewrote the hall, the attic, and the sentence that will not travel. Staying and Serving remain two ways of setting the same place.
- Files left unchanged: 0 of the 5 scoped notes. No file outside that list was edited.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Front matter, headings, in-world quotes, table rows, and wikilink targets were checked against `origin/master`. Door-Keepers still has one "will not say why" (1 → 1). The other four notes had none and still have none.
- A space-safe rerun of the invariant check passes (`invariants ok (5 files)`). The published checker does `text=True).split()`, which breaks these paths on spaces and reports `NEW FILE Door-Keepers.md` and the same for the other four. Split on newlines, or on NUL, before treating that as a failure.
- Player text did not pick up the inner circle, the founder, Vaelorn / Ornhael / Eloren, Threnvaeth, the Quiet Cut, or the keystone readings. Those stay under GM Notes.
- No pull request was opened.

## Suggested follow-ups
- Point the invariant script at newline- or NUL-separated paths before it scores this slice.
- The same voice pass still belongs on any religious-order notes outside this list, if another worker does not already have them.