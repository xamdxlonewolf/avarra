<!-- orchestrate handoff
task: world-life
branch: orch/vault-voice/world-life
agentId: bc-b69c4001-fafe-4c70-b022-5740a33e2aad
runId: run-2b4b509a-5d1b-452a-aa7d-aecc5b12f326
resultStatus: finished
finishedAt: 2026-11-11T06:20:59.721Z
-->

## Status
success

## Branch
`orch/vault-voice/world-life`

## What I did
- `01 - World/Ecology/Ecology of the Turning.md`: rewrote the rules and the prose around the tables so a new reader can follow Condition, Tithe, disease, and livelihood; inventories, row labels, and numbers stayed.
- `01 - World/Astronomy/The Reckoning of the Year.md`: rewrote the calendar explanation around the locked month table; Cut-years, pronunciations, moon names, and the GM reading of the solstice stayed in place.
- `01 - World/Astronomy/The Sky from the Ground.md`: joined the short stacks and kept the sentences that already described what a person sees.
- `01 - World/Phenomena/Brine and Rain.md`: rewrote the lot weather so salt, fresh water, Tithe, and staple are followable; Orentel's salt and the windless morning still have no cause.
- `01 - World/Phenomena/The Day-Wash.md`: rewrote the afternoon shine; the uphill thread is still unexplained.
- `01 - World/Phenomena/The Green Across the Gap.md`: rewrote the unreachable canopy; the dawn-to-noon vanishing is still unmeasured and unexplained.
- `01 - World/Planes/Planes.md`: rewrote the refusal of other planes in the same explanatory voice; no plane was added, and the GM bans stayed under GM Notes.
- Left unchanged: 0 of these 7 notes.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Front matter is unchanged on all 7 files. The month table matches `origin/master`. Invariants pass if diff paths are split on newlines: `invariants ok (7 files)`. The planner script's `.split()` breaks these paths on spaces and will false-report `NEW FILE`.
- No cause was added for Orentel's salt, the windless salting, the uphill thread, or the canopy that is gone by noon. `will not say where` and `will not say which` are still there. None of these notes used `will not say why`.
- GM-only facts (the Mother is real, photoperiod, the bounded hand, the keystone experiment, planes as a place to park a secret) stayed under GM Notes.
- Gloss that a verifier should spot-check: Grey Summer's Given, Struck, and Kept; "the stand" as the week's witness; the Shore-lands Tithe as the green the Taken-In rest in; Maiethorn's "higher on the Given" as the Leaf-Fall's gift. Leaf-Fall on the green note and "Gives nothing" on the Dry Stair were not filled in from other notes.
- Conventions, the setting book, the primer, library handouts, the roadmap, and audits were not edited. No pull request was opened.

## Suggested follow-ups
- Run the invariant check with newline-separated paths, or the slice will look like seven new files.
- The voice pass on the rest of the vault, then the setting book and the player primer, is still outstanding.