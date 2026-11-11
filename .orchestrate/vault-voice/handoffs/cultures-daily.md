<!-- orchestrate handoff
task: cultures-daily
branch: orch/vault-voice/cultures-daily
agentId: bc-f13a669d-b6ad-4e39-abb4-e0125baaa9cc
runId: run-a4b378d9-c71b-468a-8007-aeb00b3ae1d1
resultStatus: finished
finishedAt: 2026-11-11T06:20:01.421Z
-->

## Status
success

## Branch
`orch/vault-voice/cultures-daily`

## What I did
- `03 - Cultures/Social Structures/Polity Archetypes.md`: turned the axis recap, corner comparisons, seats, memories, and GM notes into connected explanation, and folded glosses into the long sections that already breathed.
- `03 - Cultures/Social Structures/Daily Life.md`: kept the marriage, medicine, and town paragraphs that already breathe, and connected the one-fact stops (city witness, the watch, the frontier, UnTurned and Kept) plus the GM notes.
- `03 - Cultures/Traditions/How the Week Is Kept.md`: rewrote the chopped week so a new reader can follow each square, dock, waiting town, and hill-hall. The four habits still have no cause.
- `03 - Cultures/Customs/What the Year Feels Like.md`: joined the short stops and kept the sentences that already sounded spoken. The four habits still refuse an explanation.
- Files left unchanged: 0 of these 4. No file outside this list was edited.

## Measurements
- words `Polity Archetypes.md`: 3682 → 4115
- words `Daily Life.md`: 3316 → 3461
- words `How the Week Is Kept.md`: 1371 → 1569
- words `What the Year Feels Like.md`: 975 → 1031
- `will not explain` in the week note: 4 → 4
- `will not explain` in the year note: 5 → 6
- front-matter mismatches: 0 → 0

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- The published invariant script splits `git diff --name-only` on whitespace, so these paths false-fail as `NEW FILE Like.md`, `Life.md`, `Archetypes.md`, and `Kept.md`. The same check with `splitlines()` prints `invariants ok (4 files)`.
- These notes say "will not explain," not "will not say why." That count did not drop. The thaw, the salt, the wet leaf, the heel, the uncorrected chart, the place already set, and "will not share ink" still have no cause.
- Player-facing text did not pick up the GM reach-edge cause. No pull request was opened.

## Suggested follow-ups
- Point the invariant script at `splitlines()` before the next vault-voice slice, or spaced paths will keep false-failing.
- The conventions and `CLAUDE.md` voice update is still a separate slice.