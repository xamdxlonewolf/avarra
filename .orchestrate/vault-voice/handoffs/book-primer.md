<!-- orchestrate handoff
task: book-primer
branch: orch/vault-voice/book-primer
agentId: bc-6e06ffa4-029d-488e-bc6e-cd6c302da7fa
runId: run-6fa0a434-0b32-496a-ab8d-6b5958040bcf
resultStatus: finished
finishedAt: 2026-11-11T07:01:48.339Z
-->

## Status
success

## Branch
`orch/vault-voice/book-primer`

## What I did
- Rewrote `14 - Assets/Documents/Primers/Player Primer.md` so it reads as someone explaining the Turning. Short stacked sentences are now connected paragraphs. Sentences that already sounded spoken stayed, including the Tengu description and "The moment you fly, anyone watching knows what you are."
- Kept the facts, the population numbers, the Tithe rules, and the character-creation steps. Terms a first-time reader needs (Kind, Condition, Tithe, Hope, a roll with Fear, Vulnerable, advantage) are explained in the sentence that uses them, from player-facing notes only.
- Rebuilt `The-Turning-Player-Primer.html` and `The-Turning-Player-Primer.pdf` with `build_player_primer.py`. Front matter, Links, and GM material stay out of the reading copy. The world book was not edited.

## Measurements
(none)

## Verification
type-check-only

## Notes, concerns, deviations, findings, thoughts, feedback
- The note went from 5048 words to 5910. The PDF is 8 pages and 61,914 bytes, up from 59,040, still a pre-session read. The extra length is gloss, not new places or new rules.
- Player-facing detail folded in where the old primer named a thing and did not say what it was: a blood-read is one drop, freely given or from a wound already there, and it does no harm. A Long-Lived death is the memories gone. Waiting at the door is manners. A djinn here has no bottle and no master. Kitsune, Selkie, and Yumboe keep the looks already in their player notes. Yumboe includes Bakhna Rakhna.
- No GM material. A text check of the HTML and the PDF found no Orledd, Unspent, Pourers, or Wide-Hand. Feeding a guest before anyone asks who they are is still unexplained.
- Chrome wrote the PDF and then timed out on the missing system bus, which the build script already treats as success. Ghostscript was not installed on the first run. I installed it and rebuilt, so the committed PDF is the compressed file.
- Character creation is still a numbered list, because a player has to follow it in order.

## Suggested follow-ups
- None for this primer. The branch is pushed and there is no pull request.