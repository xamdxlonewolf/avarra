<!-- orchestrate handoff
task: settlements-sites
branch: orch/vault-voice/settlements-sites
agentId: bc-a602aa77-339c-4b78-b033-546123fddf1c
runId: run-e9824cd4-ebf4-4c17-b74c-4167b89de60e
resultStatus: finished
finishedAt: 2026-11-11T06:19:49.892Z
-->

## Status
success

## Branch
`orch/vault-voice/settlements-sites`

## What I did
- The Dry Stair: rewrote the climb, the dry basin, and the missed child so a new reader can follow the dare.
- The Low Wall: rewrote the uncounted wall, the Cut-year 381 dig, and the quarry claim in the same explanatory voice.
- The Seeing-Ring: rewrote the ring, the emptied shrine, and Tithsael's night, and left the clockwise walk unexplained.
- The Third Hearth: rewrote the road-house, Seine's bed, and Brenthael's stone, and left the doorway broom unexplained.
- The White Note House: rewrote the quay desk, the loft, and the north-bed custom without naming the founding-name.
- Unchanged files: 0.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- The required invariant script fails on these paths because `.split()` breaks on spaces. Its output was `NEW FILE Stair.md`, `NEW FILE Wall.md`, `NEW FILE Seeing-Ring.md`, `NEW FILE Hearth.md`, and `NEW FILE House.md`. Splitting on NUL instead passes: front matter identical on all 5 files, and `will not say why` stays 1 on The Third Hearth.
- No pull request opened. The unexplained habits are still unexplained: the skipped step, standing behind the Low Wall, watering the last course, the clockwise ring, the two outlooks that face nothing, the basin's purpose, and Thilim's broom. GM-only facts stayed under GM Notes.

## Suggested follow-ups
- Run the invariant check with `git diff -z` or `splitlines()`, not `.split()`, or the next slice of settlement paths will false-fail the same way.