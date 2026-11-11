<!-- orchestrate handoff
task: merge-book
branch: orch/vault-voice/book
agentId: bc-2727c01f-3d71-4293-ace5-7c28f3bc3306
runId: run-aa500a13-527e-4877-be67-0e020cc6d9ca
resultStatus: finished
finishedAt: 2026-11-11T07:07:17.833Z
-->

## Status
success

## Branch
`orch/vault-voice/book`

## What I did
- Cut `orch/vault-voice/book` from `orch/vault-voice/notes` (`6655647`). The book branch did not exist yet.
- Merged these branches in order, each as its own merge commit, with no sentence edits: `book-front`, `book-conditions`, `book-kinds`, `book-faith`, `book-orders`, `book-living`, `book-guilds`, `book-lands`, `book-ages`, `book-powers`, `book-gazetteer`, `book-places`, `book-gm`, `book-primer`. No conflicts.
- Pushed `orch/vault-voice/book` at `b59d6c0`. No pull request.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Every source tip is an ancestor of `b59d6c0`. The diff against `orch/vault-voice/notes` is exactly 28 paths: setting-book chapters `00` through `24`, plus `Player Primer.md`, `The-Turning-Player-Primer.html`, and `The-Turning-Player-Primer.pdf`. Each of those files matches its source branch. Every other path matches the notes branch, so the vault notes are still the notes-branch notes.
- The world-book HTML and PDF were not on any of these branches, so they are still the notes-branch copies. This merge did not compile the book.
- A conflict-marker scan hit pre-existing separator lines in skill scripts. Those files are unchanged from notes and were not part of the merge.

## Suggested follow-ups
- Compile the world book from the merged chapters so the HTML and PDF pick up chapters `00`–`24`.
- Leave the open note disagreements for a later notes pass. This merge did not edit prose: chapter 20 versus chapter 19 seat stress, Nethoren stress, the reckoning note’s second moon versus Planes, Thilim’s unnamed Brenthael warden versus Meirim, and At the Table’s Stilled door versus The Stilled.