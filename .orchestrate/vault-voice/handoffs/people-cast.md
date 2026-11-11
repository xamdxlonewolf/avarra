<!-- orchestrate handoff
task: people-cast
branch: orch/vault-voice/people-cast
agentId: bc-2b376815-098a-415c-aba7-e7597b27afa1
runId: run-0d9d9863-60a9-43a3-869d-f143f8f2714e
resultStatus: finished
finishedAt: 2026-11-11T06:17:06.446Z
-->

## Status
success

## Branch
`orch/vault-voice/people-cast`

## What I did
- `08 - People/Historical Figures/Dirrol.md`: rewrote the column, the Worn Count, and the Grey Summer desk so a new reader can follow the fever year.
- `08 - People/Historical Figures/Hildal.md`: rewrote the Retreat, the Book, and the grove so the clerk’s choice reads as one account.
- `08 - People/Historical Figures/Limrae.md`: rewrote the roll-preface, the crown-count, and Manril’s refusal.
- `08 - People/Historical Figures/Monseoth.md`: rewrote the mile-shrine sermon and kept the road-speech in the speaker’s words.
- `08 - People/Historical Figures/Narol of the Pass.md`: rewrote the thaw-toll and left both rubbings of the water-line unexplained to a lowlander.
- `08 - People/Historical Figures/Rithnali.md`: rewrote the minute, the how, and the five tellings without naming a cutter.
- `08 - People/Historical Figures/Sedrad.md`: rewrote the held hull and kept the quay’s copied speech, including the reason the songs drop.
- `08 - People/Historical Figures/Taerso.md`: rewrote the hush and said what a fade is the first time the page uses the word.
- `08 - People/People of the Turning.md`: rewrote the cast index so Kind, colour, Struck, the cup, and the ordinary wants are followable, and left living secrets under GM Notes.
- `08 - People/Leaders/Leaders.md`: joined the office index’s chopped sentences and kept every holder.
- `08 - People/Heroes and Villains.md`: turned the praised, condemned, and still-argued stubs into sentences.
- `08 - People/Heroes/Heroes.md`: said what the folder points at.
- `08 - People/Villains/Villains.md`: said why there is no separate villains list.
- `08 - People/08 - People.md`: rewrote the section index so each list says who the people are.
- Files left unchanged: 0.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Front matter, headings, table rows, numbers, in-world quotations, and the name-draw commands are unchanged. A check that splits diff paths on lines reports `invariants ok (14 files)`.
- The verifier script in the brief uses `.split()`, which breaks these paths on spaces and prints false `NEW FILE` lines. Use `splitlines()` before treating that output as a failure.
- Glosses use facts the page already used or was allowed to say: Kind, colour, Given, Kept, Struck, Returned, Taken-In, Far-Voiced, Selkie, the Salt Walk, a First-Hand year, Cut-year, and a Long-Lived giving a year of memory into the Pourers’ cup. Taeren’s hidden fire, the two different walks, and Hithaen’s unsaid house stayed out of player-facing text.
- Refusals left without a cause: Manril’s home, which rubbing at the pass is the prayer, the songs that will not say the place, Hithaen’s house in the hall, and why Tesara has not been told Rosire is away. These notes had no “will not say why” lines to lose.
- No pull request was opened.

## Suggested follow-ups
- Point the voice verifier at `splitlines()` before it scores paths that contain spaces.
- The rest of the vault still needs the same pass. This slice stopped at the people notes listed above.