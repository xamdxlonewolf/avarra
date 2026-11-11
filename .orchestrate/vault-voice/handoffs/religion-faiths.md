<!-- orchestrate handoff
task: religion-faiths
branch: orch/vault-voice/religion-faiths
agentId: bc-ae866c10-b7d3-496b-93e2-4ff6685eb556
runId: run-8f630d6e-e112-438a-8911-d62393595b2d
resultStatus: finished
finishedAt: 2026-11-11T06:23:07.216Z
-->

## Status
success

## Branch
`orch/vault-voice/religion-faiths`

## What I did
- `07 - Religion/Faiths/Faiths of the Turning.md`: rewrote the map so the argument, the local quarrels, and the blends read as explanation. The glance table and the link index stayed.
- `07 - Religion/Faiths/The Fair Hand.md`: rewrote the ethic, the marks, and the book-hands into continuous prose. Ledger lines and the margin argument stayed in the speakers' words.
- `07 - Religion/Faiths/The Leaf-Mother.md`: rewrote doctrine, practice, clergy, and the schism in the same voice. The Leaf-Mother stays a belief, and the three questions stay unsettled.
- `07 - Religion/Faiths/The Old Ways.md`: rewrote the land-and-kin faith so doors, *vael*, and the two readings explain themselves. A closed door stays weather.
- `07 - Religion/Faiths/The Open Table.md`: rewrote hospitality, the two suppers, and the week that can close so belonging is followable. The blessing stayed in the speaker's voice.
- `07 - Religion/Faiths/The Watching.md`: rewrote the heartland heresy so seeing, cost, and what was spent stay open where they were open.
- Files left unchanged: 0

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- The automated script exits 1 because `.split()` breaks paths that contain spaces. A path-safe rerun (`git diff -z` / `splitlines`) prints `invariants ok (6 files)`. Front matter and headings match `origin/master`. No `will not say why` lines were present to lose.
- Word counts rose on all six notes (about 1530→1878, 1495→1774, 2331→2558, 1479→1653, 2106→2312, 1500→1658 before the last joins). Diff is 315 insertions, 220 deletions, and only these six files.
- The Tithe’s four ethics are named to the four mainland faiths in the order the old slash list already used. The Kept’s four readings are stated without pinning “passed over” on the Watching, because that note still argues both a seeing of wholeness and a seeing that did not reach.
- These notes had none of the unexplained household habits. No cause was added. GM facts stayed under `## GM Notes`. In-world quotations were kept verbatim. Link sections stayed indexes.
- No pull request was opened.

## Suggested follow-ups
- When the verifier runs the automated check, split diff names on newlines. `.split()` treats `07 - Religion/...` as several paths.
- Leave the setting book and the player primer until the rest of the note pass is in.