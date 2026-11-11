<!-- orchestrate handoff
task: cultures-law
branch: orch/vault-voice/cultures-law
agentId: bc-56811fbe-5455-480a-b5a8-6d997ca2825a
runId: run-24f1a762-b6ec-451a-8926-5977a875bb76
resultStatus: finished
finishedAt: 2026-11-11T06:20:31.689Z
-->

## Status
success

## Branch
`orch/vault-voice/cultures-law`

## What I did
- `03 - Cultures/Social Structures/Law and Citizenship.md`: rewrote the law into continuous explanation and glossed Kind, Condition, citizenship, and Tithe from facts already on the page.
- `03 - Cultures/Social Structures/Economy and the Tithe.md`: rewrote the Tithe, labor, banking, and polity sections in the same voice, keeping every rate and office.
- Files left unchanged: 0 of the 2 assigned notes. No other files were edited.

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- Front matter, headings, table row counts, and wikilinks match `origin/master`. The in-world night-gate notice is unchanged. Leaf-Mother reach, licence percentages, and the urban Tithe estimates stayed under GM Notes.
- These pages had no "will not say why" habits. Ndenjoo is still only the playable hall.
- Kind is glossed as birth, against the change the pages already call a Condition. No ancestry roster was added. Colour, blue-leaf, and pale-stone are glossed from how this page already uses them.
- The published checker splits `git diff --name-only` on whitespace, so these paths are reported as `NEW FILE Citizenship.md` and `NEW FILE Tithe.md`. Splitting on newlines passes: front matter unchanged, no lost refusals, 2 files.
- No pull request was opened.

## Suggested follow-ups
- Fix the invariant script to split diff paths on newlines before it runs on vault filenames that contain spaces.
- Continue the voice pass on the remaining culture notes with the same contract.