<!-- orchestrate handoff
task: cultures-tongue
branch: orch/vault-voice/cultures-tongue
agentId: bc-90627cd4-bad1-4e92-8f8d-c157fc09a1ef
runId: run-86ebc89d-122d-4229-bd5b-f7ecace5af6e
resultStatus: finished
finishedAt: 2026-11-11T06:21:11.184Z
-->

## Status
success

## Branch
`orch/vault-voice/cultures-tongue`

## What I did
- `03 - Cultures/Naming/Naming People in the Turning.md`: rewrote the naming rules so a new reader can follow byname, house-name, drift, and hearth-register. Tables, name lists, seeds, and generator commands stayed.
- `03 - Cultures/Naming/Naming in the Turning.md`: rewrote the dictionary prose around the institution tables so the three stances and the common versus liturgical names are explained in place.
- `03 - Cultures/Languages/How a Place Speaks.md`: rewrote place-speech and the four tones. In-world phrases stayed untranslated.
- `03 - Cultures/Languages/The Old Tongue.md`: rewrote phonology and the coinages into connected explanation. The root table, drift table, and collision table stayed.
- Files left unchanged: 0

## Measurements
(none)

## Verification
not-verified

## Notes, concerns, deviations, findings, thoughts, feedback
- The published checker splits `git diff --name-only` on whitespace, so these paths are reported as `NEW FILE Speaks.md`, `Tongue.md`, and `Turning.md` and the script exits 1. With null-delimited names, front matter matches on all four files and `will not say why` stays 1 in `The Old Tongue.md` and 0 in the others.
- Headings were not renamed. Table rows match the base. Character counts rose on every file (the Old Tongue has fewer lines because bullets became paragraphs, and it grew from 23297 to 28297 characters).
- Netstrand still has no cause: "People there will not say why the name means night." The lost fourth Fox-word stays unexplained in GM Notes. Fox, seal, and crow as a naming test stayed in GM Notes. Keystone facts (the Tree is real, bounded reach, the Mother's nearness) stayed under GM Notes.
- No pull request was opened. Conventions, `CLAUDE.md`, the setting book, and the primer were not edited.

## Suggested follow-ups
- Run the invariant check with newline- or null-delimited paths before treating `NEW FILE` on these notes as a real failure.
- The voice-rule update in `Conventions.md` and `CLAUDE.md` is still a later slice, as are the world book and the player primer.