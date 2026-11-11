<!-- orchestrate handoff
task: cultures-peoples
branch: orch/vault-voice/cultures-peoples
agentId: bc-bd637829-4a6f-4a5f-927b-37abebdb6faa
runId: run-9c579411-1064-41cd-be4c-9cb3421e17ce
resultStatus: finished
finishedAt: 2026-11-11T06:19:13.623Z
-->

## Status
success

## Branch
`orch/vault-voice/cultures-peoples`

## What I did
- `03 - Cultures/Peoples/Kinds of the Turning.md`: rewrote the distribution, hearth, mixed-child, and stock-ancestry prose so a new reader can follow Kind, Condition, hearth, and the kitchens, and left the unexplained habits with no cause.
- `03 - Cultures/Peoples/Kitsune.md`: kept the fox-born portrait and the ancestry feature numbers, and folded born-versus-Condition into that paragraph.
- `03 - Cultures/Peoples/Selkie.md`: kept the sealskin portrait and the feature numbers, and folded the same fact in.
- `03 - Cultures/Peoples/Tengu.md`: kept the crow-born overview sentence and the feature numbers, and folded the same fact in.
- `03 - Cultures/Peoples/Yumboe.md`: kept the good-people portrait, the name list, and the feature numbers. Reach-only facts stayed under GM Notes.
- `03 - Cultures/03 - Cultures.md`: turned the index lines into sentences a new reader can follow. Production citations stayed in GM Notes.
- Files left unchanged: 0

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Pushed `orch/vault-voice/cultures-peoples`. No pull request opened.
- Front matter, headings, wikilink targets, ancestry feature bullets, and numeric tokens match `origin/master`. The fourth-fox refusal, the Fungril spoonful, the unnamed current, and the ridge mark still have no cause. "Could be Given," "no Tree," household, and purchase stayed in Yumboe GM Notes.
- The planner's invariant script splits `git diff --name-only` on whitespace, so paths like `03 - Cultures/...` are reported as `NEW FILE`. Splitting on lines instead reports `invariants ok (6 files)`.
- The cultures index is still a link list. The sentences after each link are the voice pass.

## Suggested follow-ups
- Run the invariant check with `splitlines()`, not `str.split()`, before judging this slice.
- The rest of `03 - Cultures` is still in the old register. The setting book and the player primer were left alone, as scoped.