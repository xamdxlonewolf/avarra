<!-- orchestrate handoff
task: factions-guilds
branch: orch/vault-voice/factions-guilds
agentId: bc-d8fffe94-7181-42a8-8981-ab02f74579d9
runId: run-42dd3782-c696-4b25-a7da-cda9df428301
resultStatus: finished
finishedAt: 2026-11-11T06:19:10.065Z
-->

## Status
success

## Branch
`orch/vault-voice/factions-guilds`

## What I did
- `05 - Factions/Guilds/Craft Fellowships.md`: rewrote the three fellowships so a season of work is distinct from a licence, and left the grain, the silent walk, and the shovel unexplained.
- `05 - Factions/Guilds/The Element-Guilds.md`: rewrote the four doors, tickets, and exit, and left the coal, the cup, the clay, and the window unexplained.
- `05 - Factions/Guilds/The Intake.md`: rewrote the shed, the week, and the four limits, and kept the empty ticket-face and the in-world slip.
- `05 - Factions/Guilds/The Stillers.md`: rewrote the college, the Grey, and the corners, and left the knob unexplained past the practical check.
- `05 - Factions/Organizations/Movements.md`: rewrote the pear-graft, the withdrawers, and the disinherited, and left the passage and the old house-name unexplained.
- `05 - Factions/Organizations/The Greens-Keepers.md`: rewrote the door onto the furnishing note without explaining the buried leaf.
- `05 - Factions/Organizations/The Hall-Keepers.md`: rewrote the outlet and the Voice-ticket without naming which Cry the unswept bench belongs to.
- `05 - Factions/Organizations/The Protectors.md`: rewrote the public Care, and kept harvest, hush, and the bank under GM Notes.
- `05 - Factions/Organizations/Tithe-Infrastructure.md`: rewrote gates, tickets, and the three corners, and left the leaf, the seat, the cousin's name, and the room's name unexplained.
- Assigned notes left unchanged: 0. No file outside that list was edited.

## Measurements
- `body words (assigned notes): 12073 → 14614`
- `will not say why (assigned notes): 5 → 6`

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Front matter, headings, in-world quotations, and table line counts match `origin/master`. The extra "will not say why" is on the element-guild shop habits, which already said a guest is not told the reason.
- The planner's invariant script splits `git diff --name-only` on whitespace, so these paths are reported as new files (`Fellowships.md`, and so on). With `-z` / `split("\0")`, the same check prints `invariants ok (9 files)`.
- Protectors player text still says the Care holds the one and will not produce them. Controlled deaths, the store, the hush, and the missing hour stay under GM Notes.
- Conventions.md and CLAUDE.md were left alone, as this slice forbids editing them. They still prescribe the short voice.

## Suggested follow-ups
- Point the invariant check at null-terminated paths before it scores this branch.
- Give some later slice the Conventions.md and CLAUDE.md voice update, so a new session does not put the short voice back.