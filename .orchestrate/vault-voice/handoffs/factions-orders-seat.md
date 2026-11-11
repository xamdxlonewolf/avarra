<!-- orchestrate handoff
task: factions-orders-seat
branch: orch/vault-voice/factions-orders-seat
agentId: bc-5247deaa-1dc9-4196-9098-068e563ed4c7
runId: run-6cb622e0-2b65-4049-a3e8-c7034edbb33e
resultStatus: finished
finishedAt: 2026-11-11T06:19:14.806Z
-->

## Status
success

## Branch
`orch/vault-voice/factions-orders-seat`

## What I did
- `05 - Factions/Religious Orders/The Book-Hands.md`: rewrote the desk, the civic settling, and the refusals so a new reader can follow the office without losing terms, numbers, or the gift-word habit.
- `05 - Factions/Religious Orders/The Watchers.md`: rewrote the Night Watch, the second reading, and the recut beam in the same voice, and left the silence-counting refusal unexplained.
- `05 - Factions/Religious Orders/The Tree-Wardens.md`: rewrote the four offices, the queue, and the in-world pages around the existing quotes, and left GM-only facts under GM Notes.
- Files left unchanged: 0 of the three assigned notes. No other files were edited.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- The platform accepted `orch/vault-voice/factions-orders-seat`. No pull request was opened.
- Front matter, headings, table rows, block quotes, and wikilink targets match `origin/master`. A path-aware check of those invariants passed. The planner script in the brief splits `git diff --name-only` on whitespace, so these paths will be reported as `NEW FILE Book-Hands.md` (and the same for the other two). That result is the splitter, not new files.
- The only new wikilink target is `The Walled Book` on the existing word Close in the Tree-Wardens fear cell. That note already linked the Walled Book.
- No out-of-scope files (setting book, primer, library, roadmap, audits, Conventions, CLAUDE.md) were edited.

## Suggested follow-ups
- When the verifier runs the brief's Python check, pass the diff names through without splitting on spaces.
- The other religious-order notes (Door-Keepers, Table-Keepers, and the rest) are still in the short voice.