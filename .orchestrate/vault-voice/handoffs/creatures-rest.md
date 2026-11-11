<!-- orchestrate handoff
task: creatures-rest
branch: orch/vault-voice/creatures-rest
agentId: bc-243c7320-6f4e-47a8-9215-3ec522154fb4
runId: run-578b1a93-7efe-436d-815a-fb1149988e50
resultStatus: finished
finishedAt: 2026-11-11T06:18:37.648Z
-->

## Status
success

## Branch
`orch/vault-voice/creatures-rest`

## What I did
- `06 - Magic/06 - Magic.md`: Connected the hub so crafts, a warden's sentence, and the true, embellished, and never-found artifacts read as one explanation.
- `06 - Magic/Artifacts/Artifacts.md`: Pointed at the item notes in a spoken paragraph and kept the keystone warning in GM Notes.
- `06 - Magic/How the Work Is Done.md`: Joined the job list and the Speaking rules into sentences a new reader can follow, and left the domain table and its numbers in place.
- `06 - Magic/Schools/Schools.md`: Connected the "no school" ruling into one explanation.
- `06 - Magic/Systems/Systems.md`: Connected the "no second system" ruling and glossed Turn from facts already in the note.
- `06 - Magic/Traditions/Traditions.md`: Connected the "no tradition" ruling to the warden's sentence on the Turning Tree.
- `09 - Creatures/09 - Creatures.md`: Rewrote the folder intro and index glosses so each entry says what it is, without adding creatures.
- `09 - Creatures/Adversaries/Bed-Keeper.md`: Rewrote the host intro and GM Notes. Stat block unchanged.
- `09 - Creatures/Adversaries/Chart-Crew.md`: Rewrote the quay-crew intro so it is not a stack of "not a pirate." Stat block unchanged.
- `09 - Creatures/Adversaries/Colourless Host.md`: Rewrote the dead-graft intro and GM Notes. The Leaf-Mother stays unconfirmed, and the stat block is unchanged.
- `09 - Creatures/Adversaries/Gap-Cat.md`: Rewrote the cat intro so it stays an animal. Stat block unchanged.
- `09 - Creatures/Adversaries/Spent-Week Walker.md`: Rewrote the walker intro, glossing UnTurned and Kept from the note's own terms. Stat block unchanged.
- `09 - Creatures/Constructs/A Made Thing.md`: Connected the job list. The shovel in the bank still has no cause.
- `09 - Creatures/Monsters/Monsters.md`: Connected the "no bestiary" pointer. No creature was added.
- `09 - Creatures/Spirits/Kin at the Door.md`: Connected the faith pointers. No spirit was added.
- `09 - Creatures/Unique/Unique.md`: Connected the pointer to notes that already exist. No unique creature was added.
- `10 - Items/10 - Items.md`: Expanded the index glosses. Keystone facts stayed in GM Notes.
- `10 - Items/Armor/Armor.md`: Connected the coat-versus-SRD-armor ruling.
- `10 - Items/Artifacts/The Closed Lamp.md`: Smoothed chopped description and GM Notes. Player text did not gain the fire-plot truth. The guest who cannot say why is unchanged.
- `10 - Items/Artifacts/The Dry Slip.md`: Connected the dead-slip description. The refusal story is still the one visitors prefer, with no new cause.
- `10 - Items/Artifacts/The One Knife.md`: Connected the unfound-knife page. The theft-or-gift refusal and the unnamed cutter stay unexplained.
- `10 - Items/Artifacts/The Other Chip.md`: Connected the quarry account. Cut-year 381 and the fill stayed.
- `10 - Items/Artifacts/The Ribboned Knife.md`: Connected the kitchen-knife account. The house still will not sell it as the first blade.
- `10 - Items/Artifacts/The Socket Ribbon.md`: Connected the cloth account. "Will not say why" and "nobody says why" stayed, including the four gaps.
- `10 - Items/Artifacts/The Spent Leaf.md`: Smoothed chopped checks and rewrote GM Notes in place. The firing-pin facts stayed under GM Notes.
- `10 - Items/Equipment/Equipment.md`: Connected the "no other kit list" ruling.
- `10 - Items/Materials/Materials.md`: Connected the materials pointer. No market and no new graft.
- `10 - Items/Weapons/Weapons.md`: Connected the "no weapon ladder" ruling.
- `10 - Items/What a Place Needed.md`: Connected the intro and table-cell sentences. Rows, places, and the "no prices" rule stayed.
- Left 3 files unchanged: `The Cart-Ox.md`, `The Path Dog.md`, and `The Terrace Goat.md`.

## Measurements
- changed files against origin/master: 0 → 29
- beast notes left unchanged: 3 → 3
- front-matter mismatches: 0 → 0
- lost "will not say why": 0 → 0

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- No pull request was opened. The branch pushed as `orch/vault-voice/creatures-rest`.
- YAML, headings, stat blocks, table rows, and wikilink targets were checked with a space-safe compare against `origin/master`. That check passed.
- The planner's Python check uses `.split()` on `git diff --name-only`, so paths with spaces are reported as `NEW FILE`. A space-safe read of the same diff shows front matter and the "will not say why" counts intact.
- GM-only facts on the lamp and the Spent Leaf stayed under GM Notes. Unexplained habits were not given causes.
- Conventions and `CLAUDE.md` were left alone, as this slice required.

## Suggested follow-ups
- Run the invariant check with `splitlines()` or `-z`, not `.split()`, before treating a space in a filename as a new file.
- The voice rules in Conventions and `CLAUDE.md` are still the old short-prose rule. Another slice needs to update them or a later session will put that voice back.