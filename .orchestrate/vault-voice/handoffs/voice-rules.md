<!-- orchestrate handoff
task: voice-rules
branch: orch/vault-voice/voice-rules
agentId: bc-22db4738-6063-45e2-a7a5-ff13a8244474
runId: run-46dc84fc-8581-49c5-bb9c-a23c52b03994
resultStatus: finished
finishedAt: 2026-11-11T06:04:57.281Z
-->

## Status
success

## Branch
`orch/vault-voice/voice-rules`

## What I did
- `CLAUDE.md`: replaced the short-speech rule and the prose-style ban on glossing a term a new reader needs, so setting notes require connected setting-book paragraphs.
- `00 - Core/Meta/Conventions.md`: rewrote the Plain prose section to that same rule and removed the Turning Tree chapter as the short-sentence baseline.
- Left unchanged: 754 other tracked files, including `00 - Core/Meta/Roadmap.md`.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- The branch name was accepted. No pull request was opened.
- Diff against `origin/master` is only `CLAUDE.md` and `00 - Core/Meta/Conventions.md`.
- `00 - Core/Meta/Roadmap.md` and `00 - Core/Concept/Build Plan.md` still say the Turning Tree chapter is the baseline. They were left untouched. The new rule says an older tracker line that still names that chapter is not a reason to chop a setting note.
- Conventions `updated` is now `2026-11-11`. The world-book sentence is still “The world book is rebuilt only when the user asks.”

## Suggested follow-ups
- When the note pass starts, do not execute Roadmap lines that still demand short sentences or the Turning Tree baseline. Those lines will fight this rule if a later session follows them as written.
- `00 - Core/Concept/Build Plan.md` still names that chapter as the baseline voice. It was outside this task.