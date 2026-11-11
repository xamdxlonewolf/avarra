<!-- orchestrate handoff
task: world-geography
branch: orch/vault-voice/world-geography
agentId: bc-87bac6ff-361a-48bb-8eb7-ba851681ae4e
runId: run-46ea0594-edf3-41c5-bcb0-2d6d70d7ada8
resultStatus: finished
finishedAt: 2026-11-11T06:19:53.521Z
-->

## Status
success

## Branch
`orch/vault-voice/world-geography`

## What I did
- `01 - World/01 - World.md`: rewrote the folder introduction and contents lines so each link says what the note is.
- `01 - World/Geography/Heskoren.md`: rewrote the frontier continent in connected prose, including reach, powers, faith, and GM notes.
- `01 - World/Geography/Maiethorn.md`: rewrote the Motherland the same way, including the Rain-Shadow, the Watching, and GM notes.
- `01 - World/Geography/Named Ground.md`: rewrote the gazetteer prose around the existing name table, climate table, and travel table.
- `01 - World/Geography/Strandoren.md`: rewrote the Shore-lands, including trade, the Fair Hand, and GM notes.
- `01 - World/Geography/The Known Map.md`: rewrote how to read the schematic, and the GM production notes, leaving the diagram and image embed in place.
- `01 - World/Geography/The Sundering Isle.md`: rewrote the isle, the crossing order, and the GM notes, leaving in-world speech in the speaker's words.
- `01 - World/Geography/The World Frame.md`: rewrote the four-continent frame and the reach-gradient, leaving the comparison table in place.
- Files left unchanged: 0.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Pushed `orch/vault-voice/world-geography` (commit `8ab632e`). No pull request opened.
- Front matter, headings, table row counts, and wikilink targets match `origin/master`. Word counts rose on all eight files. The Core-thaw's loud week, "Watchers will not," the cup on the ford-rock, children rubbing the water-line, and the Seat's refusal to learn Brenod, Vaelun, and Ornath are still unexplained. Keystone causes stay under `## GM Notes`.
- The verifier script as pasted splits `git diff --name-only` on whitespace, so paths like `01 - World/...` are reported as new files. The same check with `splitlines()` passed: `invariants ok (8 files)`.
- Setting book, player primer, library handouts, roadmap, audits, and `Conventions.md` / `CLAUDE.md` were not edited.

## Suggested follow-ups
- Run the invariant script with `splitlines()` (or `-z`) so spaced vault paths are not treated as new files.
- When the voice rules in `Conventions.md` and `CLAUDE.md` are updated, point them at this explanatory voice so a later session does not restore the short one.