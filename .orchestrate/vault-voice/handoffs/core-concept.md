<!-- orchestrate handoff
task: core-concept
branch: orch/vault-voice/core-concept
agentId: bc-1bc4a717-9a12-4115-88f3-2b4f8243643c
runId: run-a062c9b5-439d-4b09-9966-006fae915dea
resultStatus: finished
finishedAt: 2026-11-11T06:19:46.029Z
-->

## Status
success

## Branch
`orch/vault-voice/core-concept`

## What I did
- `00 - Core/Concept/Build Plan.md`: Smoothed the world-explanation passages (the summary, the locked lines, the two clocks, and the V.3 answers) into connected sentences. Left the checklist, How to work, and the link log as lists.
- `00 - Core/Concept/The Premise.md`: Rewrote chopped definitions into explanatory prose. Kept every locked mark, population figure, schism, table row, and the GM keystone inside its GM blockquote.
- `00 - Core/00 - Core.md`: Turned the opening definition stack and the index glosses into sentences a new reader can follow.
- `00 - Core/Meta/Flight in this World.md`: Kept the tier table and every lane constraint. Rewrote stub cells and the surrounding explanation so a row is not three bare declarations.
- `00 - Core/Meta/The Wardens Ear.md`: Smoothed the study-index prose around the drill. Did not rewrite the numbered drill and did not touch the HTML.
- Left unchanged: 0 of the 5 assigned files.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- The published invariant script uses `.split()` on `git diff --name-only`. These paths contain spaces, so that split reports false `NEW FILE` hits (`Core.md`, `Plan.md`, `Premise.md`, `World.md`, `Ear.md`). The same check with `splitlines()` passes: front matter unchanged, headings unchanged, table row counts unchanged, no lost `will not say why`.
- No pull request was opened. The remote accepted `orch/vault-voice/core-concept`.
- `Conventions.md` and `CLAUDE.md` were left alone, as this slice required. They still name the short Turning Tree voice as the baseline, so a later session can put that voice back until the rules slice lands.
- The hug in the Build Plan V.3 line is glossed only as the Tree keeping the child and giving no colour. No cause was added. The heel and the other unexplained habits stay in the Do not list, still unexplained.
- Monster names in the Premise's sorting rule (vampire, werewolf, and the rest) are the roster table's own monster column, moved to first use. The GM keystone stays marked GM and is not confirmed in the belief paragraph.

## Suggested follow-ups
- Update `Conventions.md` and `CLAUDE.md` so the approved explanatory voice replaces the short Turning Tree baseline, and so unexplained habits stay unexplained.
- Point the invariant checker at `splitlines()` before it is run on this branch.