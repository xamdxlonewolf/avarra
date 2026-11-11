<!-- orchestrate handoff
task: people-npcs-major
branch: orch/vault-voice/people-npcs-major
agentId: bc-608e140d-4c33-41b0-96cb-3aeed50ea66e
runId: run-4f931f04-d34b-4e0c-9344-62fed776ee79
resultStatus: finished
finishedAt: 2026-11-11T06:17:09.093Z
-->

## Status
success

## Branch
`orch/vault-voice/people-npcs-major`

## What I did
- `08 - People/NPCs/Laevila.md`: explained the Watcher, the recut copy, and the naming so the page reads as one account.
- `08 - People/NPCs/Tesara.md`: explained the catching-week, the empty ticket, and Valen's week without adding why Rosire is gone.
- `08 - People/NPCs/Thilim.md`: explained the Held bed, the four *I walked* jobs, and the threshold courtesy, still unexplained.
- `08 - People/NPCs/Mataero.md`: explained occupancy, the twelve beds, and the north bed without revealing why the custom is the credit.
- `08 - People/NPCs/Rithim.md`: explained the Speaker, the delayed copy, and Valein as Kept.
- `08 - People/NPCs/Vaethod.md`: explained the hinge, the choice to send, and Saelid's stall.
- `08 - People/NPCs/Njunda.md`: explained the table, the extra place, and the one impiety. The heel of the loaf was not added.
- `08 - People/NPCs/Reimaethe.md`: kept the cup rules and joined them into a continuous account of four years given and a fifth not yet given.
- `08 - People/NPCs/Taeren.md`: explained the hush and left the public Phoenix sentence unchanged. The new-leaf fact stays in GM Notes.
- `08 - People/NPCs/Rosire.md`: explained the opened door and the unnamed house. The Protectors stay in GM Notes.
- `08 - People/NPCs/Ledan.md`: explained the quay-desk, the counts, and the founding-name they will not speak first.
- `08 - People/NPCs/Methei.md`: explained the turn of work. The blanket still has no cause.
- `08 - People/NPCs/Hithaen.md`: explained the Kept line and the Book of Tithes. The class-rule correction stays in GM Notes.
- `08 - People/NPCs/Dumu.md`: explained the march-voice and the queue. The latch still has no cause.
- Files left unchanged: 0.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Front matter, headings, numbers, and wikilink targets match `origin/master`. "will not say why" is still one each in Methei and Dumu.
- A path-safe rerun of the invariant check reports `invariants ok (14 files)`. The published script uses `.split()`, which breaks on the spaces in `08 - People/...` and prints `NEW FILE` for path fragments. That failure is the splitter, not the notes.
- No pull request. Setting book, primer, library, roadmap, audits, Conventions, and `CLAUDE.md` were not edited.
- Word count across the fourteen notes moved from 10577 to 13395. The added words are glosses of terms already on the page.

## Suggested follow-ups
- Run the invariant check with `git diff -z` or `splitlines()` so spaced vault paths are not reported as new files.
- Leave the world book and the player primer until the other note slices are in.