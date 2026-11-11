<!-- orchestrate handoff
task: settlements-villages
branch: orch/vault-voice/settlements-villages
agentId: bc-d8af2c00-26e5-437f-afcc-86b32b2bfd55
runId: run-3f550171-bcfe-4b51-985c-468f2726acae
resultStatus: finished
finishedAt: 2026-11-11T06:17:43.436Z
-->

## Status
success

## Branch
`orch/vault-voice/settlements-villages`

## What I did
- `04 - Settlements/Villages/Denlad.md`: rewrote the cove so the missed tide, the Hand, and the unwritten name read as one explanation.
- `04 - Settlements/Villages/Ndenjoo.md`: joined the hall's sentences and kept the heel unexplained, including the folk sentence Njunda will not confirm.
- `04 - Settlements/Villages/Raillath.md`: explained the halt, the shrine, and the unnamed ribbon without giving the ribbon a cause.
- `04 - Settlements/Villages/The First Bowl.md`: walked the guest-grove and the bowl, and left the rye-straw and the pinch unexplained.
- `04 - Settlements/Villages/The Three Hamlets Past the Ford.md`: explained the three kitchens and left the cup unexplained.
- `04 - Settlements/Villages/Tunral.md`: explained the kitchen with no sightline and left Huval's bowl unexplained.
- `04 - Settlements/Regions/Regions.md`: turned the index prose into connected sentences and left the tables in place.
- `04 - Settlements/Regions/The Down-Bank.md`: explained the stretch between the roll and the quay, and left the notches unexplained.
- `04 - Settlements/Continents/Continents.md`: explained that this folder only points at the geography notes.
- `04 - Settlements/Settlement Seeds.md`: rewrote the catalogue prose and table cells into sentences without adding a type.
- `04 - Settlements/04 - Settlements.md`: rewrote the section index so each gloss is a clause a new reader can follow.
- Files in this slice left unchanged: 0.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Front matter, headings, table rows, wikilinks, and numbers were checked against `origin/master` and held. Word counts rose on all 11 files.
- Ndenjoo "will not say why" went from 0 to 1, beside the existing line that the folk sentence about the crust is not the reason. The First Bowl and Tunral each still have one. No refusal count dropped.
- The heel, the rye-straw, the pinch from another hill, Vilraet not eating the heel, the unnamed ribbon, Huval's bowl, the Down-Bank notches, and the hamlets' cup still have no cause. GM-only facts stayed under GM Notes.
- The planner's exact Python script splits `git diff --name-only` on spaces, so paths such as `04 - Settlements/...` are reported as `NEW FILE`. A newline-safe rerun of the same checks prints `invariants ok (11 files)`.
- No pull request was opened. The setting book, primer, library, roadmap, audits, and conventions were not edited.

## Suggested follow-ups
- Point the invariant script at newline-separated paths so filenames with spaces are not flagged as new files.
- The remaining settlement notes (towns, cities, sites) still use the short voice if they are not already assigned.