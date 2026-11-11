<!-- orchestrate handoff
task: religion-practice
branch: orch/vault-voice/religion-practice
agentId: bc-bb5944ee-4314-4381-9e9b-89f1a2aec176
runId: run-6a547a58-87bb-4715-9692-f29a81a3e206
resultStatus: finished
finishedAt: 2026-11-11T06:20:10.981Z
-->

## Status
success

## Branch
`orch/vault-voice/religion-practice`

## What I did
- `07 - Religion/Mythology/The Branch That Came Away.md`: framed the Cut and a Hand for a new reader. The told story and the houses' last lines stay in the teller's voice.
- `07 - Religion/Mythology/The Child Who Climbed the Stone.md`: explained Here and Far as a square game a new reader can follow. The calls and the cargo list stay as played.
- `07 - Religion/Mythology/The Child Who Counted Stones.md`: connected the song's frame. The verses, the missing five, and both answers stay as sung.
- `07 - Religion/Mythology/The Child at Four Doors.md`: glossed a Turning in the frame. The story and each house's last line stay in the speaker's voice, and the Mother stays a belief.
- `07 - Religion/Rituals/The Guest-Meal.md`: walked the hour in each place. The heel of the loaf and the leaf on the spring stay unexplained.
- `07 - Religion/Rituals/When Someone Is Struck.md`: walked the hour of a change with no leaf. The spring's leaf is still not a sign, and no threshold is confirmed.
- `07 - Religion/Rituals/When the Town Buries.md`: walked the carry, the meal, and the door. Salt on the roots and the wet leaf stay outside the hour.
- `07 - Religion/Deities/Maieth.md`: kept her as what the devout hold, with the schism unsettled on this page.
- `07 - Religion/Deities/The Unspent.md`: explained the cup, the five-year ask, and the circle's claim. The older-than-the-name fact stays under GM Notes.
- `07 - Religion/Religious History/The Houses and the Years.md`: pointed at the ages, the five attributions, and Cut-year 248 without adding a year or a cutter.
- `07 - Religion/Turning Tree.md`: kept the Leaf-Fall's two outcomes, the colour table, and Given, Kept, and Struck distinct. City practice and the question table now read as explanation. The hug is still the faith's reading, not a confirmed kindness.
- `07 - Religion/The Uncoloured Intake.md`: explained the hall around the page. The covering note and the four slips stay in the writers' words, and they do not confirm her.
- `07 - Religion/07 - Religion.md`: opened the folder so a new reader can tell what each note is.
- Files in this slice left unchanged: 0.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Pushed `orch/vault-voice/religion-practice`. No pull request opened.
- Front matter, headings, table row counts, and wikilink targets match `origin/master`. In-world last lines, the counting-song verses, and the gift-hall slips were not rewritten into the narrator.
- The heel and the spring leaf now say they will not say why, on top of the refusal already there. That count went from 0 to 2 in The Guest-Meal. Nothing that already said "will not say why" was removed. Salt on the roots, the wet leaf, and the spring's leaf in the Struck hour are still not given a cause.
- The planner's invariant script splits `git diff --name-only` on whitespace, so on these paths it reports false `NEW FILE` errors and exits 1. The same check with paths split on newlines prints `invariants ok (13 files)`.
- Setting book, player primer, library handouts, roadmap, audits, Conventions, and CLAUDE.md were not edited.

## Suggested follow-ups
- Run the invariant check with newline-split paths. The published `.split()` call will fail this slice even when front matter is unchanged.
- The faith essays under `07 - Religion/Faiths/` were outside this slice.