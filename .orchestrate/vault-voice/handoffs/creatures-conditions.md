<!-- orchestrate handoff
task: creatures-conditions
branch: orch/vault-voice/creatures-conditions
agentId: bc-ec4deeb7-a81e-4d4c-b84e-f3ec3ee403ae
runId: run-4fa93803-d601-4c79-945b-415bf34e39ec
resultStatus: finished
finishedAt: 2026-11-11T06:20:42.788Z
-->

## Status
success

## Branch
`orch/vault-voice/creatures-conditions`

## What I did
- `09 - Creatures/Conditions/Bound.md`: Rewrote the contract, the faiths, and the release so a new reader can follow Struck-only Bound, the ~5% lane, and the Given-Over without picking up Orledd.
- `09 - Creatures/Conditions/Conditions.md`: Rewrote the index around the existing roster, clocks, and colour tables, and restored the Awakening / Leaf-Fall link.
- `09 - Creatures/Conditions/Far-Voiced.md`: Rewrote the voice, the eleven-in-twelve split, and the Cry so the danger stays on the singer.
- `09 - Creatures/Conditions/Long-Lived.md`: Rewrote the keeper and the cup (one year of memory at a time) and left the threshold courtesy unexplained.
- `09 - Creatures/Conditions/Phoenix.md`: Kept the breathing paragraphs, the card, and the tithe, and only rewrote the chopped social and table-deal lines.
- `09 - Creatures/Conditions/Returned.md`: Rewrote the unfinished death and the purpose, and left Threnvaeth under GM Notes.
- `09 - Creatures/Conditions/The Answered.md`: Rewrote the four elements and the wildcard standing around the unchanged Reach table.
- `09 - Creatures/Conditions/The Stilled.md`: Rewrote the gaze, both paths, and the Grey so the licence and the self-seizing stay distinct.
- `09 - Creatures/Conditions/The Taken-In.md`: Rewrote the frontier life and the city life, including the quay, the walled grove, and the pay gap.
- `09 - Creatures/Conditions/The Unbound.md`: Rewrote the Hollow as the downstream of Bound only, with the three Absence lanes kept apart.
- `09 - Creatures/Conditions/Two-Bodied.md`: Rewrote the common second self and kept the animal voice, the size band, and the weapon table.
- Files left unchanged: 0.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Front matter, headings, table rows, and wikilinks match `origin/master`. A space-safe run of the invariant check printed `invariants ok (11 files)`.
- The verifier script in the brief does `.split()` on `git diff --name-only`. These paths contain spaces, so that script reports phantom `NEW FILE` entries (`Answered.md`, `Creatures/Conditions/Bound.md`, and the rest) and exits 1 even when the notes are fine. Split on NUL or on lines, not on whitespace.
- No pull request was opened. Setting book, primer, library, roadmap, audits, and Conventions were not edited.
- GM-only names (Orledd, Threnvaeth, the Protectors, One Gift) stayed under GM Notes. The Long-Lived door custom still has no new cause.

## Suggested follow-ups
- Point the slice checker at `git diff --name-only -z` before it scores this branch.
- The same voice pass still has to cover the rest of the vault notes, then the setting book and the player primer.